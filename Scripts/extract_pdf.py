import sys
import PyPDF2
from pathlib import Path

pdf_path = Path("Averages 1.pdf")
with open(pdf_path, 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    text = ""
    for i, page in enumerate(reader.pages):
        text += f"\n--- Page {i+1} ---\n"
        text += page.extract_text()

with open('temp_pdf_output.txt', 'w', encoding='utf-8') as out:
    out.write(text)
print(f"Extracted {len(reader.pages)} pages.")
