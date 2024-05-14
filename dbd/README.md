# Drive-By Download Link Checker

This Python script is designed to scan a given webpage for potential drive-by download links. It fetches the webpage content, parses it, and checks all the links to identify any that might point to executable files, which are often used in drive-by download attacks.

## Features

- Fetches and parses HTML content from a specified URL.
- Identifies links pointing to executable file formats (.exe, .zip, .msi, .dmg, .pkg).
- Prints out the drive-by download links and marks if they are safe links.

## Requirements
- `requests` lib
- `beautifulsoup4` lib

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/drive-by-download-checker.git
    cd drive-by-download-checker
    ```

2. Install the required libraries:
    ```bash
    pip install requests beautifulsoup4
    ```

## Usage

1. Update the `url` variable to point to the desired target webpage:
    ```python
    url = "http://example-vulnerable-app.com"
    ```

2. Run the script:
    ```bash
    python check_drive_by_download.py
    ```

3. The script will output the identified drive-by download links and safe links.

## Example Output:

```plaintext
Drive-By Download link : http://example-vulnerable-app.com/malicious.exe
Safe-link: http://example-vulnerable-app.com/about

