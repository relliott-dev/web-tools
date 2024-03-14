# Social Link Extractor

## Overview

The Social Link Extractor is a Python script that extracts social media links from a website

## Features

- Extracts social media links from a website
- Supports multiple social media platforms including Facebook, Twitter, LinkedIn, Instagram, YouTube, Pinterest, Discord, GitHub, and WhatsApp
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

`python social_link_extractor.py [URL(s)] [--csv] [--json]`

- [URL(s)]: The URL(s) of each web page to check
- [--csv]: Optional flag to export the results as a CSV file
- [--json]: Optional flag to export the results as a JSON file

If the URL and words are not provided as arguments, the script will prompt for input

## Examples

```
python social_link_extractor.py example, example2
Export results as CSV? (y/n): y
Export results as JSON? (y/n): n
```
```
python social_link_extractor.py --csv --json
Enter URL(s) to check (separated by commas): https://example.com
```

## Output

The results will be saved to a file named `social_link_extractor.txt` by default. If the `--csv` flag is used, the results will also be saved as `social_link_extractor.csv`. Similarly, if the `--json` flag is used, the results will be saved as `social_link_extractor.json`.

Each file will contain a timestamp, the URL checked, the number of social media links found, and the links themselves

## Future Plans

- Develop a graphical user interface (GUI) for easier use
- Optimize the performance of the script for faster link extraction
- Extend support for more social media platforms
