# Theme Detector

## Overview

The Theme Detector is a Python script that detects the theme or framework used by a website. It checks for common indicators of popular themes like WordPress or Bootstrap.

## Features

- Detects common themes and frameworks used by websites
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

`python theme_detector.py [URL(s)] [--csv] [--json]`

- [URL(s)]: The URL(s) of each web page to check
- [--csv]: Optional flag to export the results as a CSV file
- [--json]: Optional flag to export the results as a JSON file

If the URL and words are not provided as arguments, the script will prompt for input

## Examples

```
python theme_detector.py example, example2
Export results as CSV? (y/n): y
Export results as JSON? (y/n): n
```
```
python theme_detector.py --csv --json
Enter URL(s) to check (separated by commas): https://example.com
```

## Output

The results will be saved to a file named `theme_detector.txt` by default. If the `--csv` flag is used, the results will also be saved as `theme_detector.csv`. Similarly, if the `--json` flag is used, the results will be saved as `theme_detector.json`.

Each file will contain a timestamp, the URL checked, and the theme the website uses.

## Future Plans

- Develop a graphical user interface (GUI) for easier use
- Optimize the performance of checking for a theme for large web pages
- Extend support for more themes to detect
