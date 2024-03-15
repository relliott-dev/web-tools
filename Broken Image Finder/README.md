# Broken Image Finder

## Overview

Broken Image Finder is a Python script that checks a webpage for broken images

## Features

- Checks a webpage for broken images
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

`python broken_image_finder.py [URL(s)] [--csv] [--json]`

- [URL(s)]: The URL(s) of each web page to check
- [--csv]: Optional flag to export the results as a CSV file
- [--json]: Optional flag to export the results as a JSON file

If the URL and words are not provided as arguments, the script will prompt for input

## Examples

```
python broken_image_finder.py example, example2
Export results as CSV? (y/n): y
Export results as JSON? (y/n): n
```
```
python broken_image_finder.py --csv --json
Enter URL(s) to check (separated by commas): https://example.com
```

## Output

The results will be saved to a file named `broken_image_finder.txt` by default. If the `--csv` flag is used, the results will also be saved as `broken_image_finder.csv`. Similarly, if the `--json` flag is used, the results will be saved as `broken_image_finder.json`.

Each file will contain a timestamp, the URL checked, the total number of broken images, and a list of broken image URLs

## Future Plans

- Develop a graphical user interface (GUI) for easier use
- Add URL filtering options to include or exclude certain types of URLs from the check
- Optimize the performance of the image checking process for large web pages
- Add more detail for where the image is failing within the script
