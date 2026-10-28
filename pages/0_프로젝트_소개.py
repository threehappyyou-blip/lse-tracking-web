import streamlit as st

# ---------- 스타일 (이 페이지 전용, 밝은 톤) ----------
CSS = """
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css">
<style>
[data-testid="stHeader"]{background:transparent}
.stApp{background:radial-gradient(circle at 100% 0%,#fde6ea 0,rgba(253,230,234,0) 30%),radial-gradient(circle at 0% 60%,#eef1ff 0,rgba(238,241,255,0) 30%),#f6f6f8}
.block-container,[data-testid="stMainBlockContainer"]{max-width:1080px !important;padding:3rem 2rem 4rem !important}
.pf,.pf *{font-family:Pretendard,-apple-system,"Noto Sans KR",sans-serif;letter-spacing:-.2px;box-sizing:border-box}
.pf{color:#1b1d21}
.pf .eyebrow{color:#e8435a;font-weight:800;font-size:13px;letter-spacing:.5px}
.pf h1{font-size:40px;line-height:1.25;font-weight:800;letter-spacing:-1.2px;margin:10px 0 14px;color:#1b1d21;padding:0}
.pf h1 em{font-style:normal;color:#e8435a}
.pf .lead{font-size:16px;line-height:1.75;color:#4b5058;max-width:760px;margin:0}
.pf .meta{display:flex;gap:8px;flex-wrap:wrap;margin-top:22px}
.pf .meta span{background:#fff;border:1px solid #eceef1;border-radius:20px;padding:7px 14px;font-size:12.5px;color:#444;font-weight:600}
.pf h2{font-size:24px;font-weight:800;letter-spacing:-.6px;margin:64px 0 6px;color:#1b1d21;padding:0}
.pf .sec-sub{font-size:14px;color:#8a909a;margin:0 0 20px}
.pf .card{background:#fff;border-radius:22px;padding:26px;box-shadow:0 1px 2px rgba(0,0,0,.03)}
.pf .q{display:grid;grid-template-columns:1fr 60px 1fr;gap:0;align-items:stretch}
.pf .q .box{background:#fff;border-radius:22px;padding:24px}
.pf .q .box.me{background:#1b1d21}
.pf .q .lbl{font-size:12px;font-weight:700;color:#8a909a;margin-bottom:10px}
.pf .q .box.me .lbl{color:#f3a6b3}
.pf .q .txt{font-size:18px;font-weight:700;line-height:1.55;color:#1b1d21}
.pf .q .box.me .txt{color:#fff}
.pf .q .ans{font-size:13px;color:#6b717a;margin-top:12px;line-height:1.65}
.pf .q .box.me .ans{color:#c5c9d1}
.pf .q .arrow{display:grid;place-items:center;color:#e8435a;font-size:26px;font-weight:800}
.pf .chain{display:flex;align-items:stretch;gap:0;flex-wrap:wrap}
.pf .chain .st{flex:1;min-width:150px;background:#fff;border-radius:18px;padding:18px 16px;position:relative}
.pf .chain .st b{display:block;font-size:15px;margin:8px 0 6px;color:#1b1d21}
.pf .chain .st p{margin:0;font-size:12.5px;color:#6b717a;line-height:1.6}
.pf .chain .st .n{font-size:11px;font-weight:800;color:#e8435a}
.pf .chain .st.goal{background:#e8435a}.pf .chain .st.goal b,.pf .chain .st.goal p,.pf .chain .st.goal .n{color:#fff}
.pf .chain .sep{display:grid;place-items:center;width:26px;color:#c2c6cc;font-weight:800}
.pf .kpi{display:inline-block;font-size:11.5px;font-weight:700;border-radius:7px;padding:3px 8px;margin:3px 4px 0 0}
.pf .kpi.dn{background:#e9f7ef;color:#16a34a}.pf .kpi.up{background:#fdecef;color:#e8435a}
.pf .two{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.pf .tool .tag{display:inline-block;font-size:11px;font-weight:800;border-radius:7px;padding:4px 9px;margin-bottom:12px}
.pf .tool h3{font-size:20px;font-weight:800;margin:0 0 6px;color:#1b1d21;padding:0}
.pf .tool .one{font-size:13.5px;color:#6b717a;margin:0 0 18px;line-height:1.6}
.pf .row{display:grid;grid-template-columns:62px 1fr;gap:12px;padding:14px 0;border-top:1px solid #f0f1f3}
.pf .row .k{font-size:12px;font-weight:800;color:#8a909a;padding-top:2px}
.pf .row ul{margin:0;padding-left:16px}.pf .row li{font-size:13.5px;line-height:1.7;color:#30343a}
.pf .row.prob .k{color:#e8435a}.pf .row.sol .k{color:#3b82f6}.pf .row.eff .k{color:#16a34a}
.pf .wide{margin-top:16px}.pf .cols3{display:grid;grid-template-columns:repeat(3,1fr);gap:22px}.pf .cols3 .row{grid-template-columns:1fr;gap:6px;align-content:start}
.pf .three{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.pf .pr .ic{width:40px;height:40px;border-radius:12px;background:#fdecef;color:#e8435a;display:grid;place-items:center;font-size:18px;margin-bottom:14px}
.pf .pr b{display:block;font-size:16px;margin-bottom:6px;color:#1b1d21}
.pf .pr p{margin:0;font-size:13px;color:#6b717a;line-height:1.65}
.pf .stack{display:flex;flex-wrap:wrap;gap:8px}
.pf .stack span{background:#f6f7f9;border-radius:9px;padding:7px 12px;font-size:12.5px;font-weight:600;color:#30343a}
.pf .stack span i{font-style:normal;color:#8a909a;font-weight:500;margin-right:6px}
.pf .cta-h{font-size:24px;font-weight:800;letter-spacing:-.6px;margin:64px 0 16px;color:#1b1d21}
[data-testid="stPageLink"] a{background:#e8435a;border-radius:14px;padding:14px 18px !important;justify-content:center}
[data-testid="stPageLink"] a p,[data-testid="stPageLink"] a span{color:#fff !important;font-weight:700;font-size:15px}
[data-testid="stPageLink"] a:hover{background:#d6324a}
@media(max-width:820px){.pf h1{font-size:30px}.pf .q,.pf .two,.pf .three,.pf .cols3{grid-template-columns:1fr}.pf .q .arrow{transform:rotate(90deg);height:40px}.pf .chain{flex-direction:column}.pf .chain .sep{width:auto;height:22px;transform:rotate(90deg)}}
</style>
"""


