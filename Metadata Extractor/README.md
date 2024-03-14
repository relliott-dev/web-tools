# Metadata Extractor

## Overview

Metadata Extractor is a Python script that extracts metadata such as title, description, and keywords from a given web page

## Features

- Extracts metadata including title, description, and keywords from a web page
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

`python metadata_extractor.py [URL(s)] [--csv] [--json]`

- [URL(s)]: The URL(s) of the web page(s) to check
- [--csv]: Optional flag to export the results as a CSV file
- [--json]: Optional flag to export the results as a JSON file

If the URL(s) are not provided as arguments, the script will prompt for input

## Examples

```
python metadata_extractor.py example, example2
Export results as CSV? (y/n): y
Export results as JSON? (y/n): n
```
```
python metadata_extractor.py --csv --json
Enter a URL to check: https://example.com
Enter comma-separated words to search for: word1, word2, word3
```

## Output

The results will be saved to a file named `metadata_extractor.txt` by default. If the `--csv` flag is used, the results will also be saved as `metadata_extractor.csv`. Similarly, if the `--json` flag is used, the results will be saved as `metadata_extractor.json`.

Each file will contain a timestamp, the URL checked, and the extracted metadata.

## Future Plans

- Develop a graphical user interface (GUI) for easier use
- Optimize the performance of the script for faster metadata extraction
- Allow users to specify HTML tags to narrow down the word count to specific sections of a web page
