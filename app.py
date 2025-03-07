import streamlit as st
import os
import openai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def translate_text(text, source_lang, target_lang):
    """
    Translate text from source language to target language using OpenAI API
    """
    if not text:
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
    st.title("Trilingual Translator - English, Latin, Classical Chinese")
    st.markdown("Enter text in any of the three languages and translate to the others.")
    
    # Initialize session state variables if they don't exist
    if 'english_text' not in st.session_state:
        st.session_state.english_text = ""
    if 'latin_text' not in st.session_state:
        st.session_state.latin_text = ""
    if 'chinese_text' not in st.session_state:
        st.session_state.chinese_text = ""
    if 'active_lang' not in st.session_state:
        st.session_state.active_lang = None
        
    # Create columns for language inputs
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("English")
        english_input = st.text_area("English Text", 
                                    value=st.session_state.english_text,
                                    height=150,
                                    key="english_input")
        
        if st.button("Translate from English"):
            st.session_state.english_text = english_input
            st.session_state.active_lang = "English"
    
    with col2:
        st.subheader("Latin")
        latin_input = st.text_area("Latin Text", 
                                  value=st.session_state.latin_text,
                                  height=150,
                                  key="latin_input")
        
        if st.button("Translate from Latin"):
            st.session_state.latin_text = latin_input
            st.session_state.active_lang = "Latin"
    
    with col3:
        st.subheader("Classical Chinese")
        chinese_input = st.text_area("Classical Chinese Text", 
                                    value=st.session_state.chinese_text,
                                    height=150,
                                    key="chinese_input")
        
        if st.button("Translate from Classical Chinese"):
            st.session_state.chinese_text = chinese_input
            st.session_state.active_lang = "Classical Chinese"
    
    # Perform translations if a language is active
    if st.session_state.active_lang == "English" and st.session_state.english_text:
        # Translate English to Latin and Chinese
        st.session_state.latin_text = translate_text(
            st.session_state.english_text, "English", "Latin")
        st.session_state.chinese_text = translate_text(
            st.session_state.english_text, "English", "Classical Chinese")
        
        # Update the interface with translations
        st.experimental_rerun()
        
    elif st.session_state.active_lang == "Latin" and st.session_state.latin_text:
        # Translate Latin to English and Chinese
        st.session_state.english_text = translate_text(
            st.session_state.latin_text, "Latin", "English")
        st.session_state.chinese_text = translate_text(
            st.session_state.latin_text, "Latin", "Classical Chinese")
        
        # Update the interface with translations
        st.experimental_rerun()
        
    elif st.session_state.active_lang == "Classical Chinese" and st.session_state.chinese_text:
        # Translate Chinese to English and Latin
        st.session_state.english_text = translate_text(
            st.session_state.chinese_text, "Classical Chinese", "English")
        st.session_state.latin_text = translate_text(
            st.session_state.chinese_text, "Classical Chinese", "Latin")
        
        # Update the interface with translations
        st.experimental_rerun()
    
    # Information about API key setup
    st.divider()
    st.subheader("Setup Instructions")
    st.markdown("""
    1. Create a file named `.env` in the same directory as this script
    2. Add your OpenAI API key to the file in this format: `OPENAI_API_KEY=your_api_key_here`
    3. Save the file and run the application with `streamlit run app.py`
    
    Note: Make sure you have installed all required packages with:
    ```
    pip install streamlit openai python-dotenv
    ```
    """)

if __name__ == "__main__":
    main()