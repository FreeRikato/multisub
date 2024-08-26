import streamlit as st

def display_subtitles():
    if st.session_state.generate_clicked and st.session_state.audio_file is not None:
        st.header('Generated Subtitles')
        
        display_subtitle_format('SRT Format', 'srt')
        display_subtitle_format('VTT Format', 'vtt')
        display_subtitle_format('TXT Format', 'txt')
    elif st.session_state.audio_file is None:
        st.sidebar.warning('Please upload an audio file.')

def display_subtitle_format(title, format):
    st.subheader(title)
    st.text(st.session_state.subtitles[format])
    st.download_button(
        label=f"Download {format.upper()}",
        data=st.session_state.subtitles[format],
        file_name=f"subtitles.{format}",
        mime="text/plain"
    )