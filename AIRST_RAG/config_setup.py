#!/usr/bin/env python3
"""
Configuration setup page for API keys
"""

import streamlit as st
import os
from auth import auth_page, is_authenticated, get_current_user

def config_page():
    """Configuration page for API keys"""
    st.title("⚙️ Configuration Setup")
    st.markdown("---")
    
    st.header("🔑 OpenRouter API Key Setup")
    
    st.markdown("""
    ### Why do you need an API key?
    
    This application uses OpenRouter's AI models to generate summaries and answer questions about your research papers. 
    You need a valid API key to access these AI services.
    
    ### How to get your API key:
    
    1. **Visit OpenRouter**: Go to https://openrouter.ai/keys
    2. **Sign up/Login**: Create an account or log in
    3. **Generate Key**: Click "Create Key" to generate a new API key
    4. **Copy the Key**: Copy the generated key (starts with `sk-or-v1-`)
    """)
    
    st.markdown("---")
    
    # Current API key status
    st.subheader("🔍 Current API Key Status")
    
    # Check if API key exists
    api_key = st.secrets.get("OPENROUTER_API_KEY", "")
    env_api_key = os.getenv("OPENROUTER_API_KEY", "")
    session_api_key = st.session_state.get("openrouter_api_key", "")
    
    if api_key and api_key != "your_openrouter_api_key_here":
        st.success("✅ API key found in secrets.toml")
        st.info("API key is configured in your secrets file.")
    elif env_api_key:
        st.success("✅ API key found in environment variables")
        st.info("API key is configured as an environment variable.")
    elif session_api_key:
        st.warning("⚠️ API key found in session (temporary)")
        st.info("API key is stored temporarily in your session.")
    else:
        st.error("❌ No API key found")
        st.info("Please configure your API key using one of the methods below.")
    
    st.markdown("---")
    
    # Configuration options
    st.subheader("🔧 Configure API Key")
    
    tab1, tab2, tab3 = st.tabs(["📝 Temporary Setup", "🔐 Secrets File", "🌍 Environment Variable"])
    
    with tab1:
        st.markdown("### Temporary Setup (Session Only)")
        st.markdown("This will store your API key temporarily for this session only.")
        
        temp_key = st.text_input(
            "Enter your OpenRouter API key:",
            type="password",
            placeholder="sk-or-v1-...",
            key="temp_api_key_input"
        )
        
        if st.button("Save Temporarily", key="save_temp_key"):
            if temp_key and temp_key.startswith("sk-or-v1-"):
                st.session_state["openrouter_api_key"] = temp_key
                st.success("✅ API key saved temporarily!")
                st.rerun()
            else:
                st.error("❌ Invalid API key format. Please enter a valid OpenRouter API key.")
    
    with tab2:
        st.markdown("### Permanent Setup (Secrets File)")
        st.markdown("This will help you set up the API key permanently in your secrets file.")
        
        st.markdown("""
        **Steps to configure permanently:**
        
        1. **Open your secrets file**: `AIRST_RAG/.streamlit/secrets.toml`
        2. **Replace the API key**: Update the `OPENROUTER_API_KEY` value
        3. **Save the file**: Save the changes
        4. **Restart the app**: Restart the Streamlit application
        
        **Example secrets.toml:**
        ```toml
        OPENROUTER_API_KEY = "sk-or-v1-your-actual-api-key-here"
        SITE_URL = "localhost"
        SITE_NAME = "Your Site Name"
        ```
        """)
        
        if st.button("Open Secrets File", key="open_secrets"):
            secrets_path = ".streamlit/secrets.toml"
            if os.path.exists(secrets_path):
                with open(secrets_path, 'r') as f:
                    current_content = f.read()
                
                st.text_area("Current secrets.toml content:", current_content, height=200)
                
                new_key = st.text_input(
                    "Enter your new API key:",
                    type="password",
                    placeholder="sk-or-v1-...",
                    key="new_secrets_key"
                )
                
                if st.button("Update Secrets File", key="update_secrets"):
                    if new_key and new_key.startswith("sk-or-v1-"):
                        new_content = f"""OPENROUTER_API_KEY = "{new_key}"
SITE_URL = "localhost"
SITE_NAME = "Your Site Name"
"""
                        try:
                            with open(secrets_path, 'w') as f:
                                f.write(new_content)
                            st.success("✅ Secrets file updated! Please restart the application.")
                        except Exception as e:
                            st.error(f"❌ Error updating file: {e}")
                    else:
                        st.error("❌ Invalid API key format.")
            else:
                st.error("❌ Secrets file not found.")
    
    with tab3:
        st.markdown("### Environment Variable Setup")
        st.markdown("Set the API key as an environment variable.")
        
        st.markdown("""
        **Windows (Command Prompt):**
        ```cmd
        set OPENROUTER_API_KEY=sk-or-v1-your-api-key-here
        ```
        
        **Windows (PowerShell):**
        ```powershell
        $env:OPENROUTER_API_KEY="sk-or-v1-your-api-key-here"
        ```
        
        **Linux/Mac:**
        ```bash
        export OPENROUTER_API_KEY="sk-or-v1-your-api-key-here"
        ```
        
        **Permanent setup (add to your shell profile):**
        - Windows: Add to system environment variables
        - Linux/Mac: Add to `~/.bashrc` or `~/.zshrc`
        """)
    
    st.markdown("---")
    
    # Test API key
    st.subheader("🧪 Test API Key")
    
    if st.button("Test Current API Key", key="test_api_key"):
        current_key = st.secrets.get("OPENROUTER_API_KEY") or os.getenv("OPENROUTER_API_KEY") or st.session_state.get("openrouter_api_key")
        
        if not current_key:
            st.error("❌ No API key found to test.")
        else:
            with st.spinner("Testing API key..."):
                import requests
                
                url = "https://openrouter.ai/api/v1/auth/key"
                headers = {"Authorization": f"Bearer {current_key}"}
                
                try:
                    response = requests.get(url, headers=headers)
                    if response.status_code == 200:
                        st.success("✅ API key is valid!")
                        data = response.json()
                        if 'data' in data:
                            st.info(f"**Account**: {data['data'].get('name', 'Unknown')}")
                            st.info(f"**Credits**: {data['data'].get('credits', 'Unknown')}")
                    else:
                        st.error(f"❌ API key test failed: {response.status_code}")
                        if response.status_code == 401:
                            st.error("Invalid or expired API key.")
                except Exception as e:
                    st.error(f"❌ Error testing API key: {e}")
    
    st.markdown("---")
    
    # Navigation
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔙 Back to Main App"):
            st.switch_page("rag.py")
    with col2:
        if st.button("📖 View Documentation"):
            st.markdown("""
            **OpenRouter Documentation:**
            - [API Keys](https://openrouter.ai/keys)
            - [API Documentation](https://openrouter.ai/docs)
            - [Pricing](https://openrouter.ai/pricing)
            """)

def main():
    """Main function"""
    # Check authentication
    if not is_authenticated():
        auth_page()
        return
    
    # Show configuration page
    current_user = get_current_user()
    
    # Header
    col1, col2, col3 = st.columns([3, 1, 1])
    with col1:
        st.title("⚙️ Configuration")
    with col2:
        st.write(f"**Welcome, {current_user}!**")
    with col3:
        if st.button("🔙 Back"):
            st.switch_page("rag.py")
    
    st.markdown("---")
    
    # Show configuration content
    config_page()

if __name__ == "__main__":
    main() 
