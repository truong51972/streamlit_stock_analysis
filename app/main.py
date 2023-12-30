import streamlit as st
from vnstock import *
from app.stock import *
from app.sidebar_UI import sidebar_UI
from app.qualitative_tab_UI import qualitative_tab_UI
from app.quantitative_tab_UI import quantitative_tab_UI

def run():
    st.set_page_config(layout="wide")

    ticker_and_name = sidebar_UI()


    if st.session_state.get('analyze'):
        qualitative_tab, quantitative_tab, valuation_tab = st.tabs(["Qualitative", "Quantitative", "Valuation"])

        with qualitative_tab:
            qualitative_tab_UI(ticker_and_name)

        with quantitative_tab:
            quantitative_tab_UI(ticker_and_name)

        with valuation_tab:
            st.header("An owl")
            st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
                

                
                    
