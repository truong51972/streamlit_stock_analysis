import streamlit as st
import pandas as pd
import numpy as np
from vnstock import *
from datetime import date, timedelta

st.set_page_config(layout="wide")
st.title('Stock analysis!')

def get_latest_price(stock):
    today = date.today()
    if (weekday := today.weekday()) > 4:
        day_delta = weekday - 4
    else:
        day_delta = 0
        
    day = str(date.today() - timedelta(days= day_delta))
    stock_price =  stock_historical_data(symbol=stock, 
                                    start_date=day, 
                                    end_date=day, resolution='1D', type='stock', beautify=True, decor=False, source='DNSE')['close'][0]
    return stock_price

def get_company_finance_info(stock, year= '2022'):
    stock_shares = company_overview(stock)['outstandingShare'][0]
    stock_companyName = company_profile(stock)['companyName'][0]
    
    stock_price = get_latest_price(stock)

    stock_financial_flow = financial_flow(symbol="VHM", report_type='balancesheet', report_range='yearly').T
    stock_debt = stock_financial_flow.loc['debt',year]
    stock_cash = stock_financial_flow.loc['cash',year]
    stock_asset = stock_financial_flow.loc['asset',year]
    
    stock_postTaxProfit = financial_flow(symbol="VHM", report_type='incomestatement', report_range='yearly')['postTaxProfit'][year]
    stock_ebitda = financial_flow(symbol="VHM", report_type='incomestatement', report_range='yearly')['ebitda'][year]
    
    companyName = stock_companyName + f' ({stock})'
    price = stock_price/1000
    shares = stock_shares
    marketCap = stock_shares*stock_price/1000
    debt = stock_debt
    eV = marketCap + debt - stock_cash
    bookValue = round((stock_asset - stock_debt)/(shares),2)
    ebitda = stock_ebitda
    earnings = stock_postTaxProfit
    pb = round((price/bookValue),2)
    ee = round(eV/ebitda,2)
    pe = round(price/(earnings/shares),2)
    
    row = [companyName, price, shares, marketCap, debt, eV, bookValue, ebitda, earnings, pb,ee, pe]
    return row

with st.container():
    industry_col, ticker_col = st.columns(2)

    with industry_col:
        select_industryName = st.selectbox(
            'Industry Name?',
            ('', 'Insurance', 'Real Estate', 'Technology', 'Oil & Gas', 'Financial Services', 'Utilities', 'Travel & Leisure', 'Industrial Goods & Services', 'Personal & Household Goods', 'Chemicals', 'Banks', 'Automobiles & Parts', 'Basic Resources', 'Food & Beverage', 'Media', 'Telecommunications', 'Construction & Materials', 'Health Care'))

    with ticker_col:
        params = {'industryName': select_industryName}
        stocks = []
        if select_industryName != '':
            df = stock_screening_insights (params, size=1700, drop_lang='vi')
            df.sort_values(by='marketCap', ascending=False, inplace=True, ignore_index=True)
            stocks = df['ticker']

        select_ticker = st.selectbox(
            'Industry Name?',
            (stocks))
        
        top_10_ticker = df['ticker'][:10].tolist()
        if select_ticker not in top_10_ticker: top_10_ticker.append(select_ticker)

df_overview_company = pd.DataFrame(columns=["Company Name", "Price (nghìn vnd)", "Shares (Triệu cp)", "Market Cap (tỷ vnd)", "Net Debt (tỷ vnd)", "EV (tỷ vnd)", "Book Value (tỷ vnd)", "EBITDA", "Earnings", "P/B", "EV/EBITDA", "P/E"])
print(top_10_ticker)
for stock in top_10_ticker:
    df_overview_company.loc[len(df_overview_company.index)] = get_company_finance_info(stock= stock)
df_overview_company.set_index('Company Name', inplace=True)
st.write(df_overview_company)