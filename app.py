import streamlit as st

st.set_page_config(page_title="물류 운영 시스템 포트폴리오", page_icon="📦", layout="wide", initial_sidebar_state="expanded")

# 왼쪽 메뉴를 항상 열린 상태로 고정 (접기 버튼 숨김) — 화면이 넓을 때만
st.markdown(
    """<style>
@media (min-width: 769px){
  [data-testid="stSidebarCollapseButton"],
  [data-testid="stSidebarCollapsedControl"],
  [data-testid="stExpandSidebarButton"]{display:none !important}
  section[data-testid="stSidebar"]{transform:none !important;visibility:visible !important;min-width:250px !important;max-width:250px !important;margin-left:0 !important}
}
</style>""",
    unsafe_allow_html=True,
)

nav = st.navigation(
    {
        "소개": [
            st.Page("pages/0_프로젝트_소개.py", title="만든 이유", icon="💡", default=True),
        ],
        "데모": [
            st.Page("pages/1_통관관리_데모.py", title="통관관리 데모", icon="🛃"),
            st.Page("pages/2_물류운영_대시보드_데모.py", title="물류운영 대시보드 데모", icon="📦"),
        ],
    }
)

with st.sidebar:
    st.caption("기획 · 설계 · 개발 1인\n\n모든 데모는 가상 데이터로 동작하며, 입력 내용은 저장되지 않습니다.")

nav.run()
