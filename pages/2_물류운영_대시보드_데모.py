import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="물류 운영 대시보드 (데모)", page_icon="📦", layout="wide")

st.markdown(
    """<style>
.stApp{background:#0e1117}
[data-testid="stHeader"]{background:transparent}
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
:root{--bg:#0e1117;--panel:#151a23;--panel2:#1b212c;--line:#2a3343;--text:#e7eaf0;--muted:#8a93a6;--dim:#5d6678;
--blue:#4a8fe7;--orange:#f08a24;--green:#2fd07f;--red:#ff4d5e;--tan:#c9a46a;--yellow:#f2d35b;--violet:#8b7cf6}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--text);font-family:Pretendard,-apple-system,"Noto Sans KR",sans-serif;font-size:13px;letter-spacing:-.2px}
button{font-family:inherit;cursor:pointer}
.top{display:flex;justify-content:space-between;align-items:center;padding:14px 16px 10px;flex-wrap:wrap;gap:10px}
.title{font-size:19px;font-weight:800;letter-spacing:-.3px}.title span{color:var(--red)}
.tr{display:flex;align-items:center;gap:14px;font-size:12px;color:var(--muted)}
.clock{color:var(--text);font-size:13px;font-weight:600}.clock b{font-size:16px;font-variant-numeric:tabular-nums;margin-left:4px}
.ring{position:relative;width:30px;height:30px}.ring svg{transform:rotate(-90deg)}.ring span{position:absolute;inset:0;display:grid;place-items:center;font-size:9px;color:var(--blue)}
.demo{font-size:10px;font-weight:800;color:#0e1117;background:var(--yellow);border-radius:5px;padding:3px 7px}
.tabs{display:flex;gap:6px;padding:0 16px 12px}
.tab{background:var(--panel2);color:var(--muted);border:1px solid var(--line);border-radius:6px;padding:7px 14px;font-size:12px;font-weight:600}
.tab.on{background:var(--blue);color:#fff;border-color:var(--blue)}
.body{display:flex;gap:12px;padding:0 16px 24px}
.lnav{width:78px;flex-shrink:0;display:flex;flex-direction:column;gap:6px;position:sticky;top:10px;align-self:flex-start}
.ln{background:var(--panel2);border:1px solid var(--line);color:#b8c0cf;border-radius:6px;padding:8px 4px;font-size:11.5px;font-weight:600;position:relative}
.ln.on{background:var(--blue);color:#fff;border-color:var(--blue)}
.ln.alert{border-color:var(--red);color:#ff8a95}.ln.alert:after{content:"";position:absolute;right:6px;top:6px;width:6px;height:6px;border-radius:50%;background:var(--red);animation:pulse 1.6s infinite}
@keyframes pulse{50%{opacity:.25}}
.grid{flex:1;display:grid;grid-template-columns:1.12fr 1fr;gap:12px;min-width:0}
.col{display:flex;flex-direction:column;gap:12px;min-width:0}
.p{background:var(--panel);border:1px solid var(--line);border-radius:8px;padding:14px;transition:box-shadow .3s,border-color .3s}
.p.flash{border-color:var(--blue);box-shadow:0 0 0 3px rgba(74,143,231,.25)}
.h{font-size:13.5px;font-weight:800;margin-bottom:12px;display:flex;align-items:center;gap:7px}.h small{font-size:11px;color:var(--muted);font-weight:500}
.h .dot{width:9px;height:9px;border-radius:50%;background:var(--red);box-shadow:0 0 0 3px rgba(255,77,94,.18)}
.h .r{margin-left:auto;font-size:11px;color:var(--muted);font-weight:500}
.muted{color:var(--muted)}.dim{color:var(--dim)}
/* inbound */
.inb{display:flex;gap:14px;align-items:flex-end}
.inb .tot{background:var(--panel2);border:1px solid var(--line);border-radius:6px;padding:14px;width:170px;flex-shrink:0}
.inb .tot .l{font-size:11px;color:var(--muted)}.inb .tot .n{font-size:30px;font-weight:800;margin-top:12px}
.cbars{flex:1;display:flex;align-items:flex-end;justify-content:space-around;height:110px;gap:4px}
.cb{flex:1;min-width:0;white-space:nowrap;text-align:center;font-size:10px;color:var(--muted);display:flex;flex-direction:column;align-items:center;justify-content:flex-end;height:100%}
.cb .v{color:var(--text);font-weight:700;font-size:11px;margin-bottom:3px}.cb .bar{width:26px;background:var(--blue);border-radius:2px 2px 0 0;margin-bottom:6px}
.cb .no{color:var(--dim);margin-bottom:24px;font-size:10.5px}.cb small{font-size:9px;color:var(--dim)}
.prog{margin-top:14px}.prog .row{display:flex;justify-content:space-between;font-size:11.5px;margin-bottom:6px}
.track{height:6px;background:var(--panel2);border-radius:3px;overflow:hidden}.track div{height:100%;background:var(--blue);border-radius:3px;transition:width .6s}
/* stages */
.sel{background:var(--panel2);color:var(--text);border:1px solid var(--line);border-radius:5px;padding:4px 6px;font-size:11px;font-family:inherit}
.stages{display:grid;grid-template-columns:repeat(5,1fr);gap:8px;margin-top:10px}
.sc{background:var(--panel2);border:1px solid var(--line);border-radius:6px;padding:11px;min-width:0}
.sc .n{font-size:13px;font-weight:800;margin-bottom:8px}
.badges{display:flex;gap:5px;margin-bottom:12px;flex-wrap:wrap}
.bd{font-size:11px;font-weight:700;border-radius:4px;padding:3px 7px;white-space:nowrap}.bd b{font-size:15px;margin-right:2px}
.trio{display:flex;gap:10px;align-items:flex-end}.trio div{font-size:9.5px;color:var(--muted);white-space:nowrap}.trio b{display:block;font-size:18px;font-weight:800;color:var(--text);font-variant-numeric:tabular-nums}
.trio .bk b{color:var(--red)}
.spark{display:flex;align-items:flex-end;gap:2px;height:28px;margin-top:10px}.spark i{flex:1;border-radius:1px;opacity:.85}
.note{font-size:10px;color:var(--dim);margin-top:8px;line-height:1.5}
.cmp{font-size:10px;margin-top:6px;background:#202734;border-radius:3px;padding:3px 6px;display:inline-block}
.up{color:var(--green)}.down{color:var(--red)}
.two{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-top:8px}
.big{font-size:22px;font-weight:800}.kv{display:flex;gap:5px;flex-wrap:wrap;margin-top:10px}.kv span{background:#202734;border-radius:3px;padding:3px 7px;font-size:10.5px}
/* right */
.pipe{display:flex;height:34px;border-radius:4px;overflow:hidden}.pipe div{height:100%;transition:flex .6s}
.leg{display:flex;flex-wrap:wrap;gap:6px 12px;margin-top:10px;font-size:10.5px}.leg span{display:flex;align-items:center;gap:4px}.leg i{width:8px;height:8px;border-radius:2px;display:inline-block}.leg em{font-style:normal;color:var(--muted)}
.flow{display:grid;grid-template-columns:62px 1fr 46px;gap:8px;align-items:center;margin:9px 0}
.flow .l{text-align:right;font-size:10px;color:var(--muted)}.flow .l b{font-size:13px;color:var(--text)}
.flow .nm{font-size:10.5px;color:#c4cbd8;margin-bottom:3px}
.fb{height:13px;background:#232a37;border-radius:2px;overflow:hidden;display:flex}.fb div{height:100%;transition:width .6s}
.flow .rr{font-size:10px;color:var(--muted)}.flow .rr b{display:block;font-size:13px;color:var(--text)}
.hatch{background:repeating-linear-gradient(45deg,#3c4a63 0 3px,#232a37 3px 7px) !important}
.hatch.red{background:repeating-linear-gradient(45deg,#7a2d36 0 3px,#232a37 3px 7px) !important}
.cm{font-size:12px;line-height:1.75;margin:0;padding-left:18px;color:#cfd5e0}.cm b{color:var(--yellow)}
.foot{font-size:10px;color:var(--dim);margin-top:8px}
/* period / s&op */
.kpis{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin-bottom:12px}
.kt{background:var(--panel);border:1px solid var(--line);border-radius:8px;padding:14px}.kt .l{font-size:11px;color:var(--muted)}.kt .n{font-size:26px;font-weight:800;margin-top:8px}.kt .d{font-size:11px;margin-top:4px}
table{width:100%;border-collapse:collapse;font-size:12px}th{text-align:left;color:var(--muted);font-weight:600;font-size:11px;padding:8px;border-bottom:1px solid var(--line)}td{padding:9px 8px;border-bottom:1px solid #212836;font-variant-numeric:tabular-nums}
.chip{font-size:10.5px;font-weight:700;border-radius:4px;padding:2px 7px}
.toast{position:fixed;left:50%;bottom:20px;transform:translateX(-50%) translateY(14px);background:#e7eaf0;color:#0e1117;padding:10px 16px;border-radius:8px;font-size:12px;font-weight:600;opacity:0;transition:.25s;pointer-events:none}
.toast.show{opacity:1;transform:translateX(-50%)}
@media(max-width:1500px){.stages{grid-template-columns:repeat(3,1fr)}}
@media(max-width:1180px){.grid{grid-template-columns:1fr}}
@media(max-width:700px){.lnav{display:none}.stages{grid-template-columns:repeat(2,1fr)}.inb{flex-direction:column;align-items:stretch}.inb .tot{width:auto}.kpis{grid-template-columns:repeat(2,1fr)}}
</style></head><body>
<div class="top">
 <div class="title">LOG DASHBOARD - <span>OpsLens</span></div>
 <div class="tr"><span class="clock" id="clock"></span>
  <div class="ring"><svg width="30" height="30"><circle cx="15" cy="15" r="12" stroke="#2a3343" stroke-width="2.5" fill="none"/><circle id="arc" cx="15" cy="15" r="12" stroke="#4a8fe7" stroke-width="2.5" fill="none" stroke-dasharray="75.4" stroke-dashoffset="0" stroke-linecap="round"/></svg><span id="cd">60</span></div>
  <span id="basis"></span><span class="demo">DEMO · 가상 데이터</span></div>
</div>
<div class="tabs"><button class="tab on" data-t="live">실시간</button><button class="tab" data-t="period">기간분석</button><button class="tab" data-t="sop">S&amp;OP</button></div>
<div class="body"><nav class="lnav" id="lnav"></nav><div style="flex:1;min-width:0" id="view"></div></div>
<div class="toast" id="toast"></div>
<script>
const $=s=>document.querySelector(s);
const DAY=['일','월','화','수','목','금','토'];
const pad=n=>String(n).padStart(2,'0');
function toast(m){const t=$('#toast');t.textContent=m;t.classList.add('show');clearTimeout(t._h);t._h=setTimeout(()=>t.classList.remove('show'),2200);}
let tab='live',cmp='전일대비',flashId=null,flashUntil=0,basis=new Date(),countdown=60;

/* ---- 가상 데이터 ---- */
const S={
 carriers:[{n:'전일잔량',v:1},{n:'CJ대한통운',v:68,t:'09:58'},{n:'한진',v:0},{n:'롯데',v:0},{n:'로젠',v:0},{n:'우체국',v:0},{n:'쿠팡',v:0},{n:'기타',v:0}],
 forecast:271,
 stages:[
  {k:'입고',c:'var(--blue)',hex:'#4a8fe7',staff:4,pph:19.2,done:48,back:21,prev:42},
  {k:'피킹',c:'var(--violet)',hex:'#8b7cf6',staff:0,pph:0,done:0,back:2,prev:3},
  {k:'출고',c:'var(--orange)',hex:'#f08a24',staff:1,pph:14.5,done:11,back:0,prev:9},
  {k:'포장',c:'var(--green)',hex:'#2fd07f',staff:1,pph:16.7,done:9,back:2,prev:11}],
 nonpick:{done:11,back:20},
 confirm:{total:352,today:0,types:[['순차출고',5],['순서변경',4],['도착입고필요',3],['출고대기(단독)',3]]},
 issue:{open:87,done:0,created:0,todo:0,prog:51,wait:36,tags:[['1차 출고 미완',23],['고객클레임',15],['통관이슈',13]]},
 extra:{influ:3,issueB:3,arrive:3,merge:0,outWait:3,seq:5,order:4,nonpickB:129,outB:0},
 issueFlow:[['도착입고필요',0,3],['출고대기(단독)',0,3],['순차출고',0,5],['순서변경',0,4],['이슈백로그',0,3,1]],
 waitFlow:[['순차대기',100,'논피킹 내 비중',78],['분리대기',1,'논피킹 내 비중',1],['대형대기',0,'오늘 출고(실측)',0,'5 0/5']]
};
const hours=[9,10,11,12,13,14,15,16,17,18];
const curHour=()=>{const h=new Date().getHours();return Math.min(Math.max(h,9),18);};
const sparkData=S.stages.map((s,i)=>hours.map((h,j)=>s.staff?Math.round(4+((j*7+i*3)%6)+(j===3?-3:0)):0));

/* ---- 계산 ---- */
function pipeline(){const st=S.stages,e=S.extra;return [
 ['인플루언서',e.influ,'#ff6b8a'],['이슈백로그',e.issueB,'#ff4d5e'],['도착입고필요',e.arrive,'#9ec5ff'],['합포장필요',e.merge,'#b7c4d8'],
 ['입고백로그',st[0].back,'#4a8fe7'],['출고대기(단독)',e.outWait,'#3e75bf'],['순차출고',e.seq,'#5b7db1'],['순서변경',e.order,'#7486ad'],
 ['피킹백로그',st[1].back,'#f2d35b'],['논피킹백로그',e.nonpickB,'#c9a46a'],['출고백로그',st[2].back,'#f08a24'],['포장백로그',st[3].back,'#2fd07f'],['포장완료',st[3].done,'#cfd8e3']];}
const inbound=()=>S.carriers.reduce((a,c)=>a+c.v,0);
function expectedPct(){const d=new Date(),m=(d.getHours()-9)*60+d.getMinutes();return Math.max(0,Math.min(100,Math.round(m/(9*60)*100)));}

/* ---- 공통 ---- */
function tickClock(){const d=new Date();$('#clock').innerHTML=`${d.getFullYear()}-${pad(d.getMonth()+1)}-${pad(d.getDate())} (${DAY[d.getDay()]}) <b>${pad(d.getHours())}:${pad(d.getMinutes())}:${pad(d.getSeconds())}</b>`;
 countdown--;if(countdown<=0){countdown=60;basis=new Date();simulate(true);}
 $('#cd').textContent=countdown+'s';$('#arc').setAttribute('stroke-dashoffset',75.4*(1-countdown/60));
 $('#basis').textContent='데이터 기준 '+pad(basis.getHours())+':'+pad(basis.getMinutes());}
document.querySelectorAll('.tab').forEach(b=>b.onclick=()=>{tab=b.dataset.t;document.querySelectorAll('.tab').forEach(x=>x.classList.toggle('on',x===b));render();window.scrollTo(0,0);});

const NAV=[['종합','top'],['운영관제','top',1],['입하','p-inb'],['입고','sc-0'],['피킹','sc-1'],['출고','sc-2'],['포장','sc-3'],['논피킹','sc-4'],['확인·이슈','p-ci'],['이상알림','p-cm'],['리드타임','lead']];
let navOn='종합';
function renderNav(){$('#lnav').style.display=tab==='live'?'':'none';$('#lnav').innerHTML=NAV.map(n=>`<button class="ln ${n[0]===navOn?'on':''} ${n[2]?'alert':''}" data-n="${n[0]}">${n[0]}</button>`).join('');
 document.querySelectorAll('.ln').forEach(b=>b.onclick=()=>{const n=NAV.find(x=>x[0]===b.dataset.n);navOn=n[0];
  if(n[1]==='lead'){toast('배송 리드타임 분석은 왼쪽 메뉴의 app 페이지에서 볼 수 있어요');renderNav();return;}
  if(n[1]==='top'){window.scrollTo({top:0,behavior:'smooth'});renderNav();return;}
  flashId=n[1];flashUntil=Date.now()+1600;render();const el=document.getElementById(n[1]);if(el)el.scrollIntoView({behavior:'smooth',block:'center'});});}
const fl=id=>(flashId===id&&Date.now()<flashUntil)?'flash':'';

/* ---- 실시간 ---- */
function stageCard(s,i){const tot=s.done+s.back,pct=tot?Math.round(s.done/tot*100):0,sp=sparkData[i],mx=Math.max(...sp,1),ch=curHour();
 const diff=cmp==='전일대비'?s.done-s.prev:s.done-Math.round(s.prev*0.9);
 return `<div class="sc ${fl('sc-'+i)}" id="sc-${i}"><div class="n">${s.k}</div>
 <div class="badges"><span class="bd" style="background:${s.hex}26;color:${s.hex}"><b>${s.staff}명</b> 근무</span>${s.staff?`<span class="bd" style="background:#232a37;color:var(--text)"><b>${s.pph.toFixed(1)}</b> PPH</span>`:'<span class="bd dim" style="background:#1f2530">근무기록 없음</span>'}</div>
 <div class="trio"><div><b>${s.done}</b>처리량</div><div class="bk"><b>${s.back}</b>백로그</div><div><b>${pct}%</b>진행률</div></div>
 <div class="track" style="margin-top:9px;background:#232a37"><div style="width:${pct}%;background:${s.hex}"></div></div>
 <div class="spark">${sp.map((v,j)=>`<i style="height:${hours[j]<=ch?Math.max(2,v/mx*28):2}px;background:${hours[j]<=ch?s.hex:'#2a3343'}"></i>`).join('')}</div>
 <span class="cmp">${s.staff?`${cmp} <span class="${diff>=0?'up':'down'}">${diff>=0?'+':''}${diff}건</span>`:'처리량 비교 불가'}</span></div>`;}
function live(){
 const inb=inbound(),prog=Math.round(inb/S.forecast*100),exp=expectedPct(),pl=pipeline(),plTot=pl.reduce((a,x)=>a+x[1],0);
 const mxC=Math.max(...S.carriers.map(c=>c.v),1);
 const np=S.nonpick,npPct=Math.round(np.done/(np.done+np.back)*100);
 const flowRows=[['입고완료',S.stages[0],'#4a8fe7'],['피킹완료',S.stages[1],'#8b7cf6'],['논피킹완료',{done:np.done,back:np.back},'#c9a46a'],['출고완료',S.stages[2],'#f08a24'],['포장완료',S.stages[3],'#2fd07f']];
 const big=pl.slice().sort((a,b)=>b[1]-a[1])[0];
 const slow=S.stages.filter(s=>s.staff).map(s=>({k:s.k,p:Math.round(s.done/(s.done+s.back||1)*100)})).sort((a,b)=>a.p-b.p)[0];
 const comments=[
  `지금 가장 큰 백로그는 <b>"${big[0]}"</b>(${big[1]}건, 전체의 ${Math.round(big[1]/plTot*100)}%)예요.`,
  `입하 진행률 <b>${prog}%</b> — 시간 기준 예상치(${exp}%) 대비 ${prog>=exp?'<span class="up">앞서 있어요</span>':'<span class="down">뒤처져 있어요</span>'}.`,
  `근무 공정 중 진행률이 가장 낮은 곳은 <b>${slow.k}</b>(${slow.p}%)이에요.`,
  `확인필요주문이 <b>${S.confirm.total}건</b> 쌓여 있어요.`,
  `이슈 잔여 <b>${S.issue.open}건</b>, 오늘 새로 생긴 이슈 ${S.issue.created}건.`];
 return `<div class="grid"><div class="col">
 <div class="p ${fl('p-inb')}" id="p-inb"><div class="h"><span class="dot"></span>입하 <small>오늘 실시간</small></div>
  <div class="inb"><div class="tot"><div class="l">입하 총량 (오늘) 전일잔량+오늘입하</div><div class="n">${inb}</div></div>
  <div class="cbars">${S.carriers.map(c=>c.v?`<div class="cb"><span class="v">${c.v}</span><div class="bar" style="height:${Math.max(3,c.v/mxC*70)}px"></div>${c.n}${c.t?`<small>마지막 ${c.t}</small>`:''}</div>`:`<div class="cb"><span class="no">미입하</span>${c.n}</div>`).join('')}</div></div>
  <div class="prog"><div class="row"><span>예측 대비 진행률 <span class="muted">(요일별 4주 평균 ${S.forecast} 기준)</span></span><b>${prog}%</b></div><div class="track"><div style="width:${Math.min(prog,100)}%"></div></div></div></div>
 <div class="p"><div class="h"><span class="dot"></span>공정별 현황 <small>오늘 실시간</small></div>
  <div style="font-size:11px">비교기준: <select class="sel" onchange="cmp=this.value;render()">${['전일대비','전주 같은요일'].map(o=>`<option ${o===cmp?'selected':''}>${o}</option>`).join('')}</select></div>
  <div class="stages">${S.stages.map(stageCard).join('')}
   <div class="sc ${fl('sc-4')}" id="sc-4"><div class="n">논피킹 <span class="dim" style="font-weight:500;font-size:10px">확인 선확 작업</span></div>
   <div class="trio" style="margin-top:4px"><div><b>${np.done}</b>처리(추정)</div><div class="bk"><b>${np.back}</b>백로그</div></div>
   <div class="track" style="margin-top:9px;background:#232a37"><div style="width:${npPct}%;background:var(--tan)"></div></div>
   <div class="note">피킹 없이 바로 단포장되는 물량의 추정 백로그예요. 이슈·분리대기·대형대기 등을 뺀 순수 논피킹 물량 기준.</div></div></div>
  <div class="two" id="p-ci">
   <div class="sc ${fl('p-ci')}"><div class="n">확인필요주문 <span class="r dim" style="float:right;font-weight:500;font-size:10px">상세 →</span></div>
    <div class="trio"><div><b style="color:var(--red)">${S.confirm.total}</b>잔여(지금)</div><div><b>${S.confirm.today||'-'}</b>처리(오늘 해결)</div></div>
    <div class="kv">${S.confirm.types.map(t=>`<span>${t[0]} <b>${t[1]}</b></span>`).join('')}</div></div>
   <div class="sc ${fl('p-ci')}"><div class="n">이슈 (LOG) <span class="dim" style="float:right;font-weight:500;font-size:10px">상세 →</span></div>
    <div class="trio"><div><b style="color:var(--red)">${S.issue.open}</b>잔여(TODO+진행+대기)</div><div><b>${S.issue.done}</b>처리(오늘)</div><div><b style="color:var(--yellow)">${S.issue.created}</b>생성(오늘)</div></div>
    <div class="note" style="color:var(--muted)">TODO ${S.issue.todo} · 진행중 ${S.issue.prog} · 대기 ${S.issue.wait}</div>
    <div class="kv">${S.issue.tags.map(t=>`<span>${t[0]} <b>${t[1]}</b></span>`).join('')}</div></div></div>
  <div class="foot">⚠ 잔량은 "앞단계 − 뒷단계" 계산이라 약간의 오차가 있을 수 있어요 (피킹대기만 실측).</div></div>
 </div><div class="col">
 <div class="p"><div class="h"><span class="dot"></span>공정 파이프라인 <small>지금 남은 백로그 분포</small><span class="r">총 ${plTot}건</span></div>
  <div class="pipe">${pl.filter(x=>x[1]).map(x=>`<div title="${x[0]} ${x[1]}건" style="flex:${x[1]};background:${x[2]}"></div>`).join('')}</div>
  <div class="leg">${pl.map(x=>`<span><i style="background:${x[2]}"></i>${x[0]} ${x[1]} <em>${Math.round(x[1]/plTot*100)}%</em></span>`).join('')}</div></div>
 <div class="p"><div class="h">공정 흐름 <small>진하게=처리 · 연하게=잔량</small></div>
  ${flowRows.map(f=>{const d=f[1].done,b=f[1].back,t=d+b||1,p=Math.round(d/t*100);return `<div class="flow"><div class="l"><b>${d}</b> ${p}%<br>처리량</div><div><div class="nm">${f[0]}</div><div class="fb"><div style="width:${p}%;background:${f[2]}"></div><div style="width:${100-p}%;background:${f[2]}40"></div></div></div><div class="rr"><b>${b}</b>잔여량</div></div>`;}).join('')}</div>
 <div class="p"><div class="h">이슈 흐름 <small>진하게=오늘 처리(추정) · 빗금=확인필요주문 파생</small></div>
  ${S.issueFlow.map(f=>`<div class="flow"><div class="l"><b>${f[1]}</b> 0%<br>오늘 처리</div><div><div class="nm">${f[0]}</div><div class="fb"><div class="hatch ${f[3]?'red':''}" style="width:100%"></div></div></div><div class="rr"><b>${f[2]}</b>잔여</div></div>`).join('')}
  <div class="foot">※ "오늘 처리"는 오늘 첫 기록 대비 순감소분 추정치예요.</div></div>
 <div class="p"><div class="h">대기 흐름 <small>논피킹 세분화 — 태그 기반 실측</small></div>
  ${[['순차대기',S.extra.nonpickB-29,78],['분리대기',1,1],['대형대기',5,62]].map(w=>`<div class="flow"><div class="l"><b>${w[2]}%</b><br>비중</div><div><div class="nm">${w[0]}</div><div class="fb"><div style="width:${w[2]}%;background:var(--tan)"></div></div></div><div class="rr"><b>${w[1]}</b>잔여</div></div>`).join('')}</div>
 <div class="p ${fl('p-cm')}" id="p-cm"><div class="h">📋 오늘의 코멘트 <small>데이터에서 자동 생성</small></div><ul class="cm">${comments.map(c=>`<li>${c}</li>`).join('')}</ul></div>
 </div></div>`;}

/* ---- 실시간 시뮬레이션 (가상) ---- */
const rnd=n=>Math.floor(Math.random()*n);
function simulate(force){
 S.stages.forEach(s=>{if(!s.staff)return;const k=rnd(3);if(s.back>0){const m=Math.min(k,s.back);s.done+=m;s.back-=m;}if(rnd(4)===0)s.back+=1;});
 if(rnd(3)===0){S.carriers[1].v+=1;S.stages[0].back+=1;const d=new Date();S.carriers[1].t=pad(d.getHours())+':'+pad(d.getMinutes());}
 if(rnd(2)===0&&S.extra.nonpickB>0){S.extra.nonpickB--;S.nonpick.done++;S.nonpick.back=Math.max(0,S.nonpick.back-1);}
 if(rnd(5)===0&&S.confirm.total>0){S.confirm.total--;S.confirm.today++;}
 if(rnd(6)===0){S.issue.open--;S.issue.done++;S.issue.prog=Math.max(0,S.issue.prog-1);}
 if(rnd(9)===0){S.issue.open++;S.issue.created++;S.issue.todo++;}
 if(tab==='live'||force)render();}
setInterval(()=>simulate(false),5000);

/* ---- 기간분석 ---- */
const days=[...Array(14)].map((_,i)=>{const d=new Date();d.setDate(d.getDate()-13+i);const wd=d.getDay(),we=wd===0||wd===6;
 const out=we?Math.round(60+((i*37)%25)):Math.round(220+60*Math.sin(i/2)+((i*13)%30));
 return {lbl:(d.getMonth()+1)+'/'+d.getDate(),wd:DAY[wd],out,pph:we?12+((i*3)%3):15+((i*7)%40)/10,lead:3.6+((i*11)%17)/10,delay:we?0:2+((i*5)%9)};});
function period(){
 const W=1100,H=300,pl=36,pr=36,pt=16,pb=28,cw=(W-pl-pr)/days.length,mo=Math.max(...days.map(d=>d.out))*1.15;
 const y=v=>pt+(H-pt-pb)*(1-v/mo),yp=v=>pt+(H-pt-pb)*(1-(v-8)/(22-8));
 const avg=k=>days.reduce((a,d)=>a+d[k],0)/days.length;
 const wk=days.filter(d=>d.out>100);const totOut=days.reduce((a,d)=>a+d.out,0),totDelay=days.reduce((a,d)=>a+d.delay,0);
 let svg=`<svg viewBox="0 0 ${W} ${H}" width="100%" style="display:block">`;
 [0,.25,.5,.75,1].forEach(f=>{const v=Math.round(mo*f),yy=y(v);svg+=`<line x1="${pl}" x2="${W-pr}" y1="${yy}" y2="${yy}" stroke="#232a37"/><text x="${pl-6}" y="${yy+3}" fill="#5d6678" font-size="9" text-anchor="end">${v}</text>`;});
 days.forEach((d,i)=>{const x=pl+i*cw+cw*.2,bw=cw*.6;svg+=`<rect x="${x}" y="${y(d.out)}" width="${bw}" height="${H-pb-y(d.out)}" rx="2" fill="#4a8fe7" opacity="${d.wd==='토'||d.wd==='일'?.4:.85}"><title>${d.lbl} 출고 ${d.out}건</title></rect><text x="${x+bw/2}" y="${H-pb+14}" fill="#8a93a6" font-size="9" text-anchor="middle">${d.lbl}</text>`;});
 svg+=`<polyline fill="none" stroke="#f2d35b" stroke-width="2" points="${days.map((d,i)=>`${pl+i*cw+cw/2},${yp(d.pph)}`).join(' ')}"/>`;
 days.forEach((d,i)=>svg+=`<circle cx="${pl+i*cw+cw/2}" cy="${yp(d.pph)}" r="2.5" fill="#f2d35b"><title>${d.lbl} PPH ${d.pph.toFixed(1)}</title></circle>`);
 [8,15,22].forEach(v=>svg+=`<text x="${W-pr+6}" y="${yp(v)+3}" fill="#a89042" font-size="9">${v}</text>`);
 svg+='</svg>';
 const stageAvg=[['입고',19.4,18.1],['피킹',22.8,23.5],['출고',14.9,13.2],['포장',16.3,16.9]];
 return `<div class="kpis">
 <div class="kt"><div class="l">14일 평균 출고량(평일)</div><div class="n">${Math.round(wk.reduce((a,d)=>a+d.out,0)/wk.length)}<span class="muted" style="font-size:13px"> 건/일</span></div><div class="d up">▲ 6.2% 직전 14일 대비</div></div>
 <div class="kt"><div class="l">평균 PPH</div><div class="n">${avg('pph').toFixed(1)}</div><div class="d up">▲ 0.8 직전 14일 대비</div></div>
 <div class="kt"><div class="l">평균 배송 리드타임</div><div class="n">${avg('lead').toFixed(1)}<span class="muted" style="font-size:13px"> 일</span></div><div class="d down">▲ 0.3일 (지연)</div></div>
 <div class="kt"><div class="l">출고 지연률</div><div class="n">${(totDelay/totOut*100).toFixed(1)}<span class="muted" style="font-size:13px"> %</span></div><div class="d muted">지연 ${totDelay}건 / 출고 ${totOut}건</div></div></div>
 <div class="p"><div class="h">일별 출고량 &amp; PPH <small>최근 14일 · 막대=출고량 · 노란선=PPH(오른쪽 축) · 주말은 흐리게</small></div>${svg}</div>
 <div class="grid" style="margin-top:12px"><div class="p"><div class="h">공정별 평균 PPH <small>이번 주 vs 지난주</small></div>
  <table><tr><th>공정</th><th>이번 주</th><th>지난주</th><th>변화</th></tr>${stageAvg.map(s=>{const d=s[1]-s[2];return `<tr><td>${s[0]}</td><td>${s[1]}</td><td class="muted">${s[2]}</td><td class="${d>=0?'up':'down'}">${d>=0?'▲':'▼'} ${Math.abs(d).toFixed(1)}</td></tr>`;}).join('')}</table></div>
  <div class="p"><div class="h">요일별 평균 출고 <small>최근 14일</small></div>
  <table><tr><th>요일</th><th>평균 출고</th><th style="width:50%"></th></tr>${['월','화','수','목','금','토','일'].map(w=>{const ds=days.filter(d=>d.wd===w),a=ds.length?Math.round(ds.reduce((x,d)=>x+d.out,0)/ds.length):0;return `<tr><td>${w}</td><td>${a}</td><td><div class="track"><div style="width:${a/3}%"></div></div></td></tr>`;}).join('')}</table></div></div>`;}

/* ---- S&OP ---- */
function sop(){const pph=16.5,hrs=8,availBy={0:2,1:6,2:5,3:6,4:6,5:4,6:2};
 const rows=[...Array(7)].map((_,i)=>{const d=new Date();d.setDate(d.getDate()+i);const wd=d.getDay(),we=wd===0||wd===6;
  const fin=we?70+i*3:240+((i*29)%60),fout=Math.round(fin*0.95),need=Math.ceil(fout/(pph*hrs)*2.2),av=availBy[wd];
  return {lbl:(d.getMonth()+1)+'/'+d.getDate()+' ('+DAY[wd]+')',fin,fout,need,av,gap:av-need};});
 const short=rows.filter(r=>r.gap<0);
 return `<div class="kpis"><div class="kt"><div class="l">향후 7일 예측 입하</div><div class="n">${rows.reduce((a,r)=>a+r.fin,0)}</div><div class="d muted">요일별 4주 평균 기반</div></div>
 <div class="kt"><div class="l">기준 PPH</div><div class="n">${pph}</div><div class="d muted">최근 14일 평균</div></div>
 <div class="kt"><div class="l">인력 부족 예상일</div><div class="n" style="color:${short.length?'var(--red)':'var(--green)'}">${short.length}<span class="muted" style="font-size:13px"> 일</span></div><div class="d muted">${short.map(r=>r.lbl).join(', ')||'없음'}</div></div>
 <div class="kt"><div class="l">최대 부족 인원</div><div class="n">${Math.max(0,...short.map(r=>-r.gap))}<span class="muted" style="font-size:13px"> 명</span></div><div class="d muted">공정 간 재배치 필요</div></div></div>
 <div class="p"><div class="h">수요 예측 vs 가용 인력 <small>필요 인원 = 예측 출고 ÷ (PPH × 8h) × 공정 계수 2.2</small></div>
 <table><tr><th>날짜</th><th>예측 입하</th><th>예측 출고</th><th>필요 인원</th><th>가용 인원</th><th>과부족</th></tr>
 ${rows.map(r=>`<tr><td>${r.lbl}</td><td>${r.fin}</td><td>${r.fout}</td><td>${r.need}명</td><td>${r.av}명</td><td><span class="chip" style="background:${r.gap<0?'#ff4d5e26':'#2fd07f22'};color:${r.gap<0?'var(--red)':'var(--green)'}">${r.gap>0?'+':''}${r.gap}명</span></td></tr>`).join('')}</table></div>`;}

function render(){renderNav();$('#view').innerHTML=tab==='live'?live():tab==='period'?period():sop();}
render();tickClock();setInterval(tickClock,1000);
</script></body></html>
"""

components.html(HTML, height=900, scrolling=True)
