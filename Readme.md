# PDF Page Counter

## Description
This script recursively scans a specified folder for PDF files, counts the number of pages in each PDF, and outputs the results to a CSV file.

## Requirements
- Python 3
- PyPDF2 library (Install using `pip install PyPDF2`)

## Usage
1. Install Python 3 and PyPDF2 if not already installed.
2. Save the script `pdf_page_counter.py`.
3. Run the script with the folder path as an argument.

   Example: `python pdf_page_counter.py /path/to/folder`

   This will scan `/path/to/folder` for PDF files.

4. After execution, the script will create a CSV file named `pdf_page_count.csv` in the current directory. This file contains two columns: `File Path` and `Number of Pages`.

## Notes
- The script counts the pages of each PDF file found in the specified directory and its subdirectories.
- If a PDF file cannot be read, it will be reported in the console, and the number of pages will be listed as -1 in the CSV.
