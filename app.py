import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="통관관리 시스템 (데모)", page_icon="🛃", layout="wide")

st.markdown(
    "<style>.block-container{padding-top:1rem;padding-bottom:0;max-width:100%}</style>",
    unsafe_allow_html=True,
)

with st.sidebar:
    st.info(
        "실무에서 운영 중인 통관 문의·이력 관리 웹앱(Google Apps Script)을 "
        "포트폴리오용으로 재구성한 데모입니다.\n\n"
        "모든 데이터는 가상이며, 입력한 내용은 저장·발송되지 않습니다."
    )

HTML = r"""
<!doctype html>
<html lang="ko"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css">
<style>
:root{--accent:#e8435a;--accent-soft:#fdecef;--bg:#f5f6f8;--card:#fff;--sub:#f7f8fa;--text:#1d1f23;--muted:#8a909a;--line:#eceef1;--ok:#16a34a;--warn:#d97706}
*{box-sizing:border-box}
body{margin:0;font-family:Pretendard,-apple-system,"Noto Sans KR",sans-serif;background:var(--bg);color:var(--text);font-size:14px}
button{font-family:inherit;cursor:pointer}
.app{display:flex;min-height:100vh}
.side{width:220px;flex-shrink:0;background:#fff;margin:12px;border-radius:20px;padding:20px 14px;align-self:flex-start;position:sticky;top:12px}
.logo{font-weight:800;font-size:20px;color:var(--accent);letter-spacing:.5px;padding:0 6px}
.logo small{display:block;font-size:10px;color:var(--muted);letter-spacing:4px;font-weight:600;margin-top:2px}
.user{display:flex;gap:10px;align-items:center;background:var(--sub);border-radius:14px;padding:12px;margin:16px 0 6px}
.avatar{width:36px;height:36px;border-radius:10px;background:var(--accent);color:#fff;display:grid;place-items:center;font-weight:700}
.user b{display:block;font-size:13px}.user span{font-size:11px;color:var(--muted)}
.hello{font-size:11px;color:var(--muted);margin:6px 4px 12px}
.nav-home{display:flex;align-items:center;gap:8px;width:100%;border:0;border-radius:12px;padding:12px;background:transparent;font-weight:700;font-size:13px;color:var(--text)}
.nav-home.active{background:var(--accent);color:#fff;box-shadow:0 6px 16px rgba(232,67,90,.3)}
.group{font-size:11px;font-weight:700;color:#555;margin:18px 6px 6px;display:flex;align-items:center;gap:6px}
.group i{width:6px;height:6px;border-radius:50%;display:inline-block}
.nav{display:flex;align-items:center;gap:10px;width:100%;border:0;background:transparent;padding:9px 8px;border-radius:10px;font-size:13px;color:var(--text);text-align:left}
.nav:hover{background:var(--sub)}.nav.active{background:var(--accent-soft);color:var(--accent);font-weight:700}
.nav .ic{width:26px;height:26px;border-radius:8px;background:var(--sub);display:grid;place-items:center;font-size:12px}
.nav.disabled{color:#bbb}.nav .soon{margin-left:auto;font-size:10px;color:#bbb}
.main{flex:1;padding:24px 32px 60px;max-width:1080px}
.demo{background:#fff4e5;color:#9a5b00;border-radius:10px;padding:8px 12px;font-size:12px;margin-bottom:18px}
.date{color:var(--accent);font-weight:700;font-size:12px}
h1{font-size:26px;margin:4px 0 16px;letter-spacing:-.5px}
h2{font-size:18px;margin:28px 0 10px}h2 small{font-size:12px;color:var(--muted);font-weight:500;margin-left:6px}
.card{background:var(--card);border-radius:18px;padding:18px}
.kpis{display:grid;grid-template-columns:repeat(4,1fr);gap:12px}
.kpi{background:var(--sub);border-radius:14px;padding:16px;cursor:pointer;border:1px solid transparent}
.kpi:hover{border-color:var(--line)}
.kpi .l{font-size:12px;color:#666;font-weight:600}.kpi .l:before{content:"● ";color:#ccc;font-size:8px}
.kpi .n{font-size:34px;font-weight:800;margin:12px 0 18px}.kpi .n.zero{color:#d4d7dc}.kpi .n small{font-size:13px;color:var(--muted);font-weight:500}
.kpi .go{font-size:12px;color:#666;font-weight:600}
.chips{display:flex;gap:8px;flex-wrap:wrap;align-items:center;background:#fff;border-radius:16px;padding:12px 16px}
.chips .t{color:var(--muted);font-size:12px;margin-right:4px}
.chip{background:var(--sub);border-radius:20px;padding:6px 12px;font-size:12px}.chip b{font-size:15px;margin:0 4px}.chip em{font-style:normal;font-size:11px;color:var(--muted)}.chip em.up{color:var(--ok)}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:14px}
.ct{display:flex;justify-content:space-between;align-items:center;font-weight:700;margin-bottom:10px}
.link{color:var(--accent);font-size:12px;font-weight:700;cursor:pointer;background:none;border:0}
.row{display:flex;gap:12px;align-items:flex-start;padding:10px 0;border-top:1px solid var(--line)}.row:first-of-type{border-top:0}
.tag{background:var(--accent-soft);color:var(--accent);font-size:11px;font-weight:700;border-radius:8px;padding:3px 8px;white-space:nowrap}
.row b{display:block;font-size:13px}.row span{font-size:11px;color:var(--muted)}
.empty{color:var(--muted);font-size:12px;text-align:center;padding:16px}
.heat{display:grid;grid-template-columns:repeat(12,14px);gap:5px}.heat div{width:14px;height:14px;border-radius:3px}
.legend{font-size:10px;color:var(--muted);margin-top:10px;display:flex;align-items:center;gap:3px}.legend i{width:9px;height:9px;border-radius:2px;display:inline-block}
label{display:block;font-size:12px;font-weight:600;margin:12px 0 5px;color:#444}
input,select,textarea{width:100%;border:1px solid var(--line);border-radius:10px;padding:10px 12px;font-family:inherit;font-size:13px;background:#fff}
textarea{min-height:70px;resize:vertical}
.btn{background:var(--accent);color:#fff;border:0;border-radius:10px;padding:10px 18px;font-weight:700;font-size:13px}
.btn.ghost{background:var(--sub);color:var(--text)}.btn.sm{padding:6px 12px;font-size:12px}
table{width:100%;border-collapse:collapse;font-size:13px}th{text-align:left;font-size:11px;color:var(--muted);font-weight:600;padding:8px;border-bottom:1px solid var(--line)}td{padding:10px 8px;border-bottom:1px solid var(--line)}
.res{font-size:11px;font-weight:700;border-radius:6px;padding:3px 8px}
.res.가능{background:#e8f7ee;color:var(--ok)}.res.불가{background:var(--accent-soft);color:var(--accent)}.res.조건부{background:#fff4e5;color:var(--warn)}
.st{font-size:11px;font-weight:700;border-radius:6px;padding:3px 8px;background:var(--sub);color:#555}
.filters{display:flex;gap:6px;margin:10px 0}.filters button{border:1px solid var(--line);background:#fff;border-radius:20px;padding:5px 12px;font-size:12px}.filters button.on{background:var(--text);color:#fff;border-color:var(--text)}
.dict{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}.dict .card b{display:block;margin-bottom:6px}.dict .card p{margin:0;font-size:12px;color:#666;line-height:1.6}
.bars{display:flex;align-items:flex-end;gap:18px;height:170px;padding-top:10px}.bar{flex:1;text-align:center;font-size:11px;color:var(--muted)}.bar div{background:var(--accent);border-radius:6px 6px 0 0;margin-bottom:6px}.bar b{display:block;color:var(--text);font-size:12px;margin-bottom:4px}
.typ{display:flex;align-items:center;gap:10px;margin:10px 0;font-size:12px}.typ span{width:56px}.typ .tr{flex:1;height:8px;background:var(--sub);border-radius:4px}.typ .tr div{height:8px;background:var(--accent);border-radius:4px}
.toast{position:fixed;left:50%;bottom:24px;transform:translateX(-50%) translateY(20px);background:#1d1f23;color:#fff;padding:12px 18px;border-radius:12px;font-size:13px;opacity:0;transition:.25s;pointer-events:none;z-index:9}
.toast.show{opacity:1;transform:translateX(-50%)}
.reply{margin-top:8px;background:var(--sub);border-radius:10px;padding:10px;font-size:12px}
@media(max-width:820px){.app{flex-direction:column}.side{width:auto;position:static}.main{padding:16px}.kpis{grid-template-columns:repeat(2,1fr)}.grid2,.dict{grid-template-columns:1fr}}
</style></head><body>
<div class="app">
 <aside class="side">
  <div class="logo">CUSTOMS DESK<small>DEMO</small></div>
  <div class="user"><div class="avatar">원</div><div><b>원지호님</b><span>LOG · 승인권자</span></div></div>
  <div class="hello">오늘도 안전한 통관을 도와드릴게요.</div>
  <button class="nav-home" data-v="home">🏠 홈</button>
  <div class="group"><i style="background:var(--accent)"></i>통관가능문의</div>
  <button class="nav" data-v="inquiry"><span class="ic">✈️</span>문의 접수</button>
  <button class="nav" data-v="answer"><span class="ic">💬</span>답변 작성</button>
  <div class="group"><i style="background:#3b82f6"></i>통관정보</div>
  <button class="nav" data-v="search"><span class="ic">🔍</span>통관정보 조회</button>
  <button class="nav" data-v="dict"><span class="ic">📘</span>통관 품목사전</button>
  <button class="nav disabled" data-v="rules"><span class="ic">📄</span>통관규정<span class="soon">준비중</span></button>
  <div class="group"><i style="background:var(--ok)"></i>이력 · 확정기준</div>
  <button class="nav" data-v="register"><span class="ic">➕</span>이력 등록</button>
  <button class="nav" data-v="review"><span class="ic">✅</span>확정 검토</button>
  <button class="nav" data-v="history"><span class="ic">🗂️</span>이력 관리</button>
  <button class="nav" data-v="incident"><span class="ic">📊</span>물류사고 현황</button>
 </aside>
 <main class="main"><div class="demo">🔒 포트폴리오 데모 · 가상 데이터 · 입력 내용은 이 화면에서만 반영되고 저장·발송되지 않습니다</div><div id="view"></div></main>
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
 {date:ago(1),item:'건조 쑥 (한약재)',hs:'1211.90',carrier:'A특송',result:'불가',reason:'식물검역 대상 품목'},
 {date:ago(2),item:'반려견 육포 간식',hs:'2309.10',carrier:'C특송',result:'불가',reason:'축산물 가공품 반입 제한'},
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
let current='home',filter='전체',query='';
const $=s=>document.querySelector(s);
function toast(m){const t=$('#toast');t.textContent=m;t.classList.add('show');clearTimeout(t._h);t._h=setTimeout(()=>t.classList.remove('show'),2200);}
function esc(s){return String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));}
function cnt(s){return inquiries.filter(q=>q.status===s).length;}
function go(v){if(v==='rules'){toast('통관규정 메뉴는 준비 중입니다');return;}current=v;render();window.scrollTo(0,0);}
document.querySelectorAll('[data-v]').forEach(b=>b.onclick=()=>go(b.dataset.v));

const V={};
V.home=()=>{
 const wait=cnt('회신대기'),arrived=cnt('회신도착'),review=cnt('확정검토'),old=inquiries.filter(q=>q.status==='회신대기'&&q.days>=3).length;
 const todo=arrived+review;
 const d=today;const ds=(d.getMonth()+1)+'월 '+d.getDate()+'일 '+DAY[d.getDay()]+'요일';
 const k=(l,n,go,v)=>`<div class="kpi" onclick="go('${v}')"><div class="l">${l}</div><div class="n ${n?'':'zero'}">${n}<small> 건</small></div><div class="go">${go?go+' ›':'&nbsp;'}</div></div>`;
 let heat='';for(let r=0;r<7;r++)for(let c=0;c<12;c++){const lv=(r*7+c*13+c*c)%9<(c>8?6:3)?((r+c)%4)+1:0;const col=['#eef0f3','#f8c9d1','#f29aa9','#ec6a80','#e8435a'][lv];heat+=`<div style="background:${col}"></div>`;}
 const fails=history.filter(h=>h.result==='불가').slice(0,2);
 return `<div class="date">${ds}</div><h1>${todo?`오늘 처리할 일이 ${todo}건 있어요`:'오늘은 처리할 일이 없어요'}</h1>
 <div class="card"><div class="kpis">${k('회신 도착',arrived,'답변 작성하기','answer')}${k('확정 검토중',review,'검토하기','review')}${k('3일 넘은 회신 대기',old,'','answer')}${k('회신 대기 전체',wait+arrived,'진행 상황 보기','answer')}</div></div>
 <h2>업무 현황<small>이번 주 흐름과 최근 소식</small></h2>
 <div class="chips"><span class="t">이번 주</span>
  <span class="chip">문의 접수<b>${weekNew.inq}</b><em class="up">+${weekNew.inq}</em></span>
  <span class="chip">특송사 회신<b>${weekNew.reply}</b><em class="up">+${weekNew.reply}</em></span>
  <span class="chip">이력 등록<b>${weekNew.hist}</b><em class="up">+${weekNew.hist}</em></span>
  <span class="chip">확정 기준<b>${weekNew.std}</b><em class="up">+${weekNew.std}</em></span></div>
 <div class="grid2">
  <div><div class="card"><div class="ct">최근 통관 불가 사례</div>${fails.map(h=>`<div class="row"><span class="tag">${h.date}</span><div><b>${esc(h.item)}</b><span>${h.carrier} · ${esc(h.reason)}</span></div></div>`).join('')||'<div class="empty">사례가 없어요</div>'}</div>
   <div class="card" style="margin-top:14px"><div class="ct">최근 등록<button class="link" onclick="go('history')">전체 보기</button></div>${history.slice(0,2).map(h=>`<div class="row"><span class="tag">${h.result==='불가'?'자체통관 불가':h.result==='가능'?'통관 가능':'조건부'}</span><div><b>${esc(h.item)}</b><span>${h.date} · ${h.carrier} · HS ${h.hs}</span></div></div>`).join('')}</div></div>
  <div><div class="card"><div class="ct">새로 확정된 기준<button class="link" onclick="go('search')">조회하기</button></div>${standards.slice(0,3).map(s=>`<div class="row"><span class="tag">${s.date}</span><div><b>${esc(s.title)}</b><span>확정 기준</span></div></div>`).join('')||'<div class="empty">아직 확정된 기준이 없어요</div>'}</div>
   <div class="card" style="margin-top:14px"><div class="ct">최근 12주 활동</div><div class="heat">${heat}</div><div class="legend">적음 <i style="background:#eef0f3"></i><i style="background:#f8c9d1"></i><i style="background:#f29aa9"></i><i style="background:#ec6a80"></i><i style="background:#e8435a"></i> 많음 · 문의·답변·등록</div></div></div>
 </div>`;};
V.inquiry=()=>`<div class="date">통관가능문의</div><h1>문의 접수</h1><div class="card" style="max-width:640px">
 <label>품목명</label><input id="f_item" placeholder="예: 홍삼 농축액 240g">
 <label>수량</label><input id="f_qty" type="number" value="1" min="1">
 <label>특송사</label><select id="f_car"><option>A특송</option><option>B특송</option><option>C특송</option></select>
 <label>확인 요청 사항</label><textarea id="f_memo" placeholder="예: 건강기능식품 해당 여부"></textarea>
 <div style="margin-top:16px"><button class="btn" onclick="submitInq()">특송사에 문의 보내기</button></div></div>
 <h2>최근 접수</h2><div class="card"><table><tr><th>번호</th><th>품목</th><th>특송사</th><th>상태</th></tr>${inquiries.map(q=>`<tr><td>${q.id}</td><td>${esc(q.item)}</td><td>${q.carrier}</td><td><span class="st">${q.status}</span></td></tr>`).join('')}</table></div>`;
window.submitInq=()=>{const item=$('#f_item').value.trim();if(!item){toast('품목명을 입력해 주세요');return;}
 const n=Math.max(...inquiries.map(q=>+q.id.slice(2)))+1;inquiries.unshift({id:'Q-'+n,item,qty:+$('#f_qty').value||1,carrier:$('#f_car').value,status:'회신대기',days:0,memo:$('#f_memo').value});weekNew.inq++;
 toast('데모 모드: 목록에만 추가되고 특송사로 발송되지 않습니다');render();};
V.answer=()=>{const list=inquiries.filter(q=>q.status==='회신도착'||q.status==='회신대기');
 return `<div class="date">통관가능문의</div><h1>답변 작성</h1>${list.map(q=>`<div class="card" style="margin-bottom:12px"><div class="ct"><span>${esc(q.item)} <span class="st">${q.status}</span></span><span style="font-size:12px;color:var(--muted)">${q.id} · ${q.carrier} · ${q.days}일 경과</span></div>
 ${q.memo?`<div style="font-size:12px;color:#666">요청: ${esc(q.memo)}</div>`:''}
 ${q.status==='회신도착'?`<div class="reply"><b>특송사 회신</b><br>${esc(q.reply)}</div><label>고객 안내 답변</label><textarea id="a_${q.id}" placeholder="회신 내용을 바탕으로 답변을 작성하세요"></textarea><div style="margin-top:10px"><button class="btn sm" onclick="saveAns('${q.id}')">답변 저장 후 확정 검토 요청</button></div>`:`<div class="reply">특송사 회신을 기다리는 중입니다${q.days>=3?' — <b style="color:var(--accent)">3일 경과, 재요청 필요</b>':''}</div>`}</div>`).join('')||'<div class="card empty">작성할 답변이 없어요</div>'}`;};
window.saveAns=id=>{const v=$('#a_'+id).value.trim();if(!v){toast('답변을 입력해 주세요');return;}const q=inquiries.find(x=>x.id===id);q.answer=v;q.status='확정검토';toast('데모 모드: 확정 검토로 넘어갔습니다 (저장되지 않음)');render();};
V.search=()=>{const rs=history.filter(h=>(filter==='전체'||h.result===filter)&&(h.item+h.hs+h.reason).toLowerCase().includes(query.toLowerCase()));
 return `<div class="date">통관정보</div><h1>통관정보 조회</h1><div class="card"><input id="q" placeholder="품목명, HS코드, 사유로 검색" value="${esc(query)}" oninput="query=this.value;rerenderTable()">
 <div class="filters">${['전체','가능','조건부','불가'].map(f=>`<button class="${f===filter?'on':''}" onclick="filter='${f}';render()">${f}</button>`).join('')}</div><div id="tbl">${table(rs)}</div></div>`;};
function table(rs){return rs.length?`<table><tr><th>등록일</th><th>품목</th><th>HS코드</th><th>특송사</th><th>결과</th><th>사유</th></tr>${rs.map(h=>`<tr><td>${h.date}</td><td>${esc(h.item)}</td><td>${h.hs}</td><td>${h.carrier}</td><td><span class="res ${h.result}">${h.result}</span></td><td>${esc(h.reason)}</td></tr>`).join('')}</table>`:'<div class="empty">검색 결과가 없어요</div>';}
window.rerenderTable=()=>{const rs=history.filter(h=>(filter==='전체'||h.result===filter)&&(h.item+h.hs+h.reason).toLowerCase().includes(query.toLowerCase()));$('#tbl').innerHTML=table(rs);};
V.dict=()=>{const cats=[['건강기능식품','개인사용 기준 수량 이내 시 통관 가능. 초과 시 정식 수입 절차 필요.'],['식물·한약재','식물검역 대상. 대부분 특송 자체통관 불가.'],['축산물 가공품','육포·소시지 등은 원칙적으로 반입 불가.'],['배터리 제품','리튬 배터리는 용량(Wh) 기준으로 항공 운송 가능 여부 결정.'],['화장품·향수','개인사용 범위 가능. 향수는 인화성으로 별도 운송.'],['니코틴 제품','전자담배 액상 등 니코틴 함유 제품 제한.']];
 return `<div class="date">통관정보</div><h1>통관 품목사전</h1><div class="dict">${cats.map(c=>`<div class="card"><b>${c[0]}</b><p>${c[1]}</p><p style="margin-top:8px;color:var(--muted)">관련 이력 ${history.filter(h=>h.reason.includes(c[0].slice(0,2))||h.item.includes(c[0].slice(0,2))).length}건</p></div>`).join('')}</div>`;};
V.register=()=>`<div class="date">이력 · 확정기준</div><h1>이력 등록</h1><div class="card" style="max-width:640px">
 <label>품목명</label><input id="r_item"><label>HS코드</label><input id="r_hs" placeholder="예: 2106.90">
 <label>특송사</label><select id="r_car"><option>A특송</option><option>B특송</option><option>C특송</option></select>
 <label>판정 결과</label><select id="r_res"><option>가능</option><option>조건부</option><option>불가</option></select>
 <label>사유</label><input id="r_reason"><div style="margin-top:16px"><button class="btn" onclick="saveHist()">이력 등록</button></div></div>`;
window.saveHist=()=>{const item=$('#r_item').value.trim();if(!item){toast('품목명을 입력해 주세요');return;}history.unshift({date:ago(0),item,hs:$('#r_hs').value||'-',carrier:$('#r_car').value,result:$('#r_res').value,reason:$('#r_reason').value||'-'});weekNew.hist++;toast('데모 모드: 이력이 화면에만 추가되었습니다');go('history');};
V.review=()=>{const list=inquiries.filter(q=>q.status==='확정검토');
 return `<div class="date">이력 · 확정기준</div><h1>확정 검토</h1>${list.map(q=>`<div class="card" style="margin-bottom:12px"><div class="ct"><span>${esc(q.item)}</span><span style="font-size:12px;color:var(--muted)">${q.id} · ${q.carrier}</span></div>
 <div class="reply"><b>특송사 회신</b><br>${esc(q.reply||'-')}</div><div class="reply"><b>작성된 답변</b><br>${esc(q.answer||'-')}</div>
 <div style="margin-top:12px;display:flex;gap:8px"><button class="btn sm" onclick="approve('${q.id}')">승인 · 기준 확정</button><button class="btn sm ghost" onclick="rejectQ('${q.id}')">반려</button></div></div>`).join('')||'<div class="card empty">검토할 항목이 없어요</div>'}`;};
window.approve=id=>{const q=inquiries.find(x=>x.id===id);q.status='완료';standards.unshift({title:q.item+' 기준',date:ago(0)});history.unshift({date:ago(0),item:q.item,hs:'-',carrier:q.carrier,result:/불가/.test(q.reply)?'불가':/조건|이내|이하/.test(q.reply)?'조건부':'가능',reason:q.reply||'-'});weekNew.std++;toast('데모 모드: 확정 기준에 추가되었습니다 (저장되지 않음)');render();};
window.rejectQ=id=>{const q=inquiries.find(x=>x.id===id);q.status='회신도착';toast('반려되어 답변 작성으로 돌아갔습니다');render();};
V.history=()=>`<div class="date">이력 · 확정기준</div><h1>이력 관리</h1><div class="card">${table(history)}</div>`;
V.incident=()=>{const ms=[];for(let i=5;i>=0;i--){const d=new Date(today.getFullYear(),today.getMonth()-i,1);ms.push((d.getMonth()+1)+'월');}
 const ns=[4,6,3,5,2,1],mx=Math.max(...ns);const types=[['파손',42],['분실',23],['오배송',20],['지연',15]];
 return `<div class="date">이력 · 확정기준</div><h1>물류사고 현황</h1><div class="grid2"><div class="card"><div class="ct">월별 사고 건수</div><div class="bars">${ms.map((m,i)=>`<div class="bar"><b>${ns[i]}</b><div style="height:${ns[i]/mx*120}px"></div>${m}</div>`).join('')}</div></div>
 <div class="card"><div class="ct">유형별 비율</div>${types.map(t=>`<div class="typ"><span>${t[0]}</span><div class="tr"><div style="width:${t[1]}%"></div></div><b>${t[1]}%</b></div>`).join('')}</div></div>`;};
function render(){$('#view').innerHTML=V[current]();document.querySelectorAll('[data-v]').forEach(b=>b.classList.toggle('active',b.dataset.v===current));}
render();
</script></body></html>
"""

components.html(HTML, height=1150, scrolling=True)

with st.expander("이 시스템에 대해"):
    st.markdown(
        """
- **목적**: 해외 특송 통관 가능 여부 문의 → 특송사 회신 → 답변 작성 → 승인권자 확정 → 이력/기준 축적까지 한 화면에서 관리
- **주요 화면**: 홈 대시보드(처리할 일·주간 현황·12주 활동), 문의 접수, 답변 작성, 통관정보 조회, 품목사전, 이력 등록, 확정 검토, 이력 관리, 물류사고 현황
- **원본 구현**: Google Apps Script 웹앱 (사내 계정 로그인 기반)
- **이 데모**: 원본 화면 흐름을 가상 데이터로 재구성. 외부 시스템과 연결되지 않음
"""
    )
