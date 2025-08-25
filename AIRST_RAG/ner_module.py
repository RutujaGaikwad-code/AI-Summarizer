import streamlit as st
from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline
import torch

# Global cache for models
_ner_models = {}

def load_ner_model(model_name="dslim/bert-base-NER"):
    """Load NER model with caching to avoid reloading."""
    if model_name in _ner_models:
        return _ner_models[model_name]
    
    try:
        with st.spinner(f"Loading NER model: {model_name}"):
            tokenizer = AutoTokenizer.from_pretrained(model_name)
            model = AutoModelForTokenClassification.from_pretrained(model_name)
            
            # Create pipeline
            ner_pipeline = pipeline(
                "ner", 
                model=model, 
                tokenizer=tokenizer, 
                aggregation_strategy="simple",
                device=0 if torch.cuda.is_available() else -1
            )
            
            _ner_models[model_name] = ner_pipeline
            return ner_pipeline
            
    except Exception as e:
        st.error(f"Error loading NER model {model_name}: {e}")
        return None

def extract_entities(text, model_pipeline, max_length=512):
    """Extract named entities from text."""
    if not text or not model_pipeline:
        return []
    
    try:
        # Truncate text if too long
        if len(text) > max_length:
            text = text[:max_length]
        
        entities = model_pipeline(text)
        return entities
        
    except Exception as e:
        st.error(f"Error extracting entities: {e}")
        return []

def get_domain_specific_ner_model(document_type):
    """Get appropriate NER model based on document type."""
    model_mapping = {
        "research": "allenai/scibert_scivocab_uncased",
        "legal": "nlpaueb/legal-bert-base-uncased",
        "medical": "emilyalsentzer/Bio_ClinicalBERT",
        "general": "dslim/bert-base-NER"
    }
    
    model_name = model_mapping.get(document_type.lower(), "dslim/bert-base-NER")
    return load_ner_model(model_name)

def categorize_entities(entities):
    """Categorize entities by type for better organization."""
    categories = {
        'PERSON': [],
        'ORG': [],
        'LOC': [],
        'MISC': [],
        'DATE': [],
        'QUANTITY': []
    }
    
    for entity in entities:
        entity_type = entity.get('entity_group', 'MISC')
        if entity_type in categories:
            categories[entity_type].append(entity)
        else:
            categories['MISC'].append(entity)
    
    return categories

def extract_key_entities(text, document_type="general", top_k=10):
    """Extract and rank key entities from text."""
    model = get_domain_specific_ner_model(document_type)
    entities = extract_entities(text, model)
    
    if not entities:
        return []
    
    # Sort by confidence score
    entities.sort(key=lambda x: x.get('score', 0), reverse=True)
    
    # Remove duplicates (keep highest confidence)
    seen = set()
    unique_entities = []
    
    for entity in entities:
        entity_text = entity.get('word', '').lower()
        if entity_text not in seen:
            seen.add(entity_text)
            unique_entities.append(entity)
    
    return unique_entities[:top_k]

def format_entities_for_display(entities):
    """Format entities for nice display in Streamlit."""
    if not entities:
        return "No entities found."
    
    formatted = []
    for entity in entities:
        word = entity.get('word', '')
        entity_type = entity.get('entity_group', 'MISC')
        confidence = entity.get('score', 0)
        
        formatted.append(f"**{word}** ({entity_type}) - {confidence:.2f}")
    
    return "\n".join(formatted)
