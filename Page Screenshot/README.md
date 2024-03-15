# Page Screenshot

## Overview

The Page Screenshot Tool is a Python script that captures a screenshot of a given webpage and saves it as an image file

## Features

- Captures a screenshot of a webpage and saves it as an image file
- Checks the website's `robots.txt` file for scraping permissions
- Supports multiple URLs and captures screenshots for each
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

`python page_screenshot.py [URL(s)]`

- [URL(s)]: The URL(s) of each web page to check

If the URL(s) are not provided as arguments, the script will prompt for input

## Examples

```
python page_screenshot.py example, example2
```
```
python page_screenshot.py
Enter URL(s) to check (separated by commas): https://example.com
```

## Output

The script will save the screenshot(s) in the same directory as the script, with filenames based on the domain name of the URL(s).

## Future Plans

- Develop a graphical user interface (GUI) for easier use
- Extend support for capturing screenshots in different file formats and sizes
- Add options for customizing screenshot dimensions and quality
