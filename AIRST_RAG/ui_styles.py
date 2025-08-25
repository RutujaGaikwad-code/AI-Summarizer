import streamlit as st

def apply_custom_styles():
    """Apply UI styling to match the provided design images"""
    st.markdown("""
    <style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Root Variables for Color Scheme - Blue Theme */
    :root {
        --primary-blue: #4F7FFF;
        --secondary-blue: #6366f1;
        --light-blue: #E8F0FF;
        --dark-blue: #1E3A8A;
        --orange-accent: #FF6B35;
        --bg-gradient: linear-gradient(135deg, #4F7FFF 0%, #6366f1 100%);
        --card-bg: #ffffff;
        --text-primary: #1f2937;
        --text-secondary: #6b7280;
        --text-muted: #9ca3af;
        --border-color: #e5e7eb;
        --shadow-card: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
    }
    
    /* Main App Container */
    .main .block-container {
        padding: 2rem 3rem;
        max-width: 1200px;
        background: var(--dark-bg);
    }
    
    /* Hide Streamlit Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Custom Header Styling */
    .main-header {
        background: var(--primary-gradient);
        padding: 2rem;
        border-radius: 20px;
        margin-bottom: 2rem;
        box-shadow: var(--shadow-lg);
        text-align: center;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    .main-header h1 {
        font-family: 'Inter', sans-serif;
        font-weight: 700;
        font-size: 3rem;
        color: white;
        margin: 0;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
    }
    
    .main-header .subtitle {
        font-family: 'Inter', sans-serif;
        font-weight: 400;
        font-size: 1.2rem;
        color: rgba(255, 255, 255, 0.9);
        margin-top: 0.5rem;
    }
    
    /* Card Styling */
    .custom-card {
        background: var(--card-bg);
        border-radius: 16px;
        padding: 2rem;
        margin: 1rem 0;
        box-shadow: var(--shadow-lg);
        border: 1px solid var(--border-color);
        transition: all 0.3s ease;
    }
    
    .custom-card:hover {
        transform: translateY(-2px);
        box-shadow: var(--shadow-xl);
        border-color: #6366f1;
    }
    
    /* Feature Cards */
    .feature-card {
        background: linear-gradient(135deg, var(--card-bg) 0%, var(--accent-bg) 100%);
        border-radius: 16px;
        padding: 1.5rem;
        margin: 1rem;
        text-align: center;
        box-shadow: var(--shadow-lg);
        border: 1px solid var(--border-color);
        transition: all 0.3s ease;
    }
    
    .feature-card:hover {
        transform: translateY(-4px);
        box-shadow: var(--shadow-xl);
    }
    
    .feature-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
        display: block;
    }
    
    .feature-title {
        font-family: 'Inter', sans-serif;
        font-weight: 600;
        font-size: 1.3rem;
        color: var(--text-primary);
        margin-bottom: 0.5rem;
    }
    
    .feature-desc {
        font-family: 'Inter', sans-serif;
        font-weight: 400;
        color: var(--text-secondary);
        line-height: 1.6;
    }
    
    /* Button Styling */
    .stButton > button {
        background: var(--primary-gradient) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 0.75rem 2rem !important;
        font-family: 'Inter', sans-serif !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
        transition: all 0.3s ease !important;
        box-shadow: var(--shadow-lg) !important;
        text-transform: uppercase !important;
        letter-spacing: 0.5px !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: var(--shadow-xl) !important;
        background: linear-gradient(135deg, #5a67d8 0%, #6b46c1 100%) !important;
    }
    
    /* File Uploader Styling */
    .stFileUploader > div {
        background: var(--card-bg) !important;
        border: 2px dashed #6366f1 !important;
        border-radius: 16px !important;
        padding: 2rem !important;
        text-align: center !important;
    }
    
    .stFileUploader label {
        color: var(--text-primary) !important;
        font-family: 'Inter', sans-serif !important;
        font-weight: 500 !important;
    }
    
    /* Progress Bar Styling */
    .stProgress > div > div > div {
        background: var(--primary-gradient) !important;
        border-radius: 10px !important;
    }
    
    /* Expander Styling */
    .streamlit-expanderHeader {
        background: var(--card-bg) !important;
        border-radius: 12px !important;
        border: 1px solid var(--border-color) !important;
        color: var(--text-primary) !important;
        font-family: 'Inter', sans-serif !important;
        font-weight: 600 !important;
    }
    
    .streamlit-expanderContent {
        background: var(--card-bg) !important;
        border: 1px solid var(--border-color) !important;
        border-radius: 0 0 12px 12px !important;
        padding: 1.5rem !important;
    }
    
    /* Sidebar Styling */
    .css-1d391kg {
        background: var(--card-bg) !important;
        border-right: 1px solid var(--border-color) !important;
    }
    
    /* Success/Error Message Styling */
    .stSuccess {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%) !important;
        color: white !important;
        border-radius: 12px !important;
        border: none !important;
        padding: 1rem !important;
        font-family: 'Inter', sans-serif !important;
    }
    
    .stError {
        background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%) !important;
        color: white !important;
        border-radius: 12px !important;
        border: none !important;
        padding: 1rem !important;
        font-family: 'Inter', sans-serif !important;
    }
    
    .stWarning {
        background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%) !important;
        color: white !important;
        border-radius: 12px !important;
        border: none !important;
        padding: 1rem !important;
        font-family: 'Inter', sans-serif !important;
    }
    
    .stInfo {
        background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%) !important;
        color: white !important;
        border-radius: 12px !important;
        border: none !important;
        padding: 1rem !important;
        font-family: 'Inter', sans-serif !important;
    }
    
    /* Selectbox Styling */
    .stSelectbox > div > div {
        background: var(--card-bg) !important;
        border: 1px solid var(--border-color) !important;
        border-radius: 12px !important;
        color: var(--text-primary) !important;
    }
    
    /* Text Input Styling */
    .stTextInput > div > div > input {
        background: var(--card-bg) !important;
        border: 1px solid var(--border-color) !important;
        border-radius: 12px !important;
        color: var(--text-primary) !important;
        font-family: 'Inter', sans-serif !important;
    }
    
    /* Metric Styling */
    .metric-container {
        background: var(--card-bg);
        border-radius: 16px;
        padding: 1.5rem;
        text-align: center;
        box-shadow: var(--shadow-lg);
        border: 1px solid var(--border-color);
        margin: 1rem 0;
    }
    
    .metric-value {
        font-family: 'Inter', sans-serif;
        font-weight: 700;
        font-size: 2.5rem;
        color: #6366f1;
        margin-bottom: 0.5rem;
    }
    
    .metric-label {
        font-family: 'Inter', sans-serif;
        font-weight: 500;
        color: var(--text-secondary);
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    /* Animation Classes */
    .fade-in {
        animation: fadeIn 0.6s ease-in;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .slide-in {
        animation: slideIn 0.8s ease-out;
    }
    
    @keyframes slideIn {
        from { opacity: 0; transform: translateX(-30px); }
        to { opacity: 1; transform: translateX(0); }
    }
    
    /* Custom Scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: var(--dark-bg);
    }
    
    ::-webkit-scrollbar-thumb {
        background: var(--primary-gradient);
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(135deg, #5a67d8 0%, #6b46c1 100%);
    }
    
    /* Typography */
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Inter', sans-serif !important;
        color: var(--text-primary) !important;
    }
    
    p, div, span {
        font-family: 'Inter', sans-serif !important;
        color: var(--text-secondary) !important;
        line-height: 1.6 !important;
    }
    
    /* Loading Spinner */
    .stSpinner > div {
        border-top-color: #6366f1 !important;
    }
    
    /* Custom Divider */
    .custom-divider {
        height: 2px;
        background: var(--primary-gradient);
        border-radius: 1px;
        margin: 2rem 0;
        opacity: 0.6;
    }
    
    /* Stats Grid */
    .stats-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 1rem;
        margin: 2rem 0;
    }
    
    /* Glassmorphism Effect */
    .glass-card {
        background: rgba(30, 41, 59, 0.8);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 16px;
        padding: 2rem;
        box-shadow: var(--shadow-lg);
    }
    </style>
    """, unsafe_allow_html=True)

