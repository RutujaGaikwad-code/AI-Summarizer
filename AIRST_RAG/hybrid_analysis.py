#!/usr/bin/env python3
"""
Hybrid Analysis Module - Combines Pre-trained Models and ChatGPT for Improved Accuracy
"""

import streamlit as st
import json
import requests
from models import process_text

def get_api_key():
    """Get API key from multiple sources with better error handling"""
    # Try to get from secrets first
    api_key = st.secrets.get("OPENROUTER_API_KEY")
    
    # If not in secrets, try environment variable
    if not api_key:
        import os
        api_key = os.getenv("OPENROUTER_API_KEY")
    
    # If still not found, check if user provided it in session state
    if not api_key:
        api_key = st.session_state.get("openrouter_api_key")
    
    return api_key

def call_chatgpt_enhanced(prompt, context=""):
    """Call ChatGPT with enhanced prompt"""
    api_key = get_api_key()
    if not api_key or api_key == "your_openrouter_api_key_here":
        return None  # Return None if no API key available
    
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "HTTP-Referer": st.secrets.get("SITE_URL", "https://example.com"),
        "X-Title": st.secrets.get("SITE_NAME", "My Site"),
        "Content-Type": "application/json"
    }
    
    full_prompt = f"{context}\n\n{prompt}" if context else prompt
    
    data = {"model": "openai/gpt-3.5-turbo", "messages": [{"role": "user", "content": full_prompt}]}
    
    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            return None
    except Exception:
        return None

def hybrid_summarization(text, filename, length_preference="Detailed (4-5 paragraphs)"):
    """
    Hybrid summarization combining pre-trained models and ChatGPT
    """
    try:
        # Check if this is a research paper with citations
        import re
        has_citations = re.search(r'\[\d+\]', text)
        has_references = re.search(r'references', text, re.IGNORECASE)
        
        # If it's a research paper, use specialized handling
        if has_citations and has_references:
            # Extract introduction section
            from rag import extract_introduction_section, extract_references_section
            introduction_text = extract_introduction_section(text)
            if not introduction_text:
                introduction_text = text
            
            # Step 1: Use pre-trained models for initial analysis
            st.info("🔄 Step 1: Analyzing research paper with pre-trained models...")
            pretrained_result = process_text(introduction_text)
            
            domain = pretrained_result.get('domain', 'scientific')
            entities = pretrained_result.get('entities', [])
            initial_summary = pretrained_result.get('summary', '')
            
            # Step 2: Use ChatGPT to enhance the summary if available
            st.info("🔄 Step 2: Enhancing research paper summary with ChatGPT...")
            
            # Create enhanced prompt for research papers
            enhancement_prompt = f"""
            You are an expert research paper summarizer. Create a DETAILED and COMPREHENSIVE summary of this introduction section:
            
            Document: {filename}
            Domain: {domain}
            Key Entities Found: {', '.join([e.get('word', '') for e in entities[:10]])}
            Initial Summary: {initial_summary}
            
            CRITICAL REQUIREMENTS:
            1. **Language**: Generate in English
            2. **Length**: Create a COMPREHENSIVE and DETAILED summary (5-6 paragraphs minimum) that thoroughly covers all key points
            3. **Citations**: PRESERVE ALL inline citations (e.g., [1], [2], [3]) exactly as they appear in the original text. Do NOT remove or modify any citation numbers.
            4. **Academic Style**: Maintain academic writing style and terminology
            5. **Structure**: Create a comprehensive summary that explains the research context, motivation, methodology, key findings, and implications
            6. **Detail Level**: Provide extensive detailed explanations, not just bullet points. Explain the significance, relationships between concepts, and real-world applications
            7. **Depth**: Include background context, methodology details, key results, limitations, and future directions
            8. **References**: The full references section will be added separately, so focus only on the summary content with preserved citations
            
            Create a PROFESSIONAL, DETAILED research paper summary that preserves ALL academic citations exactly as they appear in the original text. Make it comprehensive and informative like a ChatGPT response.
            """
            
            enhanced_summary = call_chatgpt_enhanced(enhancement_prompt)
            
            if enhanced_summary:
                # Do not add references section - removed as requested
                pass
                
                return {
                    "summary": enhanced_summary,
                    "domain": domain,
                    "entities": entities,
                    "method": "hybrid",
                    "pretrained_summary": initial_summary,
                    "enhanced": True
                }
            else:
                # Fallback to pre-trained models only
                from rag import create_research_summary_with_citations
                fallback_summary = create_research_summary_with_citations(text, filename, length_preference)
                return {
                    "summary": fallback_summary,
                    "domain": domain,
                    "entities": entities,
                    "method": "pretrained_only",
                    "enhanced": False
                }
        else:
            # Standard hybrid summarization for non-research papers
            st.info("🔄 Step 1: Analyzing with pre-trained models...")
            pretrained_result = process_text(text)
            
            domain = pretrained_result.get('domain', 'general')
            entities = pretrained_result.get('entities', [])
            initial_summary = pretrained_result.get('summary', '')
            
            st.info("🔄 Step 2: Enhancing with ChatGPT...")
            
            enhancement_prompt = f"""
            You are an expert document summarizer. Create a DETAILED and COMPREHENSIVE summary using the following information:
            
            Document: {filename}
            Domain: {domain}
            Key Entities Found: {', '.join([e.get('word', '') for e in entities[:10]])}
            Initial Summary: {initial_summary}
            
            Requirements:
            1. **Language**: Generate in English
            2. **Length**: Create a COMPREHENSIVE and DETAILED summary (5-6 paragraphs minimum) that thoroughly covers all key points
            3. **Enhancement**: Create a comprehensive summary with extensive detailed explanations, context, and analysis
            4. **Entity Integration**: Incorporate the key entities naturally into the summary with explanations of their significance
            5. **Domain-Specific**: Adapt the tone and terminology for {domain} documents with proper technical depth
            6. **Detail Level**: Provide extensive detailed explanations, not just bullet points. Explain the significance, relationships between concepts, and practical implications
            7. **Depth**: Include background context, main arguments, supporting evidence, conclusions, and real-world applications
            8. **Citations**: Preserve any citations from the original text and add [Source: {filename}] at the end
            
            Create a PROFESSIONAL, DETAILED summary that is comprehensive and informative like a ChatGPT response.
            """
            
            enhanced_summary = call_chatgpt_enhanced(enhancement_prompt)
            
            if enhanced_summary:
                return {
                    "summary": enhanced_summary,
                    "domain": domain,
                    "entities": entities,
                    "method": "hybrid",
                    "pretrained_summary": initial_summary,
                    "enhanced": True
                }
            else:
                return {
                    "summary": f"{initial_summary} [Source: {filename}]",
                    "domain": domain,
                    "entities": entities,
                    "method": "pretrained_only",
                    "enhanced": False
                }
            
    except Exception as e:
        return {
            "summary": f"Error in hybrid analysis: {str(e)}",
            "method": "error",
            "enhanced": False
        }

