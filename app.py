import streamlit as st
import os
import openai
from dotenv import load_dotenv

# Page configuration
st.set_page_config(
    page_title="Trilingual Translator",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for a more modern look
st.markdown("""
<style>
    .main {
        background-color: #f8f9fa;
    }
    .stTextArea textarea {
        border-radius: 10px;
        border: 1px solid #e0e0e0;
        font-family: 'Inter', sans-serif;
    }
    .stButton button {
        border-radius: 10px;
        padding: 10px 25px;
        font-weight: 500;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
    }
    .stButton button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    h1, h2, h3 {
        font-family: 'Inter', sans-serif;
        font-weight: 700;
    }
    .language-card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }
    .language-title {
        font-size: 1.2rem;
        font-weight: 600;
        margin-bottom: 10px;
        color: #333;
    }
    .language-icon {
        font-size: 1.4rem;
        margin-right: 8px;
    }
    .footer {
        text-align: center;
        margin-top: 40px;
        color: #666;
        font-size: 0.8rem;
    }
    .status-message {
        padding: 10px;
        border-radius: 8px;
        margin: 15px 0;
    }
    .success {
        background-color: #d4edda;
        color: #155724;
    }
    .error {
        background-color: #f8d7da;
        color: #721c24;
    }
</style>
""", unsafe_allow_html=True)

# Load environment variables from .env file
load_dotenv()

# Set up OpenAI API key
openai_api_key = os.getenv("OPENAI_API_KEY")
if openai_api_key:
    openai.api_key = openai_api_key

def translate_text(text, source_lang, target_lang):
    """
    Translate text from source language to target language using OpenAI API
    """
    if not text:
        return ""
        
    if not openai_api_key:
        st.error("⚠️ OpenAI API key not found. Please check your .env file.")
        return ""
        
    try:
        prompt = f"Translate the following {source_lang} text to {target_lang}. Return ONLY the translated text with no additional commentary, introduction, or notes: {text}"
        
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a professional translator. Provide only the requested translation without any additional text, explanations, or commentary."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
        )
        
        return response.choices[0].message.content.strip()
    
    except Exception as e:
        st.error(f"Translation error: {str(e)}")
        return ""

