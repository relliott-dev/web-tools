"""
Author: Russell Elliott
Date: 2024-03-20
This script captures and saves a screenshot of the specified webpage(s)
For full documentation, see the README in this tool's directory
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from urllib.parse import urlparse
from urllib.robotparser import RobotFileParser
import argparse
import os

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

# Capture a screenshot of the webpage
def capture_screenshot(url):
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    filename = urlparse(url).netloc.replace('www.', '') + ".png"
    driver.save_screenshot(filename)
    driver.quit()
    return filename

# Main function used to gather input and call other functions
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Webpage Screenshot Tool")
    parser.add_argument("urls", nargs='*', help="URL(s) to capture a screenshot of (separated by commas)")
    args = parser.parse_args()

    urls_input = ','.join(args.urls) if args.urls else input("\nEnter URL(s) to check (separated by commas): ")
    urls = [url.strip() for url in urls_input.split(',') if url.strip()]

    if not urls:
        print("\nNo URL(s) provided. Exiting program.")
        exit()

    for url in urls:
        formatted_url = format_url(url)
        if not is_allowed(formatted_url):
            print(f"\nAccess to {formatted_url} is disallowed by robots.txt or the URL is invalid.")
            continue

        print(f"\nCapturing screenshot of {formatted_url}...")
        filename = capture_screenshot(formatted_url)
        print(f"Screenshot saved as {filename}")