def hybrid_qa(context, question, filename=None):
    """
    Hybrid Q&A combining pre-trained models and ChatGPT
    """
    try:
        # Step 1: Use pre-trained models for initial analysis
        st.info("🔄 Step 1: Analyzing with pre-trained models...")
        pretrained_result = process_text(context)
        
        domain = pretrained_result.get('domain', 'general')
        entities = pretrained_result.get('entities', [])
        context_summary = pretrained_result.get('summary', '')
        
        # Step 2: Use ChatGPT to answer the question with enhanced context
        st.info("🔄 Step 2: Generating answer with ChatGPT...")
        
        qa_prompt = f"""
        You are an expert research assistant. Answer the following question based on the provided context.
        
        Document Analysis:
        - Domain: {domain}
        - Key Entities: {', '.join([e.get('word', '') for e in entities[:10]])}
        - Context Summary: {context_summary}
        
        Question: {question}
        
        Requirements:
        1. **Answer in English**
        2. **Use the context summary and entities to provide accurate answers**
        3. **Cite sources**: Preserve any citations from the original text and use [Source: {filename}] for references
        4. **Professional tone**: Academic and professional language
        5. **Comprehensive**: Provide detailed, well-structured answers
        6. **References**: If the context contains references, mention them in your answer
        
        Provide a comprehensive answer based on the analyzed context and preserve academic citations.
        """
        
        answer = call_chatgpt_enhanced(qa_prompt)
        
        if answer:
            return {
                "answer": answer,
                "domain": domain,
                "entities": entities,
                "method": "hybrid",
                "enhanced": True
            }
        else:
            # Fallback to pre-trained models only
            fallback_answer = f"Based on document analysis: {context_summary} [Source: {filename}]"
            # Add key references if available
            if entities:
                key_entities = [e.get('word', '') for e in entities[:5]]
                fallback_answer += f"\n\nKey entities identified: {', '.join(key_entities)}"
            return {
                "answer": fallback_answer,
                "domain": domain,
                "entities": entities,
                "method": "pretrained_only",
                "enhanced": False
            }
            
    except Exception as e:
        return {
            "answer": f"Error in hybrid Q&A: {str(e)}",
            "method": "error",
            "enhanced": False
        }

