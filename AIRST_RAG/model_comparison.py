import streamlit as st

def show_model_comparison():
    """Display a comparison table between ChatGPT and Pre-trained models."""
    
    st.markdown("## 🤖 Model Comparison Guide")
    
    comparison_data = {
        "Feature": [
            "**Model Type**",
            "**Internet Required**",
            "**API Key Required**",
            "**Cost**",
            "**Speed**",
            "**Creativity**",
            " ",
            "**Specialization**",
            "**Domain Knowledge**",
            "**Consistency**",
            "**Privacy**",
            "**Rate Limits**"
        ],
        "ChatGPT (Other Tabs)": [
            "Large Language Model (GPT)",
            "✅ Yes",
            "✅ Yes",
            "💰 Per API call",
            "⚡ Fast (API)",
            "🎨 High (creative responses)",
            " ",
            "General purpose",
            "Broad knowledge",
            "Variable (depends on prompt)",
            "⚠️ Data sent to OpenAI",
            "⚠️ API rate limits"
        ],
        "Pre-trained Models (AI Pipeline)": [
            "Specialized Transformers",
            "❌ No (offline)",
            "❌ No",
            "🆓 Free",
            "🐌 Slower (local processing)",
            "📊 Low (factual responses)",
            " ",
            "Domain-specific",
            "Specialized (research, legal, medical)",
            "High (consistent results)",
            "🔒 100% private (local)",
            "✅ No limits"
        ]
    }
    
    # Create comparison table
    st.markdown("### 📊 Feature Comparison")
    
    # Display as columns for better readability
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("**Feature**")
        for feature in comparison_data["Feature"]:
            st.markdown(feature)
    
    with col2:
        st.markdown("**🔴 ChatGPT**")
        for feature in comparison_data["ChatGPT (Other Tabs)"]:
            st.markdown(feature)
    
    with col3:
        st.markdown("**🟢 Pre-trained**")
        for feature in comparison_data["Pre-trained Models (AI Pipeline)"]:
            st.markdown(feature)
    
    st.markdown("---")
    
    # Usage recommendations
    st.markdown("### 💡 When to Use Each System")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **🔴 Use ChatGPT when:**
        - You need creative, conversational responses
        - You want to ask complex, open-ended questions
        - You need explanations in natural language
        - You have internet connection and API access
        - You're okay with potential costs
        """)
    
    with col2:
        st.markdown("""
        **🟢 Use Pre-trained Models when:**
        - You need specialized domain analysis
        - You want to work offline
        - You need consistent, factual results
        - You have privacy concerns
        - You want to avoid API costs
        """)

def show_model_details():
    """Show detailed information about the models used."""
    
    st.markdown("## 🔍 Model Details")
    
    # Pre-trained models used
    st.markdown("### 🟢 Pre-trained Models in AI Pipeline")
    
    models_info = {
        "**Named Entity Recognition (NER)**": {
            "Research Papers": "allenai/scibert_scivocab_uncased",
            "Legal Documents": "nlpaueb/legal-bert-base-uncased", 
            "Medical Documents": "emilyalsentzer/Bio_ClinicalBERT",
            "General Documents": "dslim/bert-base-NER"
        },
        "**Document Classification**": {
            "Research Papers": "allenai/scibert_scivocab_uncased",
            "Legal Documents": "nlpaueb/legal-bert-base-uncased",
            "Medical Documents": "emilyalsentzer/Bio_ClinicalBERT",
            "General Documents": "distilbert-base-uncased"
        },
        "**Summarization**": {
            "General": "facebook/bart-large-cnn",
            "Fast": "t5-base",
            "Scientific": "allenai/scibert_scivocab_uncased"
        },
        "**Language Detection**": {
            "Multi-language": "papluca/xlm-roberta-base-language-detection"
        },
        "**Sentence Embeddings**": {
            "Text Similarity": "all-MiniLM-L6-v2"
        }
    }
    
    for category, models in models_info.items():
        st.markdown(f"#### {category}")
        for model_type, model_name in models.items():
            st.markdown(f"- **{model_type}**: `{model_name}`")
        st.markdown("")
    
    # ChatGPT models
    st.markdown("### 🔴 ChatGPT Models (Other Tabs)")
    st.markdown("""
    - **Primary Model**: `openai/gpt-3.5-turbo` (via OpenRouter API)
    - **Capabilities**: Text generation, summarization, Q&A, creative writing
    - **Access**: Requires API key and internet connection
    """)

def show_output_differences():
    """Show examples of output differences between the two systems."""
    
    st.markdown("## 📝 Output Style Differences")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🔴 ChatGPT Output Style")
        st.markdown("""
        **Example Summary:**
        ```
        This research paper explores the fascinating 
        world of artificial intelligence and its 
        applications in modern technology. The authors 
        present compelling arguments about how AI 
        could revolutionize various industries...
        ```
        
        **Characteristics:**
        - More conversational tone
        - Creative language use
        - Variable length and style
        - May include opinions or interpretations
        """)
    
    with col2:
        st.markdown("### 🟢 Pre-trained Model Output Style")
        st.markdown("""
        **Example Summary:**
        ```
        The study investigates artificial intelligence 
        applications in technology. Results show 45% 
        improvement in efficiency. Key findings include 
        neural network optimization and machine learning 
        algorithms.
        ```
        
        **Characteristics:**
        - Factual and concise
        - Consistent structure
        - Focused on key information
        - More technical/formal tone
        """)
