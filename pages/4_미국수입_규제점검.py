import json

import pandas as pd
import streamlit as st

# ---------------------------------------------------------------------------
# 데이터: 규정이 바뀌면 이 부분만 고치면 됩니다.
# ---------------------------------------------------------------------------
ASOF = "2026-10-19"
INFORMAL_ENTRY_USD = 2500
DE_MINIMIS_USD = 800

CHECKLIST = [
    ("importer", "수입자(Importer of Record)를 정했다"),
    ("broker", "관세사(통관 대리인)를 지정했다"),
    ("docs", "CI·PL(송장·포장명세서)을 준비했다"),
    ("facility", "제조·가공 시설을 FDA에 등록했다"),
    ("listing", "제품을 FDA에 리스팅했다"),
    ("rp", "미국 책임자(Responsible Person)를 정했다"),
    ("safety", "제품 안전성 근거 자료를 보관한다"),
    ("label", "라벨에 책임자 연락처와 필수 표기를 넣었다"),
    ("adverse", "이상반응 접수·보고 절차가 있다"),
]

MOCRA = [
    {"id": "facility", "title": "시설 등록", "small_exempt": True,
     "text": "화장품을 제조·가공하는 시설을 FDA에 등록해야 합니다."},
    {"id": "listing", "title": "제품 리스팅", "small_exempt": True,
     "text": "판매하는 화장품을 제품 단위로 FDA에 등록(리스팅)해야 합니다. 예전 VCRP(자발 등록)를 대체했습니다."},
    {"id": "rp", "title": "미국 책임자 지정", "small_exempt": False,
     "text": "제조사·포장사·유통사 중 한 곳이 책임자(Responsible Person)가 되어 이상반응 보고와 안전성 입증을 책임집니다."},
    {"id": "safety", "title": "안전성 입증", "small_exempt": False,
     "text": "제품이 안전하다는 근거 자료를 갖추고 보관해야 합니다."},
    {"id": "label", "title": "라벨 표기", "small_exempt": False,
     "text": "이상반응을 받을 수 있는 미국 내 주소, 전화번호 또는 전자 연락처를 라벨에 표기해야 합니다."},
    {"id": "adverse", "title": "이상반응 보고", "small_exempt": False,
     "text": "심각한 이상반응은 인지 후 15영업일 이내 FDA에 보고하고 기록을 보관해야 합니다."},
]

TERMS = [
    ("미국 수입 통관", "US customs clearance",
     "해외 제품이 미국 세관(CBP)을 통과하는 절차입니다. 서류 작성, 관세 납부, 검사 대응이 포함됩니다.",
     "한국의 관세사 업무와 같은 계열입니다."),
    ("Section 321", "de minimis",
     "하루 1인당 800달러 이하의 소액 물품을 관세 없이 간단히 들여오던 제도입니다. 중국·한국발 소포와 아마존 셀러에게 중요했습니다.",
     "2025-08-29부터 면세가 중단되었습니다. 2026년 자료에도 중단 상태로 나옵니다. 신고 전 최신 상태를 확인하세요."),
    ("FDA", "Food and Drug Administration",
     "미국 식품의약국입니다. 화장품도 FDA 규제를 받습니다.", ""),
    ("MoCRA", "Modernization of Cosmetics Regulation Act of 2022",
     "2022년에 통과된 화장품 규제 현대화법입니다. 시설 등록, 제품 리스팅, 안전성 입증, 라벨 표기, 이상반응 보고를 의무로 정했습니다.",
     "연매출 100만 달러 미만 소규모 사업자는 시설 등록·제품 리스팅이 면제될 수 있습니다. 눈 주변, 주사, 내복 제품 등은 예외라 확인이 필요합니다."),
    ("VCRP", "Voluntary Cosmetic Registration Program",
     "과거에 업체가 자발적으로 하던 화장품 등록 제도입니다. MoCRA의 의무 등록으로 바뀌었습니다.",
     "공고의 \"VCRP(MoCRA)\"는 화장품 등록·규제 전반으로 읽으면 됩니다."),
    ("CBP", "U.S. Customs and Border Protection",
     "미국 세관·국경보호국입니다. 수입 신고와 관세 부과를 담당합니다.", ""),
    ("CI / PL", "Commercial Invoice / Packing List",
     "CI는 거래 금액과 품목을 적은 상업 송장, PL은 포장 단위와 수량을 적은 포장명세서입니다. 통관의 기본 서류입니다.", ""),
    ("수입자", "Importer of Record (IOR)",
     "미국 세관에 수입 책임을 지는 사업자입니다. 관세와 세금 납부, 서류 정확성에 책임이 있습니다.",
     "FBA 입고 때 누가 맡을지 먼저 정해야 합니다."),
    ("비공식 신고", "informal entry",
     "소액 물품에 쓰는 간이 수입 신고입니다. 통상 2,500달러 이하 구간입니다.",
     "기준 금액은 바뀔 수 있어 관세사에게 확인하세요."),
    ("OTC 의약품", "over-the-counter drug",
     "처방 없이 파는 의약품입니다. 자외선차단제, 여드름·비듬·탈모 방지 제품은 화장품이 아니라 이쪽으로 분류될 수 있습니다.",
     "일반 화장품보다 요건이 많아 전문가 확인이 필요합니다."),
]

