# Python-Word-Doc

## Description
This repository contains a Python script that automates the process of extracting headings and their corresponding texts from multiple Microsoft Word documents. The extracted content is then compiled into a single JSON object. This can be particularly useful for aggregating and analyzing document contents programmatically.

## How it Works
The script iterates through each `.docx` file in a specified directory, identifying headings (marked by styles like 'Heading 1', 'Heading 2', etc.) and collecting the text that follows each heading until the next heading is encountered. The data from all documents is merged into a single JSON object, where each key is a unique heading and the value is the concatenated text from all occurrences of that heading across the documents.

## Installation
To use this script, you need Python installed on your machine along with the `python-docx` library, which can be installed via pip:

```bash
pip install python-docx