def html(s: str):
    # Markdown이 들여쓰기를 코드블록으로 해석하지 않도록 공백/빈 줄 제거
    st.markdown("\n".join(l.strip() for l in s.splitlines() if l.strip()), unsafe_allow_html=True)


html(CSS)

# ---------- 1. 히어로 ----------
html("""
<div class="pf">
<div class="eyebrow">PORTFOLIO · 물류 운영 시스템</div>
<h1>관리자가 덜 찾고, 덜 기다리고,<br><em>더 빨리 판단하게</em> 만드는 도구</h1>
<p class="lead">구매대행 물류팀에서 일하며 매일 반복되던 불편을 직접 시스템으로 바꿨습니다.
흩어진 통관 문의를 한 흐름으로 묶은 <b>통관관리 시스템</b>, 사기 전에 통관 문제를 미리 확인하는 <b>통관 확인 도구</b>, 통관 지연을 룰로 걸러 "오늘 할 일"로 바꿔주는 <b>통관 예외관리 레이더</b>, 공정별 병목을 실시간으로 보여주는 <b>물류 운영 대시보드</b>, 흩어진 요청을 아침 한 화면으로 모아 주는 <b>아침 업무 브리핑</b>, 출장 신청·정산과 세금계산서 점검을 한곳에 모은 <b>BO 업무 포털</b>입니다.</p>
<div class="meta"><span>기획 · 설계 · 개발 1인</span><span>현업 실사용</span><span>이 사이트는 가상 데이터 데모</span></div>
</div>
""")

# ---------- 2. 출발점 ----------
html("""
<div class="pf">
<h2>출발점이 된 질문</h2>
<p class="sec-sub">좋은 서비스는 "사용자가 무엇을 귀찮아하는가"에서 시작합니다.</p>
<div class="q">
<div class="box">
<div class="lbl">예를 들어, 중고거래 서비스라면</div>
<div class="txt">"판매자가 어떻게 하면<br>상품 등록을 더 쉽게 할 수 있을까?"</div>
<div class="ans">→ 사진만 올리면 상품명·설명을 AI가 채워주는 기능처럼, 사용자의 수고를 줄이는 방향으로 답을 찾습니다.</div>
</div>
<div class="arrow">→</div>
<div class="box me">
<div class="lbl">제가 던진 질문</div>
<div class="txt">"관리자가 어떻게 하면 더 적은 시간으로,<br>더 정확하게 판단할 수 있을까?"</div>
<div class="ans">→ 정보를 찾고, 기다리고, 다시 묻는 시간을 줄이면 물류 전체의 속도와 비용이 달라진다고 봤습니다.</div>
</div>
</div>
</div>
""")

