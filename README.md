# Web Tools

## Overview

This repository contains a collection of web analysis tools designed for various purposes, including word counting, page content extraction, metadata extraction, and more. These tools are built using Python and other technologies, and they are designed to help web developers, SEO specialists, and content creators analyze and optimize their web pages.

## Features

### Broken Links Finder

- Checks a webpage for broken links and reports any links that lead to non-existent or inaccessible pages
- Supports multiple URLs and exports results in CSV and JSON formats

### Broken Image Finder

- Identifies images with broken links on a webpage
- Provides options to save results in CSV and JSON formats

### HTML Validator

- Validates the HTML content of a webpage for common errors
- Outputs the results in text, CSV, or JSON format

### Image Extractor

- Downloads all images from a given webpage
- Saves images in a specified directory

### Metadata Extractor

- Extracts metadata such as title, description, and keywords from the HTML head section of a webpage
- Supports exporting results to CSV and JSON

### Most Common Words

- Analyzes a web page and identifies the most frequently occurring words
- Provides options to export the results in CSV and JSON formats

### Page Finder

- Identifies all internal links (pages) within a website
- Offers options to export results in CSV and JSON formats

### Page Screenshot

- Captures a screenshot of a given webpage and saves it as an image file
- Can handle multiple URLs and save screenshots in a specified directory

### Social Link Extractor

- Extracts social links from a webpage
- Supports exporting extracted links to CSV and JSON formats

### Speed Tester

- Measures the loading speed of a webpage
- Can output results in text, CSV, or JSON format

### Stripped Content

- Extracts the main content of a webpage, removing all HTML tags
- Supports exporting the stripped content to a text file

### Theme Detector

- Detects the theme or framework used by a website, such as WordPress or Bootstrap
- Allows exporting results as CSV or JSON

### Word Counter

- Counts the occurrences of specified words on a web page
- Can output results in text, CSV, or JSON format

### Planned Features

- Unified interface with tabs for each analysis tool
- Batch processing for multiple URLs at once
- Real-time progress indicators and export status
- Charts and data visualization panels for results
- Centralized export manager for CSV, JSON, and screenshots
- Configurable settings for user preferences

## Requirements

- Python 3.10 or higher
- Required packages listed in `requirements.txt`

## Installation

1. Clone or download the repository.

2. Ensure that Python is installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

3. Install the required dependencies:

```
pip install -r requirements.txt
```

## Usage

Each tool can be run **as a standalone Python script** or **invoked directly from the command line**.

For example, to use the Word Counter tool:

`python word_counter.py [URL] [WORDS] [--csv] [--json]`

Replace [URL] with the URL of the web page you want to analyze, and [WORDS] with the words you want to count, separated by spaces. Use the --csv or --json flags to export the results in the respective format.

Refer to the README file within each tool's directory for more detailed usage instructions.

## Contributing

Contributions to this repository are welcome! If you have an idea for a new tool or an improvement to an existing tool, feel free to create a pull request or open an issue.

## License

This project is licensed under the [GNU General Public License](https://www.gnu.org/licenses/gpl-3.0.en.html).
