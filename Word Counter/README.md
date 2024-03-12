# Word Counter

## Overview

Word Counter is a Python script that takes a URL and a list of words as input and counts the occurrences of each word on the specified web page. The script also checks the website's `robots.txt` file to ensure that the page is allowed to be scraped.

## Features

- Counts the occurrences of specified words on a web page
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

python word_counter.py [URL] [WORDS] [--csv] [--json]

[URL]: The URL of the web page to check
[WORDS]: Space-separated words to search for on the page
[--csv]: Optional flag to export the results as a CSV file
[--json]: Optional flag to export the results as a JSON file

If the URL and words are not provided as arguments, the script will prompt for input

## Examples

python word_counter.py example "word1 word2 word3"

python word_counter.py --csv --json
Enter a URL to check: https://example.com
Enter comma-separated words to search for: word1, word2, word3
