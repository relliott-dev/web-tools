from bs4 import BeautifulSoup
from datetime import datetime
from urllib.robotparser import RobotFileParser
from urllib.parse import urlparse
import requests
import argparse
import csv
import json

# Add 'https://' to the URL if it doesn't have a scheme
# Append '.com' if the URL doesn't have a domain extension
def format_url(url):
    if not url:
        return None
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    if '.' not in urlparse(url).netloc:
        url += '.com'
    return url

# Check if the website's robots.txt file allows the given URL to be scraped
def is_allowed(url):
    try:
        parsed_url = urlparse(url)
        base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
        robots_url = f"{base_url}/robots.txt"
        rp = RobotFileParser()
        rp.set_url(robots_url)
        rp.read()
        return rp.can_fetch('*', url)
    except Exception:
        return False

# Detect the theme or framework used by the website
def detect_theme(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        response = requests.get(url, headers=headers, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')

        if "wp-content" in response.text:
            return "WordPress"
        for link in soup.find_all("link", href=True):
            if "bootstrap" in link["href"]:
                return "Bootstrap"
        return "Unknown"
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
        return None

# Output the results to a file and print them to the console along with datetime program was run
def output_results(url, theme, output_file, format='txt', is_last=False):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if format == 'csv':
        with open(output_file, "a", newline='', encoding="utf-8") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow([timestamp, url, theme])
    elif format == 'json':
        result_data = {'timestamp': timestamp, 'url': url, 'theme': theme}
        with open(output_file, "a", encoding="utf-8") as file:
            json.dump(result_data, file, indent=4)
            if not is_last:
                file.write(",\n")
            else:
                file.write("\n")
    else:
        with open(output_file, "a", encoding="utf-8") as file:
            file.write(f"Timestamp: {timestamp}\nURL: {url}\nDetected theme/framework: {theme}")
            if not is_last:
                file.write("\n\n")
        print(f"\nTimestamp: {timestamp}\nURL: {url}\nDetected theme/framework: {theme}")
        print(f"Results saved to {output_file}")

# Main Function used to gather input and call other functions
# It will check for accessibility and empty text before continuing to output
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Theme Detector Script")
    parser.add_argument("urls", nargs='*', help="URL(s) to check (separated by commas)")
    parser.add_argument("--csv", action='store_true', help="Export results as CSV")
    parser.add_argument("--json", action='store_true', help="Export results as JSON")
    args = parser.parse_args()

    urls_input = ','.join(args.urls) if args.urls else input("\nEnter URL(s) to check (separated by commas): ")
    urls = [url.strip() for url in urls_input.split(',') if url.strip()]

    if not urls:
        print("\nNo URL(s) provided. Exiting program.")
        exit()
        
    export_csv = args.csv
    export_json = args.json
    
    if not export_csv:
        export_csv = input("Export results as CSV? (y/n): ").strip().lower() == 'y'
    if not export_json:
        export_json = input("Export results as JSON? (y/n): ").strip().lower() == 'y'
    
    with open("theme_detector.txt", "w", encoding="utf-8") as file:
        pass
    if export_csv:
        with open("theme_detector.csv", "w", newline='', encoding="utf-8") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(['Timestamp', 'Website', 'Theme'])
    if export_json:
        with open("theme_detector.json", "w", encoding="utf-8") as file:
            file.write('[')
            file.write("\n")
    
    for i, url in enumerate(urls):
        formatted_url = format_url(url)
        if is_allowed(formatted_url):
            theme = detect_theme(formatted_url)
            is_last_url = i == len(urls) - 1
            output_results(formatted_url, theme, "theme_detector.txt", is_last=is_last_url)
            if export_csv:
                output_results(formatted_url, theme, "theme_detector.csv", format='csv')
            if export_json:
                output_results(formatted_url, theme, "theme_detector.json", format='json', is_last=is_last_url)
        else:
            print(f"\nAccess to {formatted_url} is disallowed by robots.txt or the URL is invalid.")
    
    if export_json:
        with open("theme_detector.json", "a", encoding="utf-8") as file:
            file.write(']')