import streamlit as st
from components.sidebar import render_sidebar
from components.subtitle_display import display_subtitles
from utils.state_management import initialize_session_state

def main():
    st.title('Multi Subtitles Generator')
    initialize_session_state()
    render_sidebar()
    display_subtitles()

if __name__ == "__main__":
    main()