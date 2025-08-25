# 🔧 Troubleshooting Guide

## Common Issues and Solutions

### ❌ API Key Errors

#### Error: "User not found" (401)
**Problem**: Invalid or expired OpenRouter API key

**Solutions**:
1. **Get a new API key**:
   - Visit https://openrouter.ai/keys
   - Sign up/login to your account
   - Generate a new API key
   - Copy the key (starts with `sk-or-v1-`)

2. **Configure the API key**:
   - **Option 1**: Use the Config button in the app
   - **Option 2**: Edit `.streamlit/secrets.toml` file
   - **Option 3**: Set as environment variable

3. **Test your API key**:
   - Use the "Test API Key" feature in the Config page
   - Verify the key is valid and has credits

#### Error: "Rate limit exceeded" (429)
**Problem**: Too many requests to the API

**Solutions**:
1. Wait a few minutes before trying again
2. Check your OpenRouter account for rate limits
3. Consider upgrading your plan if needed

### 🔐 Authentication Issues

#### Can't register/login
**Solutions**:
1. Check password requirements (8+ chars, uppercase, lowercase, digit)
2. Ensure email format is valid
3. Try a different username if "already exists"
4. Clear browser cache and try again

#### Session issues
**Solutions**:
1. Refresh the page
2. Logout and login again
3. Clear browser cookies for the site

### 📁 File Upload Issues

#### Files not uploading
**Solutions**:
1. Check file format (PDF, DOC, DOCX only)
2. Ensure file size is reasonable (< 50MB)
3. Check file permissions
4. Try a different file

#### Files not showing after upload
**Solutions**:
1. Refresh the page
2. Check if you're logged in with the correct account
3. Look in the "PDFs/Docs" tab
4. Try uploading again

### 🧠 AI Processing Issues

#### Summaries not generating
**Solutions**:
1. Check API key configuration
2. Ensure file contains extractable text
3. Try a different file
4. Check internet connection

#### Poor quality summaries
**Solutions**:
1. Try different summary lengths
2. Upload higher quality PDFs
3. Ensure text is properly extracted
4. Try the Q&A feature for specific questions

### 🌐 Application Issues

#### App won't start
**Solutions**:
1. Check Python dependencies: `pip install -r requirements.txt`
2. Ensure Streamlit is installed: `pip install streamlit`
3. Check port availability (default: 8501)
4. Try running: `streamlit run rag.py`

#### Slow performance
**Solutions**:
1. Close other applications
2. Check internet connection
3. Try smaller files
4. Restart the application

## 🔑 API Key Setup Guide

### Quick Setup (Recommended)
1. Click the "⚙️ Config" button in the app
2. Choose "Temporary Setup" tab
3. Enter your OpenRouter API key
4. Click "Save Temporarily"
5. Test the key

### Permanent Setup
1. Get your API key from https://openrouter.ai/keys
2. Edit `.streamlit/secrets.toml`:
   ```toml
   OPENROUTER_API_KEY = "sk-or-v1-your-actual-key-here"
   ```
3. Restart the application

### Environment Variable Setup
```bash
# Windows (PowerShell)
$env:OPENROUTER_API_KEY="sk-or-v1-your-key-here"

# Linux/Mac
export OPENROUTER_API_KEY="sk-or-v1-your-key-here"
```

## 📞 Getting Help

### Check these first:
1. ✅ API key is valid and has credits
2. ✅ File format is supported (PDF/DOCX)
3. ✅ Internet connection is stable
4. ✅ All dependencies are installed

### Still having issues?
1. Check the error messages carefully
2. Try the troubleshooting steps above
3. Restart the application
4. Clear browser cache and cookies

### Common Error Messages:
- **"User not found"**: Invalid API key
- **"Rate limit exceeded"**: Too many requests
- **"No text extracted"**: PDF has no readable text
- **"File not found"**: File was deleted or moved
- **"Authentication required"**: Need to login first

## 🚀 Performance Tips

1. **Use smaller files** for faster processing
2. **Choose appropriate summary length** (Brief for quick overview)
3. **Close unused browser tabs** to free memory
4. **Use wired internet** for better stability
5. **Restart the app** if it becomes slow

## 🔒 Security Notes

- API keys are stored securely (hashed in session, encrypted in files)
- Files are isolated per user
- Passwords are hashed using bcrypt
- No sensitive data is logged or exposed 
