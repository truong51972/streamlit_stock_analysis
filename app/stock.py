import pandas as pd
import numpy as np
from vnstock import *
from datetime import date, timedelta
import streamlit as st

@st.cache_data
def get_basic_info(stock):
    shares = company_overview(stock)['outstandingShare'][0]
    companyName = company_profile(stock)['companyName'][0]
    return shares, companyName

@st.cache_data
def get_all_ticker():
    tickers_info = listing_companies(live=True)
    tickers_info['ticker_name'] = tickers_info['ticker'] + ' - ' + tickers_info['organName']
    ticker_and_name = tickers_info['ticker_name'].tolist()
    return ticker_and_name


@st.cache_data
def get_latest_price(stock):
    today = date.today()
    while True:
        try:
            stock_price =  stock_historical_data(symbol=stock, 
                                            start_date=str(today), 
                                            end_date=str(today),
                                            resolution='1D', type='stock', beautify=True, decor=False, source='DNSE')['close'][0]
            break
        except:
            today = today - timedelta(days= 1)
            print(today)
    return stock_price

@st.cache_data
def get_balance_sheet(stock):
    balance_sheet = financial_flow(symbol=stock, report_type='balancesheet', report_range='quarterly').T
    latest = balance_sheet.columns[0]

    debt = balance_sheet[latest]['debt']
    cash = balance_sheet[latest]['cash']
    asset = balance_sheet[latest]['asset']
    return debt, cash, asset

@st.cache_data
def get_income_statement(stock):

    income_statement = financial_flow(symbol=stock, report_type='incomestatement', report_range='quarterly').T
    latest = income_statement.columns[0]

    stock_postTaxProfit = income_statement[latest]['postTaxProfit']
    stock_ebitda = income_statement[latest]['ebitda']

    return stock_postTaxProfit, stock_ebitda

@st.cache_data
def get_financial_ratio(stock):
    fiRa = financial_ratio(stock, 'quarterly')
    latest = fiRa.columns[0]
    eps = fiRa[latest]['earningPerShare']
    bvps = fiRa[latest]['bookValuePerShare']
    pe = fiRa[latest]['priceToEarning']
    pb = fiRa[latest]['priceToBook']
    try:
        ee = fiRa[latest]['valueBeforeEbitda']
    except:
        ee = 0
        
    return eps, bvps, pe, pb, ee

@st.cache_data
def get_company_finance_info(stock):
    
    stock_shares, stock_companyName = get_basic_info(stock)
    stock_price = get_latest_price(stock)

    stock_debt, stock_cash, stock_asset = get_balance_sheet(stock)
    
    stock_postTaxProfit, stock_ebitda = get_income_statement(stock)
    
    eps, bvps, pe, pb, ee = get_financial_ratio(stock)

    companyName = stock_companyName + f' ({stock})'
    price = stock_price/1000
    shares = stock_shares
    marketCap = stock_shares*stock_price/1000
    debt = stock_debt
    ebitda = stock_ebitda

    row = [companyName, price, shares, marketCap, debt, bvps, ebitda, eps, pe, pb, ee]
    return row


# @st.cache_data
def get_financial_info_from_CafeF(ticker, numType):
    today = date.today()
    quarter = round((today.month+1)/3 + 1/3)
    year = today.year
    ticker = ticker.lower()

    type = {1: 'incsta', 2: 'bsheet', 3: 'cashflow'}
    times = 0

    while True:
        url = f'https://s.cafef.vn/bao-cao-tai-chinh/{ticker}/{type[numType]}/{year}/{quarter}/0/0/ket-qua-hoat-dong-kinh-doanh-.chn'
        print(url)
        dfs = pd.read_html(url)
        if np.isnan(dfs[4].iloc[3,4]):
            quarter -= 1
            if quarter == 0:
                quarter = 4
                year -= 1
        else: break
        times += 1
        if times == 8: break

    format_table = ["Thông tin"]
    format_table.extend(dfs[3].loc[0,1:4].tolist())
    print(format_table)
    df = pd.DataFrame(columns= format_table, dtype='float32')
    pd.options.display.float_format = '{:,.2f}'.format

    for i in range(len(dfs[4])):
        df.loc[len(df.index)] = (dfs[4].loc[i,0:4]).tolist()
    df.set_index('Thông tin', inplace=True)

    df = df.astype(float, copy=True)

    df[df.abs() > 10000] = round(df[df.abs() > 10000] / 1000000000,4)
    df.fillna('-',inplace= True)
    return df