def main():
    # App header with subtle animation
    st.markdown("""
    <div style="text-align: center; margin-bottom: 30px; animation: fadeIn 1s ease-in-out;">
        <h1 style="color: #1e3a8a; margin-bottom: 5px;">🌐 Trilingual Translator</h1>
        <p style="color: #6b7280; font-size: 1.1rem;">English · Latin · Classical Chinese</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Initialize session state variables
    if 'english_text' not in st.session_state:
        st.session_state.english_text = ""
    if 'latin_text' not in st.session_state:
        st.session_state.latin_text = ""
    if 'chinese_text' not in st.session_state:
        st.session_state.chinese_text = ""
    if 'active_lang' not in st.session_state:
        st.session_state.active_lang = None
    if 'translation_status' not in st.session_state:
        st.session_state.translation_status = None
    if 'is_translating' not in st.session_state:
        st.session_state.is_translating = False
        
    # Create columns for language inputs
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="language-card">', unsafe_allow_html=True)
        st.markdown('<div class="language-title"><span class="language-icon">🇬🇧</span> English</div>', unsafe_allow_html=True)
        english_input = st.text_area(
            label="English Text Input",
            value=st.session_state.english_text,
            height=150,
            key="english_input",
            placeholder="Enter English text here...",
            label_visibility="collapsed"
        )
        
        translate_en_button = st.button(
            "Translate from English",
            key="translate_en_button",
            use_container_width=True,
            disabled=st.session_state.is_translating
        )
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="language-card">', unsafe_allow_html=True)
        st.markdown('<div class="language-title"><span class="language-icon">🏛️</span> Latin</div>', unsafe_allow_html=True)
        latin_input = st.text_area(
            label="Latin Text Input",
            value=st.session_state.latin_text,
            height=150,
            key="latin_input",
            placeholder="Enter Latin text here...",
            label_visibility="collapsed"
        )
        
        translate_la_button = st.button(
            "Translate from Latin",
            key="translate_la_button",
            use_container_width=True,
            disabled=st.session_state.is_translating
        )
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown('<div class="language-card">', unsafe_allow_html=True)
        st.markdown('<div class="language-title"><span class="language-icon">🀄</span> Classical Chinese</div>', unsafe_allow_html=True)
        chinese_input = st.text_area(
            label="Classical Chinese Text Input",
            value=st.session_state.chinese_text,
            height=150,
            key="chinese_input",
            placeholder="Enter Classical Chinese text here...",
            label_visibility="collapsed"
        )
        
        translate_zh_button = st.button(
            "Translate from Classical Chinese",
            key="translate_zh_button",
            use_container_width=True,
            disabled=st.session_state.is_translating
        )
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Status message
    if st.session_state.translation_status:
        status_class = "success" if st.session_state.translation_status.startswith("✅") else "error"
        st.markdown(f'<div class="status-message {status_class}">{st.session_state.translation_status}</div>', unsafe_allow_html=True)
    
    # Handle translation buttons
    if translate_en_button and english_input:
        st.session_state.english_text = english_input
        st.session_state.active_lang = "English"
        st.session_state.is_translating = True
        perform_translation()
        
    elif translate_la_button and latin_input:
        st.session_state.latin_text = latin_input
        st.session_state.active_lang = "Latin"
        st.session_state.is_translating = True
        perform_translation()
        
    elif translate_zh_button and chinese_input:
        st.session_state.chinese_text = chinese_input
        st.session_state.active_lang = "Classical Chinese"
        st.session_state.is_translating = True
        perform_translation()
    
    # Information section
    with st.expander("🔧 Setup Instructions"):
        st.markdown("""
        ### Getting Started
        
        1. Create a file named `.env` in the same directory as this script
        2. Add your OpenAI API key to the file: `OPENAI_API_KEY=your_api_key_here`
        3. Save the file and run: `streamlit run app.py`
        
        ### Installation
        
        ```bash
        pip install streamlit openai python-dotenv
        ```
        
        ### About
        
        This application uses OpenAI's GPT-4o-mini model to provide accurate translations between English, Latin, and Classical Chinese.
        """)
    
    # Footer
    st.markdown("""
    <div class="footer">
        <p>Built with Streamlit & OpenAI · GPT-4o-mini</p>
    </div>
    """, unsafe_allow_html=True)

def perform_translation():
    """Helper function to perform translations based on active language"""
    with st.spinner("Translating..."):
        try:
            if st.session_state.active_lang == "English" and st.session_state.english_text:
                # Translate English to Latin and Chinese
                latin_translation = translate_text(
                    st.session_state.english_text, "English", "Latin")
                    
                chinese_translation = translate_text(
                    st.session_state.english_text, "English", "Classical Chinese")
                
                if latin_translation and chinese_translation:
                    st.session_state.latin_text = latin_translation
                    st.session_state.chinese_text = chinese_translation
                    st.session_state.translation_status = "✅ Translation completed successfully!"
                else:
                    st.session_state.translation_status = "⚠️ Translation incomplete. Please check API key and try again."
                
            elif st.session_state.active_lang == "Latin" and st.session_state.latin_text:
                # Translate Latin to English and Chinese
                english_translation = translate_text(
                    st.session_state.latin_text, "Latin", "English")
                    
                chinese_translation = translate_text(
                    st.session_state.latin_text, "Latin", "Classical Chinese")
                
                if english_translation and chinese_translation:
                    st.session_state.english_text = english_translation
                    st.session_state.chinese_text = chinese_translation
                    st.session_state.translation_status = "✅ Translation completed successfully!"
                else:
                    st.session_state.translation_status = "⚠️ Translation incomplete. Please check API key and try again."
                
            elif st.session_state.active_lang == "Classical Chinese" and st.session_state.chinese_text:
                # Translate Chinese to English and Latin
                english_translation = translate_text(
                    st.session_state.chinese_text, "Classical Chinese", "English")
                    
                latin_translation = translate_text(
                    st.session_state.chinese_text, "Classical Chinese", "Latin")
                
                if english_translation and latin_translation:
                    st.session_state.english_text = english_translation
                    st.session_state.latin_text = latin_translation
                    st.session_state.translation_status = "✅ Translation completed successfully!"
                else:
                    st.session_state.translation_status = "⚠️ Translation incomplete. Please check API key and try again."
            
        except Exception as e:
            st.session_state.translation_status = f"⚠️ Error: {str(e)}"
        
        st.session_state.is_translating = False
        st.rerun()

if __name__ == "__main__":
    main()