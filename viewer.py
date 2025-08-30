import streamlit as st

# ユーザーエージェントに基づいてモバイル端末かどうかを判定する関数
# 判定に失敗した場合はif_failedの値を返す。デフォルトはFalse
def st_is_mobile(if_failed=False):
    if st.context:
        headers = st.context.headers
        user_agent_string = headers.get("User-Agent", "")
        if not user_agent_string:
            return if_failed
        ua = user_agent_string.lower()
        # 以下、典型的なパターンごとに判定していく
        if 'iphone' in ua:
            return True
        if 'android' in ua and 'mobile' in ua:
            return True
        if 'windows phone' in ua:
            return True
        if 'blackberry' in ua:
            return True
    else:
        return if_failed
    return False

st.set_page_config(page_title="テストアプリ", layout="wide")

is_mobile = st_is_mobile()
if is_mobile:
    st.markdown("## モバイル端末でアクセスしています。")
    st.image("img/vertical_image.jpg")
else:
    st.markdown("## デスクトップ端末でアクセスしています。")
    st.image("img/horizontal_image.jpg")

st.write(st.context.headers)

# st.title("動画プレーヤー")
# # サンプルとして使うURLを表示
# st.text("サンプル動画：https://youtu.be/G1_7ztjTaB4")
# video_url = st.text_input("動画のURLを入力してください")

# st.write(st.context.url)


if video_url:
    st.video(video_url)
