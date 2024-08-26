import streamlit as st
import asyncio
from utils.subtitle_generator import generate_subtitles

def render_sidebar():
    st.sidebar.header('Upload Audio')
    uploaded_file = st.sidebar.file_uploader('Choose an audio file', type=['mp3', 'wav', 'm4a'])

    if uploaded_file is not None:
        st.session_state.audio_file = uploaded_file
        st.sidebar.success('Audio uploaded successfully!')
        st.sidebar.audio(st.session_state.audio_file, format='audio/wav')

        render_language_settings()
        render_generate_button()

def render_language_settings():
    st.sidebar.header('Language Settings')
    st.session_state.input_language = st.sidebar.selectbox(
        'Select input audio language (or leave as Auto)', 
        ['Auto', 'English', 'Spanish', 'French', 'German', 'Chinese'],
        index=['Auto', 'English', 'Spanish', 'French', 'German', 'Chinese'].index(st.session_state.input_language)
    )
    
    st.session_state.target_languages = st.sidebar.multiselect(
        'Select target languages for subtitles',
        ['English', 'Spanish', 'French', 'German', 'Chinese'],
        default=st.session_state.target_languages
    )

def render_generate_button():
    if st.sidebar.button('Generate Subtitles'):
        st.session_state.generate_clicked = True
        with st.spinner('Generating subtitles...'):
            st.session_state.subtitles = asyncio.run(generate_subtitles())
        st.success('Subtitles generated successfully!')