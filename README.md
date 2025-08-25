# AIRST 1.0

<br>

![](https://raw.githubusercontent.com/pham0084/finalfantasyxv/main/Thumbnail.jpeg)

<p>
  
# Welcome to our AI-powered research paper summarization tool!

Get concise and informative summaries of research papers with just a few clicks using our tool! Designed to save you time and effort, it accurately summarizes content-heavy papers and highlights the shortened main points. Say goodbye to lengthy reading and hello to efficient research!

## Getting started
Getting started is easy. All you need to do is upload your paper, and our advanced AI algorithm will extract the most important information for you. Our algorithm uses advanced natural language processing techniques to identify the key concepts, ideas, and findings presented in the paper, and condenses them into a succinct and coherent summary presented in text. Plus, you can even get a pptx file with the main points for more effective visualization. 

Our tool is user-friendly and accessible to anyone who needs to understand research papers quickly and efficiently. Whether you're a student, researcher, or professional, our tool can help you save time and effort by providing you with a summary of the paper's main ideas and findings.

## Versatile tool
Our tool is designed to work with research papers from a variety of fields and disciplines, including but not limited to science, engineering, medicine, social sciences, and humanities. Whether you need to quickly understand the main findings of a paper for your own research or to communicate the highlights of a paper to your colleagues, our tool can help.

Our algorithm is constantly learning and improving, so you can be sure that you're getting the most accurate and up-to-date summary of the paper's main ideas and findings.

## Limitations
Please note that while our tool is highly accurate and reliable, it is not intended to replace the need for reading and understanding the full paper (only able to summarize it). Our summarization is meant to provide a quick overview of the main ideas and findings presented in the paper, and should be used as a supplement to your own reading and analysis.


## Features
- **🔐 User Authentication**: Secure login and registration system
- **👤 User-Specific Files**: Each user can only access their own uploaded files
- **📄 Enhanced Summarization**: AI-powered research paper summarization with customizable length
- **🌍 Multi-Language Support**: Choose from 12 languages for all summarization and Q&A features
- **🔬 Advanced AI Summarization**: 
  - **Source Traceable Summarization**: Every claim linked to exact paragraphs (P1, P2, P3, etc.)
  - **Multi-Document Aggregation**: Generate separate summaries for each document with citations from their respective documents
  - **Multi-Language Support**: Choose from 12 languages for summarization
  - **Legal Contract Summarization**: Specialized analysis with clause tracking and risk assessment
  - **Factual Consistency**: All claims supported by specific document sections
  - **Enhanced Download Options**: Download summaries as PDF or text files
- **📝 Professional Formatting**: Well-structured summaries with clear paragraphs and bullet points
- **📚 Automatic Citations**: Extract and include proper citations from research papers
- **🔍 Source Traceability**: Complete source attribution with paragraph-level references
- **❓ Interactive Q&A**: Ask questions and get concise answers with source citations in your chosen language
- **📁 Multi-format Support**: Upload PDF and DOCX files
- **🧠 Advanced NLP**: Natural language processing for accurate content extraction
- **💾 Download Summaries**: Export summaries as text files with citations
- **🔒 Secure Password Storage**: Passwords are hashed using bcrypt
- **📊 User Statistics**: Track user activity and file usage


## Installation
  
1. Clone the repository
  
    ```
    git clone https://github.com/Govind-Asawa/AI-PDF-Summarizer
    ```
  
2. Install the required packages
  
    ```
    pip install -r requirements.txt
    ```
  
3. Run the app

    **Option 1: Using the startup script (Recommended)**
    ```
    cd .\AIRST_RAG\
    python run_app.py
    ```
    
    **Option 2: Using the batch file (Windows)**
    ```
    cd .\AIRST_RAG\
    run_app.bat
    ```
    
    **Option 3: Manual startup**
    ```
    cd .\AIRST_RAG\
    streamlit run rag.py
    ```
  
The startup script will automatically check and install any missing dependencies. After successful installation, the application will open in your default web browser!

We hope you like it!
  
## Usage
  
### 🔐 First Time Setup
1. **Register**: Create a new account with username, email, and password
2. **Login**: Sign in with your credentials
3. **Security**: Your password must meet security requirements (8+ chars, uppercase, lowercase, digit)

### 📄 Using the Application
1. **Upload Files**: Upload healthcare-related academic papers in PDF or DOCX format
2. **Generate Summaries**: 
   - Choose summary length (Brief/Standard/Detailed)
   - Select your preferred language (12 languages supported)
   - Get well-formatted summaries with clear paragraphs
   - Include automatic citations from the source
   - Download summaries as text files
3. **Ask Questions**: 
   - Ask specific questions about your uploaded papers
   - Select your preferred language for Q&A
   - Get concise answers with proper citations
   - Select specific files to search through
4. **Quick Analysis**: Upload PDFs for instant summarization and Q&A in your chosen language
5. **Manage Files**: View and delete your uploaded files (only visible to you)

### 🔬 Advanced AI Summarization Features

#### **Multi-Language Support**
- **Purpose**: Generate summaries and Q&A in your preferred language
- **Usage**:
  1. Select your preferred language from the dropdown (12 languages available)
  2. All summaries, Q&A, and features will use the selected language
  3. Citations and formatting adapted to language conventions
- **Supported Languages**: English, Spanish, French, German, Italian, Portuguese, Russian, Chinese, Japanese, Korean, Arabic, Hindi

#### **Source Traceable Summarization**
- **Purpose**: Generate summaries with exact paragraph references for complete source traceability
- **Usage**: 
  1. Go to "Advanced Summary" tab
  2. Select "Source Traceable Summary"
  3. Choose your preferred language
  4. Choose a document to analyze
  5. Generate summary with paragraph references (P1, P2, P3, etc.)
  6. Explore paragraph mapping for detailed source information
- **Benefits**: Every claim can be traced back to specific document sections

#### **Multi-Document Aggregation**
- **Purpose**: Generate separate summaries for each document with citations from their respective documents
- **Usage**:
  1. Go to "Advanced Summary" tab
  2. Select "Multi-Document Summary"
  3. Choose 2 or more documents for analysis
  4. Select your preferred language (12 languages supported)
  5. Generate individual summaries with document-specific citations
  6. Review each document's summary separately
  7. Download individual summaries as PDF or text files
- **Benefits**: Each document gets its own comprehensive summary with citations from within that document in your chosen language
- **Download Options**: Individual PDF/text files for each document + combined download options

#### **Legal Contract Summarization**
- **Purpose**: Specialized analysis for legal documents with clause tracking
- **Usage**:
  1. Go to "Advanced Summary" tab
  2. Select "Legal Contract Summary"
  3. Upload legal document (contract, agreement, etc.)
  4. Select your preferred language
  5. Generate legal analysis with clause tracking
  6. Review compliance requirements and risk assessment
- **Benefits**: Automated clause identification and risk evaluation

#### **Enhanced Citation System**
- **Every Line Citation**: All statements include proper citations
- **Multiple Formats**: [Author et al., Year] and [Source: filename]
- **Automatic Addition**: Ensures no statement lacks proper attribution
- **Source Traceability**: Complete paragraph-level reference system
- **Multi-Language Citations**: Citations adapted to language conventions

### 🔒 Security Features
- **User Isolation**: Each user can only access their own files
- **Secure Storage**: Passwords are hashed using industry-standard bcrypt
- **Session Management**: Secure login sessions with logout functionality
- **Data Privacy**: All file operations are user-specific

## Contributing
Contributions are welcome! If you find any bugs or have any feature requests, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License.

</p>
