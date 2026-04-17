import sys
import PyPDF2
from pathlib import Path
import re

files_to_process = [
    "Blood Relations.pdf",
    "Calendars.pdf",
    "Clocks.pdf"
]

def extract_pdf_data(pdf_path):
    print(f"Parsing: {pdf_path}")
    path = Path(pdf_path)
    if not path.exists():
        print("File not found")
        return
        
    extracted_data = []
    with open(path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        full_text = ""
        for page in reader.pages:
            full_text += page.extract_text() + "\n"
            
    # Clean up the headers and random newlines
    lines = full_text.split('\n')
    cleaned_text = ""
    for line in lines:
        if "Topic/Course" in line or "Sub-Topic" in line or "THANK YOU" in line:
            continue
        line = line.strip()
        if not line:
            continue
        cleaned_text += line + " "

    out_path = path.stem + "_extracted.txt"
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(cleaned_text.strip())
    print(f"Extraction successful: {out_path}")

for f in files_to_process:
    extract_pdf_data(f)
