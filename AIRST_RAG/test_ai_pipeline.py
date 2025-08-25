#!/usr/bin/env python3
"""
Test script for the AI Pipeline modules
"""

import sys
import os

def test_imports():
    """Test if all modules can be imported successfully."""
    print("🔍 Testing module imports...")
    
    try:
        from preprocessing import clean_text, segment_text
        print("✅ preprocessing module imported successfully")
    except ImportError as e:
        print(f"❌ Error importing preprocessing: {e}")
        return False
    
    try:
        from ner_module import extract_key_entities
        print("✅ ner_module imported successfully")
    except ImportError as e:
        print(f"❌ Error importing ner_module: {e}")
        return False
    
    try:
        from classification_module import get_document_metadata
        print("✅ classification_module imported successfully")
    except ImportError as e:
        print(f"❌ Error importing classification_module: {e}")
        return False
    
    try:
        from summarizer_module import generate_multi_length_summaries
        print("✅ summarizer_module imported successfully")
    except ImportError as e:
        print(f"❌ Error importing summarizer_module: {e}")
        return False
    
    try:
        from rag_pipeline import process_document_simple
        print("✅ rag_pipeline imported successfully")
    except ImportError as e:
        print(f"❌ Error importing rag_pipeline: {e}")
        return False
    
    return True

def test_preprocessing():
    """Test preprocessing functions."""
    print("\n🧹 Testing preprocessing functions...")
    
    from preprocessing import clean_text, segment_text
    
    # Test text
    test_text = """
    This is a test document.
    
    It has multiple paragraphs.
    
    Page 1 of 5
    
    Some content here.
    """
    
    # Test cleaning
    cleaned = clean_text(test_text)
    print(f"✅ Text cleaning: {len(cleaned)} characters")
    
    # Test segmentation
    sentences = segment_text(cleaned)
    print(f"✅ Sentence segmentation: {len(sentences)} sentences")
    
    return True

def test_simple_pipeline():
    """Test the simple document processing pipeline."""
    print("\n🚀 Testing simple pipeline...")
    
    from rag_pipeline import process_document_simple
    
    # Test text
    test_text = """
    Artificial Intelligence (AI) is a branch of computer science that aims to create intelligent machines.
    These machines can perform tasks that typically require human intelligence.
    Machine learning is a subset of AI that enables computers to learn and improve from experience.
    Deep learning uses neural networks with multiple layers to process complex patterns.
    """
    
    try:
        results = process_document_simple(test_text, "general")
        
        if "error" not in results:
            print("✅ Simple pipeline executed successfully")
            print(f"   - Summary length: {len(results.get('summary', ''))}")
            print(f"   - Entities found: {len(results.get('entities', []))}")
            return True
        else:
            print(f"❌ Pipeline error: {results['error']}")
            return False
            
    except Exception as e:
        print(f"❌ Pipeline exception: {e}")
        return False

def main():
    """Main test function."""
    print("🤖 AI Pipeline Test Suite")
    print("=" * 50)
    
    # Test imports
    if not test_imports():
        print("\n❌ Import tests failed. Please check your dependencies.")
        return False
    
    # Test preprocessing
    if not test_preprocessing():
        print("\n❌ Preprocessing tests failed.")
        return False
    
    # Test simple pipeline
    if not test_simple_pipeline():
        print("\n❌ Pipeline tests failed.")
        return False
    
    print("\n🎉 All tests passed! AI Pipeline is ready to use.")
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
