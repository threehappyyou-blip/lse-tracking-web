import json

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="통관 확인 도구 (데모)", page_icon="🔎", layout="wide")

# 이 페이지만 밝은 배경으로 맞추고, 화면 전체를 데모가 채우도록 여백 제거
st.markdown(
    """<style>
.stApp{background:#f6f6f8}
[data-testid="stHeader"]{background:transparent}
[data-testid="stHeader"] button, [data-testid="stHeader"] svg{color:#777 !important}
.block-container,[data-testid="stMainBlockContainer"]{padding:2.6rem 0 0 0 !important;max-width:100% !important}
[data-testid="stVerticalBlock"]{gap:0 !important}
iframe{height:calc(100vh - 2.6rem) !important;display:block;border:0}
footer{display:none}
</style>""",
    unsafe_allow_html=True,
)

# 모든 사례·규정·한도는 가상 데이터입니다. (실제 업무용은 같은 구조로 교체)
DATA = json.loads(r'''{
 "cases": [
  {
   "id": 1,
   "category": "명품/브랜드(정품확인)",
   "name": "샘플 브랜드 러닝화 (정품 증빙 없음)",
   "verdict": "반송/폐기",
   "alt": "",
   "reason_all": "지재권",
   "qty": "",
   "issue": "S-001"
  },
  {
   "id": 2,
   "category": "명품/브랜드(정품확인)",
   "name": "샘플 브랜드 후드티",
   "verdict": "반송/폐기",
   "alt": "",
   "reason_all": "지재권",
   "qty": "",
   "issue": "S-002"
  },
  {
   "id": 3,
   "category": "명품/브랜드(정품확인)",
   "name": "샘플 브랜드 야구모자",
   "verdict": "반송/폐기",
   "alt": "",
   "reason_all": "지재권",
   "qty": "",
   "issue": "S-003"
  },
  {
   "id": 4,
   "category": "명품/브랜드(정품확인)",
   "name": "샘플 브랜드 지갑 (정품 영수증 첨부)",
   "verdict": "통관가능",
   "alt": "",
   "reason_all": "지재권",
   "qty": "1개",
   "issue": "S-004"
  },
  {
   "id": 5,
   "category": "명품/브랜드(정품확인)",
   "name": "샘플 브랜드 토트백",
   "verdict": "불가",
   "alt": "",
   "reason_all": "지재권",
   "qty": "",
   "issue": "S-005"
  },
  {
   "id": 6,
   "category": "명품/브랜드(정품확인)",
   "name": "샘플 브랜드 스니커즈 (S급 표기)",
   "verdict": "반송/폐기",
   "alt": "",
   "reason_all": "지재권",
   "qty": "",
   "issue": "S-006"
  },
  {
   "id": 7,
   "category": "명품/브랜드(정품확인)",
   "name": "샘플 브랜드 트랙팬츠",
   "verdict": "반송/폐기",
   "alt": "",
   "reason_all": "지재권",
   "qty": "",
   "issue": "S-007"
  },
  {
   "id": 8,
   "category": "화장품/뷰티",
   "name": "샘플 수분 토너 100ml x 30",
   "verdict": "분리배송",
   "alt": "",
   "reason_all": "수량",
   "qty": "품목별 24개까지",
   "issue": "S-008"
  },
  {
   "id": 9,
   "category": "화장품/뷰티",
   "name": "샘플 마스크팩 150매",
   "verdict": "분리배송",
   "alt": "",
   "reason_all": "수량",
   "qty": "120매까지",
   "issue": "S-009"
  },
  {
   "id": 10,
   "category": "화장품/뷰티",
   "name": "샘플 미백 치약",
   "verdict": "불가",
   "alt": "",
   "reason_all": "성분/재질",
   "qty": "",
   "issue": "S-010"
  },
  {
   "id": 11,
   "category": "화장품/뷰티",
   "name": "샘플 립틴트 10색",
   "verdict": "통관가능",
   "alt": "",
   "reason_all": "수량",
   "qty": "24개까지",
   "issue": "S-011"
  },
  {
   "id": 12,
   "category": "화장품/뷰티",
   "name": "샘플 향수 50ml 2개",
   "verdict": "통관가능",
   "alt": "",
   "reason_all": "수량",
   "qty": "24개까지",
   "issue": "S-012"
  },
  {
   "id": 13,
   "category": "화장품/뷰티",
   "name": "샘플 매니큐어 5개",
   "verdict": "통관가능",
   "alt": "불가",
   "reason_all": "성분/재질",
   "qty": "",
   "issue": "S-013"
  },
  {
   "id": 14,
   "category": "식품",
   "name": "샘플 육포 세트",
   "verdict": "반송/폐기",
   "alt": "",
   "reason_all": "검역",
   "qty": "",
   "issue": "S-014"
  },
  {
   "id": 15,
   "category": "식품",
   "name": "샘플 건조 나물 3종",
   "verdict": "불가",
   "alt": "",
   "reason_all": "검역",
   "qty": "",
   "issue": "S-015"
  },
  {
   "id": 16,
   "category": "식품",
   "name": "샘플 과일 음료 30캔",
   "verdict": "분리배송",
   "alt": "",
   "reason_all": "중량",
   "qty": "합산 10kg까지",
   "issue": "S-016"
  },
  {
   "id": 17,
   "category": "식품",
   "name": "샘플 비타민 6병",
   "verdict": "분리배송",
   "alt": "",
   "reason_all": "수량",
   "qty": "2개월분까지",
   "issue": "S-017"
  },
  {
   "id": 18,
   "category": "식품",
   "name": "샘플 과자 선물세트",
   "verdict": "통관가능",
   "alt": "",
   "reason_all": "수량",
   "qty": "",
   "issue": "S-018"
  },
  {
   "id": 19,
   "category": "전자/배터리",
   "name": "샘플 보조배터리 10000mAh",
   "verdict": "통관가능",
   "alt": "",
   "reason_all": "배터리/자석/전자",
   "qty": "",
   "issue": "S-019"
  },
  {
   "id": 20,
   "category": "전자/배터리",
   "name": "샘플 전자담배 기기",
   "verdict": "불가",
   "alt": "",
   "reason_all": "배터리/자석/전자",
   "qty": "",
   "issue": "S-020"
  },
  {
   "id": 21,
   "category": "전자/배터리",
   "name": "샘플 자석 스피커",
   "verdict": "불가",
   "alt": "",
   "reason_all": "배터리/자석/전자",
   "qty": "",
   "issue": "S-021"
  },
  {
   "id": 22,
   "category": "전자/배터리",
   "name": "샘플 스마트 거치대 6개",
   "verdict": "분리배송",
   "alt": "",
   "reason_all": "대량/소명",
   "qty": "",
   "issue": "S-022"
  },
  {
   "id": 23,
   "category": "완구/굿즈",
   "name": "샘플 아이돌 앨범 10장",
   "verdict": "분리배송",
   "alt": "",
   "reason_all": "수량",
   "qty": "3개까지",
   "issue": "S-023"
  },
  {
   "id": 24,
   "category": "완구/굿즈",
   "name": "샘플 아크릴 스탠드 80개",
   "verdict": "분리배송",
   "alt": "",
   "reason_all": "수량, 대량/소명",
   "qty": "24개까지",
   "issue": "S-024"
  },
  {
   "id": 25,
   "category": "완구/굿즈",
   "name": "샘플 모형 총",
   "verdict": "불가",
   "alt": "",
   "reason_all": "수량",
   "qty": "",
   "issue": "S-025"
  },
  {
   "id": 26,
   "category": "완구/굿즈",
   "name": "샘플 캐릭터 시계",
   "verdict": "통관가능",
   "alt": "",
   "reason_all": "수량",
   "qty": "",
   "issue": "S-026"
  },
  {
   "id": 27,
   "category": "생활잡화",
   "name": "샘플 접착 바인더 13개",
   "verdict": "분리배송",
   "alt": "",
   "reason_all": "수량",
   "qty": "",
   "issue": "S-027"
  },
  {
   "id": 28,
   "category": "생활잡화",
   "name": "샘플 차량 코팅제 500ml x 8",
   "verdict": "분리배송",
   "alt": "",
   "reason_all": "중량",
   "qty": "합산 4L까지",
   "issue": "S-028"
  },
  {
   "id": 29,
   "category": "생활잡화",
   "name": "샘플 가죽 지갑 (재질 미표기)",
   "verdict": "불가",
   "alt": "",
   "reason_all": "성분/재질",
   "qty": "",
   "issue": "S-029"
  },
  {
   "id": 30,
   "category": "생활잡화",
   "name": "샘플 수납 서랍장",
   "verdict": "분리배송",
   "alt": "",
   "reason_all": "대량/소명",
   "qty": "",
   "issue": "S-030"
  },
  {
   "id": 31,
   "category": "기타/미분류",
   "name": "샘플 미등록 소품",
   "verdict": "기타",
   "alt": "",
   "reason_all": "",
   "qty": "",
   "issue": "S-031"
  }
 ],
 "rules": [
  {
   "id": 1,
   "kind": "절대금지",
   "item": "육류 포함 식품",
   "detail": "육류가 들어간 식품은 반입이 안 되고 폐기됩니다",
   "note": "육포, 소시지 등",
   "status": "X",
   "cats": "식품"
  },
  {
   "id": 2,
   "kind": "절대금지",
   "item": "건조 농산물",
   "detail": "나물류 등 검역 대상 품목은 불가",
   "note": "",
   "status": "X",
   "cats": "식품"
  },
  {
   "id": 3,
   "kind": "절대금지",
   "item": "미백 치약",
   "detail": "과산화수소 등 미백 성분이 들어 있으면 불가",
   "note": "성분표 확인",
   "status": "X",
   "cats": "화장품/뷰티"
  },
  {
   "id": 4,
   "kind": "절대금지",
   "item": "모형 총기",
   "detail": "실제 총기와 모형 모두 불가",
   "note": "",
   "status": "X",
   "cats": "완구/굿즈"
  },
  {
   "id": 5,
   "kind": "절대금지",
   "item": "전자담배",
   "detail": "배터리가 들어간 제품 포함 불가",
   "note": "",
   "status": "X",
   "cats": "전자/배터리"
  },
  {
   "id": 6,
   "kind": "절대금지",
   "item": "정품 증빙이 없는 브랜드 상품",
   "detail": "정품 여부를 증빙하지 못하면 반송 또는 폐기될 수 있음",
   "note": "접수 전 증빙 확인",
   "status": "X",
   "cats": "명품/브랜드(정품확인)"
  },
  {
   "id": 7,
   "kind": "조건부",
   "item": "화장품",
   "detail": "품목별 24개까지 가능 (색상 무관)",
   "note": "합포장 포함",
   "status": "▲",
   "cats": "화장품/뷰티"
  },
  {
   "id": 8,
   "kind": "조건부",
   "item": "마스크팩",
   "detail": "120매까지 가능",
   "note": "사은품 포함 시 초과 불가",
   "status": "▲",
   "cats": "화장품/뷰티"
  },
  {
   "id": 9,
   "kind": "조건부",
   "item": "건강보조제",
   "detail": "2개월분까지 가능",
   "note": "",
   "status": "▲",
   "cats": "식품"
  },
  {
   "id": 10,
   "kind": "조건부",
   "item": "보조배터리",
   "detail": "용량 기준 이내에서 가능",
   "note": "항공 반입 기준 확인",
   "status": "O",
   "cats": "전자/배터리"
  },
  {
   "id": 11,
   "kind": "조건부",
   "item": "가죽 제품",
   "detail": "재질과 가죽 종류 표기가 필요",
   "note": "",
   "status": "▲",
   "cats": "생활잡화|명품/브랜드(정품확인)"
  },
  {
   "id": 12,
   "kind": "조건부",
   "item": "자석",
   "detail": "소량만 가능, 대량은 불가",
   "note": "",
   "status": "▲",
   "cats": "전자/배터리|생활잡화"
  },
  {
   "id": 13,
   "kind": "조건부",
   "item": "액체류",
   "detail": "합산 4L까지 가능",
   "note": "",
   "status": "▲",
   "cats": "생활잡화"
  },
  {
   "id": 14,
   "kind": "조건부",
   "item": "앨범·굿즈",
   "detail": "동일 상품 3개까지 가능",
   "note": "",
   "status": "▲",
   "cats": "완구/굿즈"
  }
 ],
 "limits": [
  {
   "id": 1,
   "group": "포장용품",
   "item": "종이컵",
   "a": "동일 디자인 300개",
   "b": "동일 디자인 600개"
  },
  {
   "id": 2,
   "group": "텀블러",
   "item": "텀블러",
   "a": "동일 상품 4개, 같은 카테고리 6개",
   "b": "동일 상품 10개, 같은 카테고리 15개"
  },
  {
   "id": 3,
   "group": "주방용품",
   "item": "고무장갑",
   "a": "동일 상품 24개",
   "b": ""
  },
  {
   "id": 4,
   "group": "화장품",
   "item": "토너·에멀전",
   "a": "품목별 24개",
   "b": ""
  },
  {
   "id": 5,
   "group": "의류",
   "item": "티셔츠",
   "a": "동일 상품 2개, 카테고리 8개",
   "b": ""
  },
  {
   "id": 6,
   "group": "식품",
   "item": "음료 캔",
   "a": "합산 10kg",
   "b": ""
  }
 ]
}''')

