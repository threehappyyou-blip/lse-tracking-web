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
@media(max-width:820px){.pf h1{font-size:30px}.pf .q,.pf .two,.pf .three{grid-template-columns:1fr}.pf .q .arrow{transform:rotate(90deg);height:40px}.pf .chain{flex-direction:column}.pf .chain .sep{width:auto;height:22px;transform:rotate(90deg)}}
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
흩어진 통관 문의를 한 흐름으로 묶은 <b>통관관리 시스템</b>과, 공정별 병목을 실시간으로 보여주는 <b>물류 운영 대시보드</b>입니다.</p>
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
<h2>그래서 만든 두 가지 도구</h2>
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
c1, c2 = st.columns(2)
with c1:
    st.page_link("pages/1_통관관리_데모.py", label="통관관리 시스템 데모 →", icon="🛃", use_container_width=True)
with c2:
    st.page_link("pages/2_물류운영_대시보드_데모.py", label="물류 운영 대시보드 데모 →", icon="📦", use_container_width=True)
