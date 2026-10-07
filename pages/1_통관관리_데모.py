import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="통관관리 시스템 (데모)", page_icon="🛃", layout="wide")

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

HTML = r"""
<!doctype html>
<html lang="ko"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css">
<style>
:root{--accent:#e8435a;--accent-soft:#fdecef;--bg:#f6f6f8;--card:#fff;--sub:#f6f7f9;--text:#1b1d21;--muted:#9097a1;--line:#eef0f2;--ok:#16a34a;--warn:#d97706}
*{box-sizing:border-box}
html,body{height:100%}
body{margin:0;font-family:Pretendard,-apple-system,"Noto Sans KR",sans-serif;color:var(--text);font-size:14px;letter-spacing:-.2px;
 background:radial-gradient(circle at 100% 0%,#fde6ea 0,rgba(253,230,234,0) 32%),radial-gradient(circle at 60% 100%,#eef1ff 0,rgba(238,241,255,0) 30%),var(--bg);background-attachment:fixed}
button{font-family:inherit;cursor:pointer}
svg.i{width:16px;height:16px;fill:none;stroke:currentColor;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round;flex-shrink:0}
.app{display:flex;min-height:100vh}
/* sidebar */
.side{width:228px;flex-shrink:0;background:#fff;margin:12px 0 12px 12px;border-radius:22px;padding:22px 14px 14px;position:sticky;top:12px;height:calc(100vh - 24px);display:flex;flex-direction:column;box-shadow:0 1px 2px rgba(0,0,0,.03);transition:width .2s}
.brand{display:flex;justify-content:space-between;align-items:flex-start;padding:0 6px}
.logo{font-weight:800;font-size:19px;color:var(--accent);display:flex;align-items:center;gap:6px;white-space:nowrap}
.logo .mk{width:20px;height:20px;border-radius:6px;background:var(--accent);display:grid;place-items:center;color:#fff;font-size:11px}
.sub{font-size:9.5px;color:var(--muted);letter-spacing:4.5px;font-weight:700;margin-top:6px;padding-left:6px;white-space:nowrap}
.fold{width:28px;height:28px;border-radius:9px;border:0;background:var(--sub);color:#888;display:grid;place-items:center}
.user{display:flex;gap:10px;align-items:center;background:var(--sub);border-radius:16px;padding:12px;margin:18px 0 8px}
.avatar{width:36px;height:36px;border-radius:11px;background:var(--accent);color:#fff;display:grid;place-items:center;font-weight:700;flex-shrink:0}
.user b{display:block;font-size:13px}.user span{font-size:11px;color:var(--muted)}
.hello{font-size:11px;color:var(--muted);margin:2px 4px 12px;white-space:nowrap}
.nav-home{display:flex;align-items:center;gap:10px;width:100%;border:0;border-radius:14px;padding:11px 12px;background:transparent;font-weight:700;font-size:13px;color:var(--text)}
.nav-home .ib{width:28px;height:28px;border-radius:9px;display:grid;place-items:center;background:var(--sub)}
.nav-home.active{background:var(--accent);color:#fff;box-shadow:0 8px 18px rgba(232,67,90,.28)}
.nav-home.active .ib{background:rgba(255,255,255,.22)}
.sbox{display:flex;align-items:center;gap:8px;border:1px solid var(--line);border-radius:12px;padding:6px 6px 6px 12px;margin:10px 0 4px;color:#aaa}
.sbox input{border:0;outline:0;flex:1;font-size:12px;padding:4px 0;min-width:0;font-family:inherit;background:transparent}
.sbox button{width:26px;height:26px;border-radius:8px;border:0;background:var(--sub);color:#777;display:grid;place-items:center}
.navs{flex:1;overflow:auto;margin:0 -4px;padding:0 4px}
.group{font-size:10.5px;font-weight:700;color:#666;margin:16px 6px 4px;display:flex;align-items:center;gap:6px;white-space:nowrap}
.group i{width:5px;height:5px;border-radius:50%;display:inline-block}
.group:after{content:"";flex:1;height:1px;background:var(--line);margin-left:4px}
.nav{display:flex;align-items:center;gap:10px;width:100%;border:0;background:transparent;padding:7px 8px;border-radius:12px;font-size:13px;color:#2b2e33;text-align:left;white-space:nowrap}
.nav .ib{width:30px;height:30px;border-radius:10px;background:var(--sub);display:grid;place-items:center;color:#555;flex-shrink:0}
.nav:hover{background:var(--sub)}
.nav.active{background:var(--accent-soft);color:var(--accent);font-weight:700}.nav.active .ib{background:#fff;color:var(--accent)}
.nav.disabled{color:#c2c6cc}.nav.disabled .ib{color:#c9ccd1}.nav .soon{margin-left:auto;font-size:9.5px;color:#c9ccd1}
.foot{font-size:10px;color:#c2c6cc;padding:10px 6px 0;white-space:nowrap}
.side.mini{width:72px}.side.mini .lbl,.side.mini .sub,.side.mini .hello,.side.mini .user div:last-child,.side.mini .sbox,.side.mini .group,.side.mini .soon,.side.mini .foot,.side.mini .logo .tx{display:none}
.side.mini .brand{flex-direction:column;align-items:center;gap:10px}.side.mini .user{justify-content:center;padding:8px}.side.mini .nav,.side.mini .nav-home{justify-content:center;padding:6px}
/* main */
.main{flex:1;padding:40px 40px 60px;display:flex;justify-content:center;min-width:0}
.wrap{width:100%;max-width:1040px}
.head{display:flex;justify-content:space-between;align-items:flex-end;margin-bottom:18px;gap:12px}
.date{color:var(--accent);font-weight:700;font-size:12px}
h1{font-size:28px;margin:6px 0 0;letter-spacing:-.8px;font-weight:800}
.hr{display:flex;gap:8px;align-items:center}
.upd{border:0;background:none;color:var(--muted);font-size:12px;font-weight:600}
.pill{font-size:10.5px;font-weight:700;color:#a0742a;background:#fff4e2;border-radius:20px;padding:4px 9px}
h2{font-size:18px;margin:34px 0 12px;font-weight:800;letter-spacing:-.5px}h2 small{font-size:12px;color:var(--muted);font-weight:500;margin-left:8px;letter-spacing:0}
.card{background:var(--card);border-radius:22px;padding:20px;box-shadow:0 1px 2px rgba(0,0,0,.03)}
.kpis{display:grid;grid-template-columns:repeat(4,1fr);gap:12px}
.kpi{background:var(--sub);border-radius:16px;padding:18px 18px 16px;cursor:pointer;transition:.15s}
.kpi:hover{background:#f0f1f4}
.kpi .l{font-size:12px;color:#555;font-weight:600;display:flex;align-items:center;gap:6px}.kpi .l:before{content:"";width:5px;height:5px;border-radius:50%;background:#c8ccd2}
.kpi.hot .l:before{background:var(--accent)}
.kpi .n{font-size:36px;font-weight:800;margin:14px 0 22px;line-height:1}.kpi .n.zero{color:#d6d9de}.kpi .n small{font-size:12px;color:var(--muted);font-weight:500;margin-left:3px}
.kpi .go{font-size:12px;color:#555;font-weight:600;min-height:16px}
.chips{display:flex;gap:8px;flex-wrap:wrap;align-items:center;background:#fff;border-radius:18px;padding:12px 18px;box-shadow:0 1px 2px rgba(0,0,0,.03)}
.chips .t{color:var(--muted);font-size:12px;margin-right:6px}
.chip{background:var(--sub);border-radius:20px;padding:7px 13px;font-size:12px;color:#444}.chip b{font-size:16px;margin:0 5px;color:var(--text)}.chip em{font-style:normal;font-size:10.5px;color:var(--muted)}.chip em.up{color:var(--ok)}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:16px}
.ct{display:flex;justify-content:space-between;align-items:center;font-weight:700;font-size:14px;margin-bottom:6px}
.link{color:var(--accent);font-size:12px;font-weight:700;background:none;border:0;padding:0}
.row{display:flex;gap:12px;align-items:center;padding:12px 0;border-top:1px solid var(--line);min-width:0}.row:first-of-type{border-top:0}
.tag{background:var(--accent-soft);color:var(--accent);font-size:11px;font-weight:700;border-radius:8px;padding:4px 9px;white-space:nowrap;flex-shrink:0}
.tag.g{background:#e9f7ef;color:var(--ok)}.tag.y{background:#fff4e2;color:var(--warn)}
.row .tx{min-width:0;flex:1}.row b{display:block;font-size:13px;margin-bottom:3px}.row span.s{display:block;font-size:11px;color:var(--muted);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.empty{color:#b5bac2;font-size:12px;text-align:center;padding:20px}
.heat{display:grid;grid-template-columns:repeat(12,15px);gap:5px;margin-top:8px}.heat div{width:15px;height:15px;border-radius:4px}
.legend{font-size:10px;color:var(--muted);margin-top:12px;display:flex;align-items:center;gap:3px}.legend i{width:9px;height:9px;border-radius:2px;display:inline-block}
label{display:block;font-size:12px;font-weight:600;margin:14px 0 6px;color:#444}
input,select,textarea{width:100%;border:1px solid #e6e8eb;border-radius:12px;padding:11px 13px;font-family:inherit;font-size:13px;background:#fff;outline:0}
input:focus,select:focus,textarea:focus{border-color:#f3a3b0;box-shadow:0 0 0 3px var(--accent-soft)}
textarea{min-height:80px;resize:vertical}
.btn{background:var(--accent);color:#fff;border:0;border-radius:12px;padding:11px 20px;font-weight:700;font-size:13px}
.btn.ghost{background:var(--sub);color:var(--text)}.btn.sm{padding:7px 13px;font-size:12px;border-radius:10px}
.form2{display:grid;grid-template-columns:1fr 1fr;gap:0 14px}
table{width:100%;border-collapse:collapse;font-size:13px}th{text-align:left;font-size:11px;color:var(--muted);font-weight:600;padding:10px 8px;border-bottom:1px solid var(--line)}td{padding:12px 8px;border-bottom:1px solid var(--line)}tr:last-child td{border-bottom:0}
.res{font-size:11px;font-weight:700;border-radius:7px;padding:3px 8px;white-space:nowrap}
.res.가능{background:#e9f7ef;color:var(--ok)}.res.불가{background:var(--accent-soft);color:var(--accent)}.res.조건부{background:#fff4e2;color:var(--warn)}
.st{font-size:11px;font-weight:700;border-radius:7px;padding:3px 8px;background:var(--sub);color:#555;white-space:nowrap}
.filters{display:flex;gap:6px;margin:12px 0 4px}.filters button{border:1px solid #e6e8eb;background:#fff;border-radius:20px;padding:6px 13px;font-size:12px;color:#555}.filters button.on{background:var(--text);color:#fff;border-color:var(--text)}
.dict{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}.dict .card b{display:block;margin-bottom:8px}.dict .card p{margin:0;font-size:12px;color:#666;line-height:1.65}
.bars{display:flex;align-items:flex-end;gap:18px;height:180px;padding-top:10px}.bar{flex:1;text-align:center;font-size:11px;color:var(--muted)}.bar div{background:var(--accent);border-radius:7px 7px 0 0;margin-bottom:8px;opacity:.85}.bar b{display:block;color:var(--text);font-size:12px;margin-bottom:4px}
.typ{display:flex;align-items:center;gap:10px;margin:14px 0;font-size:12px}.typ span{width:56px}.typ .tr{flex:1;height:8px;background:var(--sub);border-radius:4px}.typ .tr div{height:8px;background:var(--accent);border-radius:4px}
.reply{margin-top:10px;background:var(--sub);border-radius:12px;padding:12px;font-size:12px;line-height:1.6}
.meta{font-size:12px;color:var(--muted);font-weight:500}
.toast{position:fixed;left:50%;bottom:24px;transform:translateX(-50%) translateY(16px);background:#1d1f23;color:#fff;padding:12px 18px;border-radius:12px;font-size:13px;opacity:0;transition:.25s;pointer-events:none;z-index:9}
.toast.show{opacity:1;transform:translateX(-50%)}
@media(max-width:900px){.app{flex-direction:column}.side{width:auto;height:auto;position:static;margin:12px}.navs{overflow:visible}.main{padding:16px}.kpis{grid-template-columns:repeat(2,1fr)}.grid2,.dict,.form2{grid-template-columns:1fr}.fold{display:none}}
</style></head><body>
<div class="app">
 <aside class="side" id="side">
  <div class="brand"><div class="logo"><span class="mk">C</span><span class="tx">CUSTOMS</span></div>
   <button class="fold" id="fold" title="접기"><svg class="i" viewBox="0 0 24 24"><path d="m11 17-5-5 5-5M18 17l-5-5 5-5"/></svg></button></div>
  <div class="sub">DESK · DEMO</div>
  <div class="user"><div class="avatar">원</div><div><b>원지호님</b><span>LOG · 승인권자</span></div></div>
  <div class="hello">오늘도 안전한 통관을 도와드릴게요.</div>
  <button class="nav-home" data-v="home"><span class="ib"><svg class="i" viewBox="0 0 24 24"><path d="M3 10.5 12 3l9 7.5V20a1 1 0 0 1-1 1h-5v-6H9v6H4a1 1 0 0 1-1-1z"/></svg></span><span class="lbl">홈</span></button>
  <div class="sbox"><svg class="i" viewBox="0 0 24 24"><circle cx="11" cy="11" r="7"/><path d="m21 21-4.3-4.3"/></svg><input id="gq" placeholder="통관검색"><button id="gqb"><svg class="i" viewBox="0 0 24 24"><path d="M5 12h14M13 6l6 6-6 6"/></svg></button></div>
  <div class="navs">
   <div class="group"><i style="background:var(--accent)"></i>통관가능문의</div>
   <button class="nav" data-v="inquiry"><span class="ib"><svg class="i" viewBox="0 0 24 24"><path d="M22 2 11 13"/><path d="M22 2 15 22l-4-9-9-4z"/></svg></span><span class="lbl">문의 접수</span></button>
   <button class="nav" data-v="answer"><span class="ib"><svg class="i" viewBox="0 0 24 24"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg></span><span class="lbl">답변 작성</span></button>
   <div class="group"><i style="background:#3b82f6"></i>통관정보</div>
   <button class="nav" data-v="search"><span class="ib"><svg class="i" viewBox="0 0 24 24"><circle cx="11" cy="11" r="7"/><path d="m21 21-4.3-4.3"/></svg></span><span class="lbl">통관정보 조회</span></button>
   <button class="nav" data-v="dict"><span class="ib"><svg class="i" viewBox="0 0 24 24"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20V3H6.5A2.5 2.5 0 0 0 4 5.5z"/><path d="M4 19.5V21h16"/></svg></span><span class="lbl">통관 품목사전</span></button>
   <button class="nav disabled" data-v="rules"><span class="ib"><svg class="i" viewBox="0 0 24 24"><path d="M14 3H6a1 1 0 0 0-1 1v16a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V8z"/><path d="M14 3v5h5"/></svg></span><span class="lbl">통관규정</span><span class="soon">준비중</span></button>
   <div class="group"><i style="background:var(--ok)"></i>이력 · 확정기준</div>
   <button class="nav" data-v="register"><span class="ib"><svg class="i" viewBox="0 0 24 24"><path d="M14 3H6a1 1 0 0 0-1 1v16a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V8z"/><path d="M14 3v5h5M12 11v6M9 14h6"/></svg></span><span class="lbl">이력 등록</span></button>
   <button class="nav" data-v="review"><span class="ib"><svg class="i" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="m8.5 12 2.5 2.5 4.5-5"/></svg></span><span class="lbl">확정 검토</span></button>
   <button class="nav" data-v="history"><span class="ib"><svg class="i" viewBox="0 0 24 24"><path d="M4 6h9M17 6h3M4 12h3M11 12h9M4 18h11M19 18h1"/><circle cx="15" cy="6" r="2"/><circle cx="9" cy="12" r="2"/><circle cx="17" cy="18" r="2"/></svg></span><span class="lbl">이력 관리</span></button>
   <button class="nav" data-v="incident"><span class="ib"><svg class="i" viewBox="0 0 24 24"><path d="M5 20V12M11 20V6M17 20v-9"/></svg></span><span class="lbl">물류사고 현황</span></button>
  </div>
  <div class="foot">CUSTOMS DESK · Portfolio demo</div>
 </aside>
 <main class="main"><div class="wrap" id="view"></div></main>
</div>
<div class="toast" id="toast"></div>
<script>
const DAY=['일','월','화','수','목','금','토'];const today=new Date();
function ago(n){const d=new Date(today);d.setDate(d.getDate()-n);return (d.getMonth()+1)+'/'+d.getDate();}
let inquiries=[
 {id:'Q-1042',item:'홍삼 농축액 240g',qty:2,carrier:'A특송',status:'회신대기',days:4,memo:'건강기능식품 해당 여부'},
 {id:'Q-1043',item:'리튬 보조배터리 20000mAh',qty:1,carrier:'B특송',status:'회신대기',days:1,memo:'항공 운송 가능 여부'},
 {id:'Q-1039',item:'건조 쑥 (한약재)',qty:3,carrier:'A특송',status:'회신도착',days:2,reply:'식물검역 대상 — 자체통관 불가'},
 {id:'Q-1040',item:'반려견 육포 간식',qty:5,carrier:'C특송',status:'회신도착',days:2,reply:'축산물 가공품 — 반입 불가'},
 {id:'Q-1036',item:'비타민C 1000mg 120정',qty:4,carrier:'B특송',status:'확정검토',days:3,reply:'개인사용 수량 이내 시 가능',answer:'6병 이하 조건부 가능으로 안내'}
];
let history=[
 {date:ago(1),item:'건조 쑥 (한약재)',hs:'1211.90',carrier:'A특송',result:'불가',reason:'식물검역 대상 품목 · 특송사 자체통관 판정'},
 {date:ago(2),item:'반려견 육포 간식',hs:'2309.10',carrier:'C특송',result:'불가',reason:'축산물 가공품 반입 제한 · 특송사 회신 기준'},
 {date:ago(5),item:'비타민C 1000mg',hs:'2106.90',carrier:'B특송',result:'조건부',reason:'개인사용 수량 이내'},
 {date:ago(7),item:'무선 이어폰',hs:'8518.30',carrier:'A특송',result:'가능',reason:'개인사용 목적'},
 {date:ago(9),item:'립스틱 3개 세트',hs:'3304.10',carrier:'B특송',result:'가능',reason:'화장품 개인사용 범위'},
 {date:ago(12),item:'리튬 보조배터리',hs:'8507.60',carrier:'C특송',result:'조건부',reason:'100Wh 이하만 항공 가능'},
 {date:ago(15),item:'향수 50ml',hs:'3303.00',carrier:'A특송',result:'조건부',reason:'인화성 — 별도 운송'},
 {date:ago(20),item:'전자담배 액상',hs:'2404.12',carrier:'B특송',result:'불가',reason:'니코틴 함유 제품 제한'},
 {date:ago(23),item:'캠핑용 가스버너',hs:'7321.11',carrier:'A특송',result:'가능',reason:'가스 미포함 본체만'}
];
let standards=[{title:'건강기능식품 개인사용 6병 기준',date:ago(3)}];
let weekNew={inq:2,reply:2,hist:1,std:1};
let current='home',filter='전체',query='',updatedAt=Date.now();
const $=s=>document.querySelector(s);
function toast(m){const t=$('#toast');t.textContent=m;t.classList.add('show');clearTimeout(t._h);t._h=setTimeout(()=>t.classList.remove('show'),2300);}
function esc(s){return String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));}
function cnt(s){return inquiries.filter(q=>q.status===s).length;}
function go(v){if(v==='rules'){toast('통관규정 메뉴는 준비 중입니다');return;}current=v;render();window.scrollTo(0,0);}
document.querySelectorAll('[data-v]').forEach(b=>b.onclick=()=>go(b.dataset.v));
$('#fold').onclick=()=>$('#side').classList.toggle('mini');
function gsearch(){query=$('#gq').value;filter='전체';go('search');}
$('#gqb').onclick=gsearch;$('#gq').onkeydown=e=>{if(e.key==='Enter')gsearch();};
function updLabel(){const m=Math.floor((Date.now()-updatedAt)/60000);return m<1?'방금 업데이트':m+'분 전 업데이트';}
function head(sec,title){return `<div class="head"><div><div class="date">${sec}</div><h1>${title}</h1></div><div class="hr"><span class="pill">DEMO · 가상 데이터</span><button class="upd" onclick="updatedAt=Date.now();render();toast('최신 상태로 새로고침했어요')">${updLabel()}</button></div></div>`;}
setInterval(()=>{const u=document.querySelector('.upd');if(u)u.textContent=updLabel();},30000);

const V={};
V.home=()=>{
 const wait=cnt('회신대기'),arrived=cnt('회신도착'),review=cnt('확정검토'),old=inquiries.filter(q=>q.status==='회신대기'&&q.days>=3).length;
 const todo=arrived+review;
 const ds=(today.getMonth()+1)+'월 '+today.getDate()+'일 '+DAY[today.getDay()]+'요일';
 const k=(l,n,g,v,hot)=>`<div class="kpi ${hot&&n?'hot':''}" onclick="go('${v}')"><div class="l">${l}</div><div class="n ${n?'':'zero'}">${n}<small>건</small></div><div class="go">${g?g+' ›':''}</div></div>`;
 let heat='';for(let r=0;r<7;r++)for(let c=0;c<12;c++){const lv=(r*7+c*13+c*c)%9<(c>8?6:3)?((r+c)%4)+1:0;heat+=`<div style="background:${['#f0f1f4','#f9d3da','#f3a6b3','#ec7489','#e8435a'][lv]}"></div>`;}
 const fails=history.filter(h=>h.result==='불가').slice(0,2);
 const tagOf=r=>r==='불가'?'<span class="tag">자체통관 불가</span>':r==='가능'?'<span class="tag g">통관 가능</span>':'<span class="tag y">조건부</span>';
 return head(ds,todo?`오늘 처리할 일이 ${todo}건 있어요`:'오늘은 처리할 일이 없어요')+`
 <div class="card"><div class="kpis">${k('회신 도착',arrived,'답변 작성하기','answer',1)}${k('확정 검토중',review,'검토하기','review',1)}${k('3일 넘은 회신 대기',old,'','answer',1)}${k('회신 대기 전체',wait+arrived,'진행 상황 보기','answer')}</div></div>
 <h2>업무 현황<small>이번 주 흐름과 최근 소식</small></h2>
 <div class="chips"><span class="t">이번 주</span>
  <span class="chip">문의 접수<b>${weekNew.inq}</b><em class="up">+${weekNew.inq}</em></span>
  <span class="chip">특송사 회신<b>${weekNew.reply}</b><em class="up">+${weekNew.reply}</em></span>
  <span class="chip">이력 등록<b>${weekNew.hist}</b><em class="up">+${weekNew.hist}</em></span>
  <span class="chip">확정 기준<b>${weekNew.std}</b><em class="up">+${weekNew.std}</em></span></div>
 <div class="grid2">
  <div><div class="card"><div class="ct">최근 통관 불가 사례</div>${fails.map(h=>`<div class="row"><span class="tag">${h.date}</span><div class="tx"><b>${esc(h.item)}</b><span class="s">${h.carrier} · HS ${h.hs} · ${esc(h.reason)}</span></div></div>`).join('')||'<div class="empty">사례가 없어요</div>'}</div>
   <div class="card" style="margin-top:16px"><div class="ct">최근 등록<button class="link" onclick="go('history')">전체 보기</button></div>${history.slice(0,2).map(h=>`<div class="row">${tagOf(h.result)}<div class="tx"><b>${esc(h.item)}</b><span class="s">${h.date} · ${h.carrier} · HS ${h.hs}</span></div></div>`).join('')}</div></div>
  <div><div class="card"><div class="ct">새로 확정된 기준<button class="link" onclick="go('search')">조회하기</button></div>${standards.slice(0,3).map(s=>`<div class="row"><span class="tag g">${s.date}</span><div class="tx"><b>${esc(s.title)}</b><span class="s">승인권자 확정 기준</span></div></div>`).join('')||'<div class="empty">아직 확정된 기준이 없어요</div>'}</div>
   <div class="card" style="margin-top:16px"><div class="ct">최근 12주 활동</div><div class="heat">${heat}</div><div class="legend">적음 <i style="background:#f0f1f4"></i><i style="background:#f9d3da"></i><i style="background:#f3a6b3"></i><i style="background:#ec7489"></i><i style="background:#e8435a"></i> 많음 · 문의·답변·등록</div></div></div>
 </div>`;};
V.inquiry=()=>head('통관가능문의','문의 접수')+`<div class="card" style="max-width:720px"><div class="form2">
 <div><label>품목명</label><input id="f_item" placeholder="예: 홍삼 농축액 240g"></div>
 <div><label>수량</label><input id="f_qty" type="number" value="1" min="1"></div></div>
 <label>특송사</label><select id="f_car"><option>A특송</option><option>B특송</option><option>C특송</option></select>
 <label>확인 요청 사항</label><textarea id="f_memo" placeholder="예: 건강기능식품 해당 여부"></textarea>
 <div style="margin-top:18px"><button class="btn" onclick="submitInq()">특송사에 문의 보내기</button></div></div>
 <h2>최근 접수</h2><div class="card"><table><tr><th>번호</th><th>품목</th><th>수량</th><th>특송사</th><th>경과</th><th>상태</th></tr>${inquiries.map(q=>`<tr><td>${q.id}</td><td>${esc(q.item)}</td><td>${q.qty}</td><td>${q.carrier}</td><td>${q.days}일</td><td><span class="st">${q.status}</span></td></tr>`).join('')}</table></div>`;
window.submitInq=()=>{const item=$('#f_item').value.trim();if(!item){toast('품목명을 입력해 주세요');return;}
 const n=Math.max(...inquiries.map(q=>+q.id.slice(2)))+1;inquiries.unshift({id:'Q-'+n,item,qty:+$('#f_qty').value||1,carrier:$('#f_car').value,status:'회신대기',days:0,memo:$('#f_memo').value});weekNew.inq++;
 toast('데모 모드: 목록에만 추가되고 특송사로 발송되지 않습니다');render();};
V.answer=()=>{const list=inquiries.filter(q=>q.status==='회신도착'||q.status==='회신대기');
 return head('통관가능문의','답변 작성')+(list.map(q=>`<div class="card" style="margin-bottom:14px"><div class="ct"><span>${esc(q.item)} &nbsp;<span class="st">${q.status}</span></span><span class="meta">${q.id} · ${q.carrier} · ${q.days}일 경과</span></div>
 ${q.memo?`<div class="meta">요청: ${esc(q.memo)}</div>`:''}
 ${q.status==='회신도착'?`<div class="reply"><b>특송사 회신</b><br>${esc(q.reply)}</div><label>고객 안내 답변</label><textarea id="a_${q.id}" placeholder="회신 내용을 바탕으로 답변을 작성하세요"></textarea><div style="margin-top:12px"><button class="btn sm" onclick="saveAns('${q.id}')">답변 저장 후 확정 검토 요청</button></div>`:`<div class="reply">특송사 회신을 기다리는 중입니다${q.days>=3?' — <b style="color:var(--accent)">3일 경과, 재요청 필요</b>':''}</div>`}</div>`).join('')||'<div class="card empty">작성할 답변이 없어요</div>');};
window.saveAns=id=>{const v=$('#a_'+id).value.trim();if(!v){toast('답변을 입력해 주세요');return;}const q=inquiries.find(x=>x.id===id);q.answer=v;q.status='확정검토';toast('데모 모드: 확정 검토로 넘어갔습니다 (저장되지 않음)');render();};
function rows(){return history.filter(h=>(filter==='전체'||h.result===filter)&&(h.item+h.hs+h.reason).toLowerCase().includes(query.toLowerCase()));}
V.search=()=>head('통관정보','통관정보 조회')+`<div class="card"><input id="q" placeholder="품목명, HS코드, 사유로 검색" value="${esc(query)}" oninput="query=this.value;document.getElementById('tbl').innerHTML=table(rows())">
 <div class="filters">${['전체','가능','조건부','불가'].map(f=>`<button class="${f===filter?'on':''}" onclick="filter='${f}';render()">${f}</button>`).join('')}</div><div id="tbl">${table(rows())}</div></div>`;
function table(rs){return rs.length?`<table><tr><th>등록일</th><th>품목</th><th>HS코드</th><th>특송사</th><th>결과</th><th>사유</th></tr>${rs.map(h=>`<tr><td>${h.date}</td><td>${esc(h.item)}</td><td>${h.hs}</td><td>${h.carrier}</td><td><span class="res ${h.result}">${h.result}</span></td><td>${esc(h.reason)}</td></tr>`).join('')}</table>`:'<div class="empty">검색 결과가 없어요</div>';}
V.dict=()=>{const cats=[['건강기능식품','개인사용 기준 수량 이내 시 통관 가능. 초과 시 정식 수입 절차 필요.','비타민|홍삼'],['식물·한약재','식물검역 대상. 대부분 특송 자체통관 불가.','쑥|한약'],['축산물 가공품','육포·소시지 등은 원칙적으로 반입 불가.','육포|축산'],['배터리 제품','리튬 배터리는 용량(Wh) 기준으로 항공 운송 가능 여부 결정.','배터리'],['화장품·향수','개인사용 범위 가능. 향수는 인화성으로 별도 운송.','립스틱|향수|화장품'],['니코틴 제품','전자담배 액상 등 니코틴 함유 제품 제한.','니코틴|전자담배']];
 return head('통관정보','통관 품목사전')+`<div class="dict">${cats.map(c=>`<div class="card"><b>${c[0]}</b><p>${c[1]}</p><p style="margin-top:10px;color:var(--muted)">관련 이력 ${history.filter(h=>new RegExp(c[2]).test(h.item+h.reason)).length}건</p></div>`).join('')}</div>`;};
V.register=()=>head('이력 · 확정기준','이력 등록')+`<div class="card" style="max-width:720px"><div class="form2">
 <div><label>품목명</label><input id="r_item"></div><div><label>HS코드</label><input id="r_hs" placeholder="예: 2106.90"></div>
 <div><label>특송사</label><select id="r_car"><option>A특송</option><option>B특송</option><option>C특송</option></select></div>
 <div><label>판정 결과</label><select id="r_res"><option>가능</option><option>조건부</option><option>불가</option></select></div></div>
 <label>사유</label><input id="r_reason"><div style="margin-top:18px"><button class="btn" onclick="saveHist()">이력 등록</button></div></div>`;
window.saveHist=()=>{const item=$('#r_item').value.trim();if(!item){toast('품목명을 입력해 주세요');return;}history.unshift({date:ago(0),item,hs:$('#r_hs').value||'-',carrier:$('#r_car').value,result:$('#r_res').value,reason:$('#r_reason').value||'-'});weekNew.hist++;toast('데모 모드: 이력이 화면에만 추가되었습니다');go('history');};
V.review=()=>{const list=inquiries.filter(q=>q.status==='확정검토');
 return head('이력 · 확정기준','확정 검토')+(list.map(q=>`<div class="card" style="margin-bottom:14px"><div class="ct"><span>${esc(q.item)}</span><span class="meta">${q.id} · ${q.carrier}</span></div>
 <div class="reply"><b>특송사 회신</b><br>${esc(q.reply||'-')}</div><div class="reply"><b>작성된 답변</b><br>${esc(q.answer||'-')}</div>
 <div style="margin-top:14px;display:flex;gap:8px"><button class="btn sm" onclick="approve('${q.id}')">승인 · 기준 확정</button><button class="btn sm ghost" onclick="rejectQ('${q.id}')">반려</button></div></div>`).join('')||'<div class="card empty">검토할 항목이 없어요</div>');};
window.approve=id=>{const q=inquiries.find(x=>x.id===id);q.status='완료';standards.unshift({title:q.item+' 기준',date:ago(0)});history.unshift({date:ago(0),item:q.item,hs:'-',carrier:q.carrier,result:/불가/.test(q.reply)?'불가':/조건|이내|이하/.test(q.reply)?'조건부':'가능',reason:q.reply||'-'});weekNew.std++;toast('데모 모드: 확정 기준에 추가되었습니다 (저장되지 않음)');render();};
window.rejectQ=id=>{const q=inquiries.find(x=>x.id===id);q.status='회신도착';toast('반려되어 답변 작성으로 돌아갔습니다');render();};
V.history=()=>head('이력 · 확정기준','이력 관리')+`<div class="card">${table(history)}</div>`;
V.incident=()=>{const ms=[];for(let i=5;i>=0;i--){const d=new Date(today.getFullYear(),today.getMonth()-i,1);ms.push((d.getMonth()+1)+'월');}
 const ns=[4,6,3,5,2,1],mx=Math.max(...ns);const types=[['파손',42],['분실',23],['오배송',20],['지연',15]];
 return head('이력 · 확정기준','물류사고 현황')+`<div class="grid2" style="margin-top:0"><div class="card"><div class="ct">월별 사고 건수</div><div class="bars">${ms.map((m,i)=>`<div class="bar"><b>${ns[i]}</b><div style="height:${ns[i]/mx*120}px"></div>${m}</div>`).join('')}</div></div>
 <div class="card"><div class="ct">유형별 비율</div>${types.map(t=>`<div class="typ"><span>${t[0]}</span><div class="tr"><div style="width:${t[1]}%"></div></div><b>${t[1]}%</b></div>`).join('')}</div></div>`;};
function render(){$('#view').innerHTML=V[current]();document.querySelectorAll('[data-v]').forEach(b=>b.classList.toggle('active',b.dataset.v===current));}
render();
</script></body></html>
"""

components.html(HTML, height=900, scrolling=True)
