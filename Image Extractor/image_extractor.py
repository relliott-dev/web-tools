"""
Author: Russell Elliott
Date: 2024-03-20
This script downloads all images from a given webpage
For full documentation, see the README in this tool's directory
"""

from bs4 import BeautifulSoup
from datetime import datetime
from urllib.robotparser import RobotFileParser
from urllib.parse import urlparse, urljoin
import requests
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
        
# Creates a directory for the downloaded images
def create_image_directory(base_url):
    directory_name = urlparse(base_url).netloc
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)
    return directory_name

# Downloads all images from the given webpage
def download_images(url, directory_name):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        response = requests.get(url, headers=headers, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')

        image_count = 0
        for img in soup.find_all('img', src=True):
            img_url = img['src']
            if not img_url.startswith(('http://', 'https://')):
                img_url = urljoin(url, img_url)

            try:
                img_data = requests.get(img_url, headers=headers, timeout=5).content
                img_filename = os.path.join(directory_name, f'image_{image_count}.png')
                with open(img_filename, 'wb') as img_file:
                    img_file.write(img_data)
                image_count += 1
                print(f"Downloaded: {img_url}")
            except requests.exceptions.RequestException as e:
                print(f"Failed to download: {img_url} - {e}")
    except requests.exceptions.RequestException as e:
        print(f"\nError fetching URL: {e}")
    return image_count

# Main Function used to gather input and call other functions
# It will check for accessibility and empty text before continuing to output
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Image Extractor Script")
    parser.add_argument("url", help="URL to check", nargs='?', default='')
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
    
    print("\nDownloading image files...")
    formatted_url = format_url(args.url)
    directory_name = create_image_directory(formatted_url)
    image_count = download_images(formatted_url, directory_name)
    print(f"\nTotal images downloaded: {image_count}")
