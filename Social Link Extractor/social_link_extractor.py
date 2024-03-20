"""
Author: Russell Elliott
Date: 2024-03-20
This script extracts and reports social media links from a specified webpage
For full documentation, see the README in this tool's directory
"""

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

# Extracts social media URLs from the webpage
def extract_social_media_links(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        response = requests.get(url, headers=headers, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')
        social_media_links = set()

        social_media_domains = [
            'facebook.com', 'twitter.com', 'linkedin.com',
            'instagram.com', 'youtube.com', 'pinterest.com',
            'discord.gg', 'github.com', 'wa.me'
        ]

        for tag in soup.find_all(href=True):
            for domain in social_media_domains:
                if domain in tag['href']:
                    social_media_links.add(tag['href'])
                    break

        return social_media_links
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
        return set()

# Output the results to a file and print them to the console along with the datetime the program was run
def output_results(url, social_media_links, output_file, format='txt', is_last=False):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if format == 'csv':
        with open(output_file, "a", newline='', encoding="utf-8") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow([timestamp, url, len(social_media_links)] + list(social_media_links))
    elif format == 'json':
        result_data = {'timestamp': timestamp, 'url': url, 'number_of_links': len(social_media_links), 'links': list(social_media_links)}
        with open(output_file, "a", encoding="utf-8") as file:
            json.dump(result_data, file, indent=4)
            if not is_last:
                file.write(",\n")
            else:
                file.write("\n")
    else:
        with open(output_file, "a", encoding="utf-8") as file:
            file.write(f"Timestamp: {timestamp}\nURL: {url}\n\nNumber of social media links found: {len(social_media_links)}\n")
            if social_media_links:
                for link in social_media_links:
                    file.write(f"{link}\n")
            if not is_last:
                file.write("\n\n")
        print(f"\nTimestamp: {timestamp}\nURL: {url}\nNumber of social media links found: {len(social_media_links)}")
        if social_media_links:
            print("\nSocial media links:")
            for link in social_media_links:
                print(link)
        print(f"\nResults saved to {output_file}")

# Main Function used to gather input and call other functions
# It will check for accessibility and empty text before continuing to output
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Social Link Extractor Script")
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
    
    with open("social_link_extractor.txt", "w", encoding="utf-8") as file:
        pass
    if export_csv:
        with open("social_link_extractor.csv", "w", newline='', encoding="utf-8") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(['Timestamp', 'Website', 'Number of Links'] + ['Link ' + str(i+1) for i in range(max(len(extract_social_media_links(format_url(url))) for url in urls))])
    if export_json:
        with open("social_link_extractor.json", "w", encoding="utf-8") as file:
            file.write('[')
            file.write("\n")
    
    for i, url in enumerate(urls):
        formatted_url = format_url(url)
        if is_allowed(formatted_url):
            social_media_links = extract_social_media_links(formatted_url)
            is_last_url = i == len(urls) - 1
            output_results(formatted_url, social_media_links, "social_link_extractor.txt", is_last=is_last_url)
            if export_csv:
                output_results(formatted_url, social_media_links, "social_link_extractor.csv", format='csv')
            if export_json:
                output_results(formatted_url, social_media_links, "social_link_extractor.json", format='json', is_last=is_last_url)
        else:
            print(f"\nAccess to {formatted_url} is disallowed by robots.txt or the URL is invalid.")
    
    if export_json:
        with open("social_link_extractor.json", "a", encoding="utf-8") as file:
            file.write(']')
