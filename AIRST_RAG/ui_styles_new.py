import streamlit as st

def apply_custom_styles():
    """Apply custom CSS styles to the Streamlit app"""
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    
    :root {
        --primary-color: #4F7FFF;
        --secondary-color: #6366f1;
        --accent-color: #FF6B35;
        --bg-primary: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        --bg-secondary: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        --text-primary: #1a202c;
        --text-secondary: #4a5568;
        --text-muted: #718096;
        --card-bg: rgba(255, 255, 255, 0.95);
        --border-color: rgba(255, 255, 255, 0.2);
        --shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
        --shadow-hover: 0 20px 40px rgba(0, 0, 0, 0.15);
    }
    
    /* Global Styles */
    .stApp {
        background: linear-gradient(135deg, #4F7FFF 0%, #93c5fd 50%, #ffffff 100%);
        font-family: 'Inter', sans-serif;
        color: var(--text-primary);
    }
    
    .main {
        background: transparent;
        padding: 0;
    }
    
    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {display: none;}
    
    /* Custom Cards */
    .custom-card {
        background: var(--card-bg);
        backdrop-filter: blur(10px);
        border-radius: 16px;
        padding: 2rem;
        margin: 1.5rem 0;
        box-shadow: var(--shadow);
        border: 1px solid var(--border-color);
        transition: all 0.3s ease;
    }
    
    .custom-card:hover {
        transform: translateY(-5px);
        box-shadow: var(--shadow-hover);
    }
    
    .glass-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 12px;
        padding: 1.5rem;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
    }
    
    /* Upload Cards */
    .upload-card {
        background: white;
        border-radius: 16px;
        padding: 2rem;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
        border: 1px solid #e2e8f0;
        transition: all 0.3s ease;
        height: 100%;
    }
    
    .upload-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.12);
    }
    
    .upload-card h3 {
        color: var(--text-primary);
        font-size: 1.25rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }
    
    .upload-card p {
        color: var(--text-muted);
        font-size: 0.875rem;
        margin-bottom: 1.5rem;
    }
    
    .upload-area {
        border: 2px dashed #cbd5e1;
        border-radius: 12px;
        padding: 2rem;
        text-align: center;
        background: #f8fafc;
        transition: all 0.3s ease;
    }
    
    .upload-area:hover {
        border-color: var(--primary-color);
        background: #f1f5f9;
    }
    
    .upload-icon {
        font-size: 2.5rem;
        margin-bottom: 1rem;
        opacity: 0.6;
    }
    
    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, var(--primary-color) 0%, var(--secondary-color) 100%);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(79, 127, 255, 0.3);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(79, 127, 255, 0.4);
    }
    
    .orange-button button {
        background: linear-gradient(135deg, #FF6B35 0%, #f56500 100%) !important;
        box-shadow: 0 4px 15px rgba(255, 107, 53, 0.3) !important;
    }
    
    .orange-button button:hover {
        box-shadow: 0 8px 25px rgba(255, 107, 53, 0.4) !important;
    }
    
    /* Typography */
    .welcome-header {
        text-align: center;
        padding: 3rem 0;
        background: linear-gradient(135deg, rgba(255,255,255,0.1) 0%, rgba(255,255,255,0.05) 100%);
        border-radius: 20px;
        margin-bottom: 3rem;
        backdrop-filter: blur(10px);
    }
    
    .welcome-header h1 {
        font-size: 3.5rem;
        font-weight: 800;
        background: linear-gradient(135deg, #1a202c 0%, var(--primary-color) 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 1rem;
    }
    
    .welcome-header p {
        font-size: 1.25rem;
        color: var(--text-secondary);
        font-weight: 500;
    }
    
    /* Animations */
    .fade-in {
        animation: fadeIn 0.8s ease-in;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    /* Custom Divider */
    .custom-divider {
        height: 2px;
        background: linear-gradient(90deg, transparent 0%, var(--primary-color) 50%, transparent 100%);
        margin: 2rem 0;
        border-radius: 2px;
    }
    
    /* Metrics */
    .metric-container {
        background: linear-gradient(135deg, var(--primary-color) 0%, var(--secondary-color) 100%);
        color: white;
        padding: 1rem;
        border-radius: 12px;
        text-align: center;
        margin: 0.5rem 0;
    }
    
    .metric-value {
        font-size: 2rem;
        font-weight: 700;
        margin-bottom: 0.25rem;
    }
    
    .metric-label {
        font-size: 0.875rem;
        opacity: 0.9;
        font-weight: 500;
    }
    
    /* Features Section */
    .features-section {
        background: var(--card-bg);
        border-radius: 20px;
        padding: 3rem;
        margin: 3rem 0;
        box-shadow: var(--shadow);
    }
    
    .feature-item {
        text-align: center;
        padding: 1.5rem;
        background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
        border-radius: 12px;
        transition: all 0.3s ease;
    }
    
    .feature-item:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
    }
    
    .feature-icon {
        font-size: 2.5rem;
        margin-bottom: 1rem;
        color: var(--primary-color);
    }
    
    /* Account Dropdown */
    .account-dropdown {
        position: fixed;
        top: 1rem;
        right: 1rem;
        z-index: 1000;
        background: var(--card-bg);
        border-radius: 12px;
        padding: 1rem;
        box-shadow: var(--shadow);
        border: 1px solid var(--border-color);
    }
    
    /* Sidebar Enhancements */
    .css-1d391kg {
        background: linear-gradient(135deg, rgba(255,255,255,0.1) 0%, rgba(255,255,255,0.05) 100%);
        backdrop-filter: blur(10px);
    }
    
    /* File Uploader Styling */
    .stFileUploader {
        background: transparent;
    }
    
    .stFileUploader > div {
        background: transparent;
        border: none;
    }
    
    /* Success/Error Messages */
    .stSuccess {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%);
        color: white;
        border-radius: 12px;
        padding: 1rem;
        border: none;
    }
    
    .stError {
        background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%);
        color: white;
        border-radius: 12px;
        padding: 1rem;
        border: none;
    }
    
    /* Responsive Design */
    @media (max-width: 768px) {
        .welcome-header h1 {
            font-size: 2.5rem;
        }
        
        .custom-card {
            padding: 1.5rem;
            margin: 1rem 0;
        }
        
        .upload-card {
            padding: 1.5rem;
        }
    }
    </style>
    """, unsafe_allow_html=True)

def create_welcome_header():
    """Create the welcome header matching the design"""
    st.markdown("""
    <div class="welcome-header">
        <h1>Welcome to <span style="color: #FFD700;">AI Summarizer</span></h1>
        <p>🚀 From Documents to Insights in Seconds.</p>
    </div>
    """, unsafe_allow_html=True)

def create_upload_interface():
    """Create the upload interface matching the design"""
    st.markdown("""
    <div style="text-align: center; margin-bottom: 2rem;">
        <h2 style="color: white; font-family: 'Inter', sans-serif; font-weight: 600; margin-bottom: 0.5rem;">Upload Documents</h2>
        <p style="color: rgba(255, 255, 255, 0.8); font-family: 'Inter', sans-serif;">Upload your documents to generate AI-powered summaries with precise citations</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="upload-card">
            <h3>Single Document</h3>
            <p>Upload a single document for analysis and summarization</p>
            <div class="upload-area">
                <div class="upload-icon">📄</div>
                <p style="margin: 0; color: var(--text-muted);">Drag & drop or click to browse</p>
                <small style="color: var(--text-muted);">Supports PDF, Word, Text files • Max 50MB each</small>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        single_file = st.file_uploader(
            "Choose File",
            type=["pdf", "docx", "txt"],
            key="single_upload",
            label_visibility="hidden"
        )
        
        if single_file:
            st.button("Choose File", key="single_btn", use_container_width=True)
    
    with col2:
        st.markdown("""
        <div class="upload-card">
            <h3>Multiple Documents</h3>
            <p>Upload multiple documents for cross-document analysis</p>
            <div class="upload-area">
                <div class="upload-icon">📚</div>
                <p style="margin: 0; color: var(--text-muted);">Upload multiple documents</p>
                <small style="color: var(--text-muted);">Compare and synthesize across files</small>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        multiple_files = st.file_uploader(
            "Choose Files",
            type=["pdf", "docx", "txt"],
            accept_multiple_files=True,
            key="multiple_upload",
            label_visibility="hidden"
        )
        
        if multiple_files:
            st.markdown('<div class="orange-button">', unsafe_allow_html=True)
            st.button("Choose Files", key="multiple_btn", use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
    
    return single_file, multiple_files

def create_features_section():
    """Create the features section matching the design"""
    pass

def create_account_dropdown(username):
    """Create account dropdown in top right"""
    st.markdown(f"""
    <div class="account-dropdown">
        Account: {username} ▼
    </div>
    """, unsafe_allow_html=True)

def create_stats_section(stats_data):
    """Create a statistics section with metrics"""
    st.markdown("""
    <div style="background: var(--card-bg); border-radius: 16px; padding: 2rem; margin: 2rem 0; box-shadow: var(--shadow-card);">
        <h3 style="text-align: center; color: var(--text-primary); margin-bottom: 2rem;">📊 Session Statistics</h3>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div style="background: var(--card-bg); border-radius: 12px; padding: 1.5rem; text-align: center; box-shadow: var(--shadow-card); margin: 0.5rem;">
            <div style="font-size: 2rem; font-weight: 700; color: var(--primary-blue); margin-bottom: 0.5rem;">{stats_data.get('files_processed', 0)}</div>
            <div style="font-size: 0.9rem; color: var(--text-secondary); text-transform: uppercase; letter-spacing: 1px;">Files Processed</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div style="background: var(--card-bg); border-radius: 12px; padding: 1.5rem; text-align: center; box-shadow: var(--shadow-card); margin: 0.5rem;">
            <div style="font-size: 2rem; font-weight: 700; color: var(--primary-blue); margin-bottom: 0.5rem;">{stats_data.get('summaries_generated', 0)}</div>
            <div style="font-size: 0.9rem; color: var(--text-secondary); text-transform: uppercase; letter-spacing: 1px;">Summaries Generated</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div style="background: var(--card-bg); border-radius: 12px; padding: 1.5rem; text-align: center; box-shadow: var(--shadow-card); margin: 0.5rem;">
            <div style="font-size: 2rem; font-weight: 700; color: var(--primary-blue); margin-bottom: 0.5rem;">{stats_data.get('pages_analyzed', 0)}</div>
            <div style="font-size: 0.9rem; color: var(--text-secondary); text-transform: uppercase; letter-spacing: 1px;">Pages Analyzed</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div style="background: var(--card-bg); border-radius: 12px; padding: 1.5rem; text-align: center; box-shadow: var(--shadow-card); margin: 0.5rem;">
            <div style="font-size: 2rem; font-weight: 700; color: var(--primary-blue); margin-bottom: 0.5rem;">{stats_data.get('time_saved', '0m')}</div>
            <div style="font-size: 0.9rem; color: var(--text-secondary); text-transform: uppercase; letter-spacing: 1px;">Time Saved</div>
        </div>
        """, unsafe_allow_html=True)
