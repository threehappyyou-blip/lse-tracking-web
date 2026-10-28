import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="BO 업무 포털 (데모)", page_icon="🗂️", layout="wide")

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

# 모든 회사명·이름·이메일·금액·규정 수치는 가상입니다. (실제 업무용은 같은 구조로 교체)
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

.pill.info{background:#e8f0fe;color:#2f6fd6}
.brand{display:flex;align-items:center;gap:9px}
.brand i{display:grid;place-items:center;width:28px;height:28px;border-radius:8px;background:#1b1d21;color:#fff;font-style:normal;font-weight:800}
.top .who{display:flex;align-items:center;gap:8px;font-size:12px;color:var(--ink2)}
.cards4{display:grid;grid-template-columns:repeat(4,1fr);gap:12px}
.tcard{background:#fff;border:1px solid var(--line);border-radius:12px;padding:14px 16px;display:flex;flex-direction:column;gap:6px}
.tcard h4{margin:0;font-size:15px;font-weight:800}
.tcard .n{font-size:26px;font-weight:800;letter-spacing:-.8px}
.tcard .n small{font-size:12px;color:var(--mut);font-weight:600;margin-left:4px}
.tcard p{margin:0;color:var(--ink2);font-size:12px;line-height:1.55;flex:1}
.fgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(190px,1fr));gap:10px 14px}
.fgrid label{display:block;font-size:11.5px;color:var(--ink2);font-weight:700}
.fgrid input,.fgrid select{width:100%;margin-top:4px;font:inherit;font-size:13px;border:1px solid var(--line);border-radius:7px;padding:7px 8px;background:#fff}
.fgrid .full{grid-column:1/-1}
input[type=text],input[type=number],input[type=time],input[type=email]{font:inherit;font-size:12.5px;border:1px solid var(--line);border-radius:6px;padding:5px 7px;background:#fff;color:var(--ink)}
.chk{display:flex;align-items:center;gap:7px;font-size:12.5px;color:var(--ink2)}
.sub2{display:flex;gap:6px;margin:0 0 12px;flex-wrap:wrap}
.stp{display:flex;align-items:center;gap:0;flex-wrap:wrap}
.stp span{display:inline-flex;align-items:center;font-size:11px;font-weight:700;padding:3px 8px;border-radius:12px;background:#eceef1;color:var(--mut);white-space:nowrap}
.stp span.d{background:var(--goodbg);color:var(--good)}
.stp span.c{background:var(--ink);color:#fff}
.stp b{width:10px;height:1px;background:#c7cbd1;display:inline-block}
.chk-list{display:grid;gap:6px;margin-top:8px}
.chk-list div{display:flex;gap:8px;align-items:flex-start;font-size:12.5px;line-height:1.5;color:var(--ink2)}
.sum{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin:12px 0}
.sum div{background:#f6f7f9;border-radius:10px;padding:10px 12px}
.sum b{display:block;font-size:19px;letter-spacing:-.5px;margin-top:2px}
.rt{width:100%}.rt td,.rt th{padding:7px 8px}
.rt input[type=number]{width:98px}.rt input[type=date]{width:128px}
.pbar{height:8px;background:#e6e8ec;border-radius:5px;overflow:hidden;margin-top:6px}.pbar i{display:block;height:100%;background:var(--s1)}
.lgrid{display:grid;grid-template-columns:200px 1fr;gap:16px}
.lmenu{display:grid;gap:6px;align-content:start}
.lmenu button{display:flex;justify-content:space-between;text-align:left;border:1px solid var(--line);background:#fff;border-radius:8px;padding:9px 11px;font-weight:700;color:var(--ink2)}
.lmenu button.on{background:var(--ink);border-color:var(--ink);color:#fff}
.role{font:inherit;font-size:12.5px;border:1px solid var(--line);border-radius:7px;padding:5px 8px;background:#fff;font-weight:700}
.tl{border-left:3px solid var(--line);padding-left:12px;margin:8px 0;font-size:12.5px;color:var(--ink2);line-height:1.6}
@media(max-width:860px){.cards4{grid-template-columns:1fr 1fr}.sum{grid-template-columns:1fr 1fr}.lgrid{grid-template-columns:1fr}.rt{min-width:860px}}
</style></head>
<body>
<div class="wrap">
  <div class="top">
    <div class="brand"><i>D</i><div><h1 style="font-size:19px">BO 업무 포털</h1></div></div><span class="ver">Back-office Portal · v1.0 데모</span>
    <div class="sp"></div>
    <div class="who">보는 사람 <select class="role" id="role"></select></div>
  </div>
  <div class="demo"><b>DEMO</b> 회사명·이름·이메일·금액·규정 수치는 모두 가상입니다. 버튼 동작은 이 화면에서만 반영되고 저장·전송되지 않습니다.</div>
  <div class="tabs" role="tablist" id="tabs"></div>
  <div id="view"></div>
</div>
<div class="ovl" id="ovl"><div class="mdl" id="mdl"></div></div>
<div class="toast" id="toast"></div>
<div class="tip" id="tip"></div>
<script>
const DATA = {"tx": [{"id": "TX001", "date": "2026-08-05", "dir": "out", "party": "한빛로지스(주)", "kind": "dom", "cat": "taxable", "item": "물류 대행 수수료", "supply": 980000, "vat": 98000, "total": 1078000, "bn": "000-11-20001", "doc": "DOC-31001", "issuedDate": "2026-08-08", "evi": true}, {"id": "TX002", "date": "2026-08-12", "dir": "in", "party": "가온특송(주)", "kind": "dom", "cat": "taxable", "item": "특송 운임 청구", "supply": 3080000, "vat": 308000, "total": 3388000, "bn": "000-11-20002", "doc": "DOC-31002", "issuedDate": "2026-08-14", "evi": true}, {"id": "TX003", "date": "2026-08-19", "dir": "out", "party": "별빛상사(주)", "kind": "dom", "cat": "taxable", "item": "포장 작업 수수료", "supply": 1200000, "vat": 120000, "total": 1320000, "bn": "000-11-20009", "doc": "DOC-31003", "issuedDate": "2026-08-23", "evi": true}, {"id": "TX004", "date": "2026-08-26", "dir": "in", "party": "미래오피스임대(주)", "kind": "dom", "cat": "taxable", "item": "사무실 임차료", "supply": 5730000, "vat": 573000, "total": 6303000, "bn": "000-11-20005", "doc": "DOC-31004", "issuedDate": "2026-08-27", "evi": true}, {"id": "TX005", "date": "2026-09-01", "dir": "out", "party": "한빛로지스(주)", "kind": "dom", "cat": "taxable", "item": "물류 대행 수수료", "supply": 3250000, "vat": 325000, "total": 3575000, "bn": "000-11-20001", "doc": "DOC-31005", "issuedDate": "2026-09-06", "evi": true}, {"id": "TX006", "date": "2026-09-02", "dir": "in", "party": "가온특송(주)", "kind": "dom", "cat": "taxable", "item": "특송 운임 청구", "supply": 3530000, "vat": 353000, "total": 3883000, "bn": "000-11-20002", "doc": "DOC-31006", "issuedDate": "2026-09-06", "evi": true}, {"id": "TX007", "date": "2026-09-03", "dir": "out", "party": "온누리유통(주)", "kind": "dom", "cat": "taxable", "item": "보관·재고 관리료", "supply": 4540000, "vat": 454000, "total": 4994000, "bn": "000-11-20008", "doc": "DOC-31007", "issuedDate": "2026-09-05", "evi": true}, {"id": "TX008", "date": "2026-09-04", "dir": "in", "party": "누리포장(주)", "kind": "dom", "cat": "taxable", "item": "포장 자재 구매", "supply": 2290000, "vat": 229000, "total": 2519000, "bn": "000-11-20003", "doc": "DOC-31008", "issuedDate": "2026-09-06", "evi": true}, {"id": "TX009", "date": "2026-09-07", "dir": "in", "party": "미래오피스임대(주)", "kind": "dom", "cat": "taxable", "item": "사무실 임차료", "supply": 2040000, "vat": 204000, "total": 2244000, "bn": "000-11-20005", "doc": "DOC-31009", "issuedDate": "2026-09-09", "evi": true}, {"id": "TX010", "date": "2026-09-08", "dir": "in", "party": "새봄광고(주)", "kind": "dom", "cat": "taxable", "item": "온라인 광고비", "supply": 1790000, "vat": 179000, "total": 1969000, "bn": "000-11-20006", "doc": "DOC-31010", "issuedDate": "2026-09-13", "evi": true}, {"id": "TX011", "date": "2026-09-09", "dir": "out", "party": "다온아이티(주)", "kind": "dom", "cat": "taxable", "item": "업무 자동화 컨설팅", "supply": 3070000, "vat": 307000, "total": 3377000, "bn": "000-11-20004", "doc": "DOC-31011", "issuedDate": "2026-09-11", "evi": true}, {"id": "TX012", "date": "2026-09-10", "dir": "out", "party": "데모 재팬 K.K.", "kind": "ovs", "cat": "zero", "item": "법인 간 지원 용역비", "supply": 3400000, "vat": 0, "total": 3400000, "bn": null, "doc": null, "issuedDate": null, "evi": true}, {"id": "TX013", "date": "2026-09-11", "dir": "in", "party": "한빛로지스(주)", "kind": "dom", "cat": "taxable", "item": "국내 배송 대행비", "supply": 1110000, "vat": 111000, "total": 1221000, "bn": "000-11-20001", "doc": "DOC-31013", "issuedDate": "2026-09-12", "evi": true}, {"id": "TX014", "date": "2026-09-14", "dir": "out", "party": "별빛상사(주)", "kind": "dom", "cat": "taxable", "item": "포장 작업 수수료", "supply": 1180000, "vat": 118000, "total": 1298000, "bn": "000-11-20009", "doc": "DOC-31014", "issuedDate": "2026-09-18", "evi": true}, {"id": "TX015", "date": "2026-09-15", "dir": "in", "party": "다온아이티(주)", "kind": "dom", "cat": "taxable", "item": "시스템 유지보수", "supply": 3900000, "vat": 390000, "total": 4290000, "bn": "000-11-20004", "doc": "DOC-31015", "issuedDate": "2026-09-18", "evi": true}, {"id": "TX016", "date": "2026-09-16", "dir": "out", "party": "데모 USA Inc.", "kind": "ovs", "cat": "zero", "item": "법인 간 지원 용역비", "supply": 2610000, "vat": 0, "total": 2610000, "bn": null, "doc": null, "issuedDate": null, "evi": false}, {"id": "TX017", "date": "2026-09-17", "dir": "out", "party": "청명교육원", "kind": "exempt", "cat": "exempt", "item": "사내 교육 서비스", "supply": 3550000, "vat": 0, "total": 3550000, "bn": "000-11-20007", "doc": "DOC-31017", "issuedDate": "2026-09-20", "evi": true}, {"id": "TX018", "date": "2026-09-18", "dir": "out", "party": "개인 고객(비사업자)", "kind": "ind", "cat": "taxable", "item": "개인 고객 서비스 수수료", "supply": 830000, "vat": 83000, "total": 913000, "bn": null, "doc": null, "issuedDate": null, "evi": true}, {"id": "TX019", "date": "2026-09-21", "dir": "out", "party": "한빛로지스(주)", "kind": "dom", "cat": "taxable", "item": "물류 대행 수수료", "supply": 4810000, "vat": 481000, "total": 5291000, "bn": "000-11-20001", "doc": "DOC-31019", "issuedDate": "2026-10-17", "evi": true}, {"id": "TX020", "date": "2026-09-22", "dir": "in", "party": "데모 재팬 K.K.", "kind": "ovs", "cat": "taxable", "item": "해외 지원 용역(국외 사업자)", "supply": 1690000, "vat": 0, "total": 1690000, "bn": null, "doc": null, "issuedDate": null, "evi": true}, {"id": "TX021", "date": "2026-09-23", "dir": "in", "party": "가온특송(주)", "kind": "dom", "cat": "taxable", "item": "특송 운임 청구", "supply": 3700000, "vat": 370000, "total": 4070000, "bn": "000-11-20002", "doc": "DOC-31021", "issuedDate": "2026-09-26", "evi": true}, {"id": "TX022", "date": "2026-09-24", "dir": "out", "party": "온누리유통(주)", "kind": "dom", "cat": "taxable", "item": "보관·재고 관리료", "supply": 1660000, "vat": 166000, "total": 1826000, "bn": "000-11-20008", "doc": "DOC-31022", "issuedDate": "2026-10-17", "evi": true}, {"id": "TX023", "date": "2026-09-25", "dir": "in", "party": "데모 USA Inc.", "kind": "ovs", "cat": "taxable", "item": "해외 광고 플랫폼 이용료(국외 사업자)", "supply": 4620000, "vat": 0, "total": 4620000, "bn": null, "doc": null, "issuedDate": null, "evi": true}, {"id": "TX024", "date": "2026-09-28", "dir": "out", "party": "별빛상사(주)", "kind": "dom", "cat": "taxable", "item": "포장 작업 수수료", "supply": 350000, "vat": 35000, "total": 385000, "bn": "000-11-20009", "doc": null, "issuedDate": null, "evi": true}, {"id": "TX025", "date": "2026-09-29", "dir": "in", "party": "누리포장(주)", "kind": "dom", "cat": "taxable", "item": "포장 자재 구매", "supply": 2070000, "vat": 207000, "total": 2277000, "bn": "000-11-20003", "doc": null, "issuedDate": null, "evi": true}, {"id": "TX026", "date": "2026-09-30", "dir": "in", "party": "한빛로지스(주)", "kind": "dom", "cat": "taxable", "item": "국내 배송 대행비", "supply": 1800000, "vat": 180000, "total": 1980000, "bn": "000-11-20001", "doc": null, "issuedDate": null, "evi": true}, {"id": "TX027", "date": "2026-09-30", "dir": "in", "party": "새봄광고(주)", "kind": "dom", "cat": "taxable", "item": "온라인 광고비", "supply": 2930000, "vat": 293000, "total": 3223000, "bn": "000-11-20006", "doc": null, "issuedDate": null, "evi": true}, {"id": "TX028", "date": "2026-09-30", "dir": "in", "party": "다온아이티(주)", "kind": "dom", "cat": "taxable", "item": "시스템 유지보수", "supply": 2380000, "vat": 238000, "total": 2618000, "bn": "000-11-20004", "doc": null, "issuedDate": null, "evi": true}, {"id": "TX029", "date": "2026-10-01", "dir": "out", "party": "한빛로지스(주)", "kind": "dom", "cat": "taxable", "item": "물류 대행 수수료", "supply": 2090000, "vat": 209000, "total": 2299000, "bn": "000-11-20001", "doc": "DOC-31029", "issuedDate": "2026-10-02", "evi": true}, {"id": "TX030", "date": "2026-10-02", "dir": "in", "party": "가온특송(주)", "kind": "dom", "cat": "taxable", "item": "특송 운임 청구", "supply": 3060000, "vat": 306000, "total": 3366000, "bn": "000-11-20002", "doc": "DOC-31030", "issuedDate": "2026-10-03", "evi": true}, {"id": "TX031", "date": "2026-10-05", "dir": "in", "party": "미래오피스임대(주)", "kind": "dom", "cat": "taxable", "item": "사무실 임차료", "supply": 2260000, "vat": 226000, "total": 2486000, "bn": "000-11-20005", "doc": "DOC-31031", "issuedDate": "2026-10-06", "evi": true}, {"id": "TX032", "date": "2026-10-06", "dir": "out", "party": "다온아이티(주)", "kind": "dom", "cat": "taxable", "item": "업무 자동화 컨설팅", "supply": 610000, "vat": 61000, "total": 671000, "bn": "000-11-20004", "doc": "DOC-31032", "issuedDate": "2026-10-07", "evi": true}, {"id": "TX057", "date": "2026-10-06", "dir": "out", "party": "다온아이티(주)", "kind": "dom", "cat": "taxable", "item": "업무 자동화 컨설팅", "supply": 610000, "vat": 61000, "total": 671000, "bn": "000-11-20004", "doc": "DOC-31057", "issuedDate": "2026-10-08", "evi": true}, {"id": "TX033", "date": "2026-10-07", "dir": "out", "party": "데모 재팬 K.K.", "kind": "ovs", "cat": "zero", "item": "법인 간 지원 용역비", "supply": 4360000, "vat": 0, "total": 4360000, "bn": null, "doc": null, "issuedDate": null, "evi": true}, {"id": "TX034", "date": "2026-10-08", "dir": "out", "party": "청명교육원", "kind": "exempt", "cat": "exempt", "item": "사내 교육 서비스", "supply": 900000, "vat": 0, "total": 900000, "bn": "000-11-20007", "doc": "DOC-31034", "issuedDate": "2026-10-09", "evi": true}, {"id": "TX035", "date": "2026-10-09", "dir": "out", "party": "별빛상사(주)", "kind": "dom", "cat": "taxable", "item": "포장 작업 수수료", "supply": 4800000, "vat": 480000, "total": 5290000, "bn": "000-11-20009", "doc": "DOC-31035", "issuedDate": "2026-10-10", "evi": true}, {"id": "TX036", "date": "2026-10-12", "dir": "in", "party": "누리포장(주)", "kind": "dom", "cat": "taxable", "item": "포장 자재 구매", "supply": 560000, "vat": 61000, "total": 621000, "bn": "000-11-20003", "doc": "DOC-31036", "issuedDate": "2026-10-13", "evi": true}, {"id": "TX037", "date": "2026-10-13", "dir": "in", "party": "새봄광고(주)", "kind": "dom", "cat": "taxable", "item": "온라인 광고비", "supply": 4610000, "vat": 461000, "total": 5071000, "bn": null, "doc": "DOC-31037", "issuedDate": "2026-10-14", "evi": true}, {"id": "TX038", "date": "2026-10-14", "dir": "in", "party": "다온아이티(주)", "kind": "dom", "cat": "taxable", "item": "시스템 유지보수", "supply": 1060000, "vat": 106000, "total": 1166000, "bn": "000-11-20004", "doc": "DOC-31038", "issuedDate": "2026-10-15", "evi": true}, {"id": "TX039", "date": "2026-10-15", "dir": "out", "party": "온누리유통(주)", "kind": "dom", "cat": "taxable", "item": "보관·재고 관리료", "supply": 4290000, "vat": 429000, "total": 4719000, "bn": "000-11-20008", "doc": null, "issuedDate": null, "evi": true}, {"id": "TX040", "date": "2026-10-16", "dir": "out", "party": "한빛로지스(주)", "kind": "dom", "cat": "taxable", "item": "물류 대행 수수료", "supply": 1950000, "vat": 195000, "total": 2145000, "bn": "000-11-20001", "doc": null, "issuedDate": null, "evi": true}, {"id": "TX041", "date": "2026-10-19", "dir": "out", "party": "개인 고객(비사업자)", "kind": "ind", "cat": "taxable", "item": "개인 고객 서비스 수수료", "supply": 650000, "vat": 65000, "total": 715000, "bn": null, "doc": null, "issuedDate": null, "evi": true}, {"id": "TX042", "date": "2026-10-19", "dir": "out", "party": "별빛상사(주)", "kind": "dom", "cat": "taxable", "item": "포장 작업 수수료", "supply": 880000, "vat": 88000, "total": 968000, "bn": "000-11-20009", "doc": null, "issuedDate": null, "evi": true}, {"id": "TX043", "date": "2026-10-20", "dir": "in", "party": "가온특송(주)", "kind": "dom", "cat": "taxable", "item": "특송 운임 청구", "supply": 3010000, "vat": 301000, "total": 3311000, "bn": "000-11-20002", "doc": null, "issuedDate": null, "evi": true}, {"id": "TX044", "date": "2026-10-20", "dir": "in", "party": "누리포장(주)", "kind": "dom", "cat": "taxable", "item": "포장 자재 구매", "supply": 3810000, "vat": 381000, "total": 4191000, "bn": "000-11-20003", "doc": null, "issuedDate": null, "evi": true}, {"id": "TX045", "date": "2026-10-21", "dir": "out", "party": "다온아이티(주)", "kind": "dom", "cat": "taxable", "item": "업무 자동화 컨설팅", "supply": 4820000, "vat": 482000, "total": 5302000, "bn": "000-11-20004", "doc": null, "issuedDate": null, "evi": true}, {"id": "TX046", "date": "2026-10-22", "dir": "out", "party": "데모 USA Inc.", "kind": "ovs", "cat": "zero", "item": "법인 간 지원 용역비", "supply": 2460000, "vat": 0, "total": 2460000, "bn": null, "doc": null, "issuedDate": null, "evi": true}, {"id": "TX047", "date": "2026-10-22", "dir": "in", "party": "데모 재팬 K.K.", "kind": "ovs", "cat": "taxable", "item": "해외 지원 용역(국외 사업자)", "supply": 2590000, "vat": 0, "total": 2590000, "bn": null, "doc": null, "issuedDate": null, "evi": true}, {"id": "TX048", "date": "2026-10-23", "dir": "in", "party": "데모 USA Inc.", "kind": "ovs", "cat": "taxable", "item": "해외 광고 플랫폼 이용료(국외 사업자)", "supply": 3100000, "vat": 0, "total": 3100000, "bn": null, "doc": null, "issuedDate": null, "evi": true}, {"id": "TX049", "date": "2026-10-23", "dir": "in", "party": "한빛로지스(주)", "kind": "dom", "cat": "taxable", "item": "국내 배송 대행비", "supply": 3680000, "vat": 368000, "total": 4048000, "bn": "000-11-20001", "doc": null, "issuedDate": null, "evi": true}, {"id": "TX050", "date": "2026-10-26", "dir": "in", "party": "미래오피스임대(주)", "kind": "dom", "cat": "taxable", "item": "사무실 임차료", "supply": 1190000, "vat": 119000, "total": 1309000, "bn": "000-11-20005", "doc": null, "issuedDate": null, "evi": true}, {"id": "TX051", "date": "2026-10-26", "dir": "out", "party": "한빛로지스(주)", "kind": "dom", "cat": "taxable", "item": "물류 대행 수수료", "supply": 3560000, "vat": 356000, "total": 3916000, "bn": "000-11-20001", "doc": null, "issuedDate": null, "evi": true}, {"id": "TX052", "date": "2026-10-27", "dir": "out", "party": "온누리유통(주)", "kind": "dom", "cat": "taxable", "item": "보관·재고 관리료", "supply": 630000, "vat": 63000, "total": 693000, "bn": "000-11-20008", "doc": null, "issuedDate": null, "evi": true}, {"id": "TX053", "date": "2026-10-27", "dir": "out", "party": "별빛상사(주)", "kind": "dom", "cat": "taxable", "item": "포장 작업 수수료", "supply": 5160000, "vat": 516000, "total": 5676000, "bn": "000-11-20009", "doc": null, "issuedDate": null, "evi": true}, {"id": "TX054", "date": "2026-10-27", "dir": "out", "party": "개인 고객(비사업자)", "kind": "ind", "cat": "taxable", "item": "개인 고객 서비스 수수료", "supply": 1800000, "vat": 180000, "total": 1980000, "bn": null, "doc": null, "issuedDate": null, "evi": true}, {"id": "TX055", "date": "2026-10-28", "dir": "out", "party": "청명교육원", "kind": "exempt", "cat": "exempt", "item": "사내 교육 서비스", "supply": 5190000, "vat": 0, "total": 5190000, "bn": "000-11-20007", "doc": null, "issuedDate": null, "evi": true}, {"id": "TX056", "date": "2026-10-28", "dir": "out", "party": "다온아이티(주)", "kind": "dom", "cat": "taxable", "item": "업무 자동화 컨설팅", "supply": 2810000, "vat": 281000, "total": 3091000, "bn": "000-11-20004", "doc": null, "issuedDate": null, "evi": true}], "aor": {"KR": [["재무-자금", "정기·비정기 지출을 지급일에 맞춰 이체하고, 법인카드 사용 내역을 증빙과 함께 정리한다", "서하", "도윤"], ["재무-결산", "매월 세금계산서를 발행·수취하고, 월 결산을 마감한다", "서하", "도윤"], ["재무-청구관리", "법인 간 용역비를 청구서로 관리하고, 상계 기준 자료로 쓴다", "이안", "도윤"], ["재무-지출관리", "운송사 청구·세금·보험료를 지급일에 맞춰 처리하고 증빙을 확보한다", "서하", "도윤"], ["재무-출장 정산", "출장 정산 서류를 검토하고, 규정 기준에 맞는지 확인해 지급한다", "서하", "도윤"], ["인사-채용", "채용공고를 게시하고 단계별 진행 현황을 관리한다", "지안", "하린"], ["인사-입퇴사", "입사자·퇴사자 서류를 처리하고 소속 변경 시 절차를 진행한다", "지안", "하린"], ["인사-급여", "매월 급여 기초자료를 취합해 급여대장을 검수한다", "지안", "하린"], ["인사-연차", "연차를 산정·부여하고 사용·정산 내역을 관리한다", "지안", "하린"], ["총무-시설", "사무실 임차료를 지급하고 시설 이슈 발생 시 대응한다", "이안", "하린"], ["총무-계약서", "각종 계약서 초안을 작성·검토하고 날인 절차를 진행한다", "이안", "하린"], ["총무-자산관리", "사무용 가구·비품·장비 계약을 관리하고 관련 비용을 지출한다", "이안", "하린"], ["법무", "계약서·법적 리스크를 검토하고, 자문이 필요한 건은 외부 법무법인과 협의한다", "이안", "하린"], ["CX-미수금관리", "고객 미입금 건을 확인해 독촉하고, 미회수 시 법적 조치를 신청한다", "서하", "도윤"]], "JP": [["재무-자금", "지급 항목을 지급일에 맞춰 처리하고 증빙을 정리한다", "로아", "시우"], ["재무-결산", "월별 매출 청구서를 발행·수취하고 월 결산을 마감한다", "로아", "시우"], ["재무-출장 정산", "출장 비용(立替)과 정산 서류를 검토하고 지급한다", "로아", "시우"], ["인사-급여", "월 급여 기초자료를 취합해 급여대장을 검수한다", "다온", "시우"], ["인사-입퇴사", "입퇴사 서류와 사회보험 절차를 처리한다", "다온", "시우"], ["총무-시설", "사무실 임차와 시설 이슈를 관리한다", "다온", "시우"], ["총무-계약서", "계약서 초안을 작성·검토하고 날인 절차를 진행한다", "다온", "시우"], ["법무", "계약서·법적 리스크 검토, 현지 법률 자문 연계", "다온", "시우"], ["인사-근태", "근무표 게시와 연장근무 사전 승인, 실적을 관리한다", "(확인 중)", "(확인 중)"]]}, "trips": [{"id": "TR-101", "who": "김데모", "ent": "KR", "dest": "부산", "start": "2026-11-12", "end": "2026-11-13", "type": "일반", "purpose": "부산 물류센터 현장 점검", "est": 520000, "phase": "apply", "stage": 1, "team": "박팀장"}, {"id": "TR-102", "who": "이샘플", "ent": "KR", "dest": "도쿄", "start": "2026-11-24", "end": "2026-11-27", "type": "일반", "purpose": "일본 법인 월간 운영 회의", "est": 1850000, "phase": "apply", "stage": 0, "team": "박팀장"}, {"id": "TR-103", "who": "최예시", "ent": "JP", "dest": "서울", "start": "2026-12-03", "end": "2026-12-05", "type": "일반", "purpose": "본사 분기 회의", "est": 140000, "phase": "apply", "stage": 2, "team": "나팀장"}, {"id": "TR-098", "who": "김데모", "ent": "KR", "dest": "대구", "start": "2026-10-14", "end": "2026-10-15", "type": "일반", "purpose": "거래처 미팅", "est": 310000, "phase": "settle", "stage": 0, "team": "박팀장", "settleDue": "submitted"}, {"id": "TR-095", "who": "정시안", "ent": "KR", "dest": "싱가포르", "start": "2026-10-05", "end": "2026-10-09", "type": "장기", "purpose": "해외 파트너 협의", "est": 2400000, "phase": "settle", "stage": 1, "team": "박팀장"}, {"id": "TR-090", "who": "김데모", "ent": "KR", "dest": "오사카", "start": "2026-10-06", "end": "2026-10-09", "type": "일반", "purpose": "파트너 물류센터 방문", "est": 1200000, "phase": "trip", "stage": 0, "team": "박팀장"}, {"id": "TR-104", "who": "한가상", "ent": "US", "dest": "서울", "start": "2026-12-08", "end": "2026-12-11", "type": "일반", "purpose": "분기 전략 워크숍", "est": 1500, "phase": "apply", "stage": 0, "team": "나팀장"}], "legal": [{"id": "LG-041", "title": "물류 대행 계약서 개정안 검토", "req": "김데모", "type": "계약서 검토", "status": "변호사 검토 중", "owner": "이안", "created": "2026-10-21", "due": "2026-11-04"}, {"id": "LG-040", "title": "개인정보 처리 위탁 약관 문구 확인", "req": "이샘플", "type": "약관·정책", "status": "담당 배정", "owner": "이안", "created": "2026-10-23", "due": "2026-11-06"}, {"id": "LG-038", "title": "해외 파트너 비밀유지계약(NDA) 검토", "req": "정시안", "type": "계약서 검토", "status": "회신 도착", "owner": "이안", "created": "2026-10-14", "due": "2026-10-28"}, {"id": "LG-035", "title": "반품 분쟁 건 법적 대응 가능 여부", "req": "한가상", "type": "법적 리스크", "status": "접수", "owner": "", "created": "2026-10-27", "due": ""}, {"id": "LG-031", "title": "사무실 임대차 갱신 조건 검토", "req": "김데모", "type": "계약서 검토", "status": "완료·공유", "owner": "이안", "created": "2026-09-30", "due": "2026-10-12"}, {"id": "LG-029", "title": "광고 문구 표시·광고법 저촉 여부", "req": "최예시", "type": "법적 리스크", "status": "완료·공유", "owner": "이안", "created": "2026-09-22", "due": "2026-10-02"}]};
const $ = (id) => document.getElementById(id);
const esc = (t) => String(t == null ? '' : t).replace(/[&<>"]/g, (c) => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const TODAY = '2026-10-28';
const MS = 864e5, WD = ['일','월','화','수','목','금','토'];
const P = (iso) => Date.UTC(+iso.slice(0, 4), +iso.slice(5, 7) - 1, +iso.slice(8, 10));
const I = (ms) => new Date(ms).toISOString().slice(0, 10);
const fmt = (iso) => iso ? iso.slice(5, 7) + '/' + iso.slice(8, 10) + '(' + WD[new Date(P(iso)).getUTCDay()] + ')' : '-';
const diff = (a, b) => Math.round((P(a) - P(b)) / MS);
const HOL = new Set(['2026-12-25', '2027-01-01']);
const isBiz = (ms) => { const d = new Date(ms).getUTCDay(); return d > 0 && d < 6 && !HOL.has(I(ms)); };
function addBiz(iso, n) { let ms = P(iso); const s = n < 0 ? -1 : 1; let c = Math.abs(n); while (c > 0) { ms += s * MS; if (isBiz(ms)) c--; } return I(ms); }
const num = (n) => Math.round(n).toLocaleString('ko-KR');

/* ---------- 가상 규정 ---------- */
const ENT = {
  KR:{name:'한국 법인', cur:'원', ceo:1000000, meal:60000, hotel:150000, bo:'도윤'},
  JP:{name:'일본 법인', cur:'엔', ceo:100000, meal:6000, hotel:15000, bo:'시우'},
  US:{name:'미국 법인', cur:'달러', ceo:1000, meal:50, hotel:160, bo:'시우'},
};
const money = (n, ent) => num(n) + ENT[ent || 'KR'].cur;
const DEAD = {'일반':10, '장기':15, '파견':20};
const SETTLE_DAYS = 7;
const SETTLE = ['BO 검토', '팀장 확인', '재무총괄 승인'];
const ROLE_OF = {'BO 합의':'bo', 'BO 검토':'bo', '팀장 승인':'lead', '팀장 확인':'lead', '재무총괄 승인':'cfo', '대표 승인':'ceo'};
const NAMES = {trav:'김데모', lead:'박팀장', bo:'도윤', cfo:'재무총괄', ceo:'대표'};
const ROLES = {trav:'출장자 (김데모)', lead:'팀장 (박팀장)', bo:'BO 담당 (도윤)', cfo:'재무총괄', ceo:'대표'};

/* ---------- 상태 ---------- */
const S = {
  tab:'home', role:'trav', sub:'apply', asOf:TODAY, soon:5,
  trips:JSON.parse(JSON.stringify(DATA.trips)), tx:JSON.parse(JSON.stringify(DATA.tx)), legal:JSON.parse(JSON.stringify(DATA.legal)),
  me:{ent:'KR', team:'물류운영팀', lead:'lead@demo-company.example', noLead:false},
  form:{ent:'KR', dest:'', start:'2026-11-18', end:'2026-11-20', type:'일반', purpose:'', plan:'', air:300000, hotel:140000, meal:50000, other:30000, legacy:false, legacyLink:''},
  settle:{trip:'TR-090', approved:'2026-09-28', ent:'KR', rows:[
    {cat:'항공', date:'2026-10-02', amt:520000, qty:1, rec:true, quote:400000},
    {cat:'숙박', date:'2026-10-06', amt:540000, qty:3, rec:true},
    {cat:'식비', date:'2026-10-07', amt:150000, qty:3, rec:true, alc:false},
    {cat:'택시', date:'2026-10-07', amt:28000, qty:1, rec:true, time:'23:10', why:''},
    {cat:'택시', date:'2026-10-08', amt:19000, qty:1, rec:true, time:'18:30', why:''},
    {cat:'기타', date:'2026-10-08', amt:35000, qty:1, rec:true},
    {cat:'대중교통', date:'2026-09-20', amt:12000, qty:1, rec:true},
    {cat:'식비', date:'2026-10-09', amt:38000, qty:1, rec:false, alc:false},
  ]},
  tf:'all', tdir:'all', tm:'all', tq:'', ck:{dir:'out', party:'dom', nature:'taxable', date:'2026-10-20'},
  lf:'active', afil:'KR', aq:'',
};

/* ---------- 공통 UI ---------- */
function toast(t) { const e = $('toast'); e.textContent = t; e.style.display = 'block'; clearTimeout(toast.t); toast.t = setTimeout(() => e.style.display = 'none', 2400); }
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
$('role').innerHTML = Object.keys(ROLES).map((k) => `<option value="${k}">${ROLES[k]}</option>`).join('');
$('role').addEventListener('change', () => { S.role = $('role').value; draw(true); });
const TABS = [['home','홈'],['trip','출장 관리'],['tax','세금계산서 점검'],['legal','법무 검토 데스크'],['aor','담당자 찾기']];
function drawTabs() {
  $('tabs').innerHTML = TABS.map(([k, n]) => `<button class="tab" role="tab" data-t="${k}" aria-selected="${S.tab === k}">${n}</button>`).join('');
  $('tabs').querySelectorAll('.tab').forEach((b) => b.addEventListener('click', () => { S.tab = b.dataset.t; draw(); window.scrollTo(0, 0); }));
}
const sel = (opts, v, f, extra) => `<select data-f="${f}" ${extra || ''}>${opts.map((o) => { const [val, lb] = Array.isArray(o) ? o : [o, o]; return `<option value="${esc(val)}" ${String(val) === String(v) ? 'selected' : ''}>${esc(lb)}</option>`; }).join('')}</select>`;

/* ---------- 출장: 결재선 ---------- */
function stepsOf(t) { const e = ENT[t.ent]; let s = ['BO 합의', '팀장 승인', '재무총괄 승인']; if (t.est >= e.ceo) s.push('대표 승인'); if (t.noLead) s = s.filter((x) => !x.startsWith('팀장')); return s; }
function settleSteps(t) { return t.noLead ? SETTLE.filter((x) => !x.startsWith('팀장')) : SETTLE; }
function stepDots(list, cur, done) {
  return `<div class="stp">${list.map((s, i) => `${i ? '<b></b>' : ''}<span class="${done || i < cur ? 'd' : i === cur ? 'c' : ''}">${s}</span>`).join('')}${done ? '<b></b><span class="d">완료</span>' : ''}</div>`;
}
const settleDue = (t) => addBiz(t.end, SETTLE_DAYS);
function tripStatus(t) {
  if (t.phase === 'cancelled') return ['취소됨', 'gray'];
  if (t.cancel && t.cancel.pending) return ['취소 승인 대기', 'warn'];
  if (t.phase === 'apply') { const st = stepsOf(t); return [st[t.stage] + ' 대기', 'info']; }
  if (t.phase === 'trip') return [diff(settleDue(t), S.asOf) < 0 ? '정산 기한 지남' : (P(t.end) < P(S.asOf) ? '정산 제출 필요' : '승인 완료'), diff(settleDue(t), S.asOf) < 0 ? 'crit' : 'good'];
  if (t.phase === 'settle') { const st = settleSteps(t); return [t.stage >= st.length ? '지급 완료' : '정산 ' + st[t.stage] + ' 대기', t.stage >= st.length ? 'good' : 'info']; }
  return ['', 'gray'];
}
function pendingFor(role) {
  const out = [];
  S.trips.forEach((t) => {
    if (t.phase === 'cancelled') return;
    if (t.cancel && t.cancel.pending) { if ((role === 'lead' && !t.noLead) || (role === 'cfo' && t.noLead)) out.push({k:'cancel', t, label:'취소 승인', why:t.cancel.reason}); return; }
    if (t.phase === 'apply') { const st = stepsOf(t); if (t.stage < st.length && ROLE_OF[st[t.stage]] === role) out.push({k:'step', t, label:st[t.stage]}); }
    if (t.phase === 'settle') { const st = settleSteps(t); if (t.stage < st.length && ROLE_OF[st[t.stage]] === role) out.push({k:'step', t, label:'정산 ' + st[t.stage]}); }
    if (role === 'trav' && t.who === '김데모' && t.phase === 'trip' && P(t.end) < P(S.asOf)) out.push({k:'submit', t, label:'정산 제출', due:settleDue(t)});
    if (role === 'bo' && t.phase === 'trip' && diff(settleDue(t), S.asOf) < 0) out.push({k:'nudge', t, label:'정산 독촉', due:settleDue(t)});
  });
  return out;
}
function pendAct(it) {
  if (it.k === 'step') return `<button class="act" data-a="approve" data-id="${it.t.id}">승인</button><button class="btn sm ghost" data-a="reject" data-id="${it.t.id}">반려</button>`;
  if (it.k === 'cancel') return `<button class="act" data-a="cancelok" data-id="${it.t.id}">취소 승인</button><button class="btn sm ghost" data-a="cancelno" data-id="${it.t.id}">거절</button>`;
  if (it.k === 'submit') return `<button class="act" data-a="gosettle" data-id="${it.t.id}">정산하러 가기</button>`;
  return `<button class="act" data-a="nudgetrip" data-id="${it.t.id}">독촉 문구</button>`;
}
function pendRow(it) {
  const t = it.t, e = ENT[t.ent];
  return `<div class="fi"><div class="fi-l"><span class="pill ${it.k === 'nudge' ? 'warn' : it.k === 'submit' ? 'crit' : 'info'}">${it.label}</span></div>
  <div class="fi-m"><b>${esc(t.id)} · ${esc(t.dest)} ${esc(t.purpose)}</b><div class="s2">${esc(t.who)} · ${e.name} · ${fmt(t.start)}~${fmt(t.end)} · 예상 ${money(t.est, t.ent)}${it.why ? ' · 사유: ' + esc(it.why) : ''}</div></div>
  <div class="fi-d">${it.due ? (diff(it.due, S.asOf) < 0 ? `<span class="pill crit">정산 기한 ${-diff(it.due, S.asOf)}일 지남</span>` : `<span class="s2">정산 기한 ${fmt(it.due)}</span>`) : '<span class="s2">알림 봇이 DM으로 전달</span>'}</div>
  <div class="fi-a">${pendAct(it)}</div></div>`;
}

/* ---------- 출장: 정산 규정 판정 ---------- */
function judge(r, ctx) {
  const e = ENT[ctx.ent], res = (k, allowed, why) => ({k, allowed, why});
  if (!r.rec) return res('review', 0, '영수증이 없어 확인이 필요합니다');
  if (r.date < ctx.approved) return res('no', 0, '승인 전에 쓴 비용은 지급되지 않습니다');
  if (r.cat === '항공') {
    if (r.quote && r.amt > r.quote * 1.2) return res('review', 0, '신청 때 견적보다 ' + Math.round((r.amt / r.quote - 1) * 100) + '% 높음 — 사유 필요');
    return res('ok', r.amt, '견적 범위 안');
  }
  if (r.cat === '숙박') { const per = r.amt / r.qty; return per <= e.hotel ? res('ok', r.amt, '박당 ' + num(per) + e.cur + ' ≤ 상한 ' + num(e.hotel)) : res('cap', e.hotel * r.qty, '박당 ' + num(per) + e.cur + ' > 상한 ' + num(e.hotel) + ' → 상한까지 인정'); }
  if (r.cat === '식비') {
    if (r.alc) return res('review', 0, '주류가 섞여 있어 분리 필요');
    const per = r.amt / r.qty; return per <= e.meal ? res('ok', r.amt, '일 ' + num(per) + e.cur + ' ≤ 상한 ' + num(e.meal)) : res('cap', e.meal * r.qty, '일 ' + num(per) + e.cur + ' > 상한 ' + num(e.meal) + ' → 상한까지 인정');
  }
  if (r.cat === '대중교통') return res('ok', r.amt, '출장지 안 이동은 대중교통이 원칙');
  if (r.cat === '택시') {
    if (r.time >= '22:00') return res('ok', r.amt, '22시 이후 탑승(시각 확인됨)');
    if (r.why) return res('review', 0, '사유 "' + r.why + '" — 영수증과 함께 확인 필요');
    return res('no', 0, '22시 전 업무 종료 후 교통비는 지급되지 않습니다');
  }
  return res('review', 0, '규정에 없는 항목 — 담당자 판단 필요');
}
const RES_L = {ok:['인정', 'good'], cap:['상한까지 인정', 'warn'], review:['판단 필요', 'info'], no:['불인정', 'crit']};

/* ---------- 홈 ---------- */
function taxCounts() { const c = {overdue:0, soon:0, sched:0, check:0, late:0, ok:0, na:0}; S.tx.forEach((t) => { c[taxState(t).k]++; }); return c; }
function legalActive() { return S.legal.filter((x) => x.status !== '완료·공유'); }
function homeView() {
  const pend = pendingFor(S.role), tc = taxCounts(), la = legalActive();
  const taxOpen = tc.overdue + tc.soon, mine = S.role === 'bo' || S.role === 'cfo';
  const items = pend.map(pendRow);
  if (mine && tc.overdue) items.push(`<div class="fi"><div class="fi-l"><span class="pill crit">세금계산서</span></div><div class="fi-m"><b>기한 지난 발행·수취 ${tc.overdue}건</b><div class="s2">공급일 다음 달 10일까지 발행·수취해야 하는 건 중 아직 처리되지 않은 건입니다</div></div><div class="fi-d"><span class="pill crit">기한 지남</span></div><div class="fi-a"><button class="act" data-a="goto" data-id="tax">점검하러 가기</button></div></div>`);
  if (mine && tc.check) items.push(`<div class="fi"><div class="fi-l"><span class="pill warn">세금계산서</span></div><div class="fi-m"><b>확인이 필요한 건 ${tc.check}건</b><div class="s2">금액 불일치, 사업자번호 누락, 중복 발행 의심, 영세율 증빙 누락</div></div><div class="fi-d"></div><div class="fi-a"><button class="act" data-a="goto" data-id="tax">확인하러 가기</button></div></div>`);
  if (S.role === 'bo') S.legal.filter((x) => !x.owner || x.status === '회신 도착').forEach((x) => items.push(`<div class="fi"><div class="fi-l"><span class="pill info">법무 검토</span></div><div class="fi-m"><b>${esc(x.id)} · ${esc(x.title)}</b><div class="s2">${esc(x.req)} · ${esc(x.type)} · ${x.owner ? '변호사 회신이 도착했습니다' : '담당자가 아직 배정되지 않았습니다'}</div></div><div class="fi-d"></div><div class="fi-a"><button class="act" data-a="goto" data-id="legal">열기</button></div></div>`));
  const tripPend = pend.length;
  return `<div class="big" style="font-size:22px;margin:4px 0 2px">좋은 아침입니다, ${NAMES[S.role]}님</div>
  <div class="s2" style="margin-bottom:14px">${fmt(S.asOf)} · 오늘 쓸 도구를 고르세요. 아래 "처리할 일"은 위에서 고른 역할 기준입니다.</div>
  <div class="cards4">
   <div class="tcard"><h4>✈ 출장 관리</h4><div class="n">${tripPend}<small>처리할 일</small></div><p>출장 신청 → 결재 → 정산까지 한곳에서. 규정 기준은 화면이 자동으로 계산합니다.</p><button class="btn sm dk" data-a="goto" data-id="trip">열기 →</button></div>
   <div class="tcard"><h4>🧾 세금계산서 점검</h4><div class="n">${taxOpen}<small>기한 지남·임박</small></div><p>어떤 거래에 어떤 증빙이 필요한지 판정하고, 발행·수취가 빠진 건을 찾습니다.</p><button class="btn sm dk" data-a="goto" data-id="tax">열기 →</button></div>
   <div class="tcard"><h4>⚖ 법무 검토 데스크</h4><div class="n">${la.length}<small>진행 중</small></div><p>검토 요청을 등록하면 유형별 규칙으로 담당자가 배정되고, 회신까지 추적합니다.</p><button class="btn sm dk" data-a="goto" data-id="legal">열기 →</button></div>
   <div class="tcard"><h4>👥 담당자 찾기</h4><div class="n">${DATA.aor.KR.length + DATA.aor.JP.length}<small>업무</small></div><p>BO에 요청할 때 누구에게 해야 하는지, 업무별 오너와 실무자를 찾습니다.</p><button class="btn sm dk" data-a="goto" data-id="aor">열기 →</button></div>
  </div>
  <div class="h2">처리할 일 ${items.length} <small>${ROLES[S.role]} 기준 · 위에서 보는 사람을 바꿔 보세요</small></div>
  <div class="card nopad">${items.join('') || '<div class="empty">지금 처리할 일이 없습니다.</div>'}</div>`;
}
function bindHome() {}

/* ---------- 출장 관리 ---------- */
const SUBS = [['apply','출장 신청'],['mine','처리할 일 · 출장 현황'],['settle','정산'],['rules','기준']];
function tripView() {
  let h = `<div class="sub2">${SUBS.map(([k, n]) => `<button class="chip ${S.sub === k ? 'on' : ''}" data-sub="${k}">${n}</button>`).join('')}</div>`;
  return h + ({apply:applyView, mine:mineView, settle:settleView, rules:rulesView}[S.sub])();
}
function applyChecks() {
  const f = S.form, e = ENT[f.ent], days = Math.max(0, diff(f.end, f.start)) + 1, nights = Math.max(0, days - 1);
  const est = +f.air + f.hotel * nights + f.meal * days + +f.other;
  const need = DEAD[f.type], dl = addBiz(f.start, -need), late = P(TODAY) > P(dl);
  const ck = [];
  ck.push(S.me.lead || S.me.noLead ? ['good', '내 정보: 팀장 이메일 ' + (S.me.noLead ? '"결재받을 팀장 없음" 체크됨' : '입력됨')] : ['crit', '내 정보에 팀장 이메일이 없고 "팀장 없음"도 체크하지 않아 제출할 수 없습니다']);
  ck.push(P(f.end) >= P(f.start) && f.dest ? ['good', '출장지·일정 입력됨 (' + days + '일)'] : ['crit', '출장지를 입력하고, 종료일이 시작일보다 빠르지 않게 해 주세요']);
  ck.push(f.purpose.trim().length >= 5 && f.plan.trim().length >= 5 ? ['good', '출장 목적과 일자별 계획 입력됨'] : ['crit', '출장 목적과 일자별 계획을 5자 이상 적어 주세요']);
  if (!late) ck.push(['good', `신청 기한 OK — ${f.type} 출장은 출발 ${need}영업일 전(${fmt(dl)})까지, 오늘은 ${diff(dl, TODAY)}일 남음`]);
  else if (f.legacy && f.legacyLink.trim()) ck.push(['warn', `신청 기한(${fmt(dl)})이 지났지만 "도입 전 신청 건"으로 기존 신청 링크가 적혀 있어 제출됩니다`]);
  else ck.push(['crit', `신청 기한(${fmt(dl)})이 지났습니다. 도입 전에 이미 신청한 출장이면 아래에서 체크하고 기존 신청 링크를 적어 주세요`]);
  const hot = f.hotel > e.hotel, mealHot = f.meal > e.meal;
  if (hot || mealHot) ck.push(['warn', `${hot ? '숙박 박당 ' + money(f.hotel, f.ent) + '이 상한 ' + money(e.hotel, f.ent) + '을 넘어 상한까지만 인정됩니다. ' : ''}${mealHot ? '식비 일 ' + money(f.meal, f.ent) + '이 상한 ' + money(e.meal, f.ent) + '을 넘습니다.' : ''}`]);
  const chain = stepsOf({ent:f.ent, est, noLead:S.me.noLead});
  ck.push(['info', '결재 순서: ' + chain.join(' → ') + (est >= e.ceo ? ` (예상 총액 ${money(est, f.ent)} ≥ ${money(e.ceo, f.ent)}이라 대표 승인 추가)` : '')]);
  return {est, days, nights, ck, chain, ok:!ck.some((c) => c[0] === 'crit')};
}
function applyView() {
  const f = S.form, a = applyChecks(), e = ENT[f.ent];
  const late = P(TODAY) > P(addBiz(f.start, -DEAD[f.type]));
  return `<div class="two"><div>
  <div class="panel"><h3>내 정보 <small style="font-weight:500;color:var(--mut)">처음 한 번만 · 비어 있으면 신청서가 제출되지 않습니다</small></h3>
  <div class="fgrid"><label>소속 법인${sel(Object.keys(ENT).map((k) => [k, ENT[k].name]), S.me.ent, 'me.ent')}</label><label>팀<input type="text" value="${esc(S.me.team)}" data-f="me.team"></label>
  <label>팀장 이메일<input type="email" value="${esc(S.me.lead)}" data-f="me.lead" ${S.me.noLead ? 'disabled' : ''}></label>
  <label class="chk" style="align-self:end"><input type="checkbox" data-f="me.noLead" ${S.me.noLead ? 'checked' : ''}>결재받을 팀장이 따로 없습니다</label></div></div>
  <div class="panel"><h3>새 출장 신청</h3>
  <div class="fgrid"><label>법인${sel(Object.keys(ENT).map((k) => [k, ENT[k].name]), f.ent, 'form.ent')}</label><label>출장지<input type="text" value="${esc(f.dest)}" placeholder="예) 부산" data-f="form.dest"></label>
  <label>출장 유형${sel([['일반', '일반 (출발 10영업일 전)'], ['장기', '7일 이상 혼합 이동 (15영업일 전)'], ['파견', '파견 (20영업일 전)']], f.type, 'form.type')}</label>
  <label>출발일<input type="date" value="${f.start}" data-f="form.start"></label><label>종료일<input type="date" value="${f.end}" data-f="form.end"></label>
  <label class="full">출장 목적<input type="text" value="${esc(f.purpose)}" placeholder="무엇을 위해 가는지" data-f="form.purpose"></label>
  <label class="full">일자별 계획<input type="text" value="${esc(f.plan)}" placeholder="예) 1일차 센터 점검, 2일차 거래처 미팅" data-f="form.plan"></label></div>
  <div class="h2" style="margin-top:14px">예상 비용 <small>${e.cur} 기준 · 상한은 화면이 바로 비교합니다</small></div>
  <div class="fgrid"><label>항공(총액)<input type="number" value="${f.air}" data-f="form.air"></label><label>숙박(1박)<input type="number" value="${f.hotel}" data-f="form.hotel"></label><label>식비(1일)<input type="number" value="${f.meal}" data-f="form.meal"></label><label>교통·기타(총액)<input type="number" value="${f.other}" data-f="form.other"></label></div>
  ${late ? `<div class="chk" style="margin-top:12px"><input type="checkbox" data-f="form.legacy" ${f.legacy ? 'checked' : ''}> 출장 관리 도입 전에 기존 방식으로 이미 신청한 출장입니다</div>${f.legacy ? `<div class="fgrid" style="margin-top:8px"><label class="full">기존 신청 링크<input type="text" value="${esc(f.legacyLink)}" placeholder="기존 신청 링크" data-f="form.legacyLink"></label></div>` : ''}` : ''}
  <div class="sum"><div>예상 총액<b>${money(a.est, f.ent)}</b></div><div>일정<b>${a.days}일 / ${a.nights}박</b></div><div>결재 단계<b>${a.chain.length}단계</b></div><div>제출 가능<b style="color:${a.ok ? 'var(--good)' : 'var(--crit)'}">${a.ok ? '가능' : '불가'}</b></div></div>
  <button class="btn dk" data-a="submitTrip">출장 신청 제출</button> <span class="s2">제출하면 BO 합의 단계부터 시작합니다. 항공·숙소 예약은 승인 후에 하세요.</span></div></div>
  <div><div class="card" style="position:sticky;top:8px"><div class="h2" style="margin-top:0">제출 전 점검</div><div class="chk-list">${a.ck.map(([k, t]) => `<div><span class="pill ${k}">${{good:'통과', crit:'막힘', warn:'주의', info:'안내'}[k]}</span><span>${esc(t)}</span></div>`).join('')}</div>
  <div class="cap" style="margin-top:12px">Slack·메일·구두로 한 신청은 정식 신청으로 인정되지 않습니다(가상 규정). 승인 전에 쓴 비용은 지급되지 않습니다.</div></div></div></div>`;
}
function mineView() {
  const pend = pendingFor(S.role);
  const rows = S.trips.map((t) => {
    const [stt, cls] = tripStatus(t), steps = t.phase === 'settle' ? settleSteps(t) : stepsOf(t);
    const dots = t.phase === 'cancelled' ? '' : t.phase === 'trip' ? stepDots(stepsOf(t), 0, true) : stepDots(steps, t.stage, t.phase === 'settle' ? t.stage >= steps.length : t.stage >= steps.length);
    const canCancel = t.phase === 'trip' && P(t.start) > P(S.asOf) && !(t.cancel && t.cancel.pending);
    return `<tr><td><b>${esc(t.id)}</b><div class="s2">${esc(t.who)}</div></td><td>${esc(t.dest)}<div class="s2">${esc(t.purpose)}</div></td><td class="s2">${fmt(t.start)}~${fmt(t.end)}</td><td class="num">${money(t.est, t.ent)}</td><td><span class="pill ${cls}">${stt}</span><div style="margin-top:6px">${dots}</div></td><td>${canCancel ? `<button class="btn sm ghost" data-a="cancelreq" data-id="${t.id}">취소 요청</button>` : ''}</td></tr>`;
  }).join('');
  return `<div class="h2" style="margin-top:0">처리할 일 ${pend.length} <small>${ROLES[S.role]} 기준 · 단계마다 다음 차례인 사람에게 알림 봇이 DM을 보내고, 같은 내용이 여기에 보입니다</small></div>
  <div class="card nopad">${pend.map(pendRow).join('') || '<div class="empty">지금 처리할 일이 없습니다.</div>'}</div>
  <div class="h2">출장 현황 <small>법인 전체 · 정산 기한은 출장 종료 후 ${SETTLE_DAYS}영업일</small></div>
  <div class="tw"><table><thead><tr><th>번호</th><th>출장지·목적</th><th>기간</th><th class="num">예상 비용</th><th>진행 단계</th><th></th></tr></thead><tbody>${rows}</tbody></table></div>`;
}
function settleView() {
  const st = S.settle, ctx = {ent:st.ent, approved:st.approved}, e = ENT[st.ent];
  const rs = st.rows.map((r) => ({r, j:judge(r, ctx)}));
  const tot = rs.reduce((a, x) => a + x.r.amt, 0), ok = rs.reduce((a, x) => a + x.j.allowed, 0);
  const sumBy = (k) => rs.filter((x) => x.j.k === k).reduce((a, x) => a + x.r.amt, 0);
  const noAmt = sumBy('no'), revAmt = sumBy('review'), capCut = rs.filter((x) => x.j.k === 'cap').reduce((a, x) => a + x.r.amt - x.j.allowed, 0);
  const cats = ['항공', '숙박', '식비', '대중교통', '택시', '기타'];
  const extra = (r, i) => r.cat === '항공' ? `신청 견적 <input type="number" value="${r.quote || 0}" data-f="row.${i}.quote">` : r.cat === '택시' ? `탑승 <input type="time" value="${r.time || ''}" data-f="row.${i}.time" style="width:118px"> 사유 ${sel([['', '없음'], ['긴급 상황', '긴급 상황'], ['대중교통 없음', '대중교통 없음']], r.why || '', 'row.' + i + '.why')}` : r.cat === '식비' ? `<label class="chk"><input type="checkbox" data-f="row.${i}.alc" ${r.alc ? 'checked' : ''}>주류 포함</label>` : '';
  const trips = S.trips.filter((t) => t.phase === 'trip');
  return `<div class="panel"><h3>정산 규정 자동 판정 <small style="font-weight:500;color:var(--mut)">영수증 줄마다 금액·항목을 채우면 규정 기준으로 인정 / 상한까지 인정 / 판단 필요 / 불인정을 보여줍니다</small></h3>
  <div class="fgrid"><label>법인${sel(Object.keys(ENT).map((k) => [k, ENT[k].name]), st.ent, 'settle.ent')}</label><label>승인 완료일<input type="date" value="${st.approved}" data-f="settle.approved"></label>
  <label>정산할 출장${sel(trips.length ? trips.map((t) => [t.id, t.id + ' · ' + t.dest]) : [['', '정산 대기 출장 없음']], st.trip, 'settle.trip')}</label></div></div>
  <div class="sum"><div>신청 금액<b>${money(tot, st.ent)}</b></div><div>지급 예상(인정)<b style="color:var(--good)">${money(ok, st.ent)}</b></div><div>불인정<b style="color:var(--crit)">${money(noAmt, st.ent)}</b></div><div>판단 필요 · 상한 초과분<b>${money(revAmt, st.ent)} · ${money(capCut, st.ent)}</b></div></div>
  <div class="tw"><table class="rt"><thead><tr><th>항목</th><th>지출일</th><th>금액(${e.cur})</th><th>수량(박·일)</th><th>영수증</th><th>추가 정보</th><th>판정</th><th></th></tr></thead><tbody>
  ${rs.map(({r, j}, i) => `<tr><td>${sel(cats, r.cat, 'row.' + i + '.cat')}</td><td><input type="date" value="${r.date}" data-f="row.${i}.date"></td><td><input type="number" value="${r.amt}" data-f="row.${i}.amt"></td><td><input type="number" value="${r.qty}" min="1" style="width:60px" data-f="row.${i}.qty"></td><td><input type="checkbox" ${r.rec ? 'checked' : ''} data-f="row.${i}.rec"></td><td class="s2">${extra(r, i)}</td><td><span class="pill ${RES_L[j.k][1]}">${RES_L[j.k][0]}</span> <span class="s2">${num(j.allowed)}${e.cur} 인정</span><div class="s2">${esc(j.why)}</div></td><td><button class="btn sm ghost" data-a="delrow" data-id="${i}">삭제</button></td></tr>`).join('')}
  </tbody></table></div>
  <div style="margin-top:10px;display:flex;gap:8px;flex-wrap:wrap"><button class="btn" data-a="addrow">줄 추가</button><button class="btn dk" data-a="submitSettle">정산 제출</button><span class="s2" style="align-self:center">정산 기한: 출장 종료 후 ${SETTLE_DAYS}영업일 · 제출하면 BO 검토 → 팀장 확인 → 재무총괄 승인 순으로 진행됩니다</span></div>`;
}
function rulesView() {
  const rowE = (k) => { const e = ENT[k]; return `<tr><td>${e.name}</td><td class="num">${money(e.ceo, k)}</td><td class="num">${money(e.meal, k)}</td><td class="num">${money(e.hotel, k)}</td><td>${e.bo}</td></tr>`; };
  return `<div class="note">아래는 이 데모에서 쓰는 <b>가상 기준</b>입니다. 실제 회사 규정과 다릅니다.</div>
  <div class="two"><div class="card"><div class="h2" style="margin-top:0">법인별 기준</div><div class="tw"><table><thead><tr><th>법인</th><th class="num">대표 승인 기준(예상 총액)</th><th class="num">식비 상한(일)</th><th class="num">숙박 상한(박)</th><th>담당 BO</th></tr></thead><tbody>${['KR','JP','US'].map(rowE).join('')}</tbody></table></div></div>
  <div class="card"><div class="h2" style="margin-top:0">일정·결재</div><div class="rules"><div><b>신청 기한</b> 일반 출발 10영업일 전 · 7일 이상 혼합 이동 15영업일 전 · 파견 20영업일 전</div><div><b>정산 기한</b> 출장 종료 후 ${SETTLE_DAYS}영업일</div><div><b>신청 결재</b> BO 합의 → 팀장 승인 → 재무총괄 승인 (기준 금액 이상이면 대표 승인 추가)</div><div><b>정산 결재</b> BO 검토 → 팀장 확인 → 재무총괄 승인 → 지급</div></div></div></div>
  <div class="h2">항목별 판정 규칙</div>
  <div class="tw"><table><thead><tr><th>항목</th><th>판정 규칙</th></tr></thead><tbody>
  <tr><td>공통</td><td>승인 전에 쓴 비용은 <span class="pill crit">불인정</span> · 영수증이 없으면 <span class="pill info">판단 필요</span></td></tr>
  <tr><td>항공</td><td>신청 때 검색한 견적보다 20% 넘게 높으면 <span class="pill info">판단 필요</span>(사유 필요), 아니면 <span class="pill good">인정</span></td></tr>
  <tr><td>숙박</td><td>박당 금액이 상한 이하면 <span class="pill good">인정</span>, 넘으면 <span class="pill warn">상한까지 인정</span></td></tr>
  <tr><td>식비</td><td>일 금액이 상한 이하면 <span class="pill good">인정</span>, 넘으면 <span class="pill warn">상한까지 인정</span>, 주류가 섞이면 <span class="pill info">판단 필요</span></td></tr>
  <tr><td>대중교통</td><td>출장지 안 이동은 대중교통이 원칙이므로 <span class="pill good">인정</span></td></tr>
  <tr><td>택시</td><td>22시 이후 탑승은 <span class="pill good">인정</span>, 긴급·대중교통 없음 사유는 <span class="pill info">판단 필요</span>, 그 외(22시 전 업무 종료 후)는 <span class="pill crit">불인정</span></td></tr>
  <tr><td>변경·취소</td><td>승인된 출장을 취소하려면 사유가 필요하고 팀장(없으면 재무총괄)이 승인합니다. "급한 업무", "OO님 요청"처럼 무엇이 왜 바뀌었는지 없는 사유는 접수되지 않습니다.</td></tr></tbody></table></div>`;
}

/* ---------- 세금계산서 점검 ---------- */
function taxRule(t) {
  const k = t.kind, c = t.cat;
  if (t.dir === 'out') {
    if (k === 'ovs') return {doc:'영세율 증빙', need:false, ev:true, why:'국외 법인 대상 용역은 영세율 — 세금계산서 대신 입금·계약 증빙을 보관'};
    if (k === 'ind') return {doc:'현금영수증', need:false, why:'비사업자 개인은 세금계산서 대신 현금영수증·카드전표로 증빙'};
    if (k === 'exempt' || c === 'exempt') return {doc:'계산서(면세)', need:true, why:'면세 거래는 세금계산서 대신 계산서를 발급'};
    return {doc:'세금계산서', need:true, why:'국내 과세 사업자 대상 과세 용역 — 발급 대상'};
  }
  if (k === 'ovs') return {doc:'세금계산서 없음', need:false, review:true, why:'국외 사업자 용역은 세금계산서를 받을 수 없음 — 대리납부 해당 여부 검토'};
  return {doc:'세금계산서', need:true, why:'국내 과세 사업자 매입 — 수취해야 매입세액 공제 증빙이 됨'};
}
function dueOf(date) {
  const d = new Date(P(date)); let y = d.getUTCFullYear(), m = d.getUTCMonth() + 2; if (m > 12) { m = 1; y++; }
  let ms = Date.UTC(y, m - 1, 10); const wd = new Date(ms).getUTCDay(); if (wd === 6) ms += 2 * MS; else if (wd === 0) ms += MS;
  return I(ms);
}
function taxState(t) {
  const r = taxRule(t), due = dueOf(t.date), asOf = S.asOf, out = t.dir === 'out';
  if (!r.need) {
    if (r.ev && !t.evi && !t.ack) return {k:'check', label:'증빙 확인 필요', note:'영세율 증빙(입금·계약) 미첨부', due, r};
    if (r.review && !t.ack) return {k:'check', label:'대리납부 검토', note:r.why, due, r};
    return {k:'na', label:'대상 아님', note:r.why, due, r};
  }
  if (t.doc) {
    if (!t.ack) {
      if (t.cat === 'taxable' && t.total !== t.supply + t.vat) return {k:'check', label:'합계 불일치', note:'공급가액 + 세액 ≠ 합계 (' + num(t.supply + t.vat - t.total) + '원 차이)', due, r};
      if (t.cat === 'taxable' && t.vat !== Math.round(t.supply * 0.1)) return {k:'check', label:'세액 확인', note:'세액이 공급가액의 10%와 다름 (' + num(t.vat - Math.round(t.supply * 0.1)) + '원 차이)', due, r};
      if (!t.bn) return {k:'check', label:'사업자번호 누락', note:'거래처 사업자번호가 비어 있음', due, r};
      if (S.tx.some((o) => o.id < t.id && o.doc && o.dir === t.dir && o.party === t.party && o.supply === t.supply && Math.abs(diff(o.date, t.date)) <= 7)) return {k:'check', label:'중복 발행 의심', note:'같은 거래처·같은 금액의 발급 건이 1주일 안에 또 있음', due, r};
    }
    if (t.issuedDate > due) return {k:'late', label:'지연 ' + (out ? '발행' : '수취'), note:(out ? '발행' : '수취') + 'ㆍ' + fmt(t.issuedDate) + ' — 기한 ' + fmt(due) + ' 이후 (가산세 검토)', due, r};
    return {k:'ok', label:'정상', note:(out ? '발행' : '수취') + ' ' + fmt(t.issuedDate), due, r};
  }
  const left = diff(due, asOf);
  const w = out ? '미발행' : '미수취';
  if (left < 0) return {k:'overdue', label:w + ' · ' + (-left) + '일 지남', note:'기한 ' + fmt(due), due, left, r};
  if (left <= S.soon) return {k:'soon', label:w + ' · D-' + left, note:'기한 ' + fmt(due), due, left, r};
  return {k:'sched', label:w + ' · D-' + left, note:'기한 ' + fmt(due), due, left, r};
}
const TCLS = {overdue:'crit', soon:'warn', sched:'info', check:'warn', late:'warn', ok:'good', na:'gray'};
const TNAME = {overdue:'기한 지남', soon:'임박', sched:'예정', check:'확인 필요', late:'지연 발행·수취', ok:'정상', na:'대상 아님'};
function checker(c) {
  const out = c.dir === 'out'; let doc, need = false, why;
  if (out) {
    if (c.party === 'ovs') { if (c.nature === 'zero') { doc = '세금계산서 발급 불필요 (영세율)'; why = '국외 법인에 제공하는 용역은 영세율입니다. 발급 대신 입금·계약 증빙을 보관하세요.'; } else { doc = '검토 필요'; why = '국외 상대방과의 과세·면세 거래는 세무 담당자 확인이 필요합니다.'; } }
    else if (c.party === 'ind') { doc = '현금영수증·카드전표'; why = '비사업자 개인에게는 세금계산서 대신 현금영수증 등으로 증빙합니다.'; }
    else if (c.nature === 'taxable') { doc = '세금계산서 발행'; need = true; why = '국내 사업자 대상 과세 거래입니다.'; }
    else if (c.nature === 'exempt') { doc = '계산서(면세) 발행'; need = true; why = '면세 거래는 세금계산서 대신 계산서를 발급합니다.'; }
    else { doc = '영세율 세금계산서 발행'; need = true; why = '국내 사업자 대상 영세율 거래(내국신용장 등)는 영세율 세금계산서를 발급합니다.'; }
  } else {
    if (c.party === 'ovs') { doc = '세금계산서 없음 · 대리납부 검토'; why = '국외 사업자에게는 세금계산서를 받을 수 없습니다. 대리납부 해당 여부를 확인하세요.'; }
    else if (c.party === 'ind') { doc = '카드전표·현금영수증 수취'; why = '개인 거래는 카드전표 등으로 증빙을 남깁니다.'; }
    else if (c.nature === 'exempt') { doc = '계산서(면세) 수취'; need = true; why = '면세 거래는 계산서를 받습니다.'; }
    else { doc = '세금계산서 수취'; need = true; why = '국내 과세 사업자 매입은 수취해야 매입세액 공제 증빙이 됩니다.'; }
  }
  return {doc, need, why, due:need ? dueOf(c.date) : null};
}
function taxView() {
  const all = S.tx, st = all.map((t) => ({t, s:taxState(t)}));
  const cnt = {}; st.forEach((x) => { cnt[x.s.k] = (cnt[x.s.k] || 0) + 1; });
  const open = st.filter((x) => ['overdue', 'soon', 'sched'].includes(x.s.k));
  const openSup = open.reduce((a, x) => a + x.t.supply, 0), openVat = open.reduce((a, x) => a + x.t.vat, 0);
  const ck = checker(S.ck);
  let list = st.filter((x) => (S.tf === 'all' || x.s.k === S.tf) && (S.tdir === 'all' || x.t.dir === S.tdir) && (S.tm === 'all' || x.t.date.slice(0, 7) === S.tm) && (!S.tq || (x.t.party + x.t.item).includes(S.tq)));
  const order = {overdue:0, soon:1, check:2, late:3, sched:4, ok:5, na:6};
  list.sort((a, b) => order[a.s.k] - order[b.s.k] || P(a.t.date) - P(b.t.date));
  const months = ['2026-09', '2026-10'].map((m) => {
    const xs = st.filter((x) => x.t.date.slice(0, 7) === m && taxRule(x.t).need), done = xs.filter((x) => x.t.doc).length, rest = xs.filter((x) => !x.t.doc).length, ch = st.filter((x) => x.t.date.slice(0, 7) === m && x.s.k === 'check').length;
    const dueM = dueOf(m + '-15');
    return `<div class="card"><div style="display:flex;justify-content:space-between;align-items:baseline"><b>${+m.slice(5)}월 마감</b><span class="s2">발행·수취 기한 ${fmt(dueM)}</span></div><div class="pbar"><i style="width:${xs.length ? done / xs.length * 100 : 0}%"></i></div><div class="s2" style="margin:6px 0">증빙이 필요한 ${xs.length}건 중 ${done}건 완료 · 남음 ${rest}건 · 확인 필요 ${ch}건</div>${rest + ch === 0 ? '<span class="pill good">마감 가능</span>' : `<span class="pill ${rest && diff(dueM, S.asOf) < 0 ? 'crit' : 'warn'}">마감 전 ${rest + ch}건 남음</span>`}</div>`;
  }).join('');
  const kp = (k, l, cls) => `<div class="kpi ${cls || ''}"><div class="n">${cnt[k] || 0}</div><div class="l">${l}</div></div>`;
  return `<div class="two"><div class="card"><div class="h2" style="margin-top:0">세금계산서 발행 대상 판정기 <small>거래 하나를 넣어 보세요</small></div>
  <div class="fgrid"><label>거래 방향${sel([['out', '매출 (우리가 청구)'], ['in', '매입 (우리가 지급)']], S.ck.dir, 'ck.dir')}</label><label>상대방${sel([['dom', '국내 사업자'], ['ovs', '해외 법인·사업자'], ['ind', '개인(비사업자)']], S.ck.party, 'ck.party')}</label>
  <label>거래 성격${sel([['taxable', '과세'], ['exempt', '면세'], ['zero', '영세율(수출·국외 제공)']], S.ck.nature, 'ck.nature')}</label><label>공급일<input type="date" value="${S.ck.date}" data-f="ck.date"></label></div>
  <div class="pr" style="margin-top:12px"><div class="big"><span class="pill ${ck.need ? 'crit' : 'gray'}">${ck.need ? '발급·수취 필요' : '발급 대상 아님'}</span> ${esc(ck.doc)}</div>
  <div style="margin:8px 0;line-height:1.7">${esc(ck.why)}</div>${ck.due ? `<div class="s2">기한: 공급일이 속한 달의 다음 달 10일 → <b>${fmt(ck.due)}</b> (주말이면 다음 영업일) · 오늘 기준 D${diff(ck.due, TODAY) >= 0 ? '-' + diff(ck.due, TODAY) : '+' + (-diff(ck.due, TODAY))}</div>` : ''}</div>
  <div class="cap">⚠ 단순화한 데모 규칙입니다. 실제 세무 판단은 세무 담당자·세무사 확인이 필요합니다.</div></div>
  <div class="card"><div class="h2" style="margin-top:0">점검 기준 <small>바꾸면 아래가 즉시 다시 계산됩니다</small></div>
  <div class="fgrid"><label>점검 기준일<input type="date" value="${S.asOf}" data-f="asOf"></label><label>임박 기준 (기한 며칠 전부터) · <b>${S.soon}일</b><input type="range" min="1" max="20" value="${S.soon}" data-f="soon" style="padding:0"></label></div>
  <div class="chips" style="margin-top:10px"><button class="chip" data-d="2026-10-28">오늘(10/28)</button><button class="chip" data-d="2026-11-06">11/06 (기한 4일 전)</button><button class="chip" data-d="2026-11-11">11/11 (10월분 기한 다음 날)</button></div>
  <div class="cap" style="margin-top:8px">기한은 공급일이 속한 달의 다음 달 10일입니다(주말이면 다음 영업일). 기준일을 11/11로 바꾸면 10월분 미발행이 모두 "기한 지남"으로 바뀝니다.</div></div></div>
  <div class="h2">현황 <small>기준일 ${fmt(S.asOf)} · 아직 처리되지 않은 건의 공급가액 ${num(openSup)}원 · 세액 ${num(openVat)}원</small></div>
  <div class="kpis" style="grid-template-columns:repeat(6,1fr)">${kp('overdue', '기한 지남', 'crit')}${kp('soon', '임박', 'warn')}${kp('sched', '예정')}${kp('check', '확인 필요', 'warn')}${kp('late', '지연 발행·수취')}${kp('ok', '정상', 'good')}</div>
  <div class="h2">월 마감 점검 <small>매월 세금계산서를 발행·수취하고 월 결산을 마감하는 일의 체크 화면</small></div><div class="two">${months}</div>
  <div class="h2">거래 목록 <small>${list.length}건</small></div>
  <div class="chips" style="margin-bottom:8px">${[['all', '전체'], ['overdue', '기한 지남'], ['soon', '임박'], ['sched', '예정'], ['check', '확인 필요'], ['late', '지연'], ['ok', '정상'], ['na', '대상 아님']].map(([k, n]) => `<button class="chip ${S.tf === k ? 'on' : ''}" data-tf="${k}">${n}<b>${k === 'all' ? all.length : (cnt[k] || 0)}</b></button>`).join('')}
  <span style="width:10px"></span>${[['all', '매출·매입'], ['out', '매출'], ['in', '매입']].map(([k, n]) => `<button class="chip ${S.tdir === k ? 'on' : ''}" data-tdir="${k}">${n}</button>`).join('')}
  ${[['all', '전체 월'], ['2026-08', '8월'], ['2026-09', '9월'], ['2026-10', '10월']].map(([k, n]) => `<button class="chip ${S.tm === k ? 'on' : ''}" data-tm="${k}">${n}</button>`).join('')}
  <input class="search" data-q="tq" placeholder="거래처·품목 검색" value="${esc(S.tq)}"></div>
  <div class="tw"><table><thead><tr><th>번호</th><th>구분</th><th>공급일</th><th>거래처 · 품목</th><th class="num">공급가액</th><th class="num">세액</th><th>필요 증빙</th><th>상태</th><th>조치</th></tr></thead><tbody>
  ${list.map(({t, s}) => `<tr class="${s.k === 'overdue' ? 'r' : s.k === 'soon' || s.k === 'check' ? 'r amber' : ''}"><td class="s2">${t.id}${t.doc ? '<br>' + t.doc : ''}</td><td>${t.dir === 'out' ? '매출' : '매입'}</td><td>${fmt(t.date)}</td><td><b>${esc(t.party)}</b><div class="s2">${esc(t.item)}${t.bn ? ' · ' + t.bn : ''}</div></td><td class="num">${num(t.supply)}</td><td class="num">${num(t.vat)}</td><td>${esc(s.r.doc)}</td><td><span class="pill ${TCLS[s.k]}">${s.label}</span><div class="s2">${esc(s.note)}</div></td><td style="white-space:nowrap">${s.k === 'overdue' || s.k === 'soon' || s.k === 'sched' ? `<button class="btn sm" data-a="treq" data-id="${t.id}">${t.dir === 'out' ? '발행 요청 문구' : '수취 요청 문구'}</button> <button class="btn sm ghost" data-a="tissue" data-id="${t.id}">${t.dir === 'out' ? '발행 완료' : '수취 완료'}</button>` : s.k === 'check' ? `<button class="btn sm ghost" data-a="tack" data-id="${t.id}">확인 완료</button>` : ''}</td></tr>`).join('') || '<tr><td colspan="9" class="empty">해당하는 거래가 없습니다.</td></tr>'}
  </tbody></table></div>
  <div class="cap">모든 거래처·번호·금액은 가상입니다. 필요 증빙과 기한은 위의 단순화한 규칙으로 계산한 값입니다.</div>`;
}

/* ---------- 법무 검토 데스크 ---------- */
const LST = ['접수', '담당 배정', '변호사 검토 중', '회신 도착', '완료·공유'];
const LRULE = {'계약서 검토':['이안', 7], '약관·정책':['하린', 7], '법적 리스크':['이안', 3], '기타':['이안', 7]};
function legalView() {
  const mineN = S.legal.filter((x) => x.req === '김데모').length;
  const flt = {active:(x) => x.status !== '완료·공유', mine:(x) => x.req === '김데모', done:(x) => x.status === '완료·공유', all:() => true}[S.lf];
  const rows = S.legal.filter(flt);
  const menu = [['active', '진행 중', S.legal.filter((x) => x.status !== '완료·공유').length], ['mine', '내 건', mineN], ['done', '완료·공유', S.legal.filter((x) => x.status === '완료·공유').length], ['all', '전체', S.legal.length]];
  return `<div class="lgrid"><div class="lmenu">${menu.map(([k, n, c]) => `<button class="${S.lf === k ? 'on' : ''}" data-lf="${k}"><span>${n}</span><span>${c}</span></button>`).join('')}<button class="btn dk" style="justify-content:center" data-a="lnew">+ 새 검토 요청</button></div>
  <div><div class="note" style="margin-top:0">사내 법무 검토 요청을 등록하면 유형별 규칙으로 담당자가 배정되고, 변호사 회신과 결과 공유까지 한 줄로 추적합니다. 단계를 바꾸는 일은 BO 담당만 할 수 있습니다(위에서 보는 사람을 바꿔 보세요).</div>
  <div class="tw"><table><thead><tr><th>번호</th><th>검토 요청</th><th>유형</th><th>담당</th><th>진행 단계</th><th>회신 기한</th><th></th></tr></thead><tbody>
  ${rows.map((x) => { const i = LST.indexOf(x.status), od = x.due && x.status !== '완료·공유' && diff(x.due, S.asOf) < 0; return `<tr class="${od ? 'r' : ''}"><td class="s2">${x.id}</td><td><b>${esc(x.title)}</b><div class="s2">${esc(x.req)} · ${fmt(x.created)} 접수</div></td><td>${esc(x.type)}</td><td>${x.owner ? esc(x.owner) : '<span class="pill warn">미배정</span>'}</td><td>${stepDots(LST.slice(0, 5), i, i === 4)}</td><td>${x.due ? (od ? `<span class="pill crit">${-diff(x.due, S.asOf)}일 지남</span> ` : '') + fmt(x.due) : '<span class="s2">-</span>'}</td><td>${i < 4 ? `<button class="btn sm" data-a="ladv" data-id="${x.id}">→ ${LST[i + 1]}</button>` : ''}</td></tr>`; }).join('') || '<tr><td colspan="7" class="empty">표시할 요청이 없습니다. 왼쪽 "+ 새 검토 요청"으로 등록하세요.</td></tr>'}
  </tbody></table></div>
  <div class="h2">배정 규칙 <small>요청 유형에 따라 담당자와 회신 기한(영업일)이 정해집니다</small></div>
  <div class="tw"><table><thead><tr><th>유형</th><th>담당</th><th>회신 기한</th></tr></thead><tbody>${Object.keys(LRULE).map((k) => `<tr><td>${k}</td><td>${LRULE[k][0]}</td><td>접수 후 ${LRULE[k][1]}영업일</td></tr>`).join('')}</tbody></table></div></div></div>`;
}

/* ---------- 담당자 찾기 ---------- */
function aorView() {
  const list = DATA.aor[S.afil].filter((r) => !S.aq || (r[0] + r[1] + r[2] + r[3]).includes(S.aq));
  return `<div class="note">BO에 요청할 때 누구에게 해야 하는지 찾는 화면입니다. 업무마다 책임지는 <b>오너</b>와 실제로 처리하는 <b>실무자</b>가 다릅니다. 담당이 정해지지 않은 업무는 "확인 중"으로 표시해 빈 곳이 보이게 합니다.</div>
  <div class="chips" style="margin-bottom:8px">${[['KR', '한국 법인'], ['JP', '일본 법인']].map(([k, n]) => `<button class="chip ${S.afil === k ? 'on' : ''}" data-afil="${k}">${n}<b>${DATA.aor[k].length}</b></button>`).join('')}
  <span style="width:10px"></span>${['세금계산서', '출장', '급여', '계약서'].map((w) => `<button class="chip" data-aq="${w}">${w}</button>`).join('')}
  <input class="search" data-q="aq" placeholder="업무·담당자 검색" value="${esc(S.aq)}"></div>
  <div class="tw"><table><thead><tr><th>구분</th><th>하는 일</th><th>오너</th><th>실무자</th></tr></thead><tbody>
  ${list.map((r) => `<tr><td><b>${esc(r[0])}</b></td><td>${esc(r[1])}</td><td>${r[2].startsWith('(') ? '<span class="pill warn">확인 중</span>' : '● ' + esc(r[2])}</td><td>${r[3].startsWith('(') ? '<span class="pill warn">확인 중</span>' : '● ' + esc(r[3])}</td></tr>`).join('') || '<tr><td colspan="4" class="empty">검색 결과가 없습니다.</td></tr>'}
  </tbody></table></div>`;
}

/* ---------- 이벤트 ---------- */
function setPath(path, el) {
  const v = el.type === 'checkbox' ? el.checked : el.type === 'number' || el.type === 'range' ? +el.value : el.value;
  const p = path.split('.');
  if (p[0] === 'row') S.settle.rows[+p[1]][p[2]] = v;
  else if (p.length === 1) S[p[0]] = v;
  else S[p[0]][p[1]] = v;
}
document.addEventListener('change', (e) => { const el = e.target.closest('[data-f]'); if (el) { setPath(el.dataset.f, el); draw(true); } });
document.addEventListener('input', (e) => {
  const q = e.target.closest('[data-q]');
  if (q) { S[q.dataset.q] = q.value; const pos = q.selectionStart; draw(true); const n = document.querySelector('[data-q="' + q.dataset.q + '"]'); if (n) { n.focus(); n.setSelectionRange(pos, pos); } return; }
  const r = e.target.closest('input[type=range][data-f]'); if (r) { setPath(r.dataset.f, r); draw(true); const n = document.querySelector('[data-f="' + r.dataset.f + '"]'); if (n) n.focus(); }
});
document.addEventListener('click', (e) => {
  const g = (k) => { const b = e.target.closest('[' + k + ']'); return b ? b.getAttribute(k) : null; };
  let v;
  if ((v = g('data-sub'))) { S.sub = v; draw(true); return; }
  if ((v = g('data-tf'))) { S.tf = v; draw(true); return; }
  if ((v = g('data-tdir'))) { S.tdir = v; draw(true); return; }
  if ((v = g('data-tm'))) { S.tm = v; draw(true); return; }
  if ((v = g('data-lf'))) { S.lf = v; draw(true); return; }
  if ((v = g('data-afil'))) { S.afil = v; draw(true); return; }
  if ((v = g('data-aq'))) { S.aq = v; draw(true); return; }
  if ((v = g('data-d'))) { S.asOf = v; draw(true); return; }
  const b = e.target.closest('[data-a]'); if (b) act(b.dataset.a, b.dataset.id);
});
const tripOf = (id) => S.trips.find((t) => t.id === id);
function act(a, id) {
  const t = tripOf(id);
  if (a === 'goto') { S.tab = id; draw(); window.scrollTo(0, 0); return; }
  if (a === 'approve') { t.stage++; const n = (t.phase === 'settle' ? settleSteps(t) : stepsOf(t)).length; if (t.stage >= n) { if (t.phase === 'apply') { t.phase = 'trip'; t.stage = 0; toast('최종 승인 완료 · 이제 항공·숙소를 예약할 수 있습니다'); } else toast('지급 단계로 넘어갔습니다'); } else toast('승인했습니다 · 다음 차례에게 알림 봇이 DM을 보냅니다'); }
  else if (a === 'reject') { t.stage = 0; toast('반려했습니다 · 출장자에게 사유와 함께 돌아갑니다'); }
  else if (a === 'cancelreq') {
    openModal(`<h3>출장 취소 요청 · ${esc(t.id)}</h3><div class="s2">${esc(t.dest)} · ${fmt(t.start)}~${fmt(t.end)}</div><textarea id="cr" rows="4" placeholder="무엇이 왜 바뀌었는지 적어 주세요 (예: 거래처 일정이 11/20로 연기되어 현장 점검 대상이 사라짐)" style="margin-top:10px"></textarea><div class="s2">"급한 업무", "OO님 요청"만으로는 접수되지 않습니다.</div><div class="row"><button class="btn ghost" onclick="closeModal()">닫기</button><button class="btn dk" data-a="cancelsubmit" data-id="${t.id}">취소 요청 제출</button></div>`); return;
  }
  else if (a === 'cancelsubmit') {
    const r = $('cr').value.trim();
    if (r.length < 12 || /^(급한 (업무|일)|.{1,6}님 요청)\.?$/.test(r)) { toast('무엇이 왜 바뀌었는지 구체적으로 적어 주세요'); return; }
    t.cancel = {pending:true, reason:r}; closeModal(); toast('취소 요청을 제출했습니다 · 팀장 승인 대기');
  }
  else if (a === 'cancelok') { t.phase = 'cancelled'; t.cancel.pending = false; toast('취소를 승인했습니다'); }
  else if (a === 'cancelno') { t.cancel.pending = false; toast('취소 요청을 거절했습니다'); }
  else if (a === 'gosettle') { S.tab = 'trip'; S.sub = 'settle'; S.settle.trip = id; draw(); window.scrollTo(0, 0); return; }
  else if (a === 'nudgetrip') {
    const txt = `${t.who}님, 안녕하세요.\n${t.id}(${t.dest} 출장, ${fmt(t.start)}~${fmt(t.end)}) 정산 기한이 ${fmt(settleDue(t))}였습니다.\n영수증과 출장 보고서를 올려 정산을 제출해 주세요. 어려운 점이 있으면 알려 주세요.`;
    openModal(`<h3>정산 독촉 문구</h3><pre id="nt">${esc(txt)}</pre><div class="row"><button class="btn ghost" onclick="closeModal()">닫기</button><button class="btn dk" onclick="copy($('nt').textContent);closeModal();toast('복사했습니다')">복사하고 닫기</button></div>`); return;
  }
  else if (a === 'submitTrip') {
    const r = applyChecks();
    if (!r.ok) { toast(r.ck.find((c) => c[0] === 'crit')[1]); return; }
    const f = S.form, n = Math.max(...S.trips.map((q) => +q.id.slice(3))) + 1;
    S.trips.unshift({id:'TR-' + n, who:'김데모', ent:f.ent, dest:f.dest, start:f.start, end:f.end, type:f.type, purpose:f.purpose, est:r.est, phase:'apply', stage:0, team:'박팀장', noLead:S.me.noLead});
    S.form.dest = ''; S.form.purpose = ''; S.form.plan = ''; S.form.legacy = false; S.sub = 'mine'; toast('출장 신청을 제출했습니다 · BO 합의 단계부터 시작합니다');
  }
  else if (a === 'addrow') { S.settle.rows.push({cat:'식비', date:'2026-10-09', amt:0, qty:1, rec:true, alc:false}); }
  else if (a === 'delrow') { S.settle.rows.splice(+id, 1); }
  else if (a === 'submitSettle') {
    const tr = tripOf(S.settle.trip);
    if (!tr || tr.phase !== 'trip') { toast('정산할 출장을 고르세요'); return; }
    tr.phase = 'settle'; tr.stage = 0; S.sub = 'mine'; toast('정산을 제출했습니다 · BO 검토 단계부터 시작합니다');
  }
  else if (a === 'tissue') { const x = S.tx.find((q) => q.id === id); x.doc = 'DOC-' + (40000 + S.tx.indexOf(x)); x.issuedDate = S.asOf; toast((x.dir === 'out' ? '발행' : '수취') + ' 완료로 처리했습니다'); }
  else if (a === 'tack') { S.tx.find((q) => q.id === id).ack = true; toast('확인 완료로 처리했습니다'); }
  else if (a === 'treq') {
    const x = S.tx.find((q) => q.id === id), s = taxState(x), out = x.dir === 'out';
    const txt = out ? `[세금계산서 발행 요청]\n거래처: ${x.party}\n공급일: ${fmt(x.date)} · 품목: ${x.item}\n공급가액 ${num(x.supply)}원 / 세액 ${num(x.vat)}원\n발행 기한: ${fmt(s.due)}\n발행 후 번호를 이 스레드에 남겨 주세요.`
      : `[세금계산서 수취 요청]\n${x.party} 담당자님, 안녕하세요.\n${fmt(x.date)} ${x.item} 건(공급가액 ${num(x.supply)}원)의 세금계산서가 아직 확인되지 않습니다.\n${fmt(s.due)}까지 발행해 주시면 감사하겠습니다.`;
    openModal(`<h3>${out ? '발행' : '수취'} 요청 문구</h3><div class="s2">${esc(x.id)} · ${esc(s.label)}</div><pre id="nt">${esc(txt)}</pre><div class="row"><button class="btn ghost" onclick="closeModal()">닫기</button><button class="btn dk" onclick="copy($('nt').textContent);closeModal();toast('복사했습니다')">복사하고 닫기</button></div>`); return;
  }
  else if (a === 'lnew') {
    openModal(`<h3>새 검토 요청</h3><div class="fgrid" style="margin-top:8px"><label class="full">제목<input type="text" id="ln-t" placeholder="무엇을 검토받고 싶은지"></label><label>유형<select id="ln-y">${Object.keys(LRULE).map((k) => `<option>${k}</option>`).join('')}</select></label><label class="full">상세 내용<input type="text" id="ln-d" placeholder="배경과 확인하고 싶은 점 (10자 이상)"></label></div><div class="row"><button class="btn ghost" onclick="closeModal()">닫기</button><button class="btn dk" data-a="lsubmit">요청 등록</button></div>`); return;
  }
  else if (a === 'lsubmit') {
    const ti = $('ln-t').value.trim(), de = $('ln-d').value.trim(), ty = $('ln-y').value;
    if (ti.length < 5 || de.length < 10) { toast('제목은 5자, 상세 내용은 10자 이상 적어 주세요'); return; }
    const r = LRULE[ty]; S.legal.unshift({id:'LG-0' + (Math.max(...S.legal.map((q) => +q.id.slice(3))) + 1), title:ti, req:'김데모', type:ty, status:'담당 배정', owner:r[0], created:TODAY, due:addBiz(TODAY, r[1])});
    S.lf = 'active'; closeModal(); toast('등록했습니다 · ' + ty + ' 규칙으로 ' + r[0] + '님이 배정되었습니다');
  }
  else if (a === 'ladv') {
    if (S.role !== 'bo') { toast('단계를 바꾸는 일은 BO 담당만 할 수 있습니다 — 위에서 보는 사람을 "BO 담당"으로 바꿔 보세요'); return; }
    const x = S.legal.find((q) => q.id === id), i = LST.indexOf(x.status); x.status = LST[i + 1]; if (!x.owner) x.owner = LRULE[x.type][0]; toast(x.id + ' → ' + x.status);
  }
  draw(true);
}

function draw(keep) {
  const y = window.scrollY; drawTabs(); $('role').value = S.role;
  $('view').innerHTML = {home:homeView, trip:tripView, tax:taxView, legal:legalView, aor:aorView}[S.tab]();
  if (keep) window.scrollTo(0, y);
}
draw();
</script>

</body></html>"""

components.html(HTML, height=900, scrolling=True)
