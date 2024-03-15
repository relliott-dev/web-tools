# HTML Validator

## Overview

The HTML Validator is a Python script that checks the HTML content of a webpage for errors and compliance with web standards

## Features

- Validates the HTML content of a webpage for common errors
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

`python html_validator.py [URL(s)] [--csv] [--json]`

- [URL(s)]: The URL(s) of each web page to check
- [--csv]: Optional flag to export the results as a CSV file
- [--json]: Optional flag to export the results as a JSON file

If the URL(s) are not provided as arguments, the script will prompt for input

## Examples

```
python html_validator.py example, example2
Export results as CSV? (y/n): y
Export results as JSON? (y/n): n
```
```
python html_validator.py --csv --json
Enter URL(s) to check (separated by commas): https://example.com
```

## Output

The results will be saved to a file named `html_validator.txt` by default. If the `--csv` flag is used, the results will also be saved as `html_validator.csv`. Similarly, if the `--json` flag is used, the results will be saved as `html_validator.json`.

Each file will contain a timestamp, the URL checked, and the list of HTML errors found

## Future Plans

- Develop a graphical user interface (GUI) for easier use
- Extend support for more detailed HTML validation checks
