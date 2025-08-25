import streamlit as st
from transformers import pipeline
import torch

# Global cache for summarizers
_summarizers = {}

def load_summarizer(model_name="facebook/bart-large-cnn"):
    """Load summarization model with caching."""
    if model_name in _summarizers:
        return _summarizers[model_name]
    
    try:
        with st.spinner(f"Loading summarizer: {model_name}"):
            summarizer = pipeline(
                "summarization", 
                model=model_name,
                device=0 if torch.cuda.is_available() else -1
            )
            _summarizers[model_name] = summarizer
            return summarizer
            
    except Exception as e:
        st.error(f"Error loading summarizer {model_name}: {e}")
        return None

def safe_summarize(text, summarizer, max_len=200, min_len=80):
    """Safe wrapper for summarization with comprehensive error handling"""
    if not text or not summarizer:
        return "Unable to generate summary."
    
    try:
        # Validate input
        if not isinstance(text, str) or len(text.strip()) == 0:
            return "No text provided for summarization."
        
        # Clean and prepare text
        text = text.strip()
        if len(text) < 10:
            return "Text too short for summarization."
        
        # Truncate if too long
        if len(text) > 10000:
            text = text[:10000]
        
        # Attempt summarization
        result = summarizer(
            text, 
            max_length=max_len, 
            min_length=min_len, 
            do_sample=False
        )
        
        # Validate result
        if (result and 
            isinstance(result, list) and 
            len(result) > 0 and 
            isinstance(result[0], dict) and 
            "summary_text" in result[0]):
            return result[0]["summary_text"]
        else:
            return "Unable to generate summary from the provided text."
            
    except IndexError:
        return "Summarization failed: Model returned empty result."
    except Exception as e:
        return f"Summarization error: {str(e)}"

def generate_summary(text, summarizer, max_len=200, min_len=80):
    """Generate summary using the provided summarizer."""
    if not text or not summarizer:
        return "Unable to generate summary."
    
    try:
        # Handle long texts by chunking
        if len(text) > 1024:
            chunks = chunk_text_for_summarization(text)
            summaries = []
            
            for chunk in chunks[:3]:  # Limit to first 3 chunks
                if len(chunk) > 50:  # Only summarize substantial chunks
                    chunk_summary = safe_summarize(chunk, summarizer, max_len, min_len)
                    if chunk_summary and chunk_summary != "Unable to generate summary.":
                        summaries.append(chunk_summary)
            
            # Combine summaries
            if summaries:
                combined_summary = " ".join(summaries)
                # Create final summary of combined summaries
                final_summary = safe_summarize(combined_summary, summarizer, max_len, min_len)
                return final_summary
            else:
                return "Unable to generate summary from text chunks."
        else:
            # Direct summarization for shorter texts
            return safe_summarize(text, summarizer, max_len, min_len)
            
    except Exception as e:
        st.error(f"Error in summarization: {e}")
        return f"Summarization failed: {str(e)}"

def chunk_text_for_summarization(text, chunk_size=1000):
    """Split text into chunks suitable for summarization."""
    from preprocessing import segment_text
    
    sentences = segment_text(text)
    chunks = []
    current_chunk = ""
    
    for sentence in sentences:
        if len(current_chunk) + len(sentence) < chunk_size:
            current_chunk += sentence + " "
        else:
            if current_chunk.strip():
                chunks.append(current_chunk.strip())
            current_chunk = sentence + " "
    
    if current_chunk.strip():
        chunks.append(current_chunk.strip())
    
    return chunks

def get_domain_specific_summarizer(document_type):
    """Get appropriate summarizer based on document type."""
    model_mapping = {
        "research": "facebook/bart-large-cnn",  # Good for academic text
        "legal": "facebook/bart-large-cnn",     # Good for formal documents
        "medical": "facebook/bart-large-cnn",   # Good for technical text
        "general": "facebook/bart-large-cnn",
        "fast": "t5-base",                      # Faster but lighter
        "scientific": "allenai/scibert_scivocab_uncased"
    }
    
    model_name = model_mapping.get(document_type.lower(), "facebook/bart-large-cnn")
    return load_summarizer(model_name)

def generate_multi_length_summaries(text, document_type="general"):
    """Generate summaries of different lengths."""
    summarizer = get_domain_specific_summarizer(document_type)
    
    summaries = {}
    
    # Brief summary (1-2 sentences)
    summaries["brief"] = generate_summary(text, summarizer, max_len=100, min_len=30)
    
    # Standard summary (2-3 paragraphs)
    summaries["standard"] = generate_summary(text, summarizer, max_len=200, min_len=80)
    
    # Detailed summary (3-4 paragraphs)
    summaries["detailed"] = generate_summary(text, summarizer, max_len=300, min_len=150)
    
    return summaries

def generate_section_summaries(text):
    """Generate summaries for different sections of a document."""
    from preprocessing import extract_key_sections
    
    sections = extract_key_sections(text)
    section_summaries = {}
    
    summarizer = load_summarizer()
    
    for section_name, section_text in sections.items():
        if section_text and len(section_text) > 50:
            summary = generate_summary(section_text, summarizer, max_len=150, min_len=50)
            section_summaries[section_name] = summary
    
    return section_summaries

def extractive_summarization(text, top_k=5):
    """Extractive summarization using sentence ranking."""
    from preprocessing import segment_text
    from sentence_transformers import SentenceTransformer
    import numpy as np
    
    sentences = segment_text(text)
    
    if len(sentences) <= top_k:
        return " ".join(sentences)
    
    try:
        # Load sentence transformer model
        model = SentenceTransformer("all-MiniLM-L6-v2")
        
        # Get sentence embeddings
        embeddings = model.encode(sentences)
        
        # Calculate sentence importance (using cosine similarity to document center)
        doc_embedding = np.mean(embeddings, axis=0)
        similarities = []
        
        for embedding in embeddings:
            similarity = np.dot(embedding, doc_embedding) / (np.linalg.norm(embedding) * np.linalg.norm(doc_embedding))
            similarities.append(similarity)
        
        # Get top sentences
        top_indices = np.argsort(similarities)[-top_k:]
        top_indices = sorted(top_indices)  # Maintain original order
        
        # Extract top sentences
        top_sentences = [sentences[i] for i in top_indices]
        
        return " ".join(top_sentences)
        
    except Exception as e:
        st.error(f"Error in extractive summarization: {e}")
        # Fallback to first few sentences
        return " ".join(sentences[:top_k])

def hybrid_summarization(text, document_type="general"):
    """Combine extractive and abstractive summarization."""
    # First, do extractive summarization to get key sentences
    extractive_summary = extractive_summarization(text, top_k=8)
    
    # Then, do abstractive summarization on the extractive summary
    summarizer = get_domain_specific_summarizer(document_type)
    final_summary = generate_summary(extractive_summary, summarizer, max_len=250, min_len=100)
    
    return {
        "extractive_summary": extractive_summary,
        "final_summary": final_summary
    }

def format_summary_for_display(summary, summary_type="standard"):
    """Format summary for nice display."""
    if not summary:
        return "No summary available."
    
    # Add header based on type
    headers = {
        "brief": "📝 **Brief Summary**",
        "standard": "📋 **Standard Summary**", 
        "detailed": "📄 **Detailed Summary**",
        "extractive": "🔍 **Extractive Summary**",
        "final": "✨ **Final Summary**"
    }
    
    header = headers.get(summary_type, "📋 **Summary**")
    
    return f"{header}\n\n{summary}"