def create_header():
    """Create an attractive header for the application"""
    st.markdown("""
    <div class="main-header fade-in">
        <h1>🧠 Welcome to AI Summarizer</h1>
        <div class="subtitle">Secure Authentication Required</div>
    </div>
    """, unsafe_allow_html=True)

def create_feature_cards():
    """Create feature showcase cards"""
    st.markdown("""
    <div class="fade-in">
        <h2 style="text-align: center; margin: 3rem 0 2rem 0; color: #f8fafc;">✨ Powerful Features</h2>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="feature-card slide-in">
            <div class="feature-icon">📄</div>
            <div class="feature-title">Smart Document Processing</div>
            <div class="feature-desc">Advanced AI-powered extraction and analysis of research papers in PDF and DOCX formats</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card slide-in">
            <div class="feature-icon">🤖</div>
            <div class="feature-title">AI-Powered Summaries</div>
            <div class="feature-desc">Generate comprehensive, accurate summaries using state-of-the-art language models</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="feature-card slide-in">
            <div class="feature-icon">📊</div>
            <div class="feature-title">Export & Analysis</div>
            <div class="feature-desc">Export summaries to PDF, analyze multiple documents, and generate insights</div>
        </div>
        """, unsafe_allow_html=True)

def create_stats_section(stats_data):
    """Create a statistics section with metrics"""
    st.markdown("""
    <div class="custom-divider"></div>
    <h3 style="text-align: center; color: #f8fafc; margin: 2rem 0;">📊 Session Statistics</h3>
    """, unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div class="metric-container">
            <div class="metric-value">{stats_data.get('files_processed', 0)}</div>
            <div class="metric-label">Files Processed</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="metric-container">
            <div class="metric-value">{stats_data.get('summaries_generated', 0)}</div>
            <div class="metric-label">Summaries Generated</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="metric-container">
            <div class="metric-value">{stats_data.get('pages_analyzed', 0)}</div>
            <div class="metric-label">Pages Analyzed</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div class="metric-container">
            <div class="metric-value">{stats_data.get('time_saved', '0m')}</div>
            <div class="metric-label">Time Saved</div>
        </div>
        """, unsafe_allow_html=True)

def create_upload_section():
    """Create an attractive file upload section"""
    st.markdown("""
    <div class="custom-card fade-in">
        <h3 style="color: #f8fafc; margin-bottom: 1rem;">📁 Upload Research Papers</h3>
        <p style="color: #cbd5e1; margin-bottom: 1.5rem;">
            Upload your research papers in PDF or DOCX format. Our AI will analyze and generate comprehensive summaries.
        </p>
    </div>
    """, unsafe_allow_html=True)

def create_processing_animation():
    """Create a processing animation"""
    st.markdown("""
    <div style="text-align: center; padding: 2rem;">
        <div style="font-size: 3rem; animation: pulse 2s infinite;">🧠</div>
        <h3 style="color: #6366f1; margin-top: 1rem;">AI is analyzing your documents...</h3>
        <p style="color: #cbd5e1;">This may take a few moments depending on document size</p>
    </div>
    <style>
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.1); }
        100% { transform: scale(1); }
    }
    </style>
    """, unsafe_allow_html=True)
