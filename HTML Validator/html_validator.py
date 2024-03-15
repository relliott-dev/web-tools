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

# Validate the HTML content of the webpage
def validate_html(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        errors = []

        # Check for common HTML validation errors (simplified example)
        if not soup.find('title'):
            errors.append("Missing <title> tag.")
        if not soup.find('meta', {'name': 'description'}):
            errors.append("Missing meta description tag.")

        return errors
    except requests.exceptions.RequestException as e:
        print(f"\nError fetching URL: {e}")
        return None

# Output the results to a file and print them to the console along with datetime program was run
def output_results(url, errors, output_file, format='txt', is_last=False):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if format == 'csv':
        with open(output_file, "a", newline='', encoding="utf-8") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow([timestamp, url, '; '.join(errors)])
        print(f"Results saved to {output_file}")
    elif format == 'json':
        result_data = {'timestamp': timestamp, 'url': url, 'errors': errors}
        with open(output_file, "a", encoding="utf-8") as file:
            json.dump(result_data, file, indent=4)
            if not is_last:
                file.write(",\n")
            else:
                file.write("\n")
        print(f"Results saved to {output_file}")
    else:
        with open(output_file, "a", encoding="utf-8") as file:  # Changed from "w" to "a"
            file.write(f"Timestamp: {timestamp}\nURL: {url}\n\nErrors:\n")
            for error in errors:
                file.write(f"- {error}\n")
            file.write("\n")
        print(f"\nTimestamp: {timestamp}\nURL: {url}\n\nErrors:")
        for error in errors:
            print(f"- {error}")
        print(f"\nResults saved to {output_file}")

# Main function used to gather input and call other functions
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="HTML Validator Tool")
    parser.add_argument("urls", nargs='*', help="URL(s) to validate (separated by commas)")
    parser.add_argument("--csv", action='store_true', help="Export results as CSV")
    parser.add_argument("--json", action='store_true', help="Export results as JSON")
    args = parser.parse_args()

    urls_input = ','.join(args.urls) if args.urls else input("\nEnter URL(s) to validate (separated by commas): ")
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
    
    with open("html_validator.txt", "w", encoding="utf-8") as file:
        pass
    if export_csv:
        with open("html_validator.csv", "w", newline='', encoding="utf-8") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(['Timestamp', 'URL', 'Errors'])
    if export_json:
        with open("html_validator.json", "w", encoding="utf-8") as file:
            file.write('[')
            file.write("\n")

    for i, url in enumerate(urls):
        formatted_url = format_url(url)
        if not is_allowed(formatted_url):
            print(f"\nAccess to {formatted_url} is disallowed by robots.txt or the URL is invalid.")
            continue

        errors = validate_html(formatted_url)
        is_last_url = i == len(urls) - 1
        if errors:
            output_results(formatted_url, errors, "html_validator.txt")
            if export_csv:
                output_results(formatted_url, errors, "html_validator.csv", format='csv')
            if export_json:
                output_results(formatted_url, errors, "html_validator.json", format='json', is_last=is_last_url)
        else:
            print(f"No errors found for {formatted_url}.")

    if export_json:
        with open("html_validator.json", "a", encoding="utf-8") as file:
            file.write(']')