# ---------- 3. KPI 연결 ----------
html("""
<div class="pf">
<h2>편리함이 이익으로 이어지는 구조</h2>
<p class="sec-sub">관리자의 편의가 곧 회사의 KPI 개선으로 연결되도록 설계했습니다.</p>
<div class="chain">
<div class="st"><span class="n">STEP 1</span><b>관리자 편의</b><p>찾지 않아도 보이고, 놓치기 전에 알려준다</p></div>
<div class="sep">›</div>
<div class="st"><span class="n">STEP 2</span><b>판단 · 처리 속도</b><p>문의 회신, 병목 대응, 인력 배치를 더 빨리 결정</p><span class="kpi dn">처리시간 ↓</span><span class="kpi dn">백로그 ↓</span></div>
<div class="sep">›</div>
<div class="st"><span class="n">STEP 3</span><b>물류 효율</b><p>출고가 막히지 않고, 통관 리스크가 사전에 걸러짐</p><span class="kpi dn">리드타임 ↓</span><span class="kpi dn">지연률 ↓</span><span class="kpi up">PPH ↑</span></div>
<div class="sep">›</div>
<div class="st"><span class="n">STEP 4</span><b>비용 절감</b><p>반송·폐기·클레임 대응 비용과 불필요한 인건비 감소</p><span class="kpi dn">클레임 ↓</span><span class="kpi dn">반송비 ↓</span></div>
<div class="sep">›</div>
<div class="st goal"><span class="n">GOAL</span><b>이익률 증가</b><p>같은 인력으로 더 많은 물량을, 더 적은 사고로 처리</p></div>
</div>
</div>
""")

