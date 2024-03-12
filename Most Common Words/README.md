# Most Common Words

## Overview

Most Common Words is a Python script that analyzes a given web page and counts the most frequently used words. The script also checks the website's `robots.txt` file to ensure that the page is allowed to be scraped.

## Features

- Counts the most frequently used words on a web page
- Checks the website's `robots.txt` file for scraping permissions
- Outputs the results to a text file, with options to export as CSV or JSON
- Handles different URL formats and appends necessary schemes or domain extensions
- Provides informative error messages for inaccessible URLs or other issues

## Requirements

- Python 3.x
- `requests`
- `beautifulsoup4`

## Installation

1. Clone the repository or download the source code
2. Install the required dependencies:

   pip install requests beautifulsoup4

## Usage

Run the script with the following command:

python most_common_words.py [URL] [--csv] [--json]

[URL]: The URL of the web page to check (required)
[--csv]: Optional flag to export the results as a CSV file
[--json]: Optional flag to export the results as a JSON file

If the URL and words are not provided as arguments, the script will prompt for input

## Examples

python most_common_words.py example.com

python most_common_words.py --csv --json
Enter a URL to check: https://example.com
