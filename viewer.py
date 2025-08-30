# Streamlitで指定したURLの動画を表示するアプリ
import streamlit as st

st.title("動画プレーヤー")
# サンプルとして使うURLを表示
st.text("サンプル動画：https://youtu.be/G1_7ztjTaB4")
video_url = st.text_input("動画のURLを入力してください")

if video_url:
    st.video(video_url)
