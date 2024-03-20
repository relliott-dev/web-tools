"""
Author: Russell Elliott
Date: 2024-03-20
This script identifies and reports broken links on a webpage
For full documentation, see the README in this tool's directory
"""

from bs4 import BeautifulSoup
from datetime import datetime
from urllib.robotparser import RobotFileParser
from urllib.parse import urlparse, urljoin
import requests
import argparse
import csv
import json
import re

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

# Check for broken links on a webpage
def get_broken_links(url):
    links = set()
    broken_links = set()
    base_url = '{uri.scheme}://{uri.netloc}'.format(uri=urlparse(url))

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    try:
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code >= 400:
            broken_links.add(url)
            return links, broken_links

        soup = BeautifulSoup(response.text, 'html.parser')

        for link in soup.find_all('a', href=True):
            href = link['href']
            full_url = urljoin(base_url, href)

            if full_url not in links:
                links.add(full_url)

                if href.startswith(('http', 'https')):
                    try:
                        link_response = requests.get(full_url, headers=headers, timeout=5, allow_redirects=True)
                        if link_response.status_code >= 400:
                            broken_links.add(full_url)
                    except Exception:
                        broken_links.add(full_url)

                elif href.startswith('mailto:'):
                    if not re.match(r'^mailto:[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', href) and href != 'mailto:#':
                        broken_links.add(href)

                elif href.startswith('tel:'):
                    if not re.match(r'^tel:\+?[0-9\s()-]+$', href):
                        broken_links.add(href)

                elif href.startswith('#'):
                    if not soup.find(id=href[1:]) and href != '#':
                        broken_links.add(href)

    except requests.exceptions.RequestException as e:
        print(f"\nError fetching URL: {e}")

    return links, broken_links
    
# Output the results to a file and print them to the console along with datetime program was run
def output_results(url, links, broken_links, output_file, format='txt', is_last=False):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if format == 'csv':
        with open(output_file, "a", newline='', encoding="utf-8") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow([timestamp, url, len(links), len(broken_links)] + list(broken_links))
    elif format == 'json':
        result_data = {'timestamp': timestamp, 'url': url, 'total_links': len(links), 'total_broken_links': len(broken_links), 'broken_links': list(broken_links)}
        with open(output_file, "a", encoding="utf-8") as file:
            json.dump(result_data, file, indent=4)
            if not is_last:
                file.write(",\n")
            else:
                file.write("\n")
    else:
        with open(output_file, "a", encoding="utf-8") as file:
            file.write(f"Timestamp: {timestamp}\nURL: {url}\nTotal links: {len(links)}\nTotal broken links: {len(broken_links)}\n")
            for link in broken_links:
                file.write(f"{link}\n")
            if not is_last:
                file.write("\n")
        print(f"\nTimestamp: {timestamp}\nURL: {url}\nTotal links: {len(links)}\nTotal broken links: {len(broken_links)}")
        for link in broken_links:
            print(f"{link}")
        print(f"\nResults saved to {output_file}")

# Main Function used to gather input and call other functions
# It will check for accessibility and empty text before continuing to output
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Broken Links Finder Script")
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
    
    with open("broken_links_finder.txt", "w", encoding="utf-8") as file:
        pass
    if export_csv:
        with open("broken_links_finder.csv", "w", newline='', encoding="utf-8") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(['Timestamp', 'Website', 'Total Links', 'Total Broken Links'] + ['Broken Link ' + str(i+1) for i in range(max(len(get_broken_links(format_url(url))[1]) for url in urls))])
    if export_json:
        with open("broken_links_finder.json", "w", encoding="utf-8") as file:
            file.write('[')
            file.write("\n")
    
    for i, url in enumerate(urls):
        formatted_url = format_url(url)
        if not is_allowed(formatted_url):
            print(f"\nAccess to {formatted_url} is disallowed by robots.txt or the URL is invalid.")
            continue

        links, broken_links = get_broken_links(formatted_url)
        is_last_url = i == len(urls) - 1
        output_results(formatted_url, links, broken_links, "broken_links_finder.txt", is_last=is_last_url)
        if export_csv:
            output_results(formatted_url, links, broken_links, "broken_links_finder.csv", format='csv', is_last=is_last_url)
        if export_json:
            output_results(formatted_url, links, broken_links, "broken_links_finder.json", format='json', is_last=is_last_url)
    
    if export_json:
        with open("broken_links_finder.json", "a", encoding="utf-8") as file:
            file.write(']')