HTML = r"""<!doctype html>
<html lang="ko"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css">
<style>
:root{--accent:#e8435a;--bg:#f6f6f8;--card:#fff;--text:#1b1b22;--sub:#6b6b78;--line:#e8e8ee;--bad:#d62f4b;--warn:#c47a00;--ok:#16895f}
*{box-sizing:border-box}
html,body{margin:0;background:var(--bg);color:var(--text);font-family:Pretendard,-apple-system,"Noto Sans KR",sans-serif;font-size:14px;line-height:1.5;letter-spacing:-.2px}
.wrap{max-width:1040px;margin:0 auto;padding:28px 24px 48px;display:flex;flex-direction:column;gap:18px}
h1{font-size:28px;margin:0;font-weight:800;letter-spacing:-.6px}
h1 em{font-style:normal;color:var(--accent)}
h2{font-size:15px;margin:0;font-weight:700}
p{margin:0}
.sub{color:var(--sub);font-size:12.5px}
.pills{display:flex;flex-wrap:wrap;gap:8px}
.pill{background:#fff;border:1px solid var(--line);border-radius:999px;padding:5px 12px;font-size:12px;font-weight:600}
.card{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:18px;display:flex;flex-direction:column;gap:10px;box-shadow:0 1px 3px rgba(0,0,0,.04)}
.bar{display:flex;flex-wrap:wrap;gap:8px}
.bar input,.bar select{font:inherit;border:1px solid var(--line);border-radius:10px;padding:10px 12px;background:#fff;color:var(--text);min-width:0}
.bar input{flex:1 1 260px;font-size:15px}
.bar input:focus,.bar select:focus{outline:2px solid rgba(232,67,90,.35);border-color:var(--accent)}
.chips{display:flex;flex-wrap:wrap;gap:6px;align-items:center;color:var(--sub);font-size:12px}
.chip{font:inherit;font-size:12px;border:1px solid var(--line);background:#fff;border-radius:999px;padding:3px 10px;cursor:pointer;color:var(--text)}
.chip:hover{border-color:var(--accent);color:var(--accent)}
.tabs{display:flex;gap:6px;border-bottom:1px solid var(--line)}
.tab{font:inherit;font-size:14px;font-weight:600;background:none;border:0;border-bottom:2px solid transparent;margin-bottom:-1px;padding:10px 14px;color:var(--sub);cursor:pointer}
.tab[aria-selected="true"]{color:var(--text);border-bottom-color:var(--accent)}
.out{display:flex;flex-direction:column;gap:14px}
.out .banner{order:0}.out .lead{order:1}.out .cases{order:4}
.out.buy .rules{order:2}.out.buy .limits{order:3}
.out.log .limits{order:2}.out.log .rules{order:3}
.banner{border-radius:14px;padding:18px;border:1px solid var(--line);background:#fff;display:flex;flex-direction:column;gap:8px}
.banner[data-level="high"]{background:#fdecef;border-color:#f3b8c2}
.banner[data-level="mid"]{background:#fff6e5;border-color:#f0d49a}
.banner[data-level="low"]{background:#e8f6ef;border-color:#a9dcc5}
.lv{font-size:22px;font-weight:800;letter-spacing:-.5px}
.banner[data-level="high"] .lv{color:var(--bad)}.banner[data-level="mid"] .lv{color:var(--warn)}.banner[data-level="low"] .lv{color:var(--ok)}
.why{font-size:14px}
.dist{display:flex;height:10px;border-radius:999px;overflow:hidden;background:#e4e4ea}
.dist div{height:100%;min-width:3px}
.legend{display:flex;flex-wrap:wrap;gap:4px 14px;color:var(--sub);font-size:12px}
.legend span{display:inline-flex;align-items:center;gap:6px}
.legend i{width:10px;height:10px;border-radius:3px;display:inline-block}
.reasons{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:9px}
.reasons li{display:flex;gap:10px;align-items:baseline;flex-wrap:wrap}
.reasons label{display:flex;gap:8px;align-items:baseline;cursor:pointer}
.reasons .rn{color:var(--sub);font-size:12px;white-space:nowrap}
.tw{max-height:300px;overflow:auto;border:1px solid var(--line);border-radius:10px}
table{width:100%;border-collapse:collapse;font-size:12.5px}
th{position:sticky;top:0;background:#fafafc;text-align:left;color:var(--sub);font-weight:600;padding:8px 10px;border-bottom:1px solid var(--line);white-space:nowrap}
td{padding:8px 10px;border-bottom:1px solid var(--line);vertical-align:top}
tr.rel td{color:var(--sub)}
td.v-bad{color:var(--bad);font-weight:700;white-space:nowrap}td.v-warn{color:var(--warn);font-weight:700;white-space:nowrap}td.v-ok{color:var(--ok);font-weight:700;white-space:nowrap}
.empty{color:var(--sub);font-size:12.5px}
.notice{background:#fff;border:1px dashed #c9c9d3;border-radius:10px;padding:10px 12px;font-size:12.5px;color:var(--sub)}
@media(max-width:640px){.wrap{padding:18px 14px 40px}h1{font-size:23px}}
</style></head>
<body>
<div class="wrap">
  <div>
    <p class="sub" style="color:var(--accent);font-weight:700;letter-spacing:.3px">DEMO · 통관 확인 도구</p>
    <h1>이 상품, <em>통관에 문제 없을까?</em></h1>
    <p class="sub" style="margin-top:6px">구매 전에는 사도 되는 상품인지, 입고 검수 때는 무엇을 확인할지 한 번에 찾아줍니다.</p>
  </div>
  <div class="pills"><span class="pill">기획 · 설계 · 개발 1인</span><span class="pill">구매팀 · 물류팀 용</span><span class="pill">이 화면의 사례·규정은 모두 가상 데이터</span></div>

  <div class="card">
    <div class="bar">
      <input id="q" type="search" value="브랜드" placeholder="상품명이나 키워드. 예: 러닝화, 보조배터리, 미백 치약" aria-label="상품명 또는 키워드">
      <select id="fcat" aria-label="품목"></select>
    </div>
    <div class="chips"><span>예시</span>
      <button class="chip" data-q="브랜드">브랜드</button><button class="chip" data-q="미백 치약">미백 치약</button><button class="chip" data-q="보조배터리">보조배터리</button><button class="chip" data-q="앨범">앨범</button><button class="chip" data-q="비타민">비타민</button><button class="chip" data-q="토너">토너</button>
    </div>
  </div>

  <div class="tabs" role="tablist">
    <button class="tab" id="tab-buy" role="tab" aria-selected="true">구매팀 · 사도 되는 상품인가</button>
    <button class="tab" id="tab-log" role="tab" aria-selected="false">물류팀 · 입고 검수</button>
  </div>

  <div class="out buy" id="out">
    <div class="banner" id="banner" data-level="none">
      <div class="lv" id="lv"></div><p class="why" id="why"></p>
      <div id="distbox" hidden><div class="dist" id="dist"></div><div class="legend" id="legend"></div></div>
    </div>
    <div class="card lead" id="lead" hidden><h2 id="lead-h"></h2><p class="sub" id="lead-sub"></p><ul class="reasons" id="reasons"></ul></div>
    <div class="card rules"><h2>관련 규정</h2>
      <p class="sub">진한 글씨는 검색어와 직접 관련된 규정, 연한 글씨는 같은 품목의 규정입니다. X는 불가, ▲는 조건부, O는 기준 내 가능입니다.</p>
      <div class="tw"><table id="tb-rules"><thead><tr><th>구분</th><th>품목</th><th>세부 내용·조건</th><th>비고</th><th>통관여부</th></tr></thead><tbody></tbody></table></div>
      <p class="empty" id="em-rules" hidden>관련 규정을 찾지 못했습니다. 절대금지 규정을 직접 확인하세요.</p></div>
    <div class="card limits"><h2>수량·중량 한도</h2><p class="sub">특송사별 한도입니다. 동일 디자인·동일 카테고리 합산 기준입니다.</p>
      <div class="tw"><table id="tb-lim"><thead><tr><th>대분류</th><th>상품명</th><th>특송사 A 한도</th><th>특송사 B 한도</th></tr></thead><tbody></tbody></table></div>
      <p class="empty" id="em-lim" hidden>이 검색어와 맞는 한도 항목이 없습니다.</p></div>
    <div class="card cases"><h2>비슷한 과거 사례</h2><p class="sub">반송·불가가 먼저 나오고, 많으면 앞의 50건만 보입니다. 다른 기록은 두 시스템의 판정이 달랐던 사례의 상대 판정이니 원문을 확인하세요.</p>
      <div class="tw"><table id="tb-cases"><thead><tr><th>품목</th><th>상품명</th><th>판정</th><th>다른 기록</th><th>사유</th><th>수량·중량 기준</th><th>이슈#</th></tr></thead><tbody></tbody></table></div>
      <p class="empty" id="em-cases" hidden>비슷한 사례가 없습니다.</p></div>
  </div>
  <div class="notice">참고용 화면입니다. 실제 업무에서는 같은 구조에 회사의 사례·규정을 넣어 사용하고, 최종 판단은 규정 원문과 담당자 기준을 따릅니다.</div>
</div>

<script>
const D = __DATA__;
const $ = (id) => document.getElementById(id);
const PILL = {'반송/폐기':'v-bad','불가':'v-bad','X':'v-bad','분리배송':'v-warn','기타':'v-warn','▲':'v-warn','통관가능':'v-ok','O':'v-ok'};
const SEV = {'불가':0,'반송/폐기':1,'분리배송':2,'기타':3,'취소':4,'통관가능':5};
const VERDICTS = ['반송/폐기','불가','분리배송','기타','통관가능','취소'];
const VCOL = {'반송/폐기':'#d62f4b','불가':'#8f2d56','분리배송':'#e0a100','기타':'#a8a8b5','통관가능':'#2bb07f','취소':'#d4d4dc'};
const BUY = {'지재권':'브랜드·캐릭터 상품입니다. 정품 증빙이 가능한 판매처인지 확인하세요.','수량':'동일 상품, 같은 카테고리를 합친 수량이 한도 안인지 확인하세요.','중량':'합친 중량이 한도 안인지 확인하세요.','성분/재질':'성분과 재질 표기가 규정에 걸리지 않는지 확인하세요.','배터리/자석/전자':'배터리나 자석이 들어 있는 상품인지 확인하세요.','검역':'식품이나 동식물 유래 성분이 들어 있는지 확인하세요.','대량/소명':'같은 상품을 많이 사면 소명이 필요할 수 있습니다.'};
const LOG = {'지재권':'브랜드 로고, 택, 라벨이 있는지, 정품 증빙 서류가 있는지 확인','수량':'실제 입고 수량이 한도 이내인지 확인 (동일 상품, 같은 카테고리 합산)','중량':'실제 입고 중량이 한도 이내인지 확인','성분/재질':'상품의 성분과 재질 표기 확인 (가죽, 금지 성분 등)','배터리/자석/전자':'배터리나 자석이 들어 있는지 확인','검역':'식품이나 동식물 유래 성분이 들어 있는지 확인','대량/소명':'같은 상품이 대량으로 들어왔는지 확인 (소명 대상 여부)'};
const LABEL = {buy:{high:'구매 전 주의 높음',mid:'구매 전 조건 확인',low:'구매해도 사례상 문제 적음',none:'전례 없음'},log:{high:'검수 주의 높음',mid:'검수 시 조건 확인',low:'검수 시 사례상 문제 적음',none:'전례 없음'}};
let view = 'buy';
const STOP = ['상품','제품','품목','경우','포함','이상','이하','없는','있는','관련','가능','불가','확인','필요','기준'];
const wordsOf = (s) => s.split(/[\s/,·()、]+/).filter((w) => w.length >= 2 && !STOP.includes(w));

function analyze() {
  const q = $('q').value.trim().toLowerCase();
  const cat = $('fcat').value;
  if (!q && !cat) return {empty: true};
  let toks = q.split(/\s+/).filter((t) => t.length >= 2);
  if (!toks.length && q) toks = [q];
  const text = (r) => (r.name + ' ' + r.category + ' ' + r.reason_all + ' ' + r.issue).toLowerCase();
  const inCat = D.cases.filter((r) => !cat || r.category === cat);
  let hit = toks.length ? inCat.filter((r) => toks.every((t) => text(r).includes(t))) : inCat;
  let partial = false;
  if (!hit.length && toks.length > 1) { hit = inCat.filter((r) => toks.some((t) => text(r).includes(t))); partial = hit.length > 0; }
  const rtext = (r) => (r.item + ' ' + r.detail + ' ' + r.note).toLowerCase();
  const ruleA = q ? D.rules.filter((r) => toks.some((t) => rtext(r).includes(t)) || wordsOf(r.item.toLowerCase()).some((w) => q.includes(w))) : [];
  const cnt = new Map();
  hit.forEach((r) => cnt.set(r.category, (cnt.get(r.category) || 0) + 1));
  const topCats = cat ? [cat] : [...cnt].filter(([c, n]) => c !== '기타/미분류' && n / hit.length >= 0.25).sort((a, b) => b[1] - a[1]).slice(0, 2).map((x) => x[0]);
  const aIds = new Set(ruleA.map((r) => r.id));
  const ruleB = D.rules.filter((r) => !aIds.has(r.id) && r.cats && r.cats.split('|').some((c) => topCats.includes(c)));
  const limA = q ? D.limits.filter((r) => { const t = (r.group + ' ' + r.item).toLowerCase(); return toks.some((w) => t.includes(w)) || wordsOf(t).some((w) => q.includes(w)); }) : [];
  const n = hit.length;
  const c = (v) => hit.filter((r) => r.verdict === v).length;
  const bad = c('반송/폐기') + c('불가'), okc = c('통관가능');
  const nBan = ruleA.filter((r) => r.status === 'X').length;
  const brand = topCats.includes('명품/브랜드(정품확인)') || (n > 0 && hit.filter((r) => r.reason_all.includes('지재권')).length / n >= 0.3);
  let level;
  if (nBan > 0 || (n >= 2 && bad / n >= 0.5)) level = 'high';
  else if (n >= 2 && okc / n >= 0.7 && ruleA.length === 0 && !brand) level = 'low';
  else if (n > 0 || ruleA.length > 0 || ruleB.length > 0) level = 'mid';
  else level = 'none';
  return {q, cat, hit, partial, ruleA, ruleB, limA, n, c, bad, okc, nBan, brand, level};
}
function whyText(a) {
  const p = [];
  if (a.nBan) p.push('검색어와 관련된 금지(X) 규정이 ' + a.nBan + '건 있습니다. 해당 상품인지 규정 내용을 확인하세요.');
  if (a.n) p.push('비슷한 사례 ' + a.n + '건 중 반송·불가 ' + a.bad + '건, 분리배송 ' + a.c('분리배송') + '건, 통관가능 ' + a.okc + '건입니다.');
  if (a.ruleA.length && !a.nBan) p.push('조건부 규정 ' + a.ruleA.length + '건이 관련됩니다.');
  if (a.brand) p.push('브랜드 상품은 통관가능 사례도 정품 증빙이 있던 경우일 수 있습니다.');
  if (a.partial) p.push('입력한 단어가 모두 들어간 사례가 없어 일부 단어만 맞는 사례를 보여줍니다.');
  if (a.level === 'none') p.push('일치하는 사례와 규정이 없습니다. 전례 없는 품목은 절대금지 규정부터 확인하세요.');
  return p.join(' ');
}
function fillTable(id, cols, data, pills, emptyId, relFn) {
  const tb = $(id).tBodies[0];
  tb.replaceChildren();
  data.forEach((r) => {
    const tr = document.createElement('tr');
    if (relFn && relFn(r)) tr.className = 'rel';
    cols.forEach((f) => {
      const td = document.createElement('td');
      const v = r[f];
      td.textContent = v === undefined || v === null ? '' : String(v);
      if (pills.includes(f) && PILL[v]) td.className = PILL[v];
      tr.appendChild(td);
    });
    tb.appendChild(tr);
  });
  $(emptyId).hidden = data.length > 0;
}
function drawDist(a) {
  const box = $('distbox'), bar = $('dist'), lg = $('legend');
  bar.replaceChildren(); lg.replaceChildren();
  if (!a || !a.n) { box.hidden = true; return; }
  box.hidden = false;
  VERDICTS.forEach((v) => {
    const k = a.c(v); if (!k) return;
    const seg = document.createElement('div');
    seg.style.flex = String(k); seg.style.background = VCOL[v]; seg.title = v + ' ' + k + '건';
    bar.appendChild(seg);
    const s = document.createElement('span'), i = document.createElement('i');
    i.style.background = VCOL[v]; s.appendChild(i); s.appendChild(document.createTextNode(v + ' ' + k));
    lg.appendChild(s);
  });
}
function drawLead(a) {
  const lead = $('lead'), ul = $('reasons');
  ul.replaceChildren();
  if (!a || !a.n) { lead.hidden = true; return; }
  const m = new Map();
  a.hit.filter((r) => ['반송/폐기','불가','분리배송'].includes(r.verdict)).forEach((r) => {
    r.reason_all.split(',').map((x) => x.trim()).filter((x) => BUY[x]).forEach((x) => m.set(x, (m.get(x) || 0) + 1));
  });
  const list = [...m].sort((x, y) => y[1] - x[1]).slice(0, 6);
  lead.hidden = false;
  $('lead-h').textContent = view === 'buy' ? '이 상품이 자주 걸린 이유' : '입고 검수 체크리스트';
  $('lead-sub').textContent = view === 'buy' ? '비슷한 사례에서 반송·불가·분리배송이 된 사유입니다. 구매 전에 아래를 확인하세요.' : '비슷한 사례에서 문제가 된 사유를 확인 항목으로 바꾼 것입니다. 확인한 항목은 체크하세요.';
  if (!list.length) { const li = document.createElement('li'); li.textContent = '기록된 사유가 없습니다. 아래 규정과 사례를 기준으로 확인하세요.'; ul.appendChild(li); return; }
  list.forEach(([reason, k], i) => {
    const li = document.createElement('li'), body = document.createElement('span'), rn = document.createElement('span');
    body.textContent = (view === 'buy' ? BUY : LOG)[reason];
    rn.className = 'rn'; rn.textContent = reason + ' · 사례 ' + k + '건';
    if (view === 'log') {
      const lab = document.createElement('label'), cb = document.createElement('input');
      cb.type = 'checkbox'; cb.id = 'ck-' + i; lab.appendChild(cb); lab.appendChild(body); li.appendChild(lab);
    } else li.appendChild(body);
    li.appendChild(rn); ul.appendChild(li);
  });
}
function draw() {
  const sel = $('fcat'), cur = sel.value;
  if (!sel.options.length) {
    sel.appendChild(new Option('전체 품목', ''));
    [...new Set(D.cases.map((r) => r.category))].sort().forEach((c) => sel.appendChild(new Option(c, c)));
  }
  sel.value = cur;
  const a = analyze(), banner = $('banner');
  if (a.empty) {
    banner.dataset.level = 'none'; $('lv').textContent = '상품명을 입력하세요';
    $('why').textContent = '상품명이나 키워드를 넣으면 관련 규정, 수량·중량 한도, 과거 사례를 한 번에 보여줍니다.';
    drawDist(null); drawLead(null);
    fillTable('tb-rules', ['kind','item','detail','note','status'], [], ['status'], 'em-rules');
    fillTable('tb-lim', ['group','item','a','b'], [], [], 'em-lim');
    fillTable('tb-cases', ['category','name','verdict','alt','reason_all','qty','issue'], [], ['verdict','alt'], 'em-cases');
    return;
  }
  banner.dataset.level = a.level; $('lv').textContent = LABEL[view][a.level]; $('why').textContent = whyText(a);
  drawDist(a); drawLead(a);
  const xFirst = (x, y) => (x.status === 'X' ? 0 : 1) - (y.status === 'X' ? 0 : 1);
  const aIds = new Set(a.ruleA.map((r) => r.id));
  fillTable('tb-rules', ['kind','item','detail','note','status'], [...a.ruleA.slice().sort(xFirst), ...a.ruleB.slice().sort(xFirst)], ['status'], 'em-rules', (r) => !aIds.has(r.id));
  fillTable('tb-lim', ['group','item','a','b'], a.limA, [], 'em-lim');
  const sorted = a.hit.slice().sort((x, y) => (SEV[x.verdict] - SEV[y.verdict]));
  fillTable('tb-cases', ['category','name','verdict','alt','reason_all','qty','issue'], sorted.slice(0, 50), ['verdict','alt'], 'em-cases');
}
function show(name) {
  view = name; $('out').className = 'out ' + name;
  ['buy','log'].forEach((t) => $('tab-' + t).setAttribute('aria-selected', String(t === name)));
  draw();
}
['buy','log'].forEach((t) => $('tab-' + t).addEventListener('click', () => show(t)));
$('q').addEventListener('input', draw);
$('fcat').addEventListener('change', draw);
document.querySelectorAll('.chip').forEach((b) => b.addEventListener('click', () => { $('q').value = b.dataset.q; draw(); }));
draw();
</script>
</body></html>
"""

HTML = HTML.replace("__DATA__", json.dumps(DATA, ensure_ascii=False))

components.html(HTML, height=900, scrolling=True)
