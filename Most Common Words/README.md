# Most Common Words

## Overview

Most Common Words is a Python script that analyzes a web page and identifies the most frequently occurring words

## Features

- Identifies the top n most common words on a web page
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

`python most_common_words.py [URL] [TOP] [--csv] [--json]`

- [URL]: The URL of the web page to check (required)
- [TOP]: The number of top words to display
- [--csv]: Optional flag to export the results as a CSV file
- [--json]: Optional flag to export the results as a JSON file

If the URL and words are not provided as arguments, the script will prompt for input

## Examples

```
python most_common_words.py example 10
Export results as CSV? (y/n): y
Export results as JSON? (y/n): n
```
```
python most_common_words.py --csv --json
Enter a URL to check: https://example.com
Enter the number of top words to display: 10
```

## Output

The results will be saved to a file named `most_common_words.txt` by default. If the `--csv` flag is used, the results will also be saved as `most_common_words.csv`. Similarly, if the `--json` flag is used, the results will be saved as `most_common_words.json`.

Each file will contain a timestamp, the URL checked, and the list of top words along with their counts

## Future Plans

- Develop a graphical user interface (GUI) for easier use
- Improve error handling for invalid user input, such as checking for valid URLs and input number
- Optimize the performance of the word counting process for large web pages
- Allow users to specify HTML tags to narrow down the word count to specific sections of a web page
- Enable the script to analyze multiple websites simultaneously and compare the common words between different sites
- Extend support for counting words in multiple languages
- Add an option to filter out common stopwords from a user-provided text file
