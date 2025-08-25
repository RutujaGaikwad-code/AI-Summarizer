# AI Research Summary Tool - Authentication System

## Overview
This application now includes a comprehensive user authentication system that requires users to register and login before they can upload and process research papers.

## Features

### 🔐 Authentication Features
- **User Registration**: Users can create accounts with username, email, and password
- **User Login**: Secure login with username and password
- **Password Security**: Passwords are hashed using bcrypt
- **Email Validation**: Email format validation during registration
- **Password Strength**: Password must meet security requirements
- **Session Management**: Persistent login sessions
- **User-Specific Files**: Each user can only access their own uploaded files

### 📁 File Management
- **User Isolation**: Files are isolated per user
- **Personal File List**: Users can only see and manage their own files
- **Secure Deletion**: Users can only delete their own files
- **File Tracking**: All file operations are tracked per user

## Security Requirements

### Password Requirements
- Minimum 8 characters
- At least one uppercase letter
- At least one lowercase letter
- At least one digit

### Email Requirements
- Valid email format (e.g., user@example.com)
- Unique email address per user

## Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
streamlit run rag.py
```

## Usage

### First Time Setup
1. Open the application in your browser
2. Click "Switch to Register" in the sidebar
3. Fill in your details:
   - Username (minimum 3 characters)
   - Email (valid format)
   - Password (meets security requirements)
   - Confirm Password
4. Click "Register"
5. After successful registration, you'll be redirected to login

### Login
1. Enter your username and password
2. Click "Login"
3. You'll be redirected to the main application

### Using the Application
- **File Upload**: Upload PDF or DOCX files (only visible to you)
- **File Management**: View and delete your uploaded files
- **Question & Answer**: Ask questions about your uploaded documents
- **Chat**: Upload a PDF for temporary analysis

### Logout
- Click the "Logout" button in the top-right corner
- You'll be redirected to the login page

## File Structure

```
AIRST_RAG/
├── rag.py              # Main application with authentication
├── auth.py             # Authentication module
├── users.json          # User database (created automatically)
├── user_files.json     # User file mappings (created automatically)
├── uploads/            # Uploaded files directory
├── processed_files.json # Legacy file mappings
└── .streamlit/
    └── config.toml     # Streamlit configuration
```

## Data Storage

### User Data (`users.json`)
```json
{
  "username": {
    "email": "user@example.com",
    "password": "hashed_password",
    "created_at": "2024-01-01T00:00:00",
    "last_login": "2024-01-01T12:00:00"
  }
}
```

### User Files (`user_files.json`)
```json
{
  "username": {
    "original_filename.pdf": "unique_filename_uuid"
  }
}
```

## Security Notes

- Passwords are hashed using bcrypt (industry standard)
- User data is stored locally in JSON files
- Each user can only access their own files
- Session state is managed by Streamlit
- No sensitive data is logged or exposed

## Troubleshooting

### Common Issues
1. **Registration fails**: Check password requirements and email format
2. **Login fails**: Verify username and password
3. **Files not showing**: Make sure you're logged in with the correct account
4. **Permission errors**: Check file permissions in the uploads directory

### Reset User Data
To reset all user data (use with caution):
```bash
rm users.json user_files.json
```

## API Integration

The authentication system is designed to work with the existing RAG (Retrieval-Augmented Generation) functionality. All file operations are now user-specific, ensuring data privacy and security.