# ---------- 4. 두 개의 도구 ----------
html("""
<div class="pf">
<h2>그래서 만든 네 가지 도구</h2>
<p class="sec-sub">각각 "어떤 불편에서 출발했고, 무엇으로 풀었고, 무엇이 좋아지는가"로 정리했습니다.</p>
<div class="two">
<div class="card tool">
<span class="tag" style="background:#fdecef;color:#e8435a">🛃 통관관리 시스템</span>
<h3>흩어진 통관 문의를 하나의 흐름으로</h3>
<p class="one">문의 접수 → 특송사 회신 → 답변 작성 → 승인권자 확정 → 이력·기준 축적</p>
<div class="row prob"><div class="k">문제</div><ul>
<li>통관 가능 여부 문의가 메일·메신저로 흩어져 진행 상황 파악이 어려움</li>
<li>특송사 회신이 늦어져도 누가, 얼마나 기다리는지 보이지 않음</li>
<li>같은 품목을 반복 문의하고, 판정이 담당자 기억에 의존</li></ul></div>
<div class="row sol"><div class="k">해결</div><ul>
<li>첫 화면에 "오늘 처리할 일"과 상태별 건수를 바로 표시</li>
<li>회신 대기 3일 경과 건을 자동 강조해 재요청 누락 방지</li>
<li>확정된 판정을 기준으로 쌓고, 품목·HS코드로 즉시 검색</li></ul></div>
<div class="row eff"><div class="k">효과</div><ul>
<li>반복 문의에 기존 기준으로 바로 답변 → 응답 시간 단축</li>
<li>통관 불가 품목을 출고 전에 걸러 반송·폐기 리스크 감소</li>
<li>담당자가 바뀌어도 판정 기준이 시스템에 남음</li></ul></div>
</div>
<div class="card tool">
<span class="tag" style="background:#e8f0fe;color:#2f6fd6">📦 물류 운영 대시보드</span>
<h3>병목을 "사후 집계"가 아닌 "지금"으로</h3>
<p class="one">입하 → 입고 → 피킹 → 출고 → 포장, 공정별 처리량과 잔량을 실시간으로</p>
<div class="row prob"><div class="k">문제</div><ul>
<li>공정별 처리량·백로그를 하루가 끝난 뒤 엑셀로 집계</li>
<li>병목을 늦게 발견해 출고 지연이 이미 발생한 뒤에 대응</li>
<li>인력 배치가 경험과 감에 의존</li></ul></div>
<div class="row sol"><div class="k">해결</div><ul>
<li>공정별 근무 인원·PPH·백로그·진행률을 한 화면에 표시</li>
<li>파이프라인 바로 지금 가장 큰 병목을 즉시 확인</li>
<li>데이터에서 "오늘의 코멘트"를 자동 생성, 수요 예측으로 인력 과부족 계산(S&amp;OP)</li></ul></div>
<div class="row eff"><div class="k">효과</div><ul>
<li>병목 공정에 인력을 먼저 재배치 → 리드타임·지연률 감소</li>
<li>예측 기반 인력 계획으로 과잉·부족 인력 비용 축소</li>
<li>회의·보고용 수작업 집계 시간 절감</li></ul></div>
</div>
</div>
<div class="wide">
<div class="card tool">
<span class="tag" style="background:#e9f7ef;color:#16a34a">🔎 통관 확인 도구</span>
<h3>사기 전에, 받을 때, 한 번에 확인</h3>
<p class="one">상품명 검색 → 관련 규정 · 유사 사례 → 위험 신호 → 확인할 항목 체크리스트 → 답이 없으면 통관관리로 문의 등록</p>
<div class="cols3">
<div class="row prob"><div class="k">문제</div><ul>
<li>통관 사례가 엑셀·메일에 흩어지고, 같은 사례가 여러 곳에 중복으로 남아 있음</li>
<li>구매 시점에는 통관 문제 여부를 알 수 없어, 반송·폐기된 뒤에야 알게 됨</li>
<li>입고 검수 때 무엇을 볼지가 담당자 경험에 의존</li></ul></div>
<div class="row sol"><div class="k">해결</div><ul>
<li>검색하면 규정과 유사 사례를 묶어 "주의 높음 · 주의 · 해당 없음"으로 먼저 알려줌</li>
<li>중복 사례는 1건으로 병합하고, 판정이 엇갈리는 건은 "확인 필요"로 표시</li>
<li>구매팀·물류팀 탭을 나눠, 구매 전 확인과 입고 검수 체크리스트를 따로 제공</li></ul></div>
<div class="row eff"><div class="k">효과</div><ul>
<li>구매 단계에서 통관 불가 품목을 걸러 반송·폐기 비용 감소</li>
<li>검수 기준이 사람마다 달라지지 않고 통일됨</li>
<li>문의 결과가 기준에 쌓여, 쓸수록 확인이 더 정확해지는 선순환</li></ul></div>
</div>
</div>
</div>
<div class="wide">
<div class="card tool">
<span class="tag" style="background:#fff4de;color:#b86e00">📡 통관 예외관리 레이더</span>
<h3>"무엇이 막혔나"가 아니라 "오늘 누가 무엇을 해야 하나"를</h3>
<p class="one">통관 대상 457건 → 지연 기준 룰 → 오늘의 액션 54건 · 지연 70건을 "공을 누가 갖고 있나"로 분해 · 특송사 구간별 리드타임 리포트 자동 생성</p>
<div class="cols3">
<div class="row prob"><div class="k">문제</div><ul>
<li>통관이 멈춘 건을 찾으려면 엑셀·메신저·메일을 뒤져야 하고, 며칠째인지 사람이 세어야 함</li>
<li>재문의 시점이 담당자 감에 달려 있어 늦거나, 이미 보낸 문의를 또 보냄</li>
<li>열린 이슈도 문의도 없는 "사각지대" 건은 아무도 모른 채 방치</li></ul></div>
<div class="row sol"><div class="k">해결</div><ul>
<li>단계별 지연 기준과 재문의 사다리(5·10·13·15일)를 룰로 정해, 457건을 오늘 처리할 54건으로 압축</li>
<li>지연 건을 사각지대·우리 차례·파트너 대기 등으로 나누고, 문의가 없는 건은 이슈별로 묶어 일괄 문의</li>
<li>건별 구간 시각만 쌓이면 특송사 비교 리포트를 표와 요약 문장으로 자동 생성</li></ul></div>
<div class="row eff"><div class="k">효과</div><ul>
<li>찾고 세고 다시 묻는 시간을 줄이고, 후속 누락과 중복 발송 방지</li>
<li>룰 기준을 슬라이더로 바꿔 업무량 변화를 미리 시뮬레이션</li>
<li>느린 구간과 요일·공휴일 영향을 근거로 특송사 협의와 고객 안내 예상일 조정</li></ul></div>
</div>
</div>
</div>
<div class="wide">
<div class="card" style="font-size:13.5px;color:#4b5058;line-height:1.7"><b style="color:#1b1d21">세 도구는 한 흐름입니다.</b> 통관 확인 도구(구매·입고 전 예방) → 통관 예외관리 레이더(진행 중 감지·지시) → 통관관리 시스템(이슈 처리·기준 축적)</div>
</div>
</div>
""")

