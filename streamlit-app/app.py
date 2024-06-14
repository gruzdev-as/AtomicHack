import altair as alt
import streamlit as st
import io
from PIL import Image
import requests


st.set_page_config(
    page_title='Детекция дефектов сварных швов',
    page_icon='👨‍🏭',
    layout='wide',
    initial_sidebar_state='expanded'
)

alt.themes.enable('dark')


@st.cache_data
def detect_defects(image_bytes):
    image_with_bbox = image_bytes
    files = {'files': image_with_bbox}
    response = requests.post('http://flask-app:5000/process_image', files=files)
    return response.json()['message']



def main():
    state = st.session_state.get('state', 'initial')

    if state == 'initial':
        st.title('👨‍🏭 Детекция дефектов сварных швов')

        uploaded_image = st.file_uploader('Выберите изображение', type=['jpg', 'jpeg', 'png'])
        if uploaded_image is not None:
            image = Image.open(uploaded_image)
            image_bytes = io.BytesIO()
            image.save(image_bytes, format='PNG')
            st.session_state['image'] = image_bytes.getvalue()
            st.session_state['state'] = 'working'
            st.rerun()

    elif state == 'working':
        image_bytes = io.BytesIO(st.session_state['image'])
        image = Image.open(image_bytes)
        with st.sidebar:
            st.title('👨‍🏭 Детекция дефектов сварных швов')

            methods_list = [
                'ViT',
                'ResNet',
                'EfficientNet',
            ]

            selected_method = st.selectbox('Выберите режим поиска дефектов', methods_list)

            if st.button('Загрузить другое изображение'):
                st.session_state['state'] = 'initial'
                st.rerun()

            elif st.button('Документация'):
                st.session_state['state'] = 'docs'
                st.rerun()

        result = detect_defects(image_bytes)
        st.image(image.resize((600, 600)), caption='Эво как')
        st.write(result)

    elif state == 'docs':
        pass


if __name__ == '__main__':
    main()
