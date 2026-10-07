import streamlit as st

# 메뉴 구성만 담당하는 파일입니다. 실제 화면은 pages 폴더의 파일에 있습니다.
nav = st.navigation(
    [
        st.Page("pages/1_통관관리_데모.py", title="통관관리 데모", icon="🛃", default=True),
        st.Page("pages/2_물류운영_대시보드_데모.py", title="물류운영 대시보드 데모", icon="📦"),
    ]
)
nav.run()
