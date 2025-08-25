#!/usr/bin/env python3
"""
Startup script for AI Research Summary Tool with Authentication
"""

import sys
import subprocess
import importlib.util

def check_dependency(package_name):
    """Check if a package is installed"""
    spec = importlib.util.find_spec(package_name)
    return spec is not None

def install_dependency(package_name):
    """Install a package using pip"""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
        return True
    except subprocess.CalledProcessError:
        return False

def main():
    """Main startup function"""
    print("🚀 Starting AI Research Summary Tool with Authentication...")
    
    # Check required dependencies
    required_packages = [
        "streamlit",
        "bcrypt",
        "extra-streamlit-components",
        "PyMuPDF",
        "python-docx",
        "pdfplumber",
        "sentence-transformers",
        "chromadb",
        "requests"
    ]
    
    missing_packages = []
    for package in required_packages:
        if not check_dependency(package):
            missing_packages.append(package)
    
    if missing_packages:
        print(f"❌ Missing packages: {', '.join(missing_packages)}")
        print("Installing missing packages...")
        
        for package in missing_packages:
            print(f"Installing {package}...")
            if install_dependency(package):
                print(f"✅ {package} installed successfully")
            else:
                print(f"❌ Failed to install {package}")
                return False
    
    print("✅ All dependencies are installed")
    
    # Run the Streamlit app
    print("🌐 Starting Streamlit application...")
    print("📝 The application will open in your default web browser")
    print("🔐 You'll need to register/login before uploading files")
    print("⏹️  Press Ctrl+C to stop the application")
    print("-" * 50)
    
    try:
        subprocess.run([sys.executable, "-m", "streamlit", "run", "rag.py", "--server.port", "8501"])
    except KeyboardInterrupt:
        print("\n👋 Application stopped by user")
    except Exception as e:
        print(f"❌ Error starting application: {e}")
        return False
    
    return True

if __name__ == "__main__":
    success = main()
    if not success:
        sys.exit(1)