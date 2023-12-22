import pandas as pd
import numpy as np
from vnstock import *
from datetime import date, timedelta

def get_basic_info(stock):
    shares = company_overview(stock)['outstandingShare'][0]
    companyName = company_profile(stock)['companyName'][0]
    return shares, companyName

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

def get_balance_sheet(stock):
    balance_sheet = financial_flow(symbol=stock, report_type='balancesheet', report_range='quarterly').T
    latest = balance_sheet.columns[0]

    debt = balance_sheet[latest]['debt']
    cash = balance_sheet[latest]['cash']
    asset = balance_sheet[latest]['asset']
    return debt, cash, asset

def get_income_statement(stock):

    income_statement = financial_flow(symbol=stock, report_type='incomestatement', report_range='quarterly').T
    latest = income_statement.columns[0]

    stock_postTaxProfit = income_statement[latest]['postTaxProfit']
    stock_ebitda = income_statement[latest]['ebitda']

    return stock_postTaxProfit, stock_ebitda

def get_financial_ratio(stock):
    fiRa = financial_ratio(stock, 'quarterly')
    latest = fiRa.columns[0]
    eps = fiRa[latest]['earningPerShare']
    bvps = fiRa[latest]['bookValuePerShare']
    pe = fiRa[latest]['priceToEarning']
    pb = fiRa[latest]['priceToBook']
    ee = fiRa[latest]['valueBeforeEbitda']

    return eps, bvps, pe, pb, ee
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