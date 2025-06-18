
import fitz  # PyMuPDF
import re

def parse_resume(file_stream):
    text = ""
    try:
        doc = fitz.open(stream=file_stream.read(), filetype="pdf")
        for page in doc:
            text += page.get_text()
    except Exception as e:
        text = ""

    skills = extract_skills(text)
    return {
        'text': text,
        'skills': skills
    }

def extract_skills(text):
    keywords = ['Python', 'Java', 'AI', 'Machine Learning', 'Data Analysis', 'Flask', 'SQL', 'HTML', 'CSS', 'JavaScript']
    found = [kw for kw in keywords if kw.lower() in text.lower()]
    return found

