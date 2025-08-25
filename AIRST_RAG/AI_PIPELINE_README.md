# 🤖 AI Pipeline for Research Paper Summarization

This document describes the new AI Pipeline features that have been integrated into your RAG system, providing advanced document analysis using pre-trained transformer models.

## 🚀 Features

### 📋 Document Preprocessing
- **Text Cleaning**: Removes headers, footers, page numbers, and noise
- **Sentence Segmentation**: Splits text into meaningful sentences using NLTK
- **Section Extraction**: Identifies and extracts key sections (abstract, introduction, conclusion, etc.)
- **Text Chunking**: Splits long documents into manageable chunks for AI models

### 🏷️ Named Entity Recognition (NER)
- **Domain-Specific Models**:
  - **Research Papers**: `allenai/scibert_scivocab_uncased`
  - **Legal Documents**: `nlpaueb/legal-bert-base-uncased`
  - **Medical Documents**: `emilyalsentzer/Bio_ClinicalBERT`
  - **General Documents**: `dslim/bert-base-NER`
- **Entity Categories**: People, Organizations, Locations, Dates, Quantities, Misc
- **Confidence Scoring**: Each entity comes with a confidence score

### 📊 Document Classification & Metadata
- **Document Type Classification**: Automatically detects document type
- **Language Detection**: Identifies document language
- **Complexity Analysis**: Calculates readability scores and complexity levels
- **Section Classification**: Analyzes different sections of the document

### 📝 Advanced Summarization
- **Multi-Length Summaries**: Brief, Standard, and Detailed summaries
- **Domain-Specific Models**:
  - **General**: `facebook/bart-large-cnn`
  - **Fast**: `t5-base`
  - **Scientific**: `allenai/scibert_scivocab_uncased`
- **Hybrid Summarization**: Combines extractive and abstractive approaches
- **Section Summaries**: Generates summaries for individual document sections

## 🛠️ Installation

The AI Pipeline requires the following dependencies (already in your `requirements.txt`):

```bash
pip install transformers torch nltk spacy sentence-transformers
```

## 📁 Module Structure

```
AIRST_RAG/
├── preprocessing.py          # Text cleaning and segmentation
├── ner_module.py            # Named Entity Recognition
├── classification_module.py # Document classification and metadata
├── summarizer_module.py     # Advanced summarization
├── rag_pipeline.py          # Main pipeline orchestration
├── test_ai_pipeline.py      # Test script
└── AI_PIPELINE_README.md    # This file
```

## 🎯 Usage

### In Streamlit App

1. **Upload Documents**: Use the "File Upload" tab to upload your PDF/DOCX files
2. **Access AI Pipeline**: Go to the "🤖 AI Pipeline" tab
3. **Select Options**:
   - Choose a file to analyze
   - Select document type (general, research, legal, medical)
   - Choose analysis type (Comprehensive or Quick)
4. **Run Analysis**: Click "🚀 Start AI Analysis"

### Programmatic Usage

```python
from rag_pipeline import process_document_comprehensive, process_document_simple

# Comprehensive analysis
results = process_document_comprehensive(text, document_type="research")

# Quick analysis
results = process_document_simple(text, document_type="legal")
```

## 🔍 Analysis Types

### Quick Analysis
- Basic metadata extraction
- Key entity identification
- Standard summary generation
- Fast processing time

### Comprehensive Analysis
- Full document preprocessing
- Complete entity extraction and categorization
- Multi-length summaries (Brief, Standard, Detailed)
- Section-by-section analysis
- Hybrid summarization
- Key insights extraction
- Detailed complexity analysis

## 📊 Output Format

The pipeline returns structured results including:

```python
{
    "preprocessing": {
        "cleaned_text_length": 5000,
        "num_sentences": 150,
        "num_sections": 5,
        "sections_found": ["abstract", "introduction", "conclusion"]
    },
    "metadata": {
        "language": {"label": "en", "score": 0.99},
        "classification": {"label": "research", "score": 0.85},
        "complexity": {
            "complexity": "medium",
            "readability_score": 65.2,
            "avg_sentence_length": 18.5
        }
    },
    "entities": {
        "all_entities": [...],
        "categorized_entities": {
            "PERSON": [...],
            "ORG": [...],
            "LOC": [...]
        },
        "total_entities": 25
    },
    "summaries": {
        "multi_length": {
            "brief": "...",
            "standard": "...",
            "detailed": "..."
        },
        "section_summaries": {...},
        "hybrid_summarization": {...}
    },
    "insights": {
        "complexity": {...},
        "entities": {...},
        "summary": {...}
    }
}
```

## 🧪 Testing

Run the test script to verify everything works:

```bash
python test_ai_pipeline.py
```

## ⚡ Performance Notes

- **First Run**: Models will be downloaded automatically (may take a few minutes)
- **Caching**: Models are cached in memory for subsequent runs
- **GPU Support**: Automatically uses GPU if available
- **Memory Usage**: Large models may require significant RAM

## 🔧 Customization

### Adding New Models

You can easily add new models by modifying the model mappings in each module:

```python
# In ner_module.py
model_mapping = {
    "research": "allenai/scibert_scivocab_uncased",
    "legal": "nlpaueb/legal-bert-base-uncased",
    "medical": "emilyalsentzer/Bio_ClinicalBERT",
    "general": "dslim/bert-base-NER",
    "your_domain": "your/model/path"  # Add your model here
}
```

### Custom Preprocessing

Modify `preprocessing.py` to add custom text cleaning rules:

```python
def clean_text(text):
    # Your custom cleaning logic here
    text = re.sub(r"your_pattern", "replacement", text)
    return text.strip()
```

## 🚨 Troubleshooting

### Common Issues

1. **Import Errors**: Make sure all dependencies are installed
2. **Memory Issues**: Use smaller models or process shorter texts
3. **Model Download Failures**: Check internet connection and try again
4. **CUDA Errors**: Models will automatically fall back to CPU

### Getting Help

- Check the test script output for specific error messages
- Verify all dependencies are installed correctly
- Ensure you have sufficient disk space for model downloads

## 🎉 Benefits

✅ **No API Dependencies**: Works entirely offline with pre-trained models  
✅ **Domain-Specific**: Uses specialized models for different document types  
✅ **Comprehensive Analysis**: Provides detailed insights beyond simple summarization  
✅ **Fast Processing**: Cached models for quick subsequent runs  
✅ **Flexible**: Easy to customize and extend  
✅ **Integrated**: Seamlessly integrated into your existing Streamlit app  

---

**Ready to use!** 🚀 Your AI Pipeline is now integrated and ready to provide advanced document analysis capabilities.
