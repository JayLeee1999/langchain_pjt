import streamlit as st
from stock_info import Stock
from report_service import investment_report
from search_index import search_company, SearchResult

st.title("AI 투자 보고서 생성 서비스")
search_symbol = st.text_input("회사명")

company_info = search_company(search_symbol)
hits = company_info['hits']
company_list = [SearchResult(hit) for hit in hits]
company_selected = st.selectbox("회사 선택", company_list, index=0)


# 회사 이름
search_symbol = company_selected.symbol
company_selected = company_selected.name

tabs = ['주식정보', '투자 보고서']
tab1, tab2 = st.tabs(tabs)

# 주식 거래량 차트 시각화
with tab1:
    st.header(f"{company_selected}의 6개월 주식 거래량")
    stock = Stock(search_symbol)
    volume = stock.get_stock_volume()
    st.line_chart(volume, use_container_width=True)

# LLM이 만든 투자 보고서
with tab2:
    st.header(f"{company_selected} AI 투자보고서")

    if st.button("보고서 생성"):
        with st.spinner(text="진행 중..."):
            # 문자열에서 symbol과 name 분리
            report = investment_report(search_symbol, company_selected)  # 순서 맞게 전달
            st.success("완료")
        st.write(report)