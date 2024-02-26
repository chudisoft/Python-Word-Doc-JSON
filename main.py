import os
import json
from docx import Document

def extract_headings_and_text(doc, all_data):
    current_heading = None
    for para in doc.paragraphs:
        if para.style.name.startswith('Heading'):
            current_heading = para.text
            if current_heading not in all_data:
                all_data[current_heading] = ''
        elif current_heading:
            all_data[current_heading] += para.text + '\n'

def process_documents(directory):
    all_data = {}
    for filename in os.listdir(directory):
        if filename.endswith('.docx'):
            doc_path = os.path.join(directory, filename)
            doc = Document(doc_path)
            extract_headings_and_text(doc, all_data)
    return all_data

directory_path = r"C:\Users\csoft\Client\Fiverr\Python Word Doc\docs"
combined_data = process_documents(directory_path)

# Save the data to a JSON file
with open('output.json', 'w') as json_file:
    json.dump(combined_data, json_file, indent=4)

print("JSON file created successfully.")