# ---------- 4-2. 업무 브리핑 ----------
html("""
<div class="pf">
<div class="wide">
<div class="card tool">
<span class="tag" style="background:#e6f6e6;color:#006300">☀️ 아침 업무 브리핑 · AX 도구</span>
<h3>"언제까지 해 달라"는 말을 놓치지 않게, 출근하면 한 화면으로</h3>
<p class="one">Slack·메일·회의록 메시지 62건 → 요청 4종으로 분류 · 마감 추출 → 업무 관리 표의 위생 점검까지 한 번에</p>
<div class="cols3">
<div class="row prob"><div class="k">문제</div><ul>
<li>"○일까지 부탁드립니다" 요청이 채널·메일·회의에 흩어져 있어, 사람이다 보니 깜빡하는 일이 생김</li>
<li>해야 하는 일인지, 알고만 있으면 되는 공지인지 매번 읽고 판단해야 함</li>
<li>업무 관리 표는 담당·기한이 비거나 "제안" 상태로 방치되어도 아무도 모름. 자동 수집이 조용히 멈추면 "요청이 없는 것"처럼 보임</li></ul></div>
<div class="row sol"><div class="k">해결</div><ul>
<li>메시지를 해야 할 일 / 답장 대기 / 확인 필요 / 알고만 됨으로 나누고, 보낸 날짜를 기준으로 마감을 계산해 "오늘 먼저 볼 것"으로 정렬</li>
<li>요청은 먼저 "제안"으로만 등록하고 사람이 확정. 완료는 후속 메시지 근거와 함께 "후보"로만 표시</li>
<li>담당 없음·기한 없음·제안 방치를 점검하고, 수집이 실패한 채널은 화면 맨 위에 먼저 경고</li></ul></div>
<div class="row eff"><div class="k">효과</div><ul>
<li>아침에 메신저·메일·노션을 차례로 열어 확인하던 일을 한 화면으로 줄임</li>
<li>답장 없는 요청의 재촉 시점과 마감 임박 건을 기준값(슬라이더)대로 놓치지 않게 알림</li>
<li>분류 정확도(틀린 판정 포함)를 공개해, 어디까지 믿고 어디서 사람이 확인해야 하는지 분명해짐</li></ul></div>
</div>
</div>
</div>
</div>
""")

