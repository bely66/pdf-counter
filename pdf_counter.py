import os
import sys
import PyPDF2
import csv


def count_pdf_pages(pdf_path):
    try:
        with open(pdf_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            return len(reader.pages)
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
        return -1


def collect_pdfs(dir_path):
    pdf_files = []
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if file.lower().endswith(".pdf"):
                pdf_files.append(os.path.join(root, file))
    return pdf_files


def create_csv(pdf_files, csv_path):
    with open(csv_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["File Path", "Number of Pages"])
        for pdf in pdf_files:
            num_pages = count_pdf_pages(pdf)
            writer.writerow([pdf, num_pages])


def main(folder_path):
    pdf_files = collect_pdfs(folder_path)
    output_csv = "pdf_page_count.csv"
    create_csv(pdf_files, output_csv)
    print(f"CSV file created: {output_csv}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python pdf_page_counter.py <folder_path>")
        sys.exit(1)
    main(sys.argv[1])
