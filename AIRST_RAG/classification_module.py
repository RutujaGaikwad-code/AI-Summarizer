import streamlit as st
from transformers import pipeline
import torch

# Global cache for classifiers
_classifiers = {}

def load_classifier(model_name="allenai/scibert_scivocab_uncased"):
    """Load text classification model with caching."""
    if model_name in _classifiers:
        return _classifiers[model_name]
    
    try:
        with st.spinner(f"Loading classifier: {model_name}"):
            classifier = pipeline(
                "text-classification", 
                model=model_name,
                device=0 if torch.cuda.is_available() else -1
            )
            _classifiers[model_name] = classifier
            return classifier
            
    except Exception as e:
        st.error(f"Error loading classifier {model_name}: {e}")
        return None

def classify_document(text, model_name="allenai/scibert_scivocab_uncased"):
    """Classify document type."""
    if not text:
        return {"label": "unknown", "score": 0.0}
    
    classifier = load_classifier(model_name)
    if not classifier:
        return {"label": "unknown", "score": 0.0}
    
    try:
        # Use only first 512 tokens for classification
        truncated_text = text[:512]
        result = classifier(truncated_text)
        
        # Handle both single and batch results
        if isinstance(result, list):
            return result[0]
        return result
        
    except Exception as e:
        st.error(f"Error in document classification: {e}")
        return {"label": "unknown", "score": 0.0}

def get_domain_classifier(document_type):
    """Get appropriate classifier based on expected document type."""
    model_mapping = {
        "research": "allenai/scibert_scivocab_uncased",
        "legal": "nlpaueb/legal-bert-base-uncased",
        "medical": "emilyalsentzer/Bio_ClinicalBERT",
        "general": "distilbert-base-uncased"
    }
    
    model_name = model_mapping.get(document_type.lower(), "distilbert-base-uncased")
    return load_classifier(model_name)

def classify_document_sections(text):
    """Classify different sections of a document."""
    from preprocessing import extract_key_sections
    
    sections = extract_key_sections(text)
    classifications = {}
    
    for section_name, section_text in sections.items():
        if section_text:
            classification = classify_document(section_text)
            classifications[section_name] = classification
    
    return classifications

def detect_document_language(text):
    """Detect the language of the document."""
    try:
        from transformers import pipeline
        language_detector = pipeline("text-classification", model="papluca/xlm-roberta-base-language-detection")
        
        # Use first 100 characters for language detection
        sample_text = text[:100]
        result = language_detector(sample_text)
        
        return result[0] if isinstance(result, list) else result
        
    except Exception as e:
        st.warning(f"Language detection failed: {e}")
        return {"label": "en", "score": 1.0}

def analyze_document_complexity(text):
    """Analyze document complexity and readability."""
    from preprocessing import segment_text
    
    sentences = segment_text(text)
    words = text.split()
    
    if not sentences or not words:
        return {"complexity": "unknown", "readability_score": 0}
    
    # Calculate basic metrics
    avg_sentence_length = len(words) / len(sentences)
    avg_word_length = sum(len(word) for word in words) / len(words)
    
    # Determine complexity level
    if avg_sentence_length > 25 or avg_word_length > 6:
        complexity = "high"
    elif avg_sentence_length > 15 or avg_word_length > 5:
        complexity = "medium"
    else:
        complexity = "low"
    
    # Simple readability score (0-100)
    readability_score = max(0, 100 - (avg_sentence_length * 2 + avg_word_length * 5))
    
    return {
        "complexity": complexity,
        "readability_score": round(readability_score, 1),
        "avg_sentence_length": round(avg_sentence_length, 1),
        "avg_word_length": round(avg_word_length, 1),
        "total_sentences": len(sentences),
        "total_words": len(words)
    }

def get_document_metadata(text):
    """Extract comprehensive document metadata."""
    metadata = {}
    
    # Language detection
    language_info = detect_document_language(text)
    metadata["language"] = language_info
    
    # Complexity analysis
    complexity_info = analyze_document_complexity(text)
    metadata["complexity"] = complexity_info
    
    # Document classification
    classification = classify_document(text)
    metadata["classification"] = classification
    
    # Section classification
    section_classifications = classify_document_sections(text)
    metadata["sections"] = section_classifications
    
    return metadata

def format_classification_for_display(classification):
    """Format classification results for display."""
    if not classification:
        return "Classification failed."
    
    label = classification.get('label', 'unknown')
    score = classification.get('score', 0)
    
    return f"**{label}** (confidence: {score:.2f})"
