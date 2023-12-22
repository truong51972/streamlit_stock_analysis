import streamlit as st
import pandas as pd
import numpy as np
from vnstock import *
from datetime import date, timedelta
from stock import *

st.set_page_config(layout="wide")
st.title('Stock analysis!')

with st.container():
    menu_col, info_col = st.columns([1,6])

    with menu_col:
        select_industryName = st.selectbox(
            'Industry Name?',
            ('', 'Insurance', 'Real Estate', 'Technology', 'Oil & Gas', 'Financial Services', 'Utilities', 'Travel & Leisure', 'Industrial Goods & Services', 'Personal & Household Goods', 'Chemicals', 'Banks', 'Automobiles & Parts', 'Basic Resources', 'Food & Beverage', 'Media', 'Telecommunications', 'Construction & Materials', 'Health Care'))

        params = {'industryName': select_industryName}
        stocks = ['']
        top_10_ticker = None

        if select_industryName != '':
            df = stock_screening_insights(params, size=1700, drop_lang='vi')
            df.sort_values(by='marketCap', ascending=False, inplace=True, ignore_index=True)
            stocks.extend(df['ticker'].tolist())
            top_10_ticker = df['ticker'][:10].tolist()

        select_ticker = st.selectbox(
            'Industry Name?',
            (stocks))
        
        if (top_10_ticker != None) and (select_ticker not in top_10_ticker) and (select_ticker != ''):
            top_10_ticker.append(select_ticker)

        show_button = st.button("Show")

    with info_col:
        format_table = ["Company Name", "Price (nghìn)", "Shares (Triệu)", "Market Cap (tỷ)", "Net Debt (tỷ)", "Book Value (tỷ)", "EBITDA", "EPS", "P/E", "P/B", "EV/EBITDA"]
        df_overview_company = pd.DataFrame(columns= format_table)

        if show_button:
            for stock in top_10_ticker:
                df_overview_company.loc[len(df_overview_company.index)] = get_company_finance_info(stock= stock)
 
        df_overview_company.set_index('Company Name', inplace=True)
        st.write(df_overview_company)