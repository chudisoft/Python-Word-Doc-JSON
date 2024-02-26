# Python-Word-Doc

## Description
Python-Word-Doc is a streamlined and powerful tool designed to extract and compile headings and their associated text from multiple Microsoft Word (.docx) documents into a single, organized JSON object. This Python-based solution automates the process of sifting through document contents, effectively transforming traditional document formats into structured, easily manageable data.

## How it Works
The script iterates through each `.docx` file in a specified directory, identifying headings (marked by styles like 'Heading 1', 'Heading 2', etc.) and collecting the text that follows each heading until the next heading is encountered. The data from all documents is merged into a single JSON object, where each key is a unique heading and the value is the concatenated text from all occurrences of that heading across the documents.

### Key Features
- **Automated Content Extraction**: Seamlessly reads through Word documents, identifying and extracting headings and subsequent texts.
- **Aggregated Data Compilation**: Merges content from various documents, organizing it under unique headings in a JSON format, making it ideal for data analysis and content management.
- **Simplicity and Versatility**: User-friendly and adaptable to various use-cases, ranging from content aggregation to data analysis and beyond.

Ideal for professionals, researchers, and anyone looking to digitize and systematize large volumes of document content, Python-Word-Doc offers a novel approach to document management and content analysis.

## Installation
To use this script, you need Python installed on your machine along with the `python-docx` library, which can be installed via pip:

```bash
pip install python-docx
