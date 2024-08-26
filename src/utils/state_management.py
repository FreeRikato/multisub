import streamlit as st

def initialize_session_state():
    if 'audio_file' not in st.session_state:
        st.session_state.audio_file = None
    if 'input_language' not in st.session_state:
        st.session_state.input_language = 'Auto'
    if 'target_languages' not in st.session_state:
        st.session_state.target_languages = []
    if 'subtitles' not in st.session_state:
        st.session_state.subtitles = {'srt': '', 'vtt': '', 'txt': ''}
    if 'generate_clicked' not in st.session_state:
        st.session_state.generate_clicked = False