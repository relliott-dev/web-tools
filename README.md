# Web Tools

## Overview

This repository contains a collection of web analysis tools designed for various purposes, including word counting, page content extraction, metadata extraction, and more. These tools are built using Python and other technologies, and they are designed to help web developers, SEO specialists, and content creators analyze and optimize their web pages.

## Tools Included

### 1. Broken Links Finder

- Checks a webpage for broken links and reports any links that lead to non-existent or inaccessible pages
- Supports multiple URLs and exports results in CSV and JSON formats

### 2. Broken Image Finder

- Identifies images with broken links on a webpage
- Provides options to save results in CSV and JSON formats

### 3. Image Extractor

- Downloads all images from a given webpage
- Saves images in a specified directory

### 4. Metadata Extractor

- Extracts metadata such as title, description, and keywords from the HTML head section of a webpage
- Supports exporting results to CSV and JSON

### 5. Most Common Words

- Analyzes a web page and identifies the most frequently occurring words
- Provides options to export the results in CSV and JSON formats

### 6. Page Finder

- Identifies all internal links (pages) within a website
- Offers options to export results in CSV and JSON formats

### 7. Social Link Extractor

- Extracts social links from a webpage
- Supports exporting extracted links to CSV and JSON formats

### 8. Speed Tester

- Measures the loading speed of a webpage
- Can output results in text, CSV, or JSON format

### 9. Stripped Content

- Extracts the main content of a webpage, removing all HTML tags
- Supports exporting the stripped content to a text file

### 10. Theme Detector

- Detects the theme or framework used by a website, such as WordPress or Bootstrap
- Allows exporting results as CSV or JSON

### 11. Word Counter

- Counts the occurrences of specified words on a web page
- Can output results in text, CSV, or JSON format

## Installation

To use these tools, you'll need to have Python 3.x installed on your machine. You can download Python from the [official website](https://www.python.org/downloads/).

Once Python is installed, clone this repository to your local machine:

`git clone https://github.com/relliott-dev/web-tools.git`

Navigate to the cloned repository and install the required dependencies:

```
cd web-tools
pip install -r requirements.txt
```

## Usage

Each tool can be run as a standalone Python script. For example, to use the Word Counter tool, navigate to the word_counter directory and run:

`python word_counter.py [URL] [WORDS] [--csv] [--json]`

Replace [URL] with the URL of the web page you want to analyze, and [WORDS] with the words you want to count, separated by spaces. Use the --csv or --json flags to export the results in the respective format.

Refer to the README file within each tool's directory for more detailed usage instructions.

## Contributing

Contributions to this repository are welcome! If you have an idea for a new tool or an improvement to an existing tool, feel free to create a pull request or open an issue.

## License

This project is licensed under the [GNU General Public License](https://www.gnu.org/licenses/gpl-3.0.en.html).
