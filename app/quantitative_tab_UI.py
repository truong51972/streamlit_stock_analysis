import streamlit as st
import plotly.express as px
import pandas as pd
from vnstock import *
from app.bard_AI import bard_AI
from app.stock import get_financial_info_from_CafeF

def quantitative_tab_UI(ticker_and_name):

    ticker = ticker_and_name[:3]
    last_quarters = 40

    financialRatio = financial_ratio(ticker, 'quarterly', is_all=True).T
    financialRatio.reset_index(inplace=True)
    financialRatio = financialRatio.loc[:last_quarters] 
    financialRatio = financialRatio.iloc[::-1]

    valuation_df = pd.DataFrame()
    valuation_df['Quý'] = financialRatio['range']
    valuation_df['P/E'] = financialRatio['priceToEarning']
    valuation_df['P/B'] = financialRatio['priceToBook']
    valuation_df['Earning Per Share'] = financialRatio['earningPerShare']
    valuation_df['EV/EBITDA'] = financialRatio['valueBeforeEbitda']


    col1, col2 = st.columns(2)
    with col1:
        with st.container(border=True):
            fig = px.line(valuation_df, x= 'Quý', y= ['P/E', 'P/B', 'EV/EBITDA'], title='Chỉ số định giá')
            st.plotly_chart(fig, use_container_width=True)

    with col2:
        with st.container(border=True):
            fig = px.line(valuation_df, x= 'Quý', y= ['Earning Per Share'], title='Earning Per Share')
            st.plotly_chart(fig, use_container_width=True)

    operationEfficiency_df = pd.DataFrame()
    operationEfficiency_df['Quý'] = financialRatio['range']
    operationEfficiency_df['Tỷ suất sinh lời trên vốn chủ (ROE)'] = financialRatio['roe']
    operationEfficiency_df['Tỷ suất sinh lời trên tài sản (ROA)'] = financialRatio['roa']
    operationEfficiency_df['Biên LN gộp (GPM)'] = financialRatio['grossProfitMargin']
    operationEfficiency_df['Biên LN hoạt động (OPM)'] = financialRatio['operatingProfitMargin']
    operationEfficiency_df['Biên LNST (PTM)'] = financialRatio['postTaxMargin']

    col1, col2 = st.columns(2)
    with col1:
        with st.container(border=True):
            fig = px.line(operationEfficiency_df, x= 'Quý', y= ['Tỷ suất sinh lời trên vốn chủ (ROE)', 'Tỷ suất sinh lời trên tài sản (ROA)'], title='Tỷ suất sinh lời')
            st.plotly_chart(fig, use_container_width=True)

    with col2:
        with st.container(border=True):
            fig = px.line(operationEfficiency_df, x= 'Quý', y= ['Biên LN gộp (GPM)', 'Biên LN hoạt động (OPM)', 'Biên LNST (PTM)'], title='Biên lợi nhuận')
            st.plotly_chart(fig, use_container_width=True)

    debt_df = pd.DataFrame()
    debt_df['Quý'] = financialRatio['range']
    debt_df['Vay/VCSH'] = financialRatio['debtOnEquity']
    debt_df['Vay/Tài sản'] = financialRatio['debtOnAsset']
    debt_df['Đòn bẩy tài chính'] = financialRatio['assetOnEquity']

    payable_df = pd.DataFrame()
    payable_df['Quý'] = financialRatio['range']
    payable_df['Thanh toán hiện hành'] = financialRatio['currentPayment']
    payable_df['Thanh toán nhanh'] = financialRatio['quickPayment']

    col1, col2 = st.columns(2)
    with col1:
        with st.container(border=True):
            fig = px.line(debt_df, x= 'Quý', y= ['Vay/VCSH', 'Vay/Tài sản', 'Đòn bẩy tài chính'], title='Nợ')
            st.plotly_chart(fig, use_container_width=True)
    with col2:
        with st.container(border=True):
            fig = px.line(payable_df, x= 'Quý', y= ['Thanh toán hiện hành', 'Thanh toán nhanh'], title='Thanh khoản')
            st.plotly_chart(fig, use_container_width=True)
        

    with st.expander("Báo cáo tài chính"):
        df = get_financial_info_from_CafeF(ticker,1)
        st.table(df)

    with st.expander("Cân đối kế toán"):
        df = get_financial_info_from_CafeF(ticker,2)
        st.table(df)

    with st.expander("Chuyển lưu tiền tệ"):
        df = get_financial_info_from_CafeF(ticker,3)
        st.table(df)