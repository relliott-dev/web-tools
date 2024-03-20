"""
Author: Russell Elliott
Date: 2024-03-20
This script measures and reports the loading speed of a specified webpage using Selenium
For full documentation, see the README in this tool's directory
"""

from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import time
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

# Measures the loading speed of a webpage using Selenium
def measure_loading_speed(url):
    try:
        options = Options()
        options.headless = True
        driver = webdriver.Chrome(options=options)
        start_time = time()
        driver.get(url)
        end_time = time()
        driver.quit()
        return end_time - start_time
    except Exception as e:
        print(f"Error: {e}")
        return None

# Output the results to a file and print them to the console along with datetime program was run
def output_results(url, loading_time, output_file, format='txt', is_last=False):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    rounded_loading_time = round(loading_time, 2) if loading_time is not None else None
    if format == 'csv':
        with open(output_file, "a", newline='', encoding="utf-8") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow([timestamp, url, rounded_loading_time])
    elif format == 'json':
        result_data = {'timestamp': timestamp, 'url': url, 'loading_time': rounded_loading_time}
        with open(output_file, "a", encoding="utf-8") as file:
            json.dump(result_data, file, indent=4)
            if not is_last:
                file.write(",\n")
            else:
                file.write("\n")
    else:
        with open(output_file, "a", encoding="utf-8") as file:
            file.write(f"Timestamp: {timestamp}\nURL: {url}\nLoading Time: {loading_time:.2f} seconds")
            if not is_last:
                file.write("\n\n")
        print(f"\nTimestamp: {timestamp}\nURL: {url}\nLoading Time: {loading_time:.2f} seconds")
        print(f"Results saved to {output_file}")

# Main Function used to gather input and call other functions
# It will check for accessibility and empty text before continuing to output
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Speed Tester Script")
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
    
    with open("speed_tester.txt", "w", encoding="utf-8") as file:
        pass
    if export_csv:
        with open("speed_tester.csv", "w", newline='', encoding="utf-8") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(['Timestamp', 'Website', 'Loading Time'])
    if export_json:
        with open("speed_tester.json", "w", encoding="utf-8") as file:
            file.write('[')
            file.write("\n")
    
    for i, url in enumerate(urls):
        formatted_url = format_url(url)
        if is_allowed(formatted_url):
            loading_time = measure_loading_speed(formatted_url)
            is_last_url = i == len(urls) - 1
            output_results(formatted_url, loading_time, "speed_tester.txt", is_last=is_last_url)
            if export_csv:
                output_results(formatted_url, loading_time, "speed_tester.csv", format='csv')
            if export_json:
                output_results(formatted_url, loading_time, "speed_tester.json", format='json', is_last=is_last_url)
        else:
            print(f"\nAccess to {formatted_url} is disallowed by robots.txt or the URL is invalid.")
    
    if export_json:
        with open("speed_tester.json", "a", encoding="utf-8") as file:
            file.write(']')
