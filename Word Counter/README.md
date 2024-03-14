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

`pip install requests beautifulsoup4`

## Usage

Run the script with the following command:

`python word_counter.py [URL] [WORDS] [--csv] [--json]`

- [URL]: The URL of the web page to check
- [WORDS]: Space-separated words to search for on the page
- [--csv]: Optional flag to export the results as a CSV file
- [--json]: Optional flag to export the results as a JSON file

If the URL and words are not provided as arguments, the script will prompt for input

## Examples

```
python word_counter.py example "word1 word2 word3"

Export results as CSV? (y/n): y

Export results as JSON? (y/n): n
```

```
python word_counter.py --csv --json

Enter a URL to check: https://example.com

Enter comma-separated words to search for: word1, word2, word3
```

## Output

The results will be saved to a file named `word_counter.txt` by default. If the `--csv` flag is used, the results will also be saved as `word_counter.csv`. Similarly, if the `--json` flag is used, the results will be saved as `word_counter.json`.

Each file will contain a timestamp, the URL checked, and the count of each specified word.

## Future Plans

- Develop a graphical user interface (GUI) for easier use
- Add error handling for invalid user input, such as checking for valid URLs and non-empty word lists
- Optimize the performance of the word counting process for large web pages
- Allow users to specify HTML tags to narrow down the word count to specific sections of a web page
- Enable the script to check multiple websites for word occurrences and compare the usage of the same words between different sites
- Extend support for counting words in multiple languages
- Incorporate more advanced text analysis features