# ---------- 4-3. BO 업무 포털 ----------
html("""
<div class="pf">
<div class="wide">
<div class="card tool">
<span class="tag" style="background:#e8f0fe;color:#2f6fd6">🗂️ BO 업무 포털 · AX 도구</span>
<h3>출장 신청부터 정산, 세금계산서 점검까지 "누가 다음 차례인지"가 보이게</h3>
<p class="one">출장 관리(신청 · 결재 · 정산 규정 자동 판정) · 세금계산서 발행·수취 대상 점검 · 법무 검토 데스크 · 담당자 찾기를 한 포털로</p>
<div class="cols3">
<div class="row prob"><div class="k">문제</div><ul>
<li>법인마다 출장 신청·정산 방식이 달라, 누가 언제 어디로 가고 얼마를 썼는지 한 번에 보기 어려움</li>
<li>식비·숙박 상한, 승인 전 지출, 택시 규정 같은 기준을 사람이 영수증마다 계산하고 확인해야 함</li>
<li>세금계산서는 "발행·수취 대상인지, 기한 안에 처리됐는지"를 월말에 일일이 대조해야 하고, 빠뜨리면 늦게 알게 됨</li></ul></div>
<div class="row sol"><div class="k">해결</div><ul>
<li>신청 → 결재(BO 합의·팀장·재무총괄, 기준 금액 이상은 대표) → 정산을 한곳에 두고, 단계마다 다음 차례에게 알리고 "처리할 일"로 모아 보여줌</li>
<li>영수증 줄마다 규정을 적용해 인정 / 상한까지 인정 / 판단 필요 / 불인정으로 바로 판정하고, 신청 기한·내 정보 누락은 제출 전에 막음</li>
<li>거래 유형별로 필요한 증빙(세금계산서·계산서·영세율 증빙 등)과 기한(다음 달 10일)을 판정하고, 미발행·합계 불일치·중복 의심·증빙 누락을 찾아 월 마감 체크로 연결</li></ul></div>
<div class="row eff"><div class="k">효과</div><ul>
<li>신청부터 지급까지 어디서 멈췄는지 한 화면에서 확인하고, 규정 계산과 재확인 왕복을 줄임</li>
<li>세금계산서 발행·수취 누락을 월말이 아니라 기한 전에 발견하고, 점검 기준일을 바꿔 임박·기한 지남 건을 미리 확인</li>
<li>BO에 요청할 때 담당자를 바로 찾고, 법무 검토는 유형별 규칙으로 담당 배정과 회신 기한까지 추적</li></ul></div>
</div>
<div style="font-size:12px;color:#8a909a;margin-top:10px">이 화면의 회사명·이름·금액·규정 수치는 모두 가상이며, 세금계산서 판정은 단순화한 데모 규칙입니다(실제 세무 판단 아님).</div>
</div>
</div>
</div>
""")

# ---------- 5. 설계 원칙 ----------
html("""
<div class="pf">
<h2>관리자 관점의 설계 원칙</h2>
<p class="sec-sub">화면 하나하나를 만들 때 이 세 가지를 기준으로 판단했습니다.</p>
<div class="three">
<div class="card pr"><div class="ic">👀</div><b>한눈에 보이게</b><p>들어오자마자 "지금 무엇을 해야 하는지"가 보이도록, 숫자와 할 일을 첫 화면에 배치했습니다.</p></div>
<div class="card pr"><div class="ic">🔔</div><b>놓치기 전에 알려주게</b><p>3일 경과 회신, 쌓이는 백로그처럼 사람이 놓치기 쉬운 신호를 시스템이 먼저 강조합니다.</p></div>
<div class="card pr"><div class="ic">🗂️</div><b>일할수록 쌓이게</b><p>처리한 판정과 기록이 기준·이력으로 남아, 다음 사람과 다음 판단이 더 빨라집니다.</p></div>
</div>
</div>
""")

# ---------- 6. 기술 ----------
html("""
<div class="pf">
<h2>사용 기술</h2>
<p class="sec-sub">별도 서버 없이, 회사가 이미 쓰는 도구 위에서 바로 돌아가게 만드는 것을 우선했습니다.</p>
<div class="card"><div class="stack">
<span><i>실무 버전</i>Google Apps Script 웹앱</span>
<span><i>실무 버전</i>Google Sheets 데이터</span>
<span><i>화면</i>HTML · CSS · JavaScript</span>
<span><i>이 데모</i>Python · Streamlit</span>
<span><i>이 데모</i>가상 데이터 시뮬레이션</span>
</div></div>
</div>
""")

# ---------- 7. 바로가기 ----------
html('<div class="pf"><div class="cta-h">직접 사용해 보기</div></div>')
r1 = st.columns(3)
r2 = st.columns(3)
with r1[0]:
    st.page_link("pages/2_물류운영_대시보드_데모.py", label="물류 운영 대시보드 →", icon="📦", use_container_width=True)
with r1[1]:
    st.page_link("pages/1_통관관리_데모.py", label="통관관리 시스템 →", icon="🛃", use_container_width=True)
with r1[2]:
    st.page_link("pages/3_통관확인_도구.py", label="통관 확인 도구 →", icon="🔎", use_container_width=True)
with r2[0]:
    st.page_link("pages/4_통관_예외관리_레이더.py", label="통관 예외관리 레이더 →", icon="📡", use_container_width=True)
with r2[1]:
    st.page_link("pages/5_아침_업무_브리핑.py", label="아침 업무 브리핑 →", icon="☀️", use_container_width=True)
with r2[2]:
    st.page_link("pages/6_BO_업무_포털.py", label="BO 업무 포털 →", icon="🗂️", use_container_width=True)
