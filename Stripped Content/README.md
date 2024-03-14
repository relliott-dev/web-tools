# Stripped Content

## Overview

Stripped Content is a Python script that takes a URL as input and extracts the text content of the specified web page, preserving the structure of the original HTML as much as possible

## Features

- Extracts text content from a web page with preserved structure
- Checks the website's `robots.txt` file for scraping permissions
- Outputs the results to a text file
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

`python stripped_content.py [URL]`

[URL]: The URL of the web page to check

If the URL is not provided as an argument, the script will prompt for input

## Examples

```
python stripped_content.py https://example.com
```
```
python stripped_content.py
Enter a URL to check: example
```

## Output

The results will be saved to a file named `stripped_content.txt` by default.

The file will contain a timestamp, the URL checked, and the stripped content from the page.

## Future Plans

- Develop a graphical user interface (GUI) for easier use
- Allow multiple websites to be scraped at the same time
