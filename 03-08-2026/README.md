# AI Text Assistant - Streamlit

## Project Overview
This project is an AI Text Assistant created using Python, Streamlit and the Hugging Face `google/flan-t5-small` model.

## Features
- User question input
- AI-generated responses
- Hugging Face lightweight model
- Maximum output length control
- Temperature/creativity control
- Chat history using `st.session_state`
- Timestamps for conversations
- Clear history with confirmation
- Empty input validation
- 1000-character input limit
- Loading spinner
- Scrollable long responses
- Download chat history as a text file
- Sidebar application information
- Responsive columns and containers

## Run locally

```bash
pip install -r requirements.txt
python -m streamlit run app.py
```

The first run may take some time because the Hugging Face model needs to be downloaded.

## Deployment
The project can be deployed using Streamlit Community Cloud by connecting the GitHub repository and selecting `app.py` as the main file.
