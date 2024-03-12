from bs4 import BeautifulSoup
from datetime import datetime
from urllib.robotparser import RobotFileParser
from urllib.parse import urlparse
import requests
import argparse
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
        
# Fetches the content of the webpage at the given URL and returns the text content with preserved structure
def get_stripped_content(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        response = requests.get(url, headers=headers, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')

        for script_or_style in soup(['script', 'style']):
            script_or_style.decompose()

        # Extract text from the soup object, adding newlines after block-level elements
        lines = []
        for element in soup.descendants:
            if isinstance(element, str):
                lines.append(element.strip())
            elif element.name in ['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'div', 'li', 'br']:
                lines.append('\n')

        text = ' '.join(lines).strip()
        text = re.sub(r'\n+', '\n', text)
        return text
    except requests.exceptions.RequestException as e:
        print(f"\nError fetching URL: {e}")
        return None

# Output the results to a file and print them to the console along with datetime program was run
def output_results(url, content, output_file):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(f"Timestamp: {timestamp}\nURL: {url}\n\n{content}")
    print(f"\nTimestamp: {timestamp}\nURL: {url}\n\n{content}")
    print(f"\nResults saved to {output_file}")

# Main Function used to gather input and call other functions
# It will check for accessibility and empty text before continuing to output
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Stripped Content Script")
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
    
    content = get_stripped_content(formatted_url)
    if content:
        output_results(formatted_url, content, "stripped_content.txt")