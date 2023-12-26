import streamlit as st
from vnstock import *
from app.bard_AI import bard_AI


def qualitative_tab_UI(ticker):
    style = '''
            style="
                font-size: 2rem;
                text-align: center;
            "
        '''
    text = 'Tổng quan về ngành'
    st.markdown(f'<p {style}>{text}</p>', unsafe_allow_html=True)

    industry = company_overview(ticker)['industry'].values[0]

    with st.container(border=True):
        bard_output = bard_AI(prompt=f'Đặc thù của cổ phiếu ngành {industry} là gì (liệt kê, ngắn gọn)')

        col1, col2 = st.columns([0.2, 0.8])
        with col1:
            col1_container = col1.container(border=False)
            with col1_container:

                style = '''
                        style="
                            font-size: 1.5rem;
                        "
                    '''
                text = 'Đặc thù ngành'
                col1_container.markdown(f'<p {style}>{text}</p>', unsafe_allow_html=True)
        with col2:
            col2_container = col2.container(border=False)
            with col2_container:
                col2_container.markdown(bard_output, unsafe_allow_html=True)

    with st.container(border=True):
        industry = company_overview(ticker)['industry'].values[0]
        bard_output = bard_AI(prompt=f'Triển vọng của cổ phiếu ngành {industry} là gì (liệt kê, ngắn gọn)')

        col1, col2 = st.columns([0.2, 0.8])
        with col1:
            col1_container = col1.container(border=False)
            with col1_container:

                style = '''
                        style="
                            font-size: 1.5rem;
                        "
                    '''
                text = 'Triển vọng ngành'
                col1_container.markdown(f'<p {style}>{text}</p>', unsafe_allow_html=True)
        with col2:
            col2_container = col2.container(border=False)
            with col2_container:
                col2_container.markdown(bard_output, unsafe_allow_html=True)

    with st.container(border=True):
        industry = company_overview(ticker)['industry'].values[0]
        bard_output = bard_AI(prompt=f'Chu kỳ của cổ phiếu ngành {industry} là gì (liệt kê, ngắn gọn)')

        col1, col2 = st.columns([0.2, 0.8])
        with col1:
            col1_container = col1.container(border=False)
            with col1_container:

                style = '''
                        style="
                            font-size: 1.5rem;
                        "
                    '''
                text = 'Chu kỳ ngành'
                col1_container.markdown(f'<p {style}>{text}</p>', unsafe_allow_html=True)
        with col2:
            col2_container = col2.container(border=False)
            with col2_container:
                col2_container.markdown(bard_output, unsafe_allow_html=True)