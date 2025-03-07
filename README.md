# Trilingual Translator App 🌐

A modern web application that provides seamless translation between English, Latin, and Classical Chinese using OpenAI's GPT model and Streamlit.

## Features 🚀

- Real-time translation between three languages:
  - English 🇬🇧
  - Latin 🏛️
  - Classical Chinese 🀄
- Clean, modern user interface with responsive design
- Easy-to-use text input areas for each language
- Instant translation with status feedback
- Support for multi-directional translation (any language to the other two)

## Prerequisites 📋

- Python 3.6 or higher
- OpenAI API key
- pip (Python package manager)

## Installation 💻

1. Clone the repository:
```bash
git clone https://github.com/yourusername/english-latin-classic-chinese-text-translation-app.git
cd english-latin-classic-chinese-text-translation-app
```

2. Install required packages:
```bash
pip install streamlit openai python-dotenv
```

3. Create a `.env` file in the root directory and add your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

## Usage 🎯

1. Start the application:
```bash
streamlit run app.py
```

2. Open your web browser and navigate to the provided local URL (typically http://localhost:8501)

3. Enter text in any of the three language boxes

4. Click the "Translate from [Language]" button below the text you want to translate

5. The translation will appear automatically in the other two language boxes

## Features in Detail ✨

- **Modern UI**: Clean interface with cards for each language
- **Real-time Translation**: Instant translation using OpenAI's GPT model
- **Error Handling**: Comprehensive error messages and status updates
- **Responsive Design**: Works well on different screen sizes
- **Session State Management**: Maintains translation state during usage
- **Easy Setup**: Simple environment configuration with .env file

## Technical Details 🔧

- Built with Streamlit for the web interface
- Uses OpenAI's GPT-4o-mini model for translations
- Implements custom CSS for enhanced visual appeal
- Features proper error handling and API key validation
- Maintains session state for smooth user experience

## Note 📝

- The application requires a valid OpenAI API key to function
- Translation quality depends on the GPT model's capabilities
- Classical Chinese translations are optimized for historical/literary Chinese text

## Contributing 🤝

Contributions, issues, and feature requests are welcome! Feel free to check [issues page](link-to-your-issues-page).

## License 📄

This project is licensed under the MIT License - see the LICENSE file for details.