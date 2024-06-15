import altair as alt
import streamlit as st
import requests

st.set_page_config(
    page_title='Детекция дефектов сварных швов',
    page_icon='👨‍🏭',
    layout='wide',
    initial_sidebar_state='expanded'
)

alt.themes.enable('dark')



def main():
    state = st.session_state.get('state', 'initial')

    if state == 'initial':
        st.title('👨‍🏭 Детекция дефектов сварных швов')
        uploaded_image = st.file_uploader('Выберите изображение', type=['jpg', 'jpeg', 'png'])

        if st.button('Загрузить другое изображение'):
            st.session_state['state'] = 'initial'
            st.rerun()

if __name__ == '__main__':
    main()