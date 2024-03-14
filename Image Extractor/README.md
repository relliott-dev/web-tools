# Image Extractor

## Overview

Image Extractor is a Python script that downloads all images from a specified web page and saves them in a directory

## Features

- Downloads all images from a web page
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

`python image_extractor.py [URL]`

- [URL]: The URL of the web page to check
- [WORDS]: Space-separated words to search for on the page
- [--csv]: Optional flag to export the results as a CSV file
- [--json]: Optional flag to export the results as a JSON file

If the URL and words are not provided as arguments, the script will prompt for input

## Examples

```
python image_extractor.py https://example.com
```
```
python image_extractor.py
Enter a URL to check: https://example.com
```

## Output

The images will be saved in a directory named after the website's domain. The script will print the URLs of the downloaded images and the total number of images downloaded.


## Future Plans

- Develop a graphical user interface (GUI) for easier use
- Extract and save images with their actual file extensions
- Optimize the performance of the word counting process for large web pages
- Add a check to avoid downloading duplicate images
- Allow users to specify a custom directory name or path for saving images
- Improve error handling for different types of exceptions during the image downloading process
- Add functionality to save images in different file formats (e.g., JPEG, PNG, GIF) and/or sizes based on user preferences
