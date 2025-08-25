import streamlit as st
from preprocessing import clean_text, segment_text, extract_key_sections, chunk_text_for_models
from ner_module import extract_key_entities, categorize_entities, format_entities_for_display
from classification_module import get_document_metadata, format_classification_for_display
from summarizer_module import generate_multi_length_summaries, generate_section_summaries, hybrid_summarization, format_summary_for_display

def process_document_comprehensive(text, document_type="general"):
    """
    Comprehensive document processing pipeline.
    
    Args:
        text (str): Input document text
        document_type (str): Expected document type (research, legal, medical, general)
    
    Returns:
        dict: Comprehensive analysis results
    """
    if not text or not text.strip():
        return {"error": "No text provided for analysis."}
    
    try:
        results = {}
        
        # Step 1: Preprocessing
        with st.spinner("🔄 Preprocessing document..."):
            cleaned_text = clean_text(text)
            sentences = segment_text(cleaned_text)
            sections = extract_key_sections(cleaned_text)
            chunks = chunk_text_for_models(cleaned_text)
            
            results["preprocessing"] = {
                "cleaned_text_length": len(cleaned_text),
                "num_sentences": len(sentences),
                "num_sections": len(sections),
                "num_chunks": len(chunks),
                "sections_found": list(sections.keys())
            }
        
        # Step 2: Document Metadata Analysis
        with st.spinner("📊 Analyzing document metadata..."):
            metadata = get_document_metadata(cleaned_text)
            results["metadata"] = metadata
        
        # Step 3: Named Entity Recognition
        with st.spinner("🏷️ Extracting named entities..."):
            entities = extract_key_entities(cleaned_text, document_type, top_k=15)
            entity_categories = categorize_entities(entities)
            
            results["entities"] = {
                "all_entities": entities,
                "categorized_entities": entity_categories,
                "total_entities": len(entities)
            }
        
        # Step 4: Multi-length Summarization
        with st.spinner("📝 Generating summaries..."):
            summaries = generate_multi_length_summaries(cleaned_text, document_type)
            section_summaries = generate_section_summaries(cleaned_text)
            hybrid_results = hybrid_summarization(cleaned_text, document_type)
            
            results["summaries"] = {
                "multi_length": summaries,
                "section_summaries": section_summaries,
                "hybrid_summarization": hybrid_results
            }
        
        # Step 5: Key Insights
        with st.spinner("💡 Extracting key insights..."):
            key_insights = extract_key_insights(cleaned_text, entities, metadata, summaries)
            results["insights"] = key_insights
        
        return results
        
    except Exception as e:
        st.error(f"Error in comprehensive document processing: {e}")
        return {"error": f"Processing failed: {str(e)}"}

def extract_key_insights(text, entities, metadata, summaries):
    """Extract key insights from the document analysis."""
    insights = {}
    
    # Document complexity insights
    complexity = metadata.get("complexity", {})
    insights["complexity"] = {
        "level": complexity.get("complexity", "unknown"),
        "readability_score": complexity.get("readability_score", 0),
        "recommendation": get_readability_recommendation(complexity.get("readability_score", 0))
    }
    
    # Entity insights
    entity_categories = categorize_entities(entities)
    insights["entities"] = {
        "most_common_type": get_most_common_entity_type(entity_categories),
        "key_people": [e for e in entities if e.get("entity_group") == "PERSON"][:5],
        "key_organizations": [e for e in entities if e.get("entity_group") == "ORG"][:5],
        "key_locations": [e for e in entities if e.get("entity_group") == "LOC"][:5]
    }
    
    # Summary insights
    brief_summary = summaries.get("multi_length", {}).get("brief", "")
    insights["summary"] = {
        "key_topics": extract_key_topics_from_summary(brief_summary),
        "summary_length": len(brief_summary),
        "has_conclusions": "conclusion" in brief_summary.lower() or "finding" in brief_summary.lower()
    }
    
    return insights

def get_readability_recommendation(score):
    """Get readability recommendation based on score."""
    if score >= 80:
        return "Very easy to read - suitable for general audience"
    elif score >= 60:
        return "Moderately easy to read - suitable for educated audience"
    elif score >= 40:
        return "Moderately difficult - suitable for specialized audience"
    else:
        return "Very difficult - suitable for expert audience"

def get_most_common_entity_type(entity_categories):
    """Get the most common entity type."""
    if not entity_categories:
        return "None"
    
    max_count = 0
    most_common = "None"
    
    for entity_type, entities in entity_categories.items():
        if len(entities) > max_count:
            max_count = len(entities)
            most_common = entity_type
    
    return most_common

