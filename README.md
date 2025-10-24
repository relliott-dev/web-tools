# Web Tools

## Overview

This repository contains a collection of web analysis tools designed for various purposes, including word counting, page content extraction, metadata extraction, and more. These tools are built using Python and other technologies, and they are designed to help web developers, SEO specialists, and content creators analyze and optimize their web pages.

## Features

### Broken Links Finder
- Check webpages for broken or inaccessible links
- Handle multiple URLs and export results to CSV/JSON

### Broken Image Finder
- Identify images with broken or invalid sources
- Export findings to CSV/JSON

### HTML Validator
- Validate HTML content for common errors
- Output validation results as text, CSV, or JSON

### Image Extractor
- Download all images from a given webpage
- Save files to a chosen directory

### Metadata Extractor
- Extract title, description, and keywords from the HTML `<head>`
- Export metadata to CSV/JSON

### Most Common Words
- Analyze a webpage for frequency of words
- Export frequency tables to CSV/JSON

### Page Finder
- Find internal links across a site
- Export discovered URLs to CSV/JSON

### Page Screenshot
- Capture screenshots of webpages (single or multiple)
- Save images to a specified directory

### Social Link Extractor
- Extract social profile links from webpages
- Export links to CSV/JSON

### Speed Tester
- Measure page load performance
- Output metrics as text, CSV, or JSON

### Stripped Content
- Strip HTML to extract main text content
- Save extracted text to file

### Theme Detector
- Detect frameworks/themes (e.g., WordPress, Bootstrap)
- Export detection results to CSV/JSON

### Word Counter
- Count specified words on a page
- Output counts as text, CSV, or JSON

## Planned Features

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

## Contributing

Contributions to this repository are welcome! If you have an idea for a new tool or an improvement to an existing tool, feel free to create a pull request or open an issue.

## License

This project is licensed under the [GNU General Public License](https://www.gnu.org/licenses/gpl-3.0.en.html).
