import streamlit as st
import requests
import altair as alt

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
        if uploaded_image is not None:
            st.image(uploaded_image, caption='Uploaded Image.', use_column_width=True)
            if st.button('Отправить на сервер'):
                image_bytes = uploaded_image.read()
                response = requests.post('http://flask-api:5000/process_image', files={'file': image_bytes})
                st.session_state['state'] = 'working'
                if response.status_code == 200:
                    st.success("Image processed successfully!")
                    response_data = response.json()
                    filepath = response_data.get("file_path")
                    st.image(filepath)
                else:
                    st.error(f"Failed to process image. Server responded with status code: {response.status_code}")

    elif state == 'working':
        if st.button('Загрузить другое изображение'):
            st.session_state['state'] = 'initial'
            st.rerun()


if __name__ == '__main__':
    main()