LOG = [
    {"날짜": "2022-12-29", "내용": "MoCRA 제정", "영향": "화장품 규제 강화의 시작"},
    {"날짜": "2023-12-29", "내용": "시설 등록·제품 리스팅 기한", "영향": "VCRP를 대체하는 의무 등록 체계로 전환"},
    {"날짜": "2024-07-01", "내용": "FDA가 MoCRA 등록·리스팅 집행을 시작", "영향": "미등록 제품은 수입·판매에 문제가 생길 수 있음"},
    {"날짜": "2025-08-29", "내용": "Section 321 소액 면세 중단", "영향": "800달러 이하 물품도 일반 통관과 관세 부과를 전제로 준비"},
]

SOURCES = [
    ("FDA: MoCRA 안내", "https://www.fda.gov/cosmetics/cosmetics-laws-regulations/modernization-cosmetics-regulation-act-2022-mocra"),
    ("Section 321 면세 중단 설명 (GHY)", "https://www.ghy.com/trade-talk/section-321-for-low-value-shipments/"),
    ("Section 321: Suspended (GoBolt)", "https://www.gobolt.com/blog/section-321"),
    ("2026 소액 면세 중단 현황 (GetTransport)", "https://blog.gettransport.com/logistics-guide/us-de-minimis-suspension-2026-importer-status-guide/"),
]

PRODUCTS = {
    "cosmetic": "일반 화장품 (스킨케어, 메이크업 등)",
    "functional": "기능성 (자외선차단, 여드름, 비듬, 탈모 방지 등)",
    "other": "화장품이 아님",
}
CHANNELS = {
    "fba": "아마존 FBA 입고",
    "parcel": "소포·특송으로 소비자에게 직배송",
    "bulk": "대량 수입 (3PL·창고 입고)",
}
SMALL = {"unknown": "모름", "yes": "예", "no": "아니오"}

# 화면 첫 상태에 채워 둘 예시 값
EXAMPLE_DONE = {"importer", "docs"}


# ---------------------------------------------------------------------------
# 판정 로직
# ---------------------------------------------------------------------------
def route_for(value, channel):
    items = []
    if value <= DE_MINIMIS_USD:
        title = f"${value:,.0f}: 소액 구간입니다. 면세로 보지 마세요"
        items.append("Section 321(800달러 이하 면세)은 2025-08-29부터 중단된 상태입니다. 일반 통관과 관세 부과를 전제로 준비하세요.")
        items.append("현재 적용 여부와 세율은 신고 전에 관세사에게 확인하세요.")
    elif value <= INFORMAL_ENTRY_USD:
        title = f"${value:,.0f}: 비공식 신고 구간일 수 있습니다"
        items.append(f"통상 {INFORMAL_ENTRY_USD:,}달러 이하는 간이 신고(비공식 신고)를 쓰지만 품목에 따라 다릅니다. 관세사에게 확인하세요.")
    else:
        title = f"${value:,.0f}: 정식 신고 구간입니다"
        items.append(f"{INFORMAL_ENTRY_USD:,}달러를 넘으면 정식 신고가 일반적이고, 통관 보증(bond)이 필요할 수 있습니다.")
    if channel == "fba":
        items.append("FBA 입고는 수입자(IOR)가 누구인지 먼저 정해야 합니다. 아마존이 대신 해주지 않습니다.")
    elif channel == "parcel":
        items.append("소비자 직배송은 관세·세금을 누가 내는지(판매자 부담 또는 수령인 부담)를 미리 정해야 반송과 CS를 줄입니다.")
    else:
        items.append("대량 수입은 관세사, 통관 보증, 창고 입고 일정을 함께 조율하세요.")
    return title, items


def status_for(item, done, small):
    if item["id"] in done:
        return "done", "✅ 완료"
    if item["small_exempt"]:
        if small == "yes":
            return "na", "➖ 면제 가능"
        if small == "unknown":
            return "check", "🟡 해당 여부 확인"
    return "todo", "⬜ 해야 함"


# ---------------------------------------------------------------------------
# 화면
# ---------------------------------------------------------------------------
st.title("🇺🇸 미국 수입 규제 점검표")
st.caption(f"확인 기준일 {ASOF} · 가상 입력으로 동작하며 입력 내용은 저장되지 않습니다")
st.write(
    "미국 수입 통관, Section 321, FDA, MoCRA, VCRP 내용을 데이터로 정리했습니다. "
    "제품과 판매 방식을 넣으면 지금 해야 할 일과 확인할 일을 보여줍니다."
)

tab_check, tab_terms, tab_log, tab_data = st.tabs(["점검", "용어", "변경 이력", "데이터"])

