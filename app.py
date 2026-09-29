import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd

# 페이지 기본 설정
st.set_page_config(page_title="LSE 특송 배송조회", page_icon="📦", layout="centered")

BASE_URL = "https://lse-kj.com/delivery/tracking/number/{tracking_number}"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Accept-Language": "ko-KR,ko;q=0.9,ja;q=0.8,en;q=0.7",
}

def get_tracking_info(tracking_number: str):
    url = BASE_URL.format(tracking_number=tracking_number.strip())
    try:
        res = requests.get(url, headers=HEADERS, timeout=10)
        if res.status_code != 200:
            return None, f"서버 응답 오류 (HTTP {res.status_code})"
        
        soup = BeautifulSoup(res.text, "html.parser")
        if "House B/L" not in soup.get_text():
            return None, "운송장 번호가 등록되지 않았거나 조회할 수 없습니다."

        steps = ["배송준비", "발송완료", "통관중", "국내배송", "배송완료"]
        step_times = {s: "-" for s in steps}
        
        # 단계별 진행 테이블 파싱
        for table in soup.find_all("table"):
            rows = table.find_all("tr")
            if len(rows) >= 2:
                headers = [td.get_text(strip=True) for td in rows[0].find_all(["th", "td"])]
                values = [td.get_text(strip=True) for td in rows[1].find_all(["th", "td"])]
                if any(s in headers for s in steps):
                    for h, v in zip(headers, values):
                        if h in step_times and v:
                            step_times[h] = v

        latest_status = "배송준비"
        for s in reversed(steps):
            if step_times[s] != "-":
                latest_status = s
                break

        # 예정 스케줄 파싱
        schedules = {"수출통관일": "-", "출항 예정일": "-", "일본 입항 예정일": "-"}
        for table in soup.find_all("table"):
            text = table.get_text()
            if "출항" in text or "입항" in text or "통관" in text:
                rows = table.find_all("tr")
                for r in rows:
                    cells = [td.get_text(strip=True) for td in r.find_all(["th", "td"])]
                    for idx, c in enumerate(cells):
                        if "수출통관" in c and idx + 1 < len(cells):
                            schedules["수출통관일"] = cells[idx + 1]
                        elif "출항" in c and idx + 1 < len(cells):
                            schedules["출항 예정일"] = cells[idx + 1]
                        elif "입항" in c and idx + 1 < len(cells):
                            schedules["일본 입항 예정일"] = cells[idx + 1]

        return {"latest": latest_status, "steps": step_times, "schedules": schedules}, None
    except Exception as e:
        return None, f"오류 발생: {str(e)}"

# 화면 UI 구성
st.title("📦 LSE 한일특송 배송조회")
st.caption("LOTOS SUPER EXPRESS 운송장(House B/L) 실시간 추적 서비스")

tracking_input = st.text_input(
    "운송장 번호를 입력하세요", 
    placeholder="예: 454205975462",
    help="LSE 송장 번호를 입력하세요."
)

if st.button("조회하기", type="primary"):
    if not tracking_input.strip():
        st.warning("운송장 번호를 입력해 주세요.")
    else:
        with st.spinner("배송 상태를 조회 중입니다..."):
            data, err = get_tracking_info(tracking_input.strip())
            
        if err:
            st.error(err)
        else:
            st.success(f"현재 상태: **{data['latest']}**")
            
            st.subheader("진행 단계")
            df_steps = pd.DataFrame([data["steps"]])
            st.table(df_steps)
            
            st.subheader("예정 스케줄")
            col1, col2, col3 = st.columns(3)
            col1.metric("수출통관일", data["schedules"]["수출통관일"])
            col2.metric("출항 예정일", data["schedules"]["출항 예정일"])
            col3.metric("일본 입항 예정일", data["schedules"]["일본 입항 예정일"])
            
            official_url = BASE_URL.format(tracking_number=tracking_input.strip())
            st.markdown(f"[🔗 LSE 공식 조회 페이지 바로가기]({official_url})")
