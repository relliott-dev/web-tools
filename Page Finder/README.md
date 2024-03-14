# Page Finder

## Overview

Page Finder is a Python script that takes a URL as input and extracts all internal links (pages) within the specified website

## Features

- Extracts all internal links from a website

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

`python page_finder.py [URL] [--csv] [--json]`

- [URL]: The URL of the website to check
- [--csv]: Optional flag to export the results as a CSV file
- [--json]: Optional flag to export the results as a JSON file

If the URL and words are not provided as arguments, the script will prompt for input

## Examples

```
python page_finder.py example
Export results as CSV? (y/n): y
Export results as JSON? (y/n): n
```
```
python page_finder.py --csv --json
Enter a URL to check: https://example.com
```

## Output

The results will be saved to a file named `page_finder.txt` by default. If the `--csv` flag is used, the results will also be saved as `page_finder.csv`. Similarly, if the `--json` flag is used, the results will be saved as `page_finder.json`.

Each file will contain a timestamp, the URL checked, and a list of all internal links found on the website.

## Future Plans

- Develop a graphical user interface (GUI) for easier use
- Add options to filter specific types of links or limit the depth of the search
- Optimize the performance of the link extraction process for large websites
- Extend support for counting words in multiple languages
