from bs4 import BeautifulSoup
from collections import Counter
from datetime import datetime
from urllib.robotparser import RobotFileParser
from urllib.parse import urlparse
import urllib.error
import requests
import re
import socket
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
    except (socket.gaierror, urllib.error.URLError, UnicodeError):
        return False
    
# Count the occurrences of the top ten most frequently used words
def get_top_words(url, top_n=10):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        response = requests.get(url, headers=headers, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')

        text = soup.get_text().lower()
        words = re.findall(r'\b\w+\b', text)
        word_counts = Counter(words).most_common(top_n)
        
        return word_counts
    except requests.exceptions.RequestException as e:
        print(f"\nError fetching URL: {e}")
        return None

# Output the results to a file and print them to the console along with datetime program was run
def output_results(url, counts, output_file, format='txt'):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if format == 'csv':
        with open(output_file, "w", newline='', encoding="utf-8") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(['Timestamp', 'URL', 'Text', 'Count'])
            for text, count in counts:
                csv_writer.writerow([timestamp, url, text, count])
        print(f"Results saved to {output_file}")
    elif format == 'json':
        result_data = {
            'timestamp': timestamp,
            'url': url,
            'results': [{'text': text, 'count': count} for text, count in counts]
        }
        with open(output_file, "w", encoding="utf-8") as file:
            json.dump(result_data, file, indent=4)
        print(f"Results saved to {output_file}")
    else:
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(f"Timestamp: {timestamp}\nURL: {url}\n")
            print(f"\nTimestamp: {timestamp}\nURL: {url}")
            for text, count in counts:
                line = f"The text '{text}' appears {count} times on the page\n"
                file.write(line)
                print(line.strip())
        print(f"\nResults saved to {output_file}")

# Main Function used to gather input and call other functions
# It will check for accessibility and empty text before continuing to output
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Most Common Words Script")
    parser.add_argument("url", help="URL to check", nargs='?', default='')
    parser.add_argument("top", type=int, nargs='?', help="Number of top words to display")
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
        
    if args.top is None:
        args.top = int(input("Enter the number of top words to display: ").strip())

    counts = get_top_words(formatted_url, args.top)
    if counts:
        output_results(formatted_url, counts, "most_common_words.txt")

        export_csv = args.csv
        export_json = args.json
        if not export_csv:
            export_csv = input("Export results as CSV? (y/n): ").strip().lower() == 'y'
        if export_csv:
            output_results(formatted_url, counts, "most_common_words.csv", format='csv')
        if not export_json:
            export_json = input("Export results as JSON? (y/n): ").strip().lower() == 'y'
        if export_json:
            output_results(formatted_url, counts, "most_common_words.json", format='json')