import streamlit as st
from vnstock import *
from app.stock import *

def sidebar_UI():
    with st.sidebar:
        with st.container():
            ticker_and_name = get_all_ticker()

            option = st.selectbox(
                'Select your ticker',
                ticker_and_name
            )

            companyName, price, shares, marketCap, debt, bvps, ebitda, eps, pe, pb, ee = get_company_finance_info(option[:3])
            
            st.button("Analyze!", key='analyze', use_container_width=True)

            style = '''
                    style="
                        font-size: 2rem;
                    "
                '''
            text = 'Thông tin cơ bản'
            st.markdown(f'<p {style}>{text}</p>', unsafe_allow_html=True)

            style = '''
                    style="
                        font-size: 1.2rem;
                        margin-bottom: 1rem;
                    "
                '''
            text = companyName
            st.markdown(f'<p {style}>{text}</p>', unsafe_allow_html=True)


                
            st.write(f'Vốn hoá: {round(marketCap)} Tỷ')
            st.write(f'Số lượng cổ phiếu: {round(shares)} Triệu')

            col1, col2 = st.columns(2)
            with col1: 
                st.write(f'P/E: {pe}')
                st.write(f'P/B: {pb}')
            with col2: 
                st.write(f'EPS: {eps}')
                st.write(f'BVPS: {bvps}')
            
            st.write(f'EV/EBITDA: {ee}')

            st.caption(company_profile(option[:3])['companyProfile'].values[0])
    ticker = option[:3]
    return ticker