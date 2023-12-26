import streamlit as st
from vnstock import *
from app.stock import *
from app.sidebar_UI import sidebar_UI
from app.qualitative_tab_UI import qualitative_tab_UI

def run():
    st.set_page_config(layout="wide")

    ticker = sidebar_UI()


    if st.session_state.get('analyze'):
        qualitative_tab, quantitative_tab, valuation_tab = st.tabs(["Qualitative", "Quantitative", "Valuation"])

        with qualitative_tab:
            qualitative_tab_UI(ticker)

        with quantitative_tab:
            st.header("A dog")
            st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

        with valuation_tab:
            st.header("An owl")
            st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
                

                
                    
