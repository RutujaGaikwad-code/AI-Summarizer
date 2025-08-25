# AIRST_RAG/models.py
from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline

# -----------------------------
# Load NER models
# -----------------------------
def load_bert_ner():
    model_name = "dslim/bert-base-NER"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForTokenClassification.from_pretrained(model_name)
    return pipeline("ner", model=model, tokenizer=tokenizer, grouped_entities=True)

def load_scibert_ner():
    model_name = "allenai/scibert_scivocab_uncased"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForTokenClassification.from_pretrained("dslim/bert-base-NER")
    return pipeline("ner", model=model, tokenizer=tokenizer, grouped_entities=True)

def load_legalbert_ner():
    model_name = "nlpaueb/legal-bert-base-uncased"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForTokenClassification.from_pretrained("Jean-Baptiste/roberta-large-ner-english")
    return pipeline("ner", model=model, tokenizer=tokenizer, grouped_entities=True)

# -----------------------------
# Zero-Shot Domain Classifier with error handling
# -----------------------------
try:
    zero_shot_clf = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
except Exception as e:
    print(f"Warning: Could not load zero-shot classifier: {e}")
    zero_shot_clf = None

def predict_domain(text: str) -> str:
    try:
        if not text or len(text.strip()) < 10:
            return "general"
        
        if zero_shot_clf is None:
            return "general"
        
        labels = ["legal", "scientific", "report"]
        result = zero_shot_clf(text, candidate_labels=labels)
        
        if result and "labels" in result and len(result["labels"]) > 0:
            return result["labels"][0]
        else:
            return "general"
    except Exception as e:
        return "general"

# -----------------------------
# Summarizer with error handling
# -----------------------------
try:
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
except Exception as e:
    print(f"Warning: Could not load summarizer model: {e}")
    summarizer = None

# -----------------------------
# Load models once with error handling
# -----------------------------
try:
    bert_ner = load_bert_ner()
except Exception as e:
    print(f"Warning: Could not load BERT NER model: {e}")
    bert_ner = None

try:
    scibert_ner = load_scibert_ner()
except Exception as e:
    print(f"Warning: Could not load SciBERT NER model: {e}")
    scibert_ner = None

try:
    legalbert_ner = load_legalbert_ner()
except Exception as e:
    print(f"Warning: Could not load LegalBERT NER model: {e}")
    legalbert_ner = None

def create_fallback_summary(text: str) -> str:
    """Create a simple extractive summary when transformer models fail"""
    try:
        # Split into sentences
        sentences = text.split('.')
        sentences = [s.strip() for s in sentences if s.strip()]
        
        if len(sentences) <= 3:
            return text[:500] + "..." if len(text) > 500 else text
        
        # Take first few sentences as summary
        summary_sentences = sentences[:3]
        summary = '. '.join(summary_sentences) + '.'
        
        return summary
    except Exception:
        return text[:300] + "..." if len(text) > 300 else text

def process_text(text: str):
    """Run classification, NER, and summarization on input text"""
    try:
        # Validate input text
        if not text or not isinstance(text, str) or len(text.strip()) == 0:
            return {
                "domain": "general",
                "entities": [],
                "summary": "No text provided for analysis."
            }
        
        # Clean and prepare text
        text = text.strip()
        if len(text) < 10:
            return {
                "domain": "general",
                "entities": [],
                "summary": "Text too short for meaningful analysis."
            }
        
        # Domain classification with error handling
        try:
            domain = predict_domain(text)
        except Exception as domain_error:
            domain = "general"
        
        # NER with error handling
        try:
            if domain == "legal" and legalbert_ner is not None:
                ner_model = legalbert_ner
            elif domain == "scientific" and scibert_ner is not None:
                ner_model = scibert_ner
            elif bert_ner is not None:
                ner_model = bert_ner
            else:
                # Fallback if no models are available
                entities = []
                raise Exception("No NER models available")
            
            entities = ner_model(text)
            if not entities:
                entities = []
        except Exception as ner_error:
            entities = []
        
        # Summarization with comprehensive error handling
        try:
            if summarizer is None:
                summary_text = create_fallback_summary(text)
            else:
                # Check if text is too long for the model
                if len(text) > 10000:
                    # Truncate text to avoid model limits
                    text = text[:10000]
                
                summary_result = summarizer(text, max_length=150, min_length=40, do_sample=False)
                
                # Multiple checks for valid result
                if (summary_result and 
                    isinstance(summary_result, list) and 
                    len(summary_result) > 0 and 
                    isinstance(summary_result[0], dict) and 
                    "summary_text" in summary_result[0]):
                    summary_text = summary_result[0]["summary_text"]
                else:
                    summary_text = create_fallback_summary(text)
                    
        except IndexError as index_error:
            summary_text = create_fallback_summary(text)
        except Exception as summary_error:
            summary_text = create_fallback_summary(text)

        return {
            "domain": domain,
            "entities": entities,
            "summary": summary_text
        }
    except Exception as e:
        return {
            "domain": "general",
            "entities": [],
            "summary": create_fallback_summary(text) if text else "No text provided for analysis."
        }
