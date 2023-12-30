import streamlit as st
import plotly.express as px
import pandas as pd
from vnstock import *
from app.bard_AI import bard_AI

def financial_cal(ticker):
    incomestatement = financial_flow(symbol="TCB", report_type='incomestatement', report_range='quarterly')
    incomestatement.reset_index(inplace=True)

    balancesheet = financial_flow(symbol="TCB", report_type='balancesheet', report_range='quarterly')
    balancesheet.reset_index(inplace=True)

    cashflow = financial_flow(symbol="TCB", report_type='cashflow', report_range='quarterly')
    cashflow.reset_index(inplace=True)

    financial_df = pd.DataFrame()
    # financial_df['range'] = 
    print(balancesheet)

def quantitative_tab_UI(ticker_and_name):

    ticker = ticker_and_name[:3]
    df = financial_ratio(ticker, 'quarterly', is_all= True)
    df = df.T
    df.reset_index(inplace=True)
    # financial_cal(ticker)
    
    fig = go.Figure()
    roe = go.Scatter(
        x=df['range'].values.tolist()[::-1],
        y=df['roe'].values.tolist()[::-1],
        mode='lines',
        name='Lợi nhuận trên vốn chủ (ROE)'
        )
    fig.add_trace(roe)

    roa = go.Scatter(
        x=df['range'].values.tolist()[::-1],
        y=df['roa'].values.tolist()[::-1],
        mode='lines',
        name='Lợi nhuận trên tài sản (ROA)',
        )
    fig.add_trace(roa)

    st.plotly_chart(fig, use_container_width=True)

    with st.expander("Báo cáo tài chính"):
        df = financial_report(ticker, report_type='IncomeStatement', frequency='Quarterly')
        st.table(df.iloc[:,[0, -4, -3, -2, -1]])

    with st.expander("Cân đối kế toán"):
        df = financial_report(ticker, report_type='BalanceSheet', frequency='Quarterly')
        st.table(df.iloc[:,[0, -4, -3, -2, -1]])

    with st.expander("Chuyển lưu tiền tệ"):
        df = financial_report(ticker, report_type='CashFlow', frequency='Quarterly')
        st.table(df.iloc[:,[0, -4, -3, -2, -1]])
