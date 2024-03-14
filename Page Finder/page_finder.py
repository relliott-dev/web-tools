from bs4 import BeautifulSoup
from datetime import datetime
from urllib.robotparser import RobotFileParser
from urllib.parse import urlparse, urljoin
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
        
# Iterates through every link of the website at the given URL and returns a set of unique internal links (pages)
def get_internal_links(url):
    internal_links = set()
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        response = requests.get(url, headers=headers, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')

        base_url = '{uri.scheme}://{uri.netloc}'.format(uri=urlparse(url))
        for link in soup.find_all('a', href=True):
            href = link['href']
            if href.startswith('/'):
                href = urljoin(base_url, href)
            if href.startswith(base_url):
                internal_links.add(href)
    except requests.exceptions.RequestException as e:
        print(f"\nError fetching URL: {e}")
    return internal_links

# Output the results to a file and print them to the console along with datetime program was run
def output_results(url, internal_links, output_file, format='txt'):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if format == 'csv':
        with open(output_file, "w", newline='', encoding="utf-8") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(['Timestamp', 'URL', 'Number of Pages'] + ['Page ' + str(i + 1) for i in range(len(internal_links))])
            csv_writer.writerow([timestamp, url, len(internal_links)] + list(internal_links))
        print(f"Results saved to {output_file}")
    elif format == 'json':
        result_data = {'timestamp': timestamp, 'url': url, 'number_of_pages': len(internal_links), 'pages': list(internal_links)}
        with open(output_file, "w", encoding="utf-8") as file:
            json.dump(result_data, file, indent=4)
        print(f"Results saved to {output_file}")
    else:
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(f"Timestamp: {timestamp}\nURL: {url}\n\nNumber of pages (approximate): {len(internal_links)}\n")
            for link in internal_links:
                file.write(f"{link}\n")
        print(f"\nTimestamp: {timestamp}\nURL: {url}\nNumber of pages (approximate): {len(internal_links)}")
        print("\nList of pages:")
        for link in internal_links:
            print(link)
        print(f"\nResults saved to {output_file}")

# Main Function used to gather input and call other functions
# It will check for accessibility and empty text before continuing to output
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Page Finder Script")
    parser.add_argument("url", help="URL to check", nargs='?', default='')
    parser.add_argument("--csv", action='store_true', help="Export results as CSV")
    parser.add_argument("--json", action='store_true', help="Export results as JSON")
    args = parser.parse_args()

    if not args.url.strip():
        args.url = input("\nEnter a URL to check: ").strip()
    
    if not args.url:
        print("\nNo URL provided. Exiting program.")
        exit()

    formatted_url = format_url(args.url)
    if not is_allowed(formatted_url):
        print(f"\nAccess to {formatted_url} is disallowed by robots.txt or the URL is invalid. Exiting program.")
        exit()

    internal_links = get_internal_links(formatted_url)
    if internal_links:
        output_results(formatted_url, internal_links, "page_finder.txt")

        export_csv = args.csv
        export_json = args.json
        if not export_csv:
            export_csv = input("Export results as CSV? (y/n): ").strip().lower() == 'y'
        if export_csv:
            output_results(formatted_url, internal_links, "page_finder.csv", format='csv')
        if not export_json:
            export_json = input("Export results as JSON? (y/n): ").strip().lower() == 'y'
        if export_json:
            output_results(formatted_url, internal_links, "page_finder.json", format='json')