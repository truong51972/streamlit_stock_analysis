import pandas as pd
import streamlit as st

def stock_menu():
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