import streamlit as st
import bcrypt
import json
import os
from datetime import datetime, timedelta
import re

# User data file
USERS_FILE = "users.json"

def load_users():
    """Load users from JSON file"""
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_users(users):
    """Save users to JSON file"""
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f, indent=2)

def hash_password(password):
    """Hash password using bcrypt"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def verify_password(password, hashed_password):
    """Verify password against hash"""
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

def is_valid_email(email):
    """Validate email format"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def is_valid_password(password):
    """Validate password strength"""
    # At least 8 characters, 1 uppercase, 1 lowercase, 1 digit
    if len(password) < 8:
        return False, "Password must be at least 8 characters long"
    if not re.search(r'[A-Z]', password):
        return False, "Password must contain at least one uppercase letter"
    if not re.search(r'[a-z]', password):
        return False, "Password must contain at least one lowercase letter"
    if not re.search(r'\d', password):
        return False, "Password must contain at least one digit"
    return True, "Password is valid"

def register_user(username, email, password):
    """Register a new user"""
    users = load_users()
    
    # Check if username already exists
    if username in users:
        return False, "Username already exists"
    
    # Check if email already exists
    for user in users.values():
        if user['email'] == email:
            return False, "Email already registered"
    
    # Validate email format
    if not is_valid_email(email):
        return False, "Invalid email format"
    
    # Validate password strength
    is_valid, message = is_valid_password(password)
    if not is_valid:
        return False, message
    
    # Hash password and save user
    hashed_password = hash_password(password)
    users[username] = {
        'email': email,
        'password': hashed_password,
        'created_at': datetime.now().isoformat(),
        'last_login': None
    }
    save_users(users)
    return True, "Registration successful"

def login_user(username, password):
    """Login user"""
    users = load_users()
    
    if username not in users:
        return False, "Invalid username or password"
    
    user = users[username]
    if verify_password(password, user['password']):
        # Update last login
        users[username]['last_login'] = datetime.now().isoformat()
        save_users(users)
        return True, "Login successful"
    else:
        return False, "Invalid username or password"

def logout_user():
    """Logout user"""
    if 'authenticated' in st.session_state:
        del st.session_state['authenticated']
    if 'username' in st.session_state:
        del st.session_state['username']

def is_authenticated():
    """Check if user is authenticated"""
    return st.session_state.get('authenticated', False)

def get_current_user():
    """Get current authenticated user"""
    return st.session_state.get('username', None)

def auth_page():
    """Display authentication page"""
    st.set_page_config(
        page_title="AIRST - Login",
        page_icon="🧠",
        layout="centered",
        initial_sidebar_state="collapsed"
    )
    
    # Custom CSS for white background and clean UI
    st.markdown("""
    <style>
    .main {
        background-color: #ffffff;
        color: #333333;
    }
    .stApp {
        background-color: #ffffff;
        color: #333333;
    }
    .stButton > button {
        background-color: #4CAF50;
        color: #ffffff;
        border-radius: 8px;
        padding: 12px 24px;
        border: none;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        background-color: #45a049;
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(76, 175, 80, 0.3);
    }
    .stTextInput > div > div > input {
        background-color: #ffffff;
        color: #333333;
        border-radius: 8px;
        border: 2px solid #4CAF50;
    }
    .stFormSubmitButton > button {
        background-color: #4CAF50;
        color: #ffffff;
        border-radius: 8px;
        padding: 15px 30px;
        border: none;
        font-weight: bold;
        font-size: 16px;
        transition: all 0.3s ease;
    }
    .stFormSubmitButton > button:hover {
        background-color: #45a049;
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(76, 175, 80, 0.3);
    }
    .auth-container {
        background: linear-gradient(135deg, #ffffff 0%, #f5f5f5 100%);
        padding: 40px;
        border-radius: 12px;
        margin: 50px auto;
        max-width: 600px;
        border: 2px solid #4CAF50;
        box-shadow: 0 4px 12px rgba(76, 175, 80, 0.2);
    }
    .auth-header {
        text-align: center;
        margin-bottom: 30px;
        color: #333333;
    }
    .auth-tabs {
        display: flex;
        justify-content: center;
        margin-bottom: 30px;
    }
    .auth-tab {
        background-color: #ffffff;
        color: #333333;
        border: 2px solid #4CAF50;
        padding: 15px 30px;
        margin: 0 10px;
        border-radius: 8px;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    .auth-tab.active {
        background-color: #4CAF50;
        color: #ffffff;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Initialize session state
    if 'auth_mode' not in st.session_state:
        st.session_state.auth_mode = 'login'
    
    # Main authentication container
    st.markdown('<div class="auth-container">', unsafe_allow_html=True)
    
    # Header
    st.markdown("""
    <div class="auth-header">
        <h1 style="color: #4CAF50; margin-bottom: 10px;">🔐 AI Research Summary Tool</h1>
        <p style="color: #cccccc; font-size: 18px;">Secure Authentication Required</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Tab switching buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔑 Login", key="login_tab_btn", use_container_width=True):
            st.session_state.auth_mode = 'login'
            st.rerun()
    with col2:
        if st.button("📝 Register", key="register_tab_btn", use_container_width=True):
            st.session_state.auth_mode = 'register'
            st.rerun()
    
    st.markdown("---")
    
    if st.session_state.auth_mode == 'login':
        st.markdown("""
        <h2 style="color: #4CAF50; text-align: center; margin-bottom: 30px;">🔑 Login</h2>
        """, unsafe_allow_html=True)
        
        with st.form("login_form"):
            username = st.text_input("👤 Username", placeholder="Enter your username")
            password = st.text_input("🔒 Password", type="password", placeholder="Enter your password")
            submit_button = st.form_submit_button("🚀 Login")
            
            if submit_button:
                if username and password:
                    success, message = login_user(username, password)
                    if success:
                        st.session_state['authenticated'] = True
                        st.session_state['username'] = username
                        st.success(f"✅ {message}")
                        st.rerun()
                    else:
                        st.error(f"❌ {message}")
                else:
                    st.error("❌ Please fill in all fields")
    
    else:  # Register mode
        st.markdown("""
        <h2 style="color: #4CAF50; text-align: center; margin-bottom: 30px;">📝 Register</h2>
        """, unsafe_allow_html=True)
        
        with st.form("register_form"):
            username = st.text_input("👤 Username (min 3 characters)", placeholder="Choose a username")
            email = st.text_input("📧 Email", placeholder="Enter your email address")
            password = st.text_input("🔒 Password", type="password", placeholder="Create a strong password")
            confirm_password = st.text_input("🔒 Confirm Password", type="password", placeholder="Confirm your password")
            submit_button = st.form_submit_button("🚀 Register")
            
            if submit_button:
                if username and email and password and confirm_password:
                    if len(username) < 3:
                        st.error("❌ Username must be at least 3 characters long")
                    elif password != confirm_password:
                        st.error("❌ Passwords do not match")
                    else:
                        success, message = register_user(username, email, password)
                        if success:
                            st.success(f"✅ {message}")
                            st.session_state.auth_mode = 'login'
                            st.rerun()
                        else:
                            st.error(f"❌ {message}")
                else:
                    st.error("❌ Please fill in all fields")
    
    st.markdown('</div>', unsafe_allow_html=True)
