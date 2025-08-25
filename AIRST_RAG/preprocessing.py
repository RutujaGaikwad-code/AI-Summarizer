import re
import nltk
import streamlit as st

# Download NLTK data (only once)
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download("punkt", quiet=True)

from nltk.tokenize import sent_tokenize

def clean_text(text):
    """Remove headers, footers, extra spaces, and noise."""
    if not text:
        return ""
    
    # Remove page numbers
    text = re.sub(r"Page \d+", "", text)
    text = re.sub(r"\b\d+\s*of\s*\d+\b", "", text)
    
    # Remove excessive newlines and spaces
    text = re.sub(r"\n+", " ", text)
    text = re.sub(r"\s+", " ", text)
    
    # Remove common PDF artifacts
    text = re.sub(r"©\s*\d{4}", "", text)
    text = re.sub(r"All rights reserved", "", text)
    
    # Remove email addresses
    text = re.sub(r'\S+@\S+', '', text)
    
    # Remove URLs
    text = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', text)
    
    return text.strip()

def segment_text(text):
    """Split text into sentences for easier handling."""
    if not text:
        return []
    
    try:
        sentences = sent_tokenize(text)
        return [s.strip() for s in sentences if s.strip()]
    except Exception as e:
        st.warning(f"Error in sentence tokenization: {e}")
        # Fallback: split by periods
        return [s.strip() for s in text.split('.') if s.strip()]

def chunk_text_for_models(text, max_length=512):
    """Split text into chunks suitable for transformer models."""
    sentences = segment_text(text)
    chunks = []
    current_chunk = ""
    
    for sentence in sentences:
        if len(current_chunk) + len(sentence) < max_length:
            current_chunk += sentence + " "
        else:
            if current_chunk.strip():
                chunks.append(current_chunk.strip())
            current_chunk = sentence + " "
    
    if current_chunk.strip():
        chunks.append(current_chunk.strip())
    
    return chunks

def extract_key_sections(text):
    """Extract key sections like abstract, introduction, conclusion."""
    sections = {}
    
    # Common section headers
    section_patterns = {
        'abstract': r'(?i)(abstract|summary|executive\s+summary)',
        'introduction': r'(?i)(introduction|intro)',
        'conclusion': r'(?i)(conclusion|conclusions|summary)',
        'methodology': r'(?i)(methodology|methods|method)',
        'results': r'(?i)(results|findings)',
        'discussion': r'(?i)(discussion|discuss)'
    }
    
    lines = text.split('\n')
    current_section = None
    current_content = []
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Check if this line is a section header
        found_section = None
        for section_name, pattern in section_patterns.items():
            if re.search(pattern, line):
                found_section = section_name
                break
        
        if found_section:
            # Save previous section
            if current_section and current_content:
                sections[current_section] = ' '.join(current_content)
            
            # Start new section
            current_section = found_section
            current_content = []
        elif current_section:
            current_content.append(line)
    
    # Save last section
    if current_section and current_content:
        sections[current_section] = ' '.join(current_content)
    
    return sections
