import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="아침 업무 브리핑 (데모)", page_icon="☀️", layout="wide")

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

# 모든 메시지·이름·업무는 가상 데이터입니다. (실제 업무용은 같은 구조로 교체)
HTML = r"""<!doctype html>
<html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css">
<style>
:root{--bg:#f6f6f8;--card:#fff;--ink:#1b1d21;--ink2:#52565e;--mut:#8a909a;--line:#e6e8ec;--hair:#f0f1f3;--s1:#2a78d6;--s1l:#cde2fb;--crit:#d03b3b;--critbg:#fdecec;--warn:#b86e00;--warnbg:#fff4de;--good:#006300;--goodbg:#e6f6e6;--acc:#e8435a}
*{box-sizing:border-box}
html,body{margin:0;background:var(--bg);color:var(--ink);font-family:Pretendard,-apple-system,"Noto Sans KR",system-ui,sans-serif;letter-spacing:-.15px;font-size:13px}
button{font:inherit;cursor:pointer}
.wrap{max-width:1240px;margin:0 auto;padding:18px 22px 60px}
.top{display:flex;align-items:flex-end;gap:14px;flex-wrap:wrap;border-bottom:2px solid var(--ink);padding-bottom:12px}
.top h1{margin:0;font-size:22px;font-weight:800;letter-spacing:-.6px}
.top .ver{color:var(--mut);font-size:12px;padding-bottom:3px}
.top .sp{flex:1}
.btn{border:1px solid var(--ink);background:#fff;color:var(--ink);border-radius:7px;padding:7px 12px;font-weight:700;font-size:12.5px}
.btn:hover{background:#f1f2f4}
.btn.dk{background:var(--ink);color:#fff}.btn.dk:hover{background:#34373d}
.btn.sm{padding:5px 10px;font-size:12px}
.btn.ghost{border-color:var(--line);color:var(--ink2);font-weight:600}
.demo{display:inline-flex;gap:6px;align-items:center;background:#fff;border:1px solid var(--line);border-radius:20px;padding:4px 11px;font-size:11.5px;color:var(--ink2);margin-top:10px}
.demo b{color:var(--acc)}
.tabs{display:flex;gap:4px;border-bottom:1px solid var(--line);margin:14px 0 14px;overflow-x:auto}
.tab{background:none;border:0;border-bottom:2px solid transparent;padding:9px 13px;color:var(--mut);font-weight:600;font-size:13.5px;white-space:nowrap;margin-bottom:-1px}
.tab[aria-selected=true]{color:var(--ink);border-color:var(--ink);font-weight:800}
.chips{display:flex;gap:7px;flex-wrap:wrap;align-items:center}
.chip{border:1px solid var(--line);background:#fff;border-radius:20px;padding:5px 12px;font-size:12.5px;color:var(--ink2);font-weight:600}
.chip b{margin-left:4px;color:var(--ink)}
.chip.red{border-color:#f0c4c4;color:var(--crit)}.chip.red b{color:var(--crit)}
.chip.on{background:var(--ink);border-color:var(--ink);color:#fff}.chip.on b{color:#fff}
.note{color:var(--ink2);font-size:12px;line-height:1.65;margin:10px 0 6px}
.note b{color:var(--ink)}
.panel{background:#fff;border:1px solid var(--line);border-radius:12px;padding:14px 16px;margin:10px 0}
.panel h3{margin:0 0 4px;font-size:14px;font-weight:800}
.panel .sub{color:var(--mut);font-size:12px;margin:0 0 10px}
.sl{display:grid;grid-template-columns:repeat(auto-fill,minmax(210px,1fr));gap:10px 22px}
.sl label{display:block;font-size:12px;color:var(--ink2);font-weight:600}
.sl label span{float:right;color:var(--ink);font-weight:800}
.sl input[type=range]{width:100%;accent-color:var(--s1);margin:4px 0 0}
.delta{margin-top:10px;font-size:12.5px;color:var(--ink2)}
.delta b{color:var(--ink)}
.delta .up{color:var(--crit);font-weight:800}.delta .dn{color:var(--good);font-weight:800}
table{width:100%;border-collapse:collapse;background:#fff}
.tw{background:#fff;border:1px solid var(--line);border-radius:12px;overflow:auto}
th{font-size:11.5px;color:var(--mut);font-weight:700;text-align:left;padding:9px 10px;border-bottom:1px solid var(--line);white-space:nowrap}
td{padding:9px 10px;border-bottom:1px solid var(--hair);vertical-align:top;font-size:12.5px}
td.num,th.num{text-align:right;font-variant-numeric:tabular-nums}
tr:last-child td{border-bottom:0}
tr.gh td{background:var(--ink);color:#fff;font-weight:800;font-size:13px;padding:8px 10px}
tr.gh .tg{display:inline-block;background:#fff;color:var(--ink);border-radius:5px;padding:1px 7px;font-size:11px;margin-left:8px;font-weight:700}
tr.r td:first-child{border-left:4px solid var(--crit)}
tr.r.amber td:first-child{border-left-color:#e08a00}
tr.r.gray td:first-child{border-left-color:#aab0ba}
.id{color:var(--s1);font-weight:600}
.big{font-size:15px;font-weight:800}
.s2{color:var(--mut);font-size:11.5px;line-height:1.5}
.pill{display:inline-block;border-radius:5px;padding:1px 7px;font-size:11px;font-weight:700}
.pill.crit{background:var(--critbg);color:var(--crit)}.pill.warn{background:var(--warnbg);color:var(--warn)}.pill.good{background:var(--goodbg);color:var(--good)}.pill.gray{background:#eceef1;color:var(--ink2)}
.act{background:var(--ink);color:#fff;border:0;border-radius:6px;padding:6px 10px;font-weight:700;font-size:12px;white-space:nowrap}
.act:hover{background:#34373d}
.lnk{color:var(--s1);font-size:11.5px;display:block;margin-top:4px}
.kpis{display:grid;grid-template-columns:repeat(4,1fr);gap:0;background:#fff;border:1px solid var(--line);border-radius:12px;overflow:hidden}
.kpi{padding:14px 16px;border-right:1px solid var(--line)}.kpi:last-child{border-right:0}
.kpi .n{font-size:30px;font-weight:800;letter-spacing:-1px;line-height:1.1}
.kpi .l{font-weight:700;margin-top:4px}.kpi .d{color:var(--mut);font-size:11.5px;margin-top:3px;line-height:1.5}
.kpi.crit .n{color:var(--crit)}.kpi.warn .n{color:var(--warn)}.kpi.good .n{color:var(--good)}
.h2{font-size:14px;font-weight:800;margin:20px 0 8px;display:flex;gap:8px;align-items:baseline}
.h2 small{color:var(--mut);font-weight:500;font-size:11.5px}
.fun{display:grid;grid-template-columns:repeat(5,1fr);background:#fff;border:1px solid var(--line);border-radius:12px;overflow:hidden}
.fun>div{padding:12px 14px;border-right:1px solid var(--line)}.fun>div:last-child{border-right:0;background:#f3faf3}
.fun .n{font-size:24px;font-weight:800;letter-spacing:-.6px}.fun .l{font-weight:700;margin-top:2px}.fun .d{font-size:11.5px;color:var(--mut);margin-top:6px}
.fun .d b{color:var(--crit)}
.two{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.card{background:#fff;border:1px solid var(--line);border-radius:12px;padding:14px 16px}
.bl{display:grid;grid-template-columns:210px 1fr 34px;gap:8px;align-items:center;margin:7px 0;font-size:12.5px}
.bl .bar{height:12px;background:#f0f1f3;border-radius:0 4px 4px 0}
.bl .bar i{display:block;height:100%;background:var(--s1);border-radius:0 4px 4px 0}
.bl.hi .bar i{background:var(--crit)}
.bl .v{text-align:right;font-weight:800;font-variant-numeric:tabular-nums}
.bl .nm{color:var(--ink2);line-height:1.35}
.mx td,.mx th{text-align:right}.mx td:first-child,.mx th:first-child{text-align:left}
.mx td.z{color:#c3c6cc}.mx td.bad{color:var(--crit);font-weight:800}
.svgc{width:100%;height:auto;display:block}
.cap{color:var(--mut);font-size:11.5px;margin-top:6px}
.tip{position:fixed;z-index:50;background:var(--ink);color:#fff;border-radius:7px;padding:6px 9px;font-size:12px;pointer-events:none;display:none;white-space:nowrap}
.ovl{position:fixed;inset:0;background:rgba(20,22,26,.45);display:none;align-items:center;justify-content:center;z-index:60;padding:18px}
.ovl.on{display:flex}
.mdl{background:#fff;border-radius:14px;max-width:760px;width:100%;max-height:88vh;overflow:auto;padding:18px 20px}
.mdl h3{margin:0 0 4px;font-size:16px;font-weight:800}
.mdl pre{background:#f6f7f9;border-radius:9px;padding:12px;white-space:pre-wrap;font-family:inherit;font-size:12.5px;line-height:1.65;margin:10px 0}
.mdl .row{display:flex;gap:8px;justify-content:flex-end;margin-top:12px;flex-wrap:wrap}
.toast{position:fixed;left:50%;bottom:22px;transform:translateX(-50%);background:var(--ink);color:#fff;padding:9px 16px;border-radius:9px;font-weight:600;display:none;z-index:70}
.sec{margin-top:16px}
.search{border:1px solid var(--line);border-radius:7px;padding:6px 10px;font:inherit;min-width:220px}
.ib{font-size:12px;color:var(--ink2);margin:8px 0}
.ib input{vertical-align:middle}
.empty{padding:22px;text-align:center;color:var(--mut)}
.legend{display:flex;gap:14px;font-size:11.5px;color:var(--ink2);margin:4px 0 6px}
.legend i{display:inline-block;width:10px;height:10px;border-radius:2px;margin-right:5px;vertical-align:-1px}
@media(max-width:860px){.kpis{grid-template-columns:1fr 1fr}.kpi:nth-child(2){border-right:0}.kpi{border-bottom:1px solid var(--line)}.fun{grid-template-columns:1fr 1fr}.two{grid-template-columns:1fr}.bl{grid-template-columns:110px 1fr 30px}.wrap{padding:14px 12px 50px}}

.kpis.k6{grid-template-columns:repeat(6,1fr)}
.kpi .n{font-size:28px}
.warnbox{border-color:#f0d9a8;background:#fffaf0}
.src{display:flex;gap:8px;align-items:baseline;padding:4px 0;font-size:12.5px;color:var(--ink2);flex-wrap:wrap}
.src b{color:var(--ink);min-width:150px}
.src .dot{width:14px;font-weight:800}
.src.good .dot{color:#2e9e2e}.src.warn .dot{color:var(--warn)}.src.crit{color:var(--crit)}.src.crit .dot,.src.crit b{color:var(--crit)}
.nopad{padding:0;overflow:hidden}
.fi{display:grid;grid-template-columns:92px 1fr 130px auto;gap:12px;align-items:center;padding:11px 14px;border-bottom:1px solid var(--hair)}
.fi:last-child{border-bottom:0}
.fi-a{display:flex;gap:6px;justify-content:flex-end;flex-wrap:wrap}
mark{background:#fff0a8;border-radius:3px;padding:0 2px;color:inherit}
.board{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;align-items:start}
.col{background:#eceef1;border-radius:12px;padding:10px}
.colh{display:flex;justify-content:space-between;font-size:13px}
.cnt{background:#fff;border-radius:10px;padding:0 8px;font-weight:800}
.bc2{background:#fff;border:1px solid var(--line);border-radius:9px;padding:9px 10px;margin-bottom:8px;font-size:12.5px;line-height:1.55}
.ba{display:flex;gap:6px;margin-top:8px;flex-wrap:wrap}
.empty.sm{padding:10px}
.pill{white-space:nowrap}
.pb{display:inline-block;width:60px;height:7px;background:#e6e8ec;border-radius:4px;vertical-align:middle;overflow:hidden}
.pb i{display:block;height:100%;background:var(--s1)}
select,input[type=date],textarea{font:inherit;font-size:12px;border:1px solid var(--line);border-radius:6px;padding:4px 6px;background:#fff;color:var(--ink)}
textarea{width:100%;padding:9px;font-size:13px;line-height:1.6}
.three{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}
.pr2 p{margin:6px 0 0;color:var(--ink2);line-height:1.7}
.pr{background:#f6f7f9;border-radius:10px;padding:12px;margin-top:8px}
.rules{display:grid;gap:8px;color:var(--ink2);line-height:1.6}.rules b{color:var(--ink);margin-right:6px}
@media(max-width:860px){.kpis.k6{grid-template-columns:repeat(2,1fr)}.board{grid-template-columns:1fr}.fi{grid-template-columns:1fr}.fi-a{justify-content:flex-start}.three{grid-template-columns:1fr}}
</style></head>
<body>
<div class="wrap">
  <div class="top">
    <h1>아침 업무 브리핑</h1><span class="ver">Morning Briefing · v1.0 데모</span><span class="ver">2026. 10. 26.(월) 오전 9:05 기준</span>
    <div class="sp"></div>
    <button class="btn" id="b-copy">브리핑 문구 복사</button>
  </div>
  <div class="demo"><b>DEMO</b> 모든 메시지·이름·업무는 가상입니다. 버튼 동작은 이 화면에서만 반영되고 저장·전송되지 않습니다.</div>
  <div class="tabs" role="tablist" id="tabs"></div>
  <div id="view"></div>
</div>
<div class="ovl" id="ovl"><div class="mdl" id="mdl"></div></div>
<div class="toast" id="toast"></div>
<div class="tip" id="tip"></div>
<script>
const DATA = {"msgs":[{"id":"m1","date":"2026-10-26","time":"08:40","src":"slack","where":"#물류운영","frm":"정 매니저","mention":"me","text":"@나 내일 오전까지 11월 입고 예정 리스트 정리해서 공유 부탁드립니다.","thread":null,"truth":{"label":"todo","due":"2026-10-27"}},{"id":"m2","date":"2026-10-23","time":"15:10","src":"slack","where":"#물류운영","frm":"최 파트장","mention":"me","text":"@나 다음주 월요일까지 박스 재고 실사 결과 올려주세요.","thread":null,"truth":{"label":"todo","due":"2026-10-26"}},{"id":"m3","date":"2026-10-23","time":"11:20","src":"mail","where":"메일","frm":"윤 구매","mention":"me","text":"[요청] 10/28까지 비품 구매 견적 3곳 비교 검토 부탁드립니다.","thread":null,"truth":{"label":"todo","due":"2026-10-28"}},{"id":"m4","date":"2026-10-23","time":"17:05","src":"slack","where":"#출고","frm":"최 파트장","mention":"me","text":"@나 배차 시간을 18시 50분으로 당기는 안, 목요일 회의 전까지 의견 주세요.","thread":null,"truth":{"label":"todo","due":"2026-10-29"}},{"id":"m5","date":"2026-10-22","time":"10:30","src":"meeting","where":"회의록","frm":"박 팀장","mention":"me","text":"[회의 결정] 나: 11월 3일까지 파손 방지 교육 자료 초안 작성","thread":null,"truth":{"label":"todo","due":"2026-11-03"}},{"id":"m6","date":"2026-10-26","time":"08:55","src":"mail","where":"메일","frm":"이 대리","mention":"me","text":"급히 부탁드립니다. 오늘 중으로 특송사 A 정산서 금액 재확인해 주세요.","thread":null,"truth":{"label":"todo","due":"2026-10-26"}},{"id":"m7","date":"2026-10-20","time":"14:00","src":"slack","where":"#구매-물류","frm":"윤 구매","mention":"me","text":"@나 월말까지 부자재 발주 주기표 최신화 부탁합니다.","thread":null,"truth":{"label":"todo","due":"2026-10-31"}},{"id":"m8","date":"2026-10-22","time":"16:30","src":"slack","where":"#프로젝트-sop","frm":"한 CX","mention":"me","text":"@나 입고 SOP 초안 검토 후 수요일까지 코멘트 부탁드려요.","thread":null,"truth":{"label":"todo","due":"2026-10-28"}},{"id":"m9","date":"2026-10-21","time":"09:10","src":"mail","where":"메일","frm":"박 팀장","mention":"me","text":"내일까지 부서별 비용 절감 아이디어 3개씩 회신 바랍니다.","thread":null,"truth":{"label":"todo","due":"2026-10-22"}},{"id":"m10","date":"2026-10-23","time":"13:00","src":"slack","where":"#물류운영","frm":"정 매니저","mention":"me","text":"@나 반송 접수 건 처리 현황 오늘 중으로 알려주세요.","thread":"t10","truth":{"label":"done","due":"2026-10-23"}},{"id":"m10b","date":"2026-10-23","time":"18:00","src":"slack","where":"#물류운영","frm":"나","mention":"none","text":"처리 현황 정리해서 스레드에 올렸습니다.","thread":"t10","truth":{"label":"fyi","due":null}},{"id":"m41","date":"2026-10-22","time":"09:20","src":"mail","where":"메일","frm":"윤 구매","mention":"me","text":"[긴급] 박스 납품 지연 건, 대체 업체 확인해 주세요. 오늘 퇴근 전까지 부탁드립니다.","thread":"t41","truth":{"label":"todo","due":"2026-10-22"}},{"id":"m41b","date":"2026-10-22","time":"17:30","src":"mail","where":"메일","frm":"나","mention":"none","text":"대체 업체 두 곳 확인했습니다만, 단가 확인이 더 필요합니다.","thread":"t41","truth":{"label":"fyi","due":null}},{"id":"m42","date":"2026-10-23","time":"10:20","src":"slack","where":"#출고","frm":"최 파트장","mention":"me","text":"@나 에어캡 재사용 기준 초안 11/6까지 부탁.","thread":null,"truth":{"label":"todo","due":"2026-11-06"}},{"id":"m43","date":"2026-10-19","time":"15:00","src":"mail","where":"메일","frm":"박 팀장","mention":"me","text":"10월 말까지 지게차 인원 계획 확인 요청드립니다.","thread":null,"truth":{"label":"todo","due":"2026-10-31"}},{"id":"m44","date":"2026-10-23","time":"16:40","src":"slack","where":"#프로젝트-sop","frm":"한 CX","mention":"me","text":"@나 SOP 3장 반영해 주세요. 다음 주 내로 가능할까요?","thread":null,"truth":{"label":"todo","due":"2026-10-30"}},{"id":"m45","date":"2026-10-26","time":"08:45","src":"mail","where":"메일","frm":"택배사 담당자","mention":"me","text":"견적서 첨부드립니다. 검토 후 회신 주시면 감사하겠습니다.","thread":null,"truth":{"label":"todo","due":null}},{"id":"m46","date":"2026-10-22","time":"13:00","src":"mail","where":"메일","frm":"박 팀장","mention":"me","text":"지게차 보험 갱신 서류 보내주세요.","thread":"t46","truth":{"label":"done","due":null}},{"id":"m46b","date":"2026-10-22","time":"15:00","src":"mail","where":"메일","frm":"나","mention":"none","text":"서류 메일로 보냈습니다.","thread":"t46","truth":{"label":"fyi","due":null}},{"id":"m47","date":"2026-10-23","time":"09:00","src":"slack","where":"#물류운영","frm":"정 매니저","mention":"me","text":"@나 어제 출고 마감 오류 건 원인 파악해서 알려주세요. 오늘 중으로.","thread":"t47","truth":{"label":"done","due":"2026-10-23"}},{"id":"m47b","date":"2026-10-23","time":"16:00","src":"slack","where":"#물류운영","frm":"나","mention":"none","text":"원인 파악해서 스레드에 올렸습니다.","thread":"t47","truth":{"label":"fyi","due":null}},{"id":"m50","date":"2026-10-20","time":"10:00","src":"meeting","where":"회의록","frm":"박 팀장","mention":"me","text":"[회의 결정] 나: 부서 간 SOP 조정회의 안건 목록 정리","thread":null,"truth":{"label":"todo","due":null}},{"id":"m51","date":"2026-10-21","time":"15:30","src":"slack","where":"#물류운영","frm":"정 매니저","mention":"me","text":"@나 혹시 시간 되시면 박스 재고 숫자 한번만 봐주실 수 있을까요? 급하진 않아요.","thread":null,"truth":{"label":"todo","due":null}},{"id":"m53","date":"2026-10-23","time":"14:30","src":"slack","where":"#cx-공유","frm":"한 CX","mention":"me","text":"@나 반송 건 고객 안내 문구, 다음 주 월요일까지 검토 바랍니다.","thread":null,"truth":{"label":"todo","due":"2026-10-26"}},{"id":"m54","date":"2026-10-22","time":"10:10","src":"slack","where":"#물류운영","frm":"정 매니저","mention":"me","text":"@나 입고 마감 체크리스트만 오늘 정리해 주세요.","thread":null,"truth":{"label":"todo","due":"2026-10-22"}},{"id":"m55","date":"2026-10-23","time":"09:40","src":"mail","where":"메일","frm":"박 팀장","mention":"me","text":"금주 마감 전에 비용 절감안 확인 요청드립니다.","thread":null,"truth":{"label":"todo","due":"2026-10-23"}},{"id":"m57","date":"2026-10-21","time":"10:40","src":"mail","where":"메일","frm":"윤 구매","mention":"me","text":"회신은 불필요하지만, 28일까지 계약서 검토는 부탁드립니다.","thread":null,"truth":{"label":"todo","due":"2026-10-28"}},{"id":"m36","date":"2026-10-21","time":"10:00","src":"slack","where":"#프로젝트-sop","frm":"한 CX","mention":"me","text":"@나 SOP 건 가능한 빨리 봐주세요.","thread":null,"truth":{"label":"todo","due":null}},{"id":"m35","date":"2026-10-22","time":"11:30","src":"mail","where":"메일","frm":"박 팀장","mention":"me","text":"다음 주 중으로 비용 절감안 방향 한번 정리해 보면 좋겠습니다.","thread":null,"truth":{"label":"todo","due":"2026-10-30"}},{"id":"m38","date":"2026-10-22","time":"18:00","src":"mail","where":"메일","frm":"택배사 담당자","mention":"me","text":"11월 단가 협의 일정 조율 부탁드립니다. 편하신 일정 알려주세요.","thread":null,"truth":{"label":"todo","due":null}},{"id":"m11","date":"2026-10-22","time":"09:30","src":"mail","where":"메일","frm":"나","mention":"none","text":"특송사 A 담당자님, 소명 요청 건 진행 상황 확인 부탁드립니다. 모레까지 회신 주시면 감사하겠습니다.","thread":null,"truth":{"label":"wait","due":"2026-10-24"}},{"id":"m12","date":"2026-10-23","time":"10:00","src":"slack","where":"#cx-공유","frm":"나","mention":"none","text":"@한 CX 고객 안내 문구 확정본 전달 부탁드립니다.","thread":null,"truth":{"label":"wait","due":null}},{"id":"m13","date":"2026-10-20","time":"15:00","src":"slack","where":"#구매-물류","frm":"나","mention":"none","text":"@윤 구매 발주 단가표 최신본 보내주실 수 있을까요?","thread":null,"truth":{"label":"wait","due":null}},{"id":"m14","date":"2026-10-26","time":"07:50","src":"mail","where":"메일","frm":"나","mention":"none","text":"택배사 담당자님, 당일 저녁 집하 시간 조정 가능한지 회신 부탁드립니다.","thread":null,"truth":{"label":"wait","due":null}},{"id":"m15","date":"2026-10-19","time":"17:00","src":"slack","where":"#프로젝트-sop","frm":"나","mention":"none","text":"@최 파트장 SOP 3장 수정안 확인 부탁드립니다.","thread":"t15","truth":{"label":"done","due":null}},{"id":"m15b","date":"2026-10-20","time":"09:00","src":"slack","where":"#프로젝트-sop","frm":"최 파트장","mention":"none","text":"확인했습니다. 수정 없이 진행하세요.","thread":"t15","truth":{"label":"fyi","due":null}},{"id":"m16","date":"2026-10-21","time":"11:00","src":"mail","where":"메일","frm":"나","mention":"none","text":"윤 구매님, 박스 업체 견적 회신 부탁드립니다.","thread":"t16","truth":{"label":"wait","due":null}},{"id":"m16b","date":"2026-10-22","time":"10:00","src":"mail","where":"메일","frm":"윤 구매","mention":"none","text":"내일 오전 중 보내드리겠습니다.","thread":"t16","truth":{"label":"fyi","due":null}},{"id":"m17","date":"2026-10-22","time":"14:00","src":"slack","where":"#출고","frm":"나","mention":"none","text":"@최 파트장 지게차 가능 인원 정리해서 알려주세요.","thread":null,"truth":{"label":"wait","due":null}},{"id":"m18","date":"2026-10-26","time":"09:00","src":"slack","where":"#물류운영","frm":"나","mention":"none","text":"@정 매니저 금주 입고 지연 건 사유 정리 부탁드려요.","thread":null,"truth":{"label":"wait","due":null}},{"id":"m33","date":"2026-10-26","time":"08:25","src":"slack","where":"#cx-공유","frm":"한 CX","mention":"team","text":"고객 문의 건 배송사 회신 현황 확인 가능한 분 계실까요?","thread":null,"truth":{"label":"unclear","due":null}},{"id":"m34","date":"2026-10-26","time":"08:30","src":"slack","where":"#cx-공유","frm":"한 CX","mention":"team","text":"@here 오늘 중으로 반송 접수 건 재확인 부탁드립니다.","thread":null,"truth":{"label":"unclear","due":"2026-10-26"}},{"id":"m37","date":"2026-10-23","time":"12:00","src":"slack","where":"#물류운영","frm":"정 매니저","mention":"team","text":"누가 지게차 점검 일정 잡아주실 수 있나요?","thread":null,"truth":{"label":"unclear","due":null}},{"id":"m39","date":"2026-10-26","time":"07:30","src":"slack","where":"#출고","frm":"최 파트장","mention":"team","text":"@here 팔레트 부족하니 확인 부탁드립니다. 오전 중으로","thread":null,"truth":{"label":"unclear","due":"2026-10-26"}},{"id":"m19","date":"2026-10-26","time":"08:36","src":"slack","where":"#물류운영","frm":"정 매니저","mention":"team","text":"공유드립니다. 11월부터 택배 단가가 일부 변경됩니다. 참고 부탁드립니다.","thread":null,"truth":{"label":"fyi","due":null}},{"id":"m20","date":"2026-10-26","time":"08:10","src":"slack","where":"#cx-공유","frm":"한 CX","mention":"team","text":"오늘 오후 2시까지 도착하면 당일 선적 가능합니다. 안내드립니다.","thread":null,"truth":{"label":"fyi","due":null}},{"id":"m21","date":"2026-10-23","time":"18:00","src":"slack","where":"#출고","frm":"최 파트장","mention":"team","text":"금요일 마감 기준 출고 실적: 입고 96, 출고 88, 이슈 4건입니다.","thread":null,"truth":{"label":"fyi","due":null}},{"id":"m22","date":"2026-10-22","time":"09:00","src":"meeting","where":"회의록","frm":"박 팀장","mention":"team","text":"[공지] 부서 간 SOP 조정회의는 이번 달 진행하지 않습니다.","thread":null,"truth":{"label":"fyi","due":null}},{"id":"m23","date":"2026-10-21","time":"13:00","src":"mail","where":"메일","frm":"박 팀장","mention":"team","text":"11월 인력 배치표 공유드립니다. 확인 후 회신은 필요 없습니다.","thread":null,"truth":{"label":"fyi","due":null}},{"id":"m24","date":"2026-10-26","time":"08:00","src":"slack","where":"#물류운영","frm":"정 매니저","mention":"team","text":"일요일 배차는 월요일 입고로 변경 예정입니다. 참고해 주세요.","thread":null,"truth":{"label":"fyi","due":null}},{"id":"m25","date":"2026-10-23","time":"09:30","src":"slack","where":"#cx-공유","frm":"한 CX","mention":"team","text":"특송사 A 소명 3일 무회신 건 7건, CX 안내 완료했습니다.","thread":null,"truth":{"label":"fyi","due":null}},{"id":"m26","date":"2026-10-20","time":"11:00","src":"mail","where":"메일","frm":"윤 구매","mention":"team","text":"박스 단가 인상 안내드립니다. 11월 1일 입고분부터 적용됩니다.","thread":null,"truth":{"label":"fyi","due":null}},{"id":"m27","date":"2026-10-22","time":"15:00","src":"slack","where":"#구매-물류","frm":"윤 구매","mention":"team","text":"발주 마감은 매주 수요일 16시입니다. 참고만 해주세요.","thread":null,"truth":{"label":"fyi","due":null}},{"id":"m28","date":"2026-10-26","time":"08:20","src":"slack","where":"#출고","frm":"최 파트장","mention":"team","text":"어제 출고 22건, 이슈 잔여 14건입니다.","thread":null,"truth":{"label":"fyi","due":null}},{"id":"m29","date":"2026-10-19","time":"16:00","src":"meeting","where":"회의록","frm":"박 팀장","mention":"team","text":"[회의] 파손 사례 공유: 에어캡 부족 시 파손 증가 경향.","thread":null,"truth":{"label":"fyi","due":null}},{"id":"m30","date":"2026-10-21","time":"17:00","src":"mail","where":"메일","frm":"이 대리","mention":"team","text":"택배사 휴무 일정 안내드립니다. 11/3 휴무.","thread":null,"truth":{"label":"fyi","due":null}},{"id":"m31","date":"2026-10-23","time":"14:00","src":"slack","where":"#cx-공유","frm":"한 CX","mention":"team","text":"고객 문의 응대 템플릿 업데이트했습니다. 필요하신 분 참고하세요.","thread":null,"truth":{"label":"fyi","due":null}},{"id":"m32","date":"2026-10-26","time":"08:50","src":"slack","where":"#물류운영","frm":"정 매니저","mention":"team","text":"아침 회의는 10시에 시작합니다.","thread":null,"truth":{"label":"fyi","due":null}},{"id":"m40","date":"2026-10-21","time":"12:30","src":"meeting","where":"회의록","frm":"박 팀장","mention":"team","text":"[논의] 부자재 사용주기 관리 방식은 추후 결정.","thread":null,"truth":{"label":"fyi","due":null}},{"id":"m48","date":"2026-10-26","time":"08:05","src":"mail","where":"메일","frm":"자동 알림","mention":"team","text":"[자동] 어제 수집 실패 채널: #재고-공유 (권한 만료)","thread":null,"truth":{"label":"fyi","due":null}},{"id":"m49","date":"2026-10-23","time":"19:00","src":"slack","where":"#출고","frm":"최 파트장","mention":"team","text":"금요일 마감 완료했습니다.","thread":null,"truth":{"label":"fyi","due":null}},{"id":"m52","date":"2026-10-26","time":"08:15","src":"slack","where":"#구매-물류","frm":"윤 구매","mention":"team","text":"박스 단가표 최신본 올렸습니다.","thread":null,"truth":{"label":"fyi","due":null}}],"tasks":[{"id":"T1","title":"신규 대시보드 접근 코드 변경 기록","status":"진행","cat":"","kind":"기록","owner":"","imp":null,"due":null,"prog":null,"issue":false,"upd":3,"next":"","src":null},{"id":"T2","title":"당일 오후 2시까지 도착 시 당일 선적 규칙 공지","status":"진행","cat":"","kind":"공지·교육","owner":"","imp":null,"due":null,"prog":null,"issue":false,"upd":2,"next":"","src":null},{"id":"T3","title":"일요 배차의 월요일 입고 변경 공지","status":"진행","cat":"","kind":"공지·교육","owner":"","imp":null,"due":null,"prog":null,"issue":false,"upd":0,"next":"","src":null},{"id":"T4","title":"SOP 개정안 작성(입고·반품)","status":"진행","cat":"조직·관리›교육·SOP","kind":"개선","owner":"최 파트장","imp":null,"due":null,"prog":40,"issue":false,"upd":2,"next":"","src":null},{"id":"T5","title":"비품 관리 업무 개선안(2주)","status":"진행","cat":"재고·자재›비품 구매","kind":"개선","owner":"최 파트장","imp":null,"due":null,"prog":0,"issue":false,"upd":4,"next":"","src":null},{"id":"T6","title":"작업 화면 통합 후 점검","status":"제안","cat":"시스템›어드민·WMS","kind":"실행","owner":"공통","imp":"긴급","due":"2026-10-21","prog":null,"issue":true,"upd":9,"next":"","src":null},{"id":"T7","title":"10월 말 인력 이탈 대비 지게차 운전 가능 인원 확인","status":"제안","cat":"조직·관리›인원·근무","kind":"실행","owner":"공통","imp":"중요","due":"2026-10-31","prog":null,"issue":false,"upd":8,"next":"","src":"m43"},{"id":"T8","title":"특송사 소명 3일 무회신 건 CX 안내 후 라벨 정리","status":"제안","cat":"통관·배송›통관·소명","kind":"실행","owner":"공통","imp":"중요","due":null,"prog":null,"issue":false,"upd":10,"next":"","src":null},{"id":"T9","title":"배차 시간 18시 50분으로 조정","status":"제안","cat":"물류공정›출하·배차","kind":"실행","owner":"공통","imp":"보통","due":null,"prog":null,"issue":true,"upd":3,"next":"","src":"m4"},{"id":"T10","title":"입고 SOP(초안) 확인·확정 후 전원 공지","status":"제안","cat":"조직·관리›교육·SOP","kind":"공지·교육","owner":"공통","imp":"보통","due":null,"prog":60,"issue":false,"upd":6,"next":"","src":null},{"id":"T11","title":"택배 당일 저녁 집하 조정 가능 여부 확인","status":"제안","cat":"물류공정›출하·배차","kind":"실행","owner":"공통","imp":"중요","due":null,"prog":60,"issue":false,"upd":7,"next":"","src":null},{"id":"T12","title":"택배사 단가 협의 일정 조율","status":"제안","cat":"물류공정›출하·배차","kind":"실행","owner":"공통","imp":"보통","due":null,"prog":null,"issue":false,"upd":2,"next":"","src":null},{"id":"T13","title":"지게차 점검 일정 수립","status":"제안","cat":"조직·관리›인원·근무","kind":"실행","owner":"","imp":"보통","due":null,"prog":null,"issue":false,"upd":1,"next":"","src":null},{"id":"T14","title":"스캐너 기반 랙 피킹 테스트","status":"진행","cat":"물류공정›입고·적치","kind":"실행","owner":"공통","imp":null,"due":null,"prog":null,"issue":false,"upd":5,"next":"","src":null},{"id":"T15","title":"부서 간 SOP 조정회의 안건 정리","status":"진행","cat":"조직·관리›교육·SOP","kind":"공지·교육","owner":"나","imp":null,"due":null,"prog":null,"issue":false,"upd":1,"next":"","src":"m50"},{"id":"T16","title":"박스·소모품 대량 구매 검토","status":"진행","cat":"재고·자재›박스·부자재","kind":"개선","owner":"공통","imp":null,"due":null,"prog":null,"issue":false,"upd":6,"next":"","src":null},{"id":"T17","title":"파손 방지 교육 자료 작성","status":"진행","cat":"물류공정›출고·포장","kind":"공지·교육","owner":"나","imp":"중요","due":"2026-11-03","prog":null,"issue":false,"upd":1,"next":"","src":"m5"},{"id":"T18","title":"차량 톤수별 배차 기준 정리","status":"진행","cat":"물류공정›출하·배차","kind":"개선","owner":"공통","imp":null,"due":null,"prog":null,"issue":true,"upd":4,"next":"","src":null},{"id":"T19","title":"구매 주기 관리표 작성","status":"진행","cat":"재고·자재›박스·부자재","kind":"개선","owner":"공통","imp":null,"due":"2026-10-31","prog":null,"issue":false,"upd":3,"next":"","src":null},{"id":"T20","title":"출고 동선 레이아웃 재검토","status":"진행","cat":"물류공정›출고·포장","kind":"개선","owner":"공통","imp":null,"due":null,"prog":null,"issue":false,"upd":5,"next":"","src":null},{"id":"T21","title":"출차 기준 조정(적재율 미만 시 대기)","status":"진행","cat":"물류공정›출하·배차","kind":"개선","owner":"공통","imp":null,"due":null,"prog":null,"issue":true,"upd":4,"next":"","src":null},{"id":"T22","title":"부자재 사용주기·팔레트당 수량 정리","status":"진행","cat":"재고·자재›박스·부자재","kind":"개선","owner":"공통","imp":"보통","due":"2026-10-24","prog":null,"issue":false,"upd":2,"next":"","src":null},{"id":"T23","title":"부자재 목록 정비","status":"진행","cat":"재고·자재›박스·부자재","kind":"실행","owner":"공통","imp":null,"due":null,"prog":null,"issue":false,"upd":6,"next":"","src":null},{"id":"T24","title":"에어캡 재사용 기준 정리","status":"진행","cat":"재고·자재›박스·부자재","kind":"개선","owner":"나","imp":null,"due":"2026-11-06","prog":null,"issue":false,"upd":1,"next":"","src":"m42"},{"id":"T25","title":"11월 입고 예정 리스트 정리","status":"진행","cat":"물류공정›입고·적치","kind":"실행","owner":"나","imp":"중요","due":"2026-10-27","prog":null,"issue":false,"upd":0,"next":"","src":"m1"},{"id":"T26","title":"박스 재고 실사 결과 정리","status":"진행","cat":"재고·자재›박스·부자재","kind":"실행","owner":"나","imp":"보통","due":"2026-10-26","prog":null,"issue":false,"upd":0,"next":"","src":"m2"},{"id":"T27","title":"비품 구매 견적 3곳 비교","status":"진행","cat":"재고·자재›비품 구매","kind":"실행","owner":"나","imp":"보통","due":"2026-10-28","prog":null,"issue":false,"upd":2,"next":"","src":"m3"},{"id":"T28","title":"특송사 정산서 금액 재확인","status":"진행","cat":"통관·배송›통관·소명","kind":"실행","owner":"나","imp":"긴급","due":"2026-10-26","prog":null,"issue":false,"upd":0,"next":"","src":"m6"},{"id":"T29","title":"발주 주기표 최신화","status":"진행","cat":"재고·자재›박스·부자재","kind":"실행","owner":"나","imp":null,"due":"2026-10-31","prog":null,"issue":false,"upd":6,"next":"","src":"m7"},{"id":"T30","title":"입고 SOP 초안 코멘트 정리","status":"대기","cat":"조직·관리›교육·SOP","kind":"실행","owner":"나","imp":"보통","due":"2026-10-28","prog":null,"issue":false,"upd":4,"next":"초안 최종본 수신 후","src":"m8"},{"id":"T31","title":"택배 단가 변경 반영(11월)","status":"진행","cat":"물류공정›출하·배차","kind":"실행","owner":"공통","imp":null,"due":"2026-10-31","prog":null,"issue":false,"upd":0,"next":"","src":null},{"id":"T32","title":"대체 박스 업체 확인","status":"진행","cat":"재고·자재›박스·부자재","kind":"실행","owner":"나","imp":"중요","due":"2026-10-22","prog":null,"issue":false,"upd":4,"next":"단가 확인","src":"m41"},{"id":"T33","title":"지게차 보험 갱신 서류","status":"완료","cat":"조직·관리›인원·근무","kind":"실행","owner":"나","imp":null,"due":null,"prog":null,"issue":false,"upd":4,"next":"","src":"m46"},{"id":"T34","title":"반송 접수 현황 보고","status":"완료","cat":"통관·배송›통관·소명","kind":"실행","owner":"나","imp":null,"due":null,"prog":null,"issue":false,"upd":3,"next":"","src":"m10"},{"id":"T35","title":"출고 마감 오류 원인 파악","status":"완료","cat":"물류공정›출고·포장","kind":"실행","owner":"나","imp":null,"due":null,"prog":null,"issue":false,"upd":3,"next":"","src":"m47"},{"id":"T36","title":"입고 체크리스트 개정","status":"완료","cat":"조직·관리›교육·SOP","kind":"개선","owner":"최 파트장","imp":null,"due":null,"prog":null,"issue":false,"upd":7,"next":"","src":null},{"id":"T37","title":"월 마감 비용표 정리","status":"완료","cat":"재고·자재›비품 구매","kind":"실행","owner":"공통","imp":null,"due":null,"prog":null,"issue":false,"upd":9,"next":"","src":null},{"id":"T38","title":"SOP 3장 수정안 확인","status":"완료","cat":"조직·관리›교육·SOP","kind":"실행","owner":"나","imp":null,"due":null,"prog":null,"issue":false,"upd":6,"next":"","src":"m15"}],"sources":[{"name":"Slack · 참여 채널 12개","state":"ok","detail":"오늘 08:30 수집 · 신규 메시지 24건"},{"name":"Slack · #재고-공유","state":"fail","detail":"수집 실패(권한 만료) · 마지막 정상 수집 10/24 18:20 — 이 채널의 요청은 누락될 수 있음"},{"name":"메일 · 담당자 라벨 5개","state":"ok","detail":"오늘 08:31 수집 · 신규 메일 9건"},{"name":"회의록","state":"warn","detail":"오늘 10:00 회의 기록은 아직 없음(회의 후 수집)"},{"name":"업무 관리 DB","state":"warn","detail":"제안 상태 8건 중 7일 이상 방치된 건이 있음"}],"fixes":{"m33":{"phrase":"가능한 분","label":"unclear","why":"질문형 요청 — 요청 문구가 없어 참고로 분류됨"},"m35":{"phrase":"좋겠습니다","label":"todo","why":"완곡한 요청 — \"부탁/주세요\" 같은 표준 문구가 없음"},"m37":{"phrase":"잡아주실 수 있나요","label":"unclear","why":"질문형 요청 — 담당 불명인데 참고로 분류됨"},"m41":{"phrase":"했습니다만","label":"notdone","why":"완료 문구 뒤에 단서(\"~했습니다만\")가 붙어 완료로 오판"},"m57":{"phrase":"불필요하지만","label":"todo","why":"\"불필요\"가 앞에 있어 뒤의 실제 요청을 놓침"},"m25":{"phrase":"안내 완료했습니다","label":"fyi","why":"\"회신\"이라는 단어만 보고 요청으로 오판 — 이미 끝난 보고 문장"}},"duefix":{"m54":{"phrase":"오늘 정리","rel":"today","why":"\"오늘 ~해 주세요\"처럼 \"까지\" 없는 마감 표현"},"m55":{"phrase":"금주 마감","rel":"fri","why":"\"금주 마감\"처럼 사전에 없는 마감 표현"}}};
const $ = (id) => document.getElementById(id);
const esc = (t) => String(t == null ? '' : t).replace(/[&<>"]/g, (c) => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const WD = ['일','월','화','수','목','금','토'];
const T0 = Date.UTC(2026, 9, 26);                         // 오늘(월)
const off = (iso) => Math.round((Date.parse(iso + 'T00:00:00Z') - T0) / 864e5);   // 오늘 기준 일수 차
const isoOf = (o) => new Date(T0 + o * 864e5).toISOString().slice(0, 10);
const fmt = (o) => { const d = new Date(T0 + o * 864e5); return String(d.getUTCMonth() + 1).padStart(2, '0') + '/' + String(d.getUTCDate()).padStart(2, '0') + '(' + WD[d.getUTCDay()] + ')'; };
const wdOf = (o) => new Date(T0 + o * 864e5).getUTCDay();

/* ---------------- 상태 ---------------- */
const S = {tab:'today', remind:1, waitDays:2, stale:7, view:'owner', mstate:{}, custom:[], dueRules:[], q:'', ft:'all', tasks:JSON.parse(JSON.stringify(DATA.tasks)), tid:100, ignored:new Set(), sample:0};

/* ---------------- 규칙 기반 분류기 ---------------- */
const REQ = ['부탁','주세요','해 주세요','주시면','회신','검토','확인 요청','보내주','알려주','올려주','봐주','바랍니다','가능한지','가능할까요','요청드립니다'];
const FYI_PRIO = ['참고 부탁','참고해 주','참고만','참고하세요','참고해주'];
const NEG = ['불필요','안 주셔도','않으셔도','필요 없','필요없'];
const DONE = /(완료했습니다|처리했습니다|반영했습니다|올렸습니다|보냈습니다|확인했습니다|마쳤습니다|전달했습니다)/;
const WDI = {'일':0,'월':1,'화':2,'수':3,'목':4,'금':5,'토':6};
function nextWd(ref, idx, strict) { for (let k = strict ? 1 : 0; k < 8; k++) if (wdOf(ref + k) === idx) return ref + k; return ref; }
function parseDue(t, ref) {
  let m, due = null, how = '', urgent = /급히|급하게|ASAP|즉시|가능한 빨리|\[긴급\]/.test(t);
  for (const r of S.dueRules) if (t.includes(r.phrase)) return {due: r.rel === 'today' ? ref : nextWd(ref - 1, 5, true), how:r.phrase, urgent};
  if ((m = t.match(/오늘\s*중|오늘[^.。]{0,6}?까지|(오전|오후)\s*중/))) { due = ref; how = m[0]; }
  else if ((m = t.match(/내일(?:\s*(?:오전|오후))?\s*까지/))) { due = ref + 1; how = m[0]; }
  else if ((m = t.match(/모레\s*까지/))) { due = ref + 2; how = m[0]; }
  else if ((m = t.match(/다음\s*주\s*([월화수목금])요일/))) { const mon = ref + ((8 - wdOf(ref)) % 7 || 7); due = mon + (WDI[m[1]] - 1); how = m[0]; }
  else if ((m = t.match(/([월화수목금])요일[^.。]{0,6}?까지/))) { due = nextWd(ref, WDI[m[1]], true); how = m[0]; }
  else if ((m = t.match(/(이번|다음)\s*주\s*(내|중)/))) { const base = m[1] === '이번' ? ref : ref + ((8 - wdOf(ref)) % 7 || 7); due = nextWd(base - 1, 5, true); how = m[0]; }
  else if ((m = t.match(/(\d{1,2})월\s*(\d{1,2})일/))) { due = off('2026-' + String(m[1]).padStart(2, '0') + '-' + String(m[2]).padStart(2, '0')); how = m[0]; }
  else if ((m = t.match(/(\d{1,2})\/(\d{1,2})\s*까지/))) { due = off('2026-' + String(m[1]).padStart(2, '0') + '-' + String(m[2]).padStart(2, '0')); how = m[0]; }
  else if ((m = t.match(/(\d{1,2})월\s*말/))) { due = off('2026-' + String(m[1]).padStart(2, '0') + '-' + (+m[1] === 11 ? '30' : '31')); how = m[0]; }
  else if ((m = t.match(/월말/))) { const d = new Date(T0 + ref * 864e5); due = off(new Date(Date.UTC(d.getUTCFullYear(), d.getUTCMonth() + 1, 0)).toISOString().slice(0, 10)); how = m[0]; }
  else if ((m = t.match(/(\d{1,2})일\s*까지/))) { const d = new Date(T0 + ref * 864e5); due = off(new Date(Date.UTC(d.getUTCFullYear(), d.getUTCMonth(), +m[1])).toISOString().slice(0, 10)); how = m[0]; }
  return {due, how, urgent};
}
const MSG = DATA.msgs;
function classify(m) {
  const t = m.text, ref = off(m.date), cues = [];
  const cr = S.custom.find((r) => r.label !== 'notdone' && t.includes(r.phrase));
  const neg = NEG.find((w) => t.includes(w)), prio = FYI_PRIO.find((w) => t.includes(w));
  const reqs = REQ.filter((w) => t.includes(w)), tag = /\[회의 결정\]|\[요청\]|\[긴급\]/.test(t);
  let label;
  if (cr) { label = cr.label; cues.push(cr.phrase); }
  else if (neg || prio) { label = 'fyi'; cues.push(neg || prio); }
  else if (reqs.length || tag) { label = m.frm === '나' ? 'wait' : (m.mention === 'me' ? 'todo' : 'unclear'); cues.push(...reqs); if (tag) cues.push('[태그]'); }
  else label = 'fyi';
  const d = parseDue(t, ref);
  let evidence = null;
  if ((label === 'todo' || label === 'wait') && m.thread) {
    evidence = MSG.find((x) => x.thread === m.thread && x.id !== m.id && off(x.date) >= ref && DONE.test(x.text) && !S.custom.some((r) => r.label === 'notdone' && x.text.includes(r.phrase)));
    if (evidence) label = 'done';
  }
  return {label, due:d.due, how:d.how, urgent:d.urgent, cues, evidence};
}
const LBL = {todo:'해야 할 일', wait:'답장 대기', unclear:'확인 필요', fyi:'알고만 됨', done:'완료 후보'};
const SRC = {slack:'Slack', mail:'메일', meeting:'회의록'};
function hl(t, c) {
  let h = esc(t);
  [c.how, ...c.cues.filter((x) => x !== '[태그]')].filter(Boolean).forEach((w) => { const e = esc(w); if (e) h = h.split(e).join('<mark>' + e + '</mark>'); });
  return h;
}
const allC = () => MSG.map((m) => ({m, c:classify(m)}));
const registered = (id) => S.tasks.some((t) => t.src === id);
const taskOfMsg = (id) => S.tasks.find((t) => t.src === id);

/* ---------------- 공통 UI ---------------- */
function toast(t) { const e = $('toast'); e.textContent = t; e.style.display = 'block'; clearTimeout(toast.t); toast.t = setTimeout(() => e.style.display = 'none', 2300); }
function copy(text) {
  const fb = () => { const t = document.createElement('textarea'); t.value = text; t.style.position = 'fixed'; t.style.opacity = '0'; document.body.appendChild(t); t.select(); try { document.execCommand('copy'); } catch (_) {} t.remove(); };
  try { if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(text).catch(fb); else fb(); } catch (e) { fb(); }
}
function openModal(h) { $('mdl').innerHTML = h; $('ovl').classList.add('on'); }
function closeModal() { $('ovl').classList.remove('on'); }
$('ovl').addEventListener('click', (e) => { if (e.target === $('ovl')) closeModal(); });
const tip = $('tip');
document.addEventListener('mouseover', (e) => { const t = e.target.closest('[data-tip]'); if (t) { tip.textContent = t.dataset.tip; tip.style.display = 'block'; } });
document.addEventListener('mousemove', (e) => { if (tip.style.display === 'block') { tip.style.left = Math.min(e.clientX + 12, innerWidth - tip.offsetWidth - 8) + 'px'; tip.style.top = (e.clientY + 14) + 'px'; } });
document.addEventListener('mouseout', (e) => { if (e.target.closest('[data-tip]')) tip.style.display = 'none'; });
const TABS = [['today','오늘의 브리핑'],['db','업무 관리'],['inbox','요청 수집'],['acc','분류 정확도'],['arch','구조']];
function drawTabs() {
  $('tabs').innerHTML = TABS.map(([k, n]) => `<button class="tab" role="tab" data-t="${k}" aria-selected="${S.tab === k}">${n}</button>`).join('');
  $('tabs').querySelectorAll('.tab').forEach((b) => b.addEventListener('click', () => { S.tab = b.dataset.t; draw(); window.scrollTo(0, 0); }));
}
function dueChip(d, done) {
  if (d == null) return '<span class="s2">기한 없음</span>';
  const n = d - 0;
  if (done) return `<span class="s2">${fmt(d)}</span>`;
  if (n < 0) return `<span class="pill crit">기한 지남 ${-n}일</span> <span class="s2">${fmt(d)}</span>`;
  if (n === 0) return `<span class="pill warn">오늘 마감</span>`;
  if (n === 1) return `<span class="pill warn">내일 마감</span>`;
  return `<span class="pill gray">${fmt(d)}</span>`;
}
const tDue = (t) => t.due ? off(t.due) : null;

/* ---------------- 업무 DB 계산 ---------------- */
function kpis() {
  const open = S.tasks.filter((t) => t.status !== '완료');
  return {
    prog: S.tasks.filter((t) => t.status === '진행').length, wait: S.tasks.filter((t) => t.status === '대기').length,
    prop: S.tasks.filter((t) => t.status === '제안').length,
    over: open.filter((t) => t.due && tDue(t) < 0).length, issue: open.filter((t) => t.issue).length,
    today: open.filter((t) => t.due && tDue(t) === 0).length,
  };
}
/* ---------------- 오늘 먼저 볼 것 ---------------- */
function focusItems() {
  const items = [];
  S.tasks.filter((t) => t.status !== '완료' && t.due && tDue(t) <= S.remind && t.owner !== '최 파트장' && !S.ignored.has('T' + t.id)).forEach((t) => {
    const d = tDue(t); items.push({k:'task', id:t.id, score:(d < 0 ? 1000 - d : 500 - d) + (t.imp === '긴급' ? 50 : 0), t});
  });
  allC().forEach(({m, c}) => {
    if (registered(m.id) || S.mstate[m.id]) return;
    const age = -off(m.date);
    if (c.label === 'todo' && ((c.due != null && c.due <= S.remind) || c.urgent)) items.push({k:'msg', id:m.id, score:(c.due != null && c.due < 0 ? 900 - c.due : 400 - (c.due || 0)) + (c.urgent ? 30 : 0), m, c});
    else if (c.label === 'unclear' && c.due != null && c.due <= S.remind) items.push({k:'msg', id:m.id, score:350, m, c});
    else if (c.label === 'wait' && age >= S.waitDays) items.push({k:'msg', id:m.id, score:100 + age * 10, m, c, age});
  });
  S.tasks.filter((t) => t.status === '제안' && t.upd >= S.stale).forEach((t) => items.push({k:'stale', id:t.id, score:50 + t.upd, t}));
  return items.sort((a, b) => b.score - a.score);
}
function actions(it) {
  if (it.k === 'task') return `<button class="act" data-a="tdone" data-id="${it.id}">완료</button><button class="btn sm ghost" data-a="tpush" data-id="${it.id}">내일로</button>`;
  if (it.k === 'stale') return `<button class="act" data-a="tpromote" data-id="${it.id}">진행으로 승격</button><button class="btn sm ghost" data-a="tdrop" data-id="${it.id}">폐기</button>`;
  const c = it.c, id = it.id;
  if (c.label === 'wait') return `<button class="act" data-a="nudge" data-id="${id}">재촉 문구</button><button class="btn sm ghost" data-a="got" data-id="${id}">답 받음</button>`;
  if (c.label === 'done') return `<button class="act" data-a="mdone" data-id="${id}">완료 확인</button><button class="btn sm ghost" data-a="notyet" data-id="${id}">아직</button>`;
  if (c.label === 'unclear') return `<button class="act" data-a="reg" data-id="${id}">내 일로 등록</button><button class="btn sm ghost" data-a="tofyi" data-id="${id}">참고로</button>`;
  return `<button class="act" data-a="reg" data-id="${id}">진행으로 등록</button><button class="btn sm ghost" data-a="tofyi" data-id="${id}">참고로</button><button class="btn sm ghost" data-a="mdone" data-id="${id}">이미 함</button>`;
}
function rowOf(it) {
  if (it.k === 'task' || it.k === 'stale') {
    const t = it.t;
    return `<div class="fi"><div class="fi-l"><span class="pill ${it.k === 'stale' ? 'gray' : 'good'}">${it.k === 'stale' ? '제안 방치' : '업무 DB'}</span></div>
    <div class="fi-m"><b>${esc(t.title)}</b><div class="s2">${esc(t.owner || '담당 없음')} · ${esc(t.cat || '분류 없음')}${t.imp ? ' · 중요도 ' + t.imp : ''}${it.k === 'stale' ? ' · 제안 상태로 ' + t.upd + '일째' : ''}</div></div>
    <div class="fi-d">${it.k === 'stale' ? '<span class="pill warn">승격·폐기 필요</span>' : dueChip(tDue(t))}</div><div class="fi-a">${actions(it)}</div></div>`;
  }
  const m = it.m, c = it.c;
  const meta = `${SRC[m.src]} · ${esc(m.where)} · ${esc(m.frm)} · ${fmt(off(m.date))} ${m.time}`;
  const d = c.label === 'wait' ? `<span class="pill warn">${it.age}일째 무응답</span>` : (c.due != null ? dueChip(c.due) : (c.urgent ? '<span class="pill warn">급함(기한 불명)</span>' : '<span class="s2">기한 불명</span>'));
  return `<div class="fi"><div class="fi-l"><span class="pill ${c.label === 'wait' ? 'gray' : c.label === 'unclear' ? 'warn' : 'crit'}">${LBL[c.label]}</span></div>
  <div class="fi-m"><div>${hl(m.text, c)}</div><div class="s2">${meta}${c.evidence ? ' · 근거: ' + esc(c.evidence.text) : ''}</div></div>
  <div class="fi-d">${d}</div><div class="fi-a">${actions(it)}</div></div>`;
}

/* ---------------- 오늘의 브리핑 ---------------- */
function todayView() {
  const k = kpis(), items = focusItems(), cs = allC().filter((x) => !registered(x.m.id) && !S.mstate[x.m.id]);
  const by = (l) => cs.filter((x) => x.c.label === l);
  const stIcon = {ok:'●', warn:'▲', fail:'✕'}, stCls = {ok:'good', warn:'warn', fail:'crit'};
  let h = `<div class="panel warnbox"><h3>자료 확인 <small style="font-weight:500;color:var(--mut)">자동화가 조용히 멈추지 않도록, 수집 상태를 가장 먼저 알립니다</small></h3>
  ${DATA.sources.map((s) => `<div class="src ${stCls[s.state]}"><span class="dot">${stIcon[s.state]}</span><b>${esc(s.name)}</b><span>${esc(s.detail)}</span></div>`).join('')}</div>`;
  h += `<div class="kpis k6"><div class="kpi"><div class="n">${k.prog}</div><div class="l">진행</div></div><div class="kpi"><div class="n">${k.wait}</div><div class="l">대기</div></div><div class="kpi"><div class="n">${k.prop}</div><div class="l">제안</div></div>
  <div class="kpi crit"><div class="n">${k.over}</div><div class="l">기한 지남</div></div><div class="kpi warn"><div class="n">${k.today}</div><div class="l">오늘 마감</div></div><div class="kpi"><div class="n">${k.issue}</div><div class="l">쟁점</div></div></div>`;
  h += `<div class="panel"><h3>알림 기준 <small style="font-weight:500;color:var(--mut)">기준을 바꾸면 "오늘 먼저 볼 것"이 즉시 바뀝니다</small></h3><div class="sl">
  <label>마감 며칠 전부터 알릴까<span>${S.remind}일 전</span><input type="range" min="0" max="5" value="${S.remind}" data-p="remind"></label>
  <label>답장이 없으면 며칠 뒤 재촉할까<span>${S.waitDays}일</span><input type="range" min="1" max="7" value="${S.waitDays}" data-p="waitDays"></label>
  <label>제안 상태 방치를 며칠부터 경고할까<span>${S.stale}일</span><input type="range" min="3" max="14" value="${S.stale}" data-p="stale"></label></div></div>`;
  h += `<div class="h2">오늘 먼저 볼 것 ${items.length} <small>기한 지남 → 오늘·내일 마감 → 무응답 → 방치된 제안 순</small></div>
  <div class="card nopad">${items.map(rowOf).join('') || '<div class="empty">지금 먼저 볼 항목이 없습니다.</div>'}</div>`;
  const card = (x) => `<div class="bc2"><div>${hl(x.m.text, x.c)}</div><div class="s2">${SRC[x.m.src]} · ${esc(x.m.where)} · ${esc(x.m.frm)} · ${fmt(off(x.m.date))}</div><div class="s2" style="margin-top:4px">${x.c.due != null ? dueChip(x.c.due) : '<span class="s2">기한 불명</span>'}</div><div class="ba">${x.c.label === 'todo' ? `<button class="btn sm" data-a="reg" data-id="${x.m.id}">진행으로 등록</button>` : x.c.label === 'unclear' ? `<button class="btn sm" data-a="reg" data-id="${x.m.id}">내 일로 등록</button>` : x.c.label === 'wait' ? `<button class="btn sm" data-a="nudge" data-id="${x.m.id}">재촉 문구</button>` : ''}<button class="btn sm ghost" data-a="tofyi" data-id="${x.m.id}">${x.c.label === 'fyi' ? '유지' : '참고로'}</button></div></div>`;
  const col = (l, ttl, desc) => `<div class="col"><div class="colh"><b>${ttl}</b> <span class="cnt">${by(l).length}</span></div><div class="s2" style="margin-bottom:8px">${desc}</div>${by(l).slice(0, l === 'fyi' ? 5 : 8).map(card).join('') || '<div class="empty sm">없음</div>'}${l === 'fyi' && by(l).length > 5 ? `<div class="s2" style="text-align:center">외 ${by(l).length - 5}건은 눈에서 치워 둠</div>` : ''}</div>`;
  h += `<div class="h2">요청 분류 보드 <small>메시지에서 규칙으로 뽑은 결과 · 이미 업무로 등록된 건은 제외</small></div><div class="board">${col('todo', '해야 할 일', '나에게 온 요청')}${col('wait', '답장 대기', '내가 보낸 요청')}${col('unclear', '확인 필요', '담당·요청이 불분명')}${col('fyi', '알고만 됨', '행동 불필요')}</div>`;
  const dn = cs.filter((x) => x.c.label === 'done');
  if (dn.length) h += `<div class="h2">완료로 보이는 건 ${dn.length} <small>후속 메시지에 완료 문구가 있어 후보로 올렸습니다 — 사람이 확인해야 확정됩니다</small></div><div class="card nopad">${dn.map((x) => rowOf({k:'msg', id:x.m.id, m:x.m, c:x.c})).join('')}</div>`;
  return h;
}
function bindToday() {
  document.querySelectorAll('input[data-p]').forEach((r) => r.addEventListener('input', () => { S[r.dataset.p] = +r.value; draw(true); }));
  document.querySelectorAll('[data-a]').forEach((b) => b.addEventListener('click', () => act(b.dataset.a, b.dataset.id)));
}
function newTask(m, c, status) {
  const t = {id:'T' + (S.tid++), title:m.text.replace(/^@나\s*/, '').replace(/^\[[^\]]+\]\s*/, '').slice(0, 44), status, cat:'', kind:'실행', owner:'나', imp:c.urgent ? '긴급' : null,
    due:c.due != null ? isoOf(c.due) : null, prog:null, issue:false, upd:0, next:'', src:m.id};
  S.tasks.unshift(t); return t;
}
function act(a, id) {
  const tk = S.tasks.find((t) => String(t.id) === String(id)), m = MSG.find((x) => x.id === id);
  if (a === 'tdone') { tk.status = '완료'; tk.upd = 0; toast('완료 처리 · 기한 지남 숫자에서 빠집니다'); }
  else if (a === 'tpush') { tk.due = isoOf(tDue(tk) + 1 < 1 ? 1 : tDue(tk) + 1); toast('기한을 미뤘습니다'); }
  else if (a === 'tpromote') { tk.status = '진행'; tk.upd = 0; toast('진행으로 승격했습니다'); }
  else if (a === 'tdrop') { S.tasks.splice(S.tasks.indexOf(tk), 1); toast('폐기했습니다'); }
  else if (a === 'reg') { const t = newTask(m, classify(m), '진행'); S.mstate[id] = 'reg'; toast('업무 관리에 등록했습니다 · ' + t.title); }
  else if (a === 'tofyi') { S.mstate[id] = 'fyi'; toast('참고로 옮겼습니다'); }
  else if (a === 'got') { S.mstate[id] = 'got'; toast('답을 받은 것으로 처리했습니다'); }
  else if (a === 'mdone') { S.mstate[id] = 'done'; toast('완료로 확정했습니다'); }
  else if (a === 'notyet') { S.mstate[id] = 'notyet'; toast('아직 진행 중으로 남깁니다 · 완료 판정은 후보일 뿐입니다'); }
  else if (a === 'nudge') {
    const c = classify(m), to = m.text.match(/^@(\S+(?: \S+)?)/);
    const txt = `안녕하세요. ${fmt(off(m.date))}에 요청드린 건(${m.text.replace(/^@\S+\s*/, '').slice(0, 30)}…) 진행 상황이 궁금해 다시 연락드립니다.\n가능한 일정을 알려주시면 일정에 반영하겠습니다. 감사합니다.`;
    openModal(`<h3>재촉 문구</h3><div class="s2">${esc(m.where)} · ${fmt(off(m.date))} 요청 · ${-off(m.date)}일째 무응답</div><pre id="nt">${esc(txt)}</pre><div class="row"><button class="btn ghost" onclick="closeModal()">닫기</button><button class="btn dk" id="nt-ok">복사하고 닫기</button></div>`);
    $('nt-ok').onclick = () => { copy($('nt').textContent); closeModal(); toast('복사했습니다'); };
    return;
  }
  draw(true);
}

/* ---------------- 업무 관리(DB) ---------------- */
const VIEWS = [['owner','담당별'],['cat','분류별'],['kind','종류별'],['notice','공지·교육'],['issue','쟁점'],['prop','제안 확인'],['done','완료 목록'],['all','전체']];
function hygiene() {
  const open = S.tasks.filter((t) => t.status !== '완료');
  return [
    {k:'h-owner', n:'담당 없음', items:open.filter((t) => !t.owner), tip:'담당이 없으면 아무도 안 합니다'},
    {k:'h-due', n:'긴급·중요인데 기한 없음', items:open.filter((t) => (t.imp === '긴급' || t.imp === '중요') && !t.due), tip:'기한이 없으면 우선순위가 말뿐입니다'},
    {k:'h-stale', n:'제안 ' + S.stale + '일+ 방치', items:S.tasks.filter((t) => t.status === '제안' && t.upd >= S.stale), tip:'승격하거나 폐기해야 합니다'},
    {k:'h-over', n:'기한 지남', items:open.filter((t) => t.due && tDue(t) < 0), tip:'재설정하거나 완료 처리'},
    {k:'h-prog', n:'진행인데 진행률 없음', items:S.tasks.filter((t) => t.status === '진행' && t.prog == null), tip:'낮은 우선순위의 정리 대상'},
  ];
}
function taskRow(t) {
  const d = tDue(t), over = t.due && d < 0 && t.status !== '완료';
  const pr = t.prog == null ? '<span class="s2">-</span>' : `<span class="pb"><i style="width:${t.prog}%"></i></span> <span class="s2">${t.prog}%</span>`;
  const sel = (arr, v, f) => `<select data-f="${f}" data-id="${t.id}">${arr.map((o) => `<option ${o === v ? 'selected' : ''} value="${o}">${o || '(없음)'}</option>`).join('')}</select>`;
  return `<tr class="${over ? 'r' : ''}"><td style="min-width:240px"><b>${esc(t.title)}</b>${t.src ? ` <span class="pill gray" data-tip="메시지에서 등록된 업무">메시지 ${t.src}</span>` : ''}${t.issue ? ' <span class="pill warn">쟁점</span>' : ''}</td>
  <td>${sel(['제안','진행','대기','완료'], t.status, 'status')}</td><td>${pr}</td><td class="s2">${esc(t.cat || '-')}</td><td>${esc(t.kind)}</td>
  <td>${t.imp ? `<span class="pill ${t.imp === '긴급' ? 'crit' : t.imp === '중요' ? 'warn' : 'gray'}">${t.imp}</span>` : '<span class="s2">-</span>'}</td>
  <td><input type="date" value="${t.due || ''}" data-f="due" data-id="${t.id}"></td><td>${over ? `<span class="pill crit">${-d}일</span>` : '<span class="s2">-</span>'}</td>
  <td>${sel(['', '나', '최 파트장', '공통'], t.owner, 'owner')}</td><td class="s2">${esc(t.next || '')}</td></tr>`;
}
function dbView() {
  const H = hygiene(), hv = S.view.startsWith('h-');
  const total = H.slice(0, 4).reduce((a, x) => a + x.items.length, 0);
  let list = S.tasks.slice(), groups = null;
  if (hv) list = H.find((x) => x.k === S.view).items;
  else if (S.view === 'owner') groups = ['', '나', '최 파트장', '공통'].map((o) => [o || '담당 없음', list.filter((t) => t.owner === o && t.status !== '완료')]);
  else if (S.view === 'cat') { const cs = [...new Set(list.filter((t) => t.status !== '완료').map((t) => (t.cat || '분류 없음').split('›')[0]))]; groups = cs.map((c) => [c, list.filter((t) => t.status !== '완료' && (t.cat || '분류 없음').split('›')[0] === c)]); }
  else if (S.view === 'kind') groups = ['실행', '개선', '공지·교육', '기록'].map((k) => [k, list.filter((t) => t.kind === k && t.status !== '완료')]);
  else if (S.view === 'notice') list = list.filter((t) => t.kind === '공지·교육' && t.status !== '완료');
  else if (S.view === 'issue') list = list.filter((t) => t.issue && t.status !== '완료');
  else if (S.view === 'prop') list = list.filter((t) => t.status === '제안').sort((a, b) => b.upd - a.upd);
  else if (S.view === 'done') list = list.filter((t) => t.status === '완료');
  const head = '<thead><tr><th>업무</th><th>상태</th><th>진행률</th><th>분류</th><th>종류</th><th>중요도</th><th>기한</th><th>기한 지남</th><th>담당</th><th>다음 할 일</th></tr></thead>';
  let body = '';
  if (groups) groups.forEach(([g, rs]) => { if (rs.length) body += `<tr class="gh"><td colspan="10">${esc(g)} ${rs.length}</td></tr>` + rs.map(taskRow).join(''); });
  else body = list.map(taskRow).join('') || '<tr><td colspan="10" class="empty">해당하는 업무가 없습니다. 👍</td></tr>';
  return `<div class="panel"><h3>업무 위생 점검 <small style="font-weight:500;color:var(--mut)">고쳐야 할 것 ${total}건 · 칩을 누르면 해당 업무만 보입니다. 표에서 담당·기한·상태를 고치면 숫자가 줄어듭니다</small></h3>
  <div class="chips">${H.map((x) => `<button class="chip ${S.view === x.k ? 'on' : (x.items.length && x.k !== 'h-prog' ? 'red' : '')}" data-v="${x.k}" data-tip="${esc(x.tip)}">${x.n}<b>${x.items.length}</b></button>`).join('')}</div></div>
  <div class="chips" style="margin:10px 0">${VIEWS.map(([k, n]) => `<button class="chip ${S.view === k ? 'on' : ''}" data-v="${k}">${n}</button>`).join('')}</div>
  <div class="tw"><table>${head}<tbody>${body}</tbody></table></div>
  <div class="cap">메시지에서 뽑은 요청은 먼저 "제안" 상태로 들어오고, 사람이 진행으로 올릴 때 확정됩니다. 기한 지남은 기한과 오늘의 차이로 계산됩니다.</div>`;
}
function bindDb() {
  document.querySelectorAll('[data-v]').forEach((b) => b.addEventListener('click', () => { S.view = b.dataset.v; draw(true); }));
  document.querySelectorAll('[data-f]').forEach((el) => el.addEventListener('change', () => {
    const t = S.tasks.find((x) => String(x.id) === el.dataset.id); const f = el.dataset.f;
    if (f === 'status') { t.status = el.value; t.upd = 0; } else if (f === 'due') t.due = el.value || null; else if (f === 'owner') t.owner = el.value;
    draw(true);
  }));
}

/* ---------------- 요청 수집(분류기) ---------------- */
const SAMPLES = [
  ['@나 모레까지 11월 정산 자료 정리해서 회신 부탁드립니다.', 'slack', 'me', '정 매니저'],
  ['공유드립니다. 다음 주 월요일부터 배차 시간이 변경됩니다. 참고 부탁드립니다.', 'slack', 'team', '최 파트장'],
  ['@here 팔레트 재고 확인해 주실 분 오후 중으로 부탁드립니다.', 'slack', 'team', '최 파트장'],
  ['10/30까지 견적서 검토해 주시면 감사하겠습니다.', 'mail', 'me', '윤 구매'],
  ['누가 이거 한번 봐주실 수 있나요?', 'slack', 'team', '한 CX'],
];
function inboxView() {
  const cs = allC().filter((x) => S.ft === 'all' || x.c.label === S.ft).filter((x) => !S.q || x.m.text.includes(S.q));
  const cnt = (l) => allC().filter((x) => x.c.label === l).length;
  return `<div class="two"><div class="card"><div class="h2" style="margin-top:0">메시지 붙여넣기 분류기 <small>규칙 기반 데모 · 실무 버전은 AI 분류</small></div>
  <textarea id="pt" rows="4" placeholder="메시지를 붙여넣어 보세요. 예) @나 내일까지 견적 정리 부탁드립니다.">${esc(SAMPLES[S.sample][0])}</textarea>
  <div class="ib" style="display:flex;gap:10px;flex-wrap:wrap;align-items:center"><label>보낸 곳 <select id="ps"><option value="slack">Slack</option><option value="mail">메일</option></select></label>
  <label>나를 지목 <select id="pm"><option value="me">나에게</option><option value="team">전체/불특정</option><option value="own">내가 보냄</option></select></label>
  <label>보낸 날 <select id="pd"><option value="0">오늘(월)</option><option value="-3">3일 전(금)</option><option value="-4">4일 전(목)</option></select></label>
  <button class="btn sm dk" id="pgo">분류</button></div>
  <div class="chips" style="margin:6px 0">${SAMPLES.map((s, i) => `<button class="chip ${S.sample === i ? 'on' : ''}" data-s="${i}">예시 ${i + 1}</button>`).join('')}</div>
  <div id="pres"></div></div>
  <div class="card"><div class="h2" style="margin-top:0">분류 규칙 <small>어떻게 판단하는지 그대로 공개합니다</small></div>
  <div class="rules"><div><b>알고만 됨</b> "참고 부탁" "불필요" 같은 문구가 있으면 요청 문구보다 먼저 적용</div><div><b>해야 할 일</b> 요청 문구("부탁·주세요·회신…") + 나를 지목</div><div><b>답장 대기</b> 요청 문구 + 내가 보낸 메시지</div><div><b>확인 필요</b> 요청 문구는 있는데 나를 지목하지 않음(담당 불명)</div><div><b>완료 후보</b> 같은 스레드의 뒤 메시지에 "처리했습니다·올렸습니다" 등이 있음</div><div><b>마감 추출</b> 오늘·내일·요일·M/D·월말 등. 보낸 날짜를 기준으로 계산("내일까지"가 5일 전 메시지면 이미 지남)</div></div></div></div>
  <div class="h2">수집된 메시지 ${MSG.length} <small>스레드 안의 답글까지 포함</small></div>
  <div class="chips" style="margin-bottom:8px"><button class="chip ${S.ft === 'all' ? 'on' : ''}" data-ft="all">전체<b>${MSG.length}</b></button>${Object.keys(LBL).map((l) => `<button class="chip ${S.ft === l ? 'on' : ''}" data-ft="${l}">${LBL[l]}<b>${cnt(l)}</b></button>`).join('')}<input class="search" id="mq" placeholder="문구 검색" value="${esc(S.q)}"></div>
  <div class="tw"><table><thead><tr><th>시각</th><th>출처</th><th>보낸 사람</th><th>메시지</th><th>분류</th><th>추출 마감</th><th>업무</th></tr></thead><tbody>${cs.map(({m, c}) => `<tr><td class="s2" style="white-space:nowrap">${fmt(off(m.date))}<br>${m.time}</td><td>${SRC[m.src]}<div class="s2">${esc(m.where)}</div></td><td>${esc(m.frm)}</td><td style="min-width:300px">${hl(m.text, c)}${c.evidence ? `<div class="s2">완료 근거: ${esc(c.evidence.text)}</div>` : ''}</td><td><span class="pill ${c.label === 'todo' ? 'crit' : c.label === 'fyi' ? 'gray' : c.label === 'done' ? 'good' : 'warn'}">${LBL[c.label]}</span></td><td>${c.due != null ? fmt(c.due) + `<div class="s2">${esc(c.how)}</div>` : '<span class="s2">-</span>'}</td><td>${registered(m.id) ? `<span class="pill good">${taskOfMsg(m.id).id} 등록됨</span>` : (c.label === 'todo' || c.label === 'unclear') ? `<button class="btn sm" data-a="reg" data-id="${m.id}">제안으로 등록</button>` : ''}</td></tr>`).join('')}</tbody></table></div>`;
}
function runPaste() {
  const text = $('pt').value.trim(); if (!text) return;
  const who = $('pm').value, ref = +$('pd').value;
  const m = {id:'x', text, date:isoOf(ref), time:'09:05', src:$('ps').value, where:'붙여넣기', frm:who === 'own' ? '나' : '상대', mention:who === 'own' ? 'none' : who, thread:null};
  const c = classify(m), reasons = [];
  if (c.cues.length) reasons.push('찾은 문구: ' + c.cues.map((x) => '"' + esc(x) + '"').join(', '));
  reasons.push(c.label === 'todo' ? '요청 문구가 있고 나를 지목했으므로 <b>내가 해야 할 일</b>' : c.label === 'wait' ? '내가 보낸 요청이므로 <b>답장 대기</b>' : c.label === 'unclear' ? '요청 문구는 있지만 나를 지목하지 않아 <b>담당 불명 → 확인 필요</b>' : '요청 문구가 없거나 "참고·불필요" 문구가 우선해 <b>행동이 필요 없는 건</b>');
  $('pres').innerHTML = `<div class="pr"><div class="big"><span class="pill ${c.label === 'todo' ? 'crit' : c.label === 'fyi' ? 'gray' : 'warn'}">${LBL[c.label]}</span> ${c.due != null ? '마감 ' + fmt(c.due) + ` <span class="s2">("${esc(c.how)}")</span>` : (c.urgent ? '<span class="pill warn">급함 · 기한 불명</span>' : '<span class="s2">추출된 마감 없음</span>')}</div><div style="margin:8px 0;line-height:1.7">${hl(text, c)}</div><div class="s2">${reasons.join('<br>')}</div><div class="s2" style="margin-top:6px">⚠ 규칙 기반이라 완곡한 표현("~해 주시면 좋겠습니다")이나 질문형은 놓칠 수 있습니다. 그래서 사람이 확인하는 단계가 있습니다.</div></div>`;
}
function bindInbox() {
  document.querySelectorAll('[data-s]').forEach((b) => b.addEventListener('click', () => { S.sample = +b.dataset.s; const s = SAMPLES[S.sample]; draw(true); $('pt').value = s[0]; $('ps').value = s[1]; $('pm').value = s[2]; runPaste(); }));
  document.querySelectorAll('[data-ft]').forEach((b) => b.addEventListener('click', () => { S.ft = b.dataset.ft; draw(true); }));
  $('pgo').addEventListener('click', runPaste);
  const q = $('mq'); q.addEventListener('input', () => { S.q = q.value; const p = q.selectionStart; draw(true); const n = $('mq'); n.focus(); n.setSelectionRange(p, p); });
  document.querySelectorAll('[data-a]').forEach((b) => b.addEventListener('click', () => act(b.dataset.a, b.dataset.id)));
  runPaste();
}

/* ---------------- 분류 정확도 ---------------- */
function accView() {
  const rows = MSG.map((m) => ({m, c:classify(m)}));
  const ok = rows.filter((r) => r.c.label === r.m.truth.label).length;
  const dueRows = rows.filter((r) => r.m.truth.label !== 'fyi');
  const dueOk = dueRows.filter((r) => (r.c.due == null ? null : isoOf(r.c.due)) === r.m.truth.due).length;
  const labs = ['todo', 'wait', 'unclear', 'done', 'fyi'];
  const conf = labs.map((t) => labs.map((p) => rows.filter((r) => r.m.truth.label === t && r.c.label === p).length));
  const wrong = rows.filter((r) => r.c.label !== r.m.truth.label);
  const dwrong = dueRows.filter((r) => (r.c.due == null ? null : isoOf(r.c.due)) !== r.m.truth.due);
  let h = `<div class="note"><b>정답을 사람이 붙여 둔 가상 메시지 ${MSG.length}건</b>으로 규칙의 성적을 매깁니다. 틀린 건은 숨기지 않고 원인과 함께 보여줍니다.</div>
  <div class="kpis" style="grid-template-columns:repeat(3,1fr)"><div class="kpi good"><div class="n">${(ok / rows.length * 100).toFixed(0)}%</div><div class="l">분류 정확도</div><div class="d">${ok}/${rows.length}건 일치</div></div>
  <div class="kpi"><div class="n">${(dueOk / dueRows.length * 100).toFixed(0)}%</div><div class="l">마감 추출 정확도</div><div class="d">${dueOk}/${dueRows.length}건 (행동이 필요한 메시지 기준)</div></div>
  <div class="kpi crit"><div class="n">${wrong.length + dwrong.length}</div><div class="l">틀린 판정</div><div class="d">분류 ${wrong.length}건 · 마감 ${dwrong.length}건</div></div></div>`;
  h += `<div class="h2">혼동표 <small>행 = 정답, 열 = 규칙의 판정 · 대각선 밖이 오류</small></div><div class="tw"><table class="mx"><thead><tr><th>정답＼판정</th>${labs.map((l) => `<th>${LBL[l]}</th>`).join('')}</tr></thead><tbody>${labs.map((t, i) => `<tr><td><b>${LBL[t]}</b></td>${conf[i].map((n, j) => `<td class="${i === j ? '' : (n ? 'bad' : 'z')}" style="${i === j && n ? 'font-weight:800' : ''}">${n || '·'}</td>`).join('')}</tr>`).join('')}</tbody></table></div>`;
  h += `<div class="h2">틀린 판정과 원인 <small>"규칙에 추가"를 누르면 그 문구가 규칙에 들어가고 정확도가 다시 계산됩니다</small></div><div class="tw"><table><thead><tr><th>메시지</th><th>정답</th><th>규칙의 판정</th><th>원인</th><th></th></tr></thead><tbody>
  ${wrong.map(({m, c}) => { const f = DATA.fixes[m.id]; return `<tr class="r"><td style="min-width:280px">${esc(m.text)}</td><td><span class="pill good">${LBL[m.truth.label]}</span></td><td><span class="pill crit">${LBL[c.label]}</span></td><td class="s2">${esc(f ? f.why : '')}</td><td>${f ? `<button class="btn sm" data-fix="${m.id}">"${esc(f.phrase)}" 규칙에 추가</button>` : ''}</td></tr>`; }).join('')}
  ${dwrong.map(({m, c}) => { const f = DATA.duefix[m.id]; return `<tr class="r"><td style="min-width:280px">${esc(m.text)}</td><td>마감 ${m.truth.due ? fmt(off(m.truth.due)) : '-'}</td><td><span class="pill crit">${c.due != null ? fmt(c.due) : '마감 없음'}</span></td><td class="s2">${esc(f ? f.why : '')}</td><td>${f ? `<button class="btn sm" data-dfix="${m.id}">"${esc(f.phrase)}" 마감 표현 추가</button>` : ''}</td></tr>`; }).join('')}
  ${wrong.length + dwrong.length ? '' : '<tr><td colspan="5" class="empty">틀린 판정이 없습니다.</td></tr>'}</tbody></table></div>`;
  if (S.custom.length || S.dueRules.length) h += `<div class="panel warnbox" style="margin-top:14px"><b>⚠ 추가한 규칙 ${S.custom.length + S.dueRules.length}개.</b> 위 정확도는 이 ${MSG.length}건에 맞춰 고친 값이라 실제 성능보다 높게 나옵니다. 새로 모은 메시지로 따로 검증해야 하고, 규칙이 늘수록 서로 충돌하는지도 확인해야 합니다. <button class="btn sm ghost" id="rstc" style="margin-left:8px">추가한 규칙 지우기</button></div>`;
  return h;
}
function bindAcc() {
  document.querySelectorAll('[data-fix]').forEach((b) => b.addEventListener('click', () => { const f = DATA.fixes[b.dataset.fix]; S.custom.push({phrase:f.phrase, label:f.label}); draw(true); toast('규칙을 추가했습니다'); }));
  document.querySelectorAll('[data-dfix]').forEach((b) => b.addEventListener('click', () => { const f = DATA.duefix[b.dataset.dfix]; S.dueRules.push({phrase:f.phrase, rel:f.rel}); draw(true); toast('마감 표현을 추가했습니다'); }));
  const r = $('rstc'); if (r) r.addEventListener('click', () => { S.custom = []; S.dueRules = []; draw(true); });
}

/* ---------------- 구조 ---------------- */
function archView() {
  const box = (x, y, w, t, s, c) => `<g><rect x="${x}" y="${y}" width="${w}" height="64" rx="10" fill="${c || '#fff'}" stroke="#d9dce1"/><text x="${x + w / 2}" y="${y + 27}" text-anchor="middle" font-size="13" font-weight="800" fill="#1b1d21">${t}</text><text x="${x + w / 2}" y="${y + 46}" text-anchor="middle" font-size="11" fill="#6b717a">${s}</text></g>`;
  const ar = (x) => `<path d="M${x} 42 h22" stroke="#8a909a" stroke-width="1.6" marker-end="url(#ah)"/>`;
  const svg = `<svg class="svgc" viewBox="0 0 1100 150" role="img" aria-label="아침 업무 브리핑 흐름도"><defs><marker id="ah" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8 z" fill="#8a909a"/></marker></defs>
  <g transform="translate(0,20)">${box(0, 0, 150, '소스', 'Slack · 메일 · 회의록')}${ar(150)}${box(172, 0, 150, '수집', '채널·라벨 목록 + 갱신 확인', '#fff4de')}${ar(322)}${box(344, 0, 150, '분류', '요청 / 참고 / 마감 / 담당')}${ar(494)}${box(516, 0, 150, '제안 등록', '상태 = 제안 (확정 아님)', '#e8f0fe')}${ar(666)}${box(688, 0, 150, '사람 확인', '진행으로 승격 · 폐기')}${ar(838)}${box(860, 0, 240, '업무 관리 DB → 아침 브리핑', '기한 지남 · 위생 점검 · 익일 이월', '#e6f6e6')}</g></svg>`;
  return `<div class="card">${svg}<div class="cap">데모의 화면은 위 흐름의 결과입니다. 실제 연동(Slack·메일·노션)은 공개 사이트에 올릴 수 없어 가상 메시지로 같은 로직을 시연합니다.</div></div>
  <div class="three" style="margin-top:14px"><div class="card pr2"><b>AI는 제안, 사람이 확정</b><p>메시지에서 뽑은 요청은 먼저 "제안"으로만 들어옵니다. 사람이 진행으로 올려야 업무가 됩니다. 완료 판정도 "후보"와 근거 메시지까지만 보여줍니다.</p></div>
  <div class="card pr2"><b>자동화가 멈추면 먼저 알린다</b><p>수집이 실패했거나 갱신이 오래된 소스를 화면 맨 위에 경고합니다. 조용히 멈춘 자동화는 "요청이 없는 것"처럼 보여 가장 위험합니다.</p></div>
  <div class="card pr2"><b>기록은 기존 도구에, 프로그램은 점검을</b><p>팀이 이미 쓰는 업무 DB를 대체하지 않고, 그 위에서 수집·분류·위생 점검(담당·기한 누락, 제안 방치)을 맡습니다.</p></div></div>
  <div class="h2">한계와 다음 개선</div><div class="card" style="color:var(--ink2);line-height:1.9"><ul style="margin:0;padding-left:18px"><li>규칙 기반은 완곡한 표현·질문형 요청에 약합니다 → 실무 버전은 AI 분류 + 정확도 측정을 병행</li><li>"완료로 보임"은 추정입니다 → 근거 메시지를 같이 보여주고 사람이 확정</li><li>이 화면의 수치는 모두 가상이며 실제 업무 효과를 뜻하지 않습니다</li></ul></div>`;
}

/* ---------------- 브리핑 문구 ---------------- */
$('b-copy').addEventListener('click', () => {
  const k = kpis(), items = focusItems();
  const line = (it) => it.k === 'msg' ? `- [${LBL[it.c.label]}] ${it.m.text.replace(/^@나\s*/, '').slice(0, 40)}${it.c.due != null ? ' (' + fmt(it.c.due) + ')' : ''}` : `- [업무] ${it.t.title}${it.t.due ? ' (' + fmt(tDue(it.t)) + ')' : ''}`;
  copy(`[아침 업무 브리핑 · 10/26(월)]\n진행 ${k.prog} · 대기 ${k.wait} · 제안 ${k.prop} · 기한 지남 ${k.over} · 오늘 마감 ${k.today}\n\n오늘 먼저 볼 것 ${items.length}건\n${items.slice(0, 8).map(line).join('\n')}`);
  toast('브리핑 문구를 복사했습니다');
});

function draw(keep) {
  const y = window.scrollY; drawTabs();
  $('view').innerHTML = {today:todayView, db:dbView, inbox:inboxView, acc:accView, arch:archView}[S.tab]();
  if (S.tab === 'today') bindToday(); if (S.tab === 'db') bindDb(); if (S.tab === 'inbox') bindInbox(); if (S.tab === 'acc') bindAcc();
  if (keep) window.scrollTo(0, y);
}
draw();
</script>

</body></html>"""

components.html(HTML, height=900, scrolling=True)
