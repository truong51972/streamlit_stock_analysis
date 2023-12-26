import pandas as pd
import streamlit as st
from vnstock import *
from app.stock import *

def industry_overview():
    format_table = ["Company Name", "Price (nghìn)", "Shares (Triệu)", "Market Cap (tỷ)", "Net Debt (tỷ)", "Book Value (tỷ)", "EBITDA", "EPS", "P/E", "P/B", "EV/EBITDA"]
    df_overview_company = pd.DataFrame(columns= format_table)

    if show_button:
        for stock in top_10_ticker:
            df_overview_company.loc[len(df_overview_company.index)] = get_company_finance_info(stock= stock)

    df_overview_company.set_index('Company Name', inplace=True)
    st.write(df_overview_company)