def hybrid_entity_analysis(text, filename):
    """
    Enhanced entity analysis combining pre-trained models and ChatGPT
    """
    try:
        # Step 1: Use pre-trained models for entity extraction
        st.info("🔄 Step 1: Extracting entities with pre-trained models...")
        pretrained_result = process_text(text)
        
        domain = pretrained_result.get('domain', 'general')
        entities = pretrained_result.get('entities', [])
        
        # Step 2: Use ChatGPT to analyze and explain the entities
        st.info("🔄 Step 2: Analyzing entities with ChatGPT...")
        
        entity_analysis_prompt = f"""
        Analyze and explain the key entities found in this document:
        
        Document: {filename}
        Domain: {domain}
        Entities Found: {json.dumps(entities[:15], indent=2)}
        
        Provide:
        1. **Entity Categories**: Group entities by type (People, Organizations, Locations, etc.)
        2. **Significance**: Explain why these entities are important in this context
        3. **Relationships**: Identify any relationships between entities
        4. **Domain Context**: Explain how these entities relate to the {domain} domain
        
        Format your response clearly with sections and bullet points.
        """
        
        entity_analysis = call_chatgpt_enhanced(entity_analysis_prompt)
        
        if entity_analysis:
            return {
                "entities": entities,
                "analysis": entity_analysis,
                "domain": domain,
                "method": "hybrid",
                "enhanced": True
            }
        else:
            # Fallback to pre-trained models only
            return {
                "entities": entities,
                "analysis": f"Found {len(entities)} entities in {domain} domain",
                "domain": domain,
                "method": "pretrained_only",
                "enhanced": False
            }
            
    except Exception as e:
        return {
            "entities": [],
            "analysis": f"Error in entity analysis: {str(e)}",
            "method": "error",
            "enhanced": False
        }

def get_analysis_method(key=None):
    """
    Get the preferred analysis method from user settings
    """
    methods = {
        "Hybrid (Recommended)": "hybrid",
        "Pre-trained Models Only": "pretrained_only", 
        "ChatGPT Only": "chatgpt_only"
    }
    
    # Generate a unique key if none provided
    if key is None:
        key = f"analysis_method_{id(methods)}"
    
    return st.selectbox(
        "Choose Analysis Method:",
        list(methods.keys()),
        index=0,
        help="Hybrid combines both for best results, Pre-trained models work offline, ChatGPT requires API key",
        key=key
    )

def display_hybrid_results(results):
    """
    Display hybrid analysis results with method indicators
    """
    method = results.get("method", "unknown")
    enhanced = results.get("enhanced", False)
    
    # Display method indicator
    if method == "hybrid":
        if enhanced:
            st.success("✅ Hybrid Analysis (Pre-trained + ChatGPT)")
        else:
            st.warning("⚠️ Hybrid Analysis (Pre-trained only - ChatGPT unavailable)")
    elif method == "pretrained_only":
        st.info("🟢 Pre-trained Models Only")
    elif method == "chatgpt_only":
        st.info("🔴 ChatGPT Only")
    else:
        st.error("❌ Analysis Error")
    
    # Display results
    if "summary" in results:
        st.subheader("📝 Summary")
        st.write(results["summary"])
        
        if "pretrained_summary" in results:
            with st.expander("🔍 Original Pre-trained Summary"):
                st.write(results["pretrained_summary"])
    
    if "answer" in results:
        st.subheader("💡 Answer")
        st.write(results["answer"])
    
    if "entities" in results:
        st.subheader("🏷️ Named Entities")
        entities = results["entities"]
        if entities:
            for entity in entities[:10]:
                st.write(f"• **{entity.get('word', '')}** ({entity.get('entity_group', 'MISC')}) - {entity.get('score', 0):.2f}")
        else:
            st.write("No entities found.")
    
    if "analysis" in results:
        st.subheader("📊 Entity Analysis")
        st.write(results["analysis"])
    
    # Display domain information
    if "domain" in results:
        st.info(f"📋 Detected Domain: {results['domain']}")
