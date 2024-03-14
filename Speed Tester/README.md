# Speed Tester

## Overview

The Speed Tester is a Python script that measures the loading speed of web pages using Selenium WebDriver to simulate a browser

## Features

- Measures the loading speed of web pages
- Checks the website's `robots.txt` file for scraping permissions
- Outputs the results to a text file, with options to export as CSV or JSON
- Handles different URL formats and appends necessary schemes or domain extensions
- Provides informative error messages for inaccessible URLs or other issues

## Requirements

- Python 3.x
- `selenium`
- `webdriver-manager`

## Installation

1. Clone the repository or download the source code
2. Install the required dependencies:

    `pip install selenium webdriver-manager`

## Usage

Run the script with the following command:

`python speed_tester.py [URL(s)] [--csv] [--json]`

- [URL(s)]: The URL(s) of each web page to check
- [--csv]: Optional flag to export the results as a CSV file
- [--json]: Optional flag to export the results as a JSON file

If the URL and words are not provided as arguments, the script will prompt for input

## Examples

```
python speed_tester.py example, example2
Export results as CSV? (y/n): y
Export results as JSON? (y/n): n
```
```
python speed_tester.py --csv --json
Enter URL(s) to check (separated by commas): https://example.com
```

## Output

The results will be saved to a file named `speed_tester.txt` by default. If the `--csv` flag is used, the results will also be saved as `speed_tester.csv`. Similarly, if the `--json` flag is used, the results will be saved as `speed_tester.json`.

Each file will contain a timestamp, the URL checked, and the loading time for each website

## Future Plans

- Develop a graphical user interface (GUI) for easier use
- Extend support for more detailed performance metrics