with tab_check:
    st.caption("처음에는 예시 값이 들어 있습니다. 값을 바꾸면 결과가 바로 달라집니다.")
    c1, c2 = st.columns(2)
    with c1:
        product = st.selectbox("제품 종류", list(PRODUCTS), format_func=PRODUCTS.get, key="product")
        value = st.number_input("한 번에 신고하는 물품 가치 (달러, 송장 합계 기준)", min_value=0, value=650, step=50, key="value")
    with c2:
        channel = st.selectbox("판매·입고 방식", list(CHANNELS), format_func=CHANNELS.get, key="channel")
        small = st.selectbox("브랜드 소유 회사의 최근 3년 평균 연매출이 100만 달러 미만인가요?",
                             list(SMALL), format_func=SMALL.get, key="small")

    st.markdown("**이미 한 일에 체크하세요**")
    cols = st.columns(2)
    done = set()
    for i, (cid, label) in enumerate(CHECKLIST):
        if cols[i % 2].checkbox(label, value=(cid in EXAMPLE_DONE), key=f"chk_{cid}"):
            done.add(cid)

    st.divider()
    title, items = route_for(float(value), channel)
    st.subheader("통관 경로")
    st.info(f"**{title}**\n\n" + "\n".join(f"- {t}" for t in items))

    if product == "other":
        st.warning("화장품이 아닙니다. 이 표는 화장품 기준입니다. 다른 품목은 해당 품목의 규제와 관세 분류를 관세사에게 확인하세요.")
    else:
        if product == "functional":
            st.error(
                "**먼저 확인: 의약품으로 분류될 수 있습니다.** 자외선차단, 여드름, 비듬, 탈모 방지처럼 효능을 내세우는 제품은 "
                "FDA에서 OTC 의약품으로 보는 경우가 있습니다. 일반 화장품보다 요건이 많으니 입고 전에 전문가에게 분류부터 확인하세요."
            )
        rows = [(m, *status_for(m, done, small)) for m in MOCRA]
        counted = [r for r in rows if r[1] != "na"]
        done_n = sum(1 for r in counted if r[1] == "done")
        pct = done_n / len(counted) if counted else 1.0
        st.subheader("MoCRA 점검")
        st.progress(pct, text=f"{done_n} / {len(counted)} 완료")
        for m, state, label in rows:
            with st.container(border=True):
                st.markdown(f"**{m['title']}** · {label}")
                st.caption(m["text"])
        if small == "yes":
            st.info("소규모 사업자 면제는 시설 등록과 제품 리스팅에만 적용됩니다. 눈 주변·주사·내복 제품, "
                    "24시간 이상 외관을 바꾸는 제품은 예외라 해당 여부를 확인하세요. 책임자, 안전성, 라벨, 이상반응 보고는 면제되지 않습니다.")
        with st.container(border=True):
            st.markdown("**제조 품질 기준(GMP)** · 🟡 확인")
            st.caption("MoCRA는 화장품 GMP 규정을 정하도록 했지만 시행 여부는 FDA 규칙 진행 상황에 따라 달라집니다. 시행 현황을 확인하세요.")
        docs_n = sum(1 for k in ("importer", "broker", "docs") if k in done)
        with st.container(border=True):
            st.markdown(f"**수입 서류와 담당자** · {'✅ 완료' if docs_n == 3 else '⬜ 해야 함'}")
            st.caption(f"수입자, 관세사, CI·PL이 모두 준비되어야 신고를 시작할 수 있습니다. 현재 {docs_n}/3 준비되었습니다.")

    st.caption("참고용 정리입니다. 법률·통관 자문이 아니며, 실제 신고 전에는 관세사와 FDA 규제 전문가에게 확인하세요. 규정은 자주 바뀝니다.")

with tab_terms:
    q = st.text_input("용어 검색", placeholder="예: MoCRA, 321, 관세사").strip().lower()
    shown = 0
    for k, en, d, note in TERMS:
        if q and q not in f"{k} {en} {d} {note}".lower():
            continue
        shown += 1
        with st.container(border=True):
            st.markdown(f"**{k}**  `{en}`")
            st.write(d)
            if note:
                st.caption("⚠ " + note)
    if not shown:
        st.write("검색 결과가 없습니다. 다른 단어로 찾아보세요.")

with tab_log:
    st.subheader("규정 변경 이력")
    st.dataframe(pd.DataFrame(LOG), hide_index=True)
    st.subheader("출처")
    for t, u in SOURCES:
        st.markdown(f"- [{t}]({u})")

with tab_data:
    st.subheader("원본 데이터")
    st.caption("이 화면의 판정은 아래 데이터로 계산됩니다. 규정이 바뀌면 이 내용만 고치면 됩니다.")
    payload = {
        "asOf": ASOF,
        "thresholds": {"informalEntryUsd": INFORMAL_ENTRY_USD, "deMinimisUsd": DE_MINIMIS_USD},
        "mocra": MOCRA,
        "terms": [{"term": k, "en": en, "desc": d, "note": n} for k, en, d, n in TERMS],
        "log": LOG,
    }
    st.json(payload, expanded=False)
    st.download_button("데이터 내려받기 (JSON)", json.dumps(payload, ensure_ascii=False, indent=2),
                       file_name="us_import_rules.json", mime="application/json")
