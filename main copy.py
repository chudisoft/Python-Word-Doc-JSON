import os
import json
from docx import Document

def extract_headings_and_text(doc):
    content = {}
    current_heading = None
    for para in doc.paragraphs:
        if para.style.name.startswith('Heading'):
            current_heading = para.text
            content[current_heading] = ''
        elif current_heading:
            content[current_heading] += para.text + '\n'
    return content

def process_documents(directory):
    all_data = {}
    for filename in os.listdir(directory):
        if filename.endswith('.docx'):
            doc_path = os.path.join(directory, filename)
            doc = Document(doc_path)
            all_data[filename] = extract_headings_and_text(doc)
    return all_data

directory_path = r"C:\Users\csoft\Client\Fiverr\Python Word Doc\docs"
data = process_documents(directory_path)

# Save the data to a JSON file
with open('output.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)

print("JSON file created successfully.")