def extract_key_topics_from_summary(summary):
    """Extract key topics from summary text."""
    if not summary:
        return []
    
    # Simple keyword extraction (can be enhanced with more sophisticated methods)
    import re
    
    # Remove common words
    stop_words = {"the", "a", "an", "and", "or", "but", "in", "on", "at", "to", "for", "of", "with", "by", "is", "are", "was", "were", "be", "been", "have", "has", "had", "do", "does", "did", "will", "would", "could", "should", "may", "might", "can", "this", "that", "these", "those", "i", "you", "he", "she", "it", "we", "they", "me", "him", "her", "us", "them"}
    
    words = re.findall(r'\b[a-zA-Z]+\b', summary.lower())
    words = [word for word in words if word not in stop_words and len(word) > 3]
    
    # Count word frequency
    from collections import Counter
    word_counts = Counter(words)
    
    # Return top 5 most common words
    return [word for word, count in word_counts.most_common(5)]

def format_comprehensive_results(results):
    """Format comprehensive results for Streamlit display."""
    if "error" in results:
        st.error(results["error"])
        return
    
    # Show which models were used
    st.markdown("🟢 **Analysis performed using pre-trained models (no API calls)**")
    st.markdown("""
    **Models Used:**
    - **NER**: Domain-specific BERT models (SciBERT, LegalBERT, etc.)
    - **Classification**: Transformer-based classifiers
    - **Summarization**: BART and T5 models
    - **Embeddings**: Sentence Transformers
    """)
    st.markdown("---")
    
    # Display preprocessing info
    st.subheader("📊 Document Analysis Overview")
    preprocessing = results.get("preprocessing", {})
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Text Length", f"{preprocessing.get('cleaned_text_length', 0):,} chars")
    with col2:
        st.metric("Sentences", preprocessing.get('num_sentences', 0))
    with col3:
        st.metric("Sections", preprocessing.get('num_sections', 0))
    with col4:
        st.metric("Entities", results.get("entities", {}).get("total_entities", 0))
    
    # Display metadata
    st.subheader("📋 Document Metadata")
    metadata = results.get("metadata", {})
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("**Language:**", metadata.get("language", {}).get("label", "Unknown"))
        st.write("**Classification:**", format_classification_for_display(metadata.get("classification", {})))
    
    with col2:
        complexity = metadata.get("complexity", {})
        st.write("**Complexity:**", complexity.get("complexity", "Unknown"))
        st.write("**Readability Score:**", complexity.get("readability_score", 0))
    
    # Display entities
    st.subheader("🏷️ Named Entities")
    entities = results.get("entities", {})
    categorized = entities.get("categorized_entities", {})
    
    for entity_type, entity_list in categorized.items():
        if entity_list:
            with st.expander(f"{entity_type} ({len(entity_list)})"):
                for entity in entity_list[:10]:  # Show first 10
                    st.write(f"• **{entity.get('word', '')}** (confidence: {entity.get('score', 0):.2f})")
    
    # Display summaries
    st.subheader("📝 Summaries")
    summaries = results.get("summaries", {})
    multi_length = summaries.get("multi_length", {})
    
    tab1, tab2, tab3, tab4 = st.tabs(["Brief", "Standard", "Detailed", "Hybrid"])
    
    with tab1:
        st.markdown(format_summary_for_display(multi_length.get("brief", ""), "brief"))
    
    with tab2:
        st.markdown(format_summary_for_display(multi_length.get("standard", ""), "standard"))
    
    with tab3:
        st.markdown(format_summary_for_display(multi_length.get("detailed", ""), "detailed"))
    
    with tab4:
        hybrid = summaries.get("hybrid_summarization", {})
        st.markdown("**Extractive Summary:**")
        st.write(hybrid.get("extractive_summary", ""))
        st.markdown("**Final Summary:**")
        st.write(hybrid.get("final_summary", ""))
    
    # Display insights
    st.subheader("💡 Key Insights")
    insights = results.get("insights", {})
    
    col1, col2 = st.columns(2)
    with col1:
        complexity_insights = insights.get("complexity", {})
        st.write("**Readability:**", complexity_insights.get("recommendation", ""))
        
        entity_insights = insights.get("entities", {})
        st.write("**Most Common Entity Type:**", entity_insights.get("most_common_type", ""))
    
    with col2:
        summary_insights = insights.get("summary", {})
        st.write("**Key Topics:**", ", ".join(summary_insights.get("key_topics", [])))
        st.write("**Has Conclusions:**", "Yes" if summary_insights.get("has_conclusions", False) else "No")

def process_document_simple(text, document_type="general"):
    """Simplified document processing for quick analysis."""
    if not text or not text.strip():
        return {"error": "No text provided."}
    
    try:
        # Clean text
        cleaned_text = clean_text(text)
        
        # Get basic metadata
        metadata = get_document_metadata(cleaned_text)
        
        # Extract key entities
        entities = extract_key_entities(cleaned_text, document_type, top_k=10)
        
        # Generate standard summary
        summaries = generate_multi_length_summaries(cleaned_text, document_type)
        
        return {
            "metadata": metadata,
            "entities": entities,
            "summary": summaries.get("standard", "Unable to generate summary.")
        }
        
    except Exception as e:
        return {"error": f"Processing failed: {str(e)}"}
