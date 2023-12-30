import streamlit as st
from vnstock import *
from app.bard_AI import bard_AI
import plotly.express as px

def get_info_and_display(title, question, getAnswer:bool= True):
    with st.container(border=True):

        col1, col2 = st.columns([0.2, 0.8])
        with col1:
            col1_container = col1.container(border=False)
            with col1_container:

                style = '''
                        style="
                            font-size: 1.5rem;
                        "
                    '''
                col1_container.markdown(f'<p {style}>{title}</p>', unsafe_allow_html=True)
        with col2:
            col2_container = col2.container(border=False)
            with col2_container:
                if getAnswer:
                    tab1, tab2, tab3 = st.tabs(['Thông tin thứ 1', 'Thông tin thứ 2', 'Thông tin thứ 3'])

                    with tab1:
                        bard_output = bard_AI(prompt=question)
                        tab1.markdown(bard_output, unsafe_allow_html=True)

                    with tab2:
                        bard_output = bard_AI(prompt=question)
                        tab2.markdown(bard_output, unsafe_allow_html=True)

                    with tab3:
                        bard_output = bard_AI(prompt=question)
                        tab3.markdown(bard_output, unsafe_allow_html=True)

def qualitative_tab_UI(ticker_and_name):
    
    getAnswer = True
    
    ticker = ticker_and_name[:3]
    industry = company_overview(ticker)['industry'].values[0]

    style = '''
            style="
                font-size: 2rem;
                text-align: center;
            "
        '''
    text = 'Tổng quan về ngành'

    st.markdown(f'<p {style}>{text}</p>', unsafe_allow_html=True)

    get_info_and_display(title='Đặc thù ngành', question=f'Đặc thù của cổ phiếu ngành {industry} là gì (liệt kê, ngắn gọn)',getAnswer= getAnswer)
    
    get_info_and_display(title='Triển vọng ngành', question=f'Triển vọng của cổ phiếu ngành {industry} là gì (liệt kê, ngắn gọn)',getAnswer= getAnswer)
    
    get_info_and_display(title='Chu kỳ ngành', question=f'Chu kỳ của cổ phiếu ngành {industry} là gì (liệt kê, ngắn gọn)',getAnswer= getAnswer)
    

    style = '''
            style="
                font-size: 2rem;
                text-align: center;
            "
        '''
    text = 'Tổng quan về công ty'
    st.markdown(f'<p {style}>{text}</p>', unsafe_allow_html=True)

    with st.container(border=True):
        col1, col2 = st.columns([0.2, 0.8])
        with col1:
            col1_container = col1.container(border=False)
            with col1_container:

                style = '''
                        style="
                            font-size: 1.5rem;
                        "
                    '''
                text = 'Các cổ đông chính'
                col1_container.markdown(f'<p {style}>{text}</p>', unsafe_allow_html=True)
        with col2:
            df = company_large_shareholders(ticker)
            fig = px.pie(df, values='shareOwnPercent', names='shareHolder')
            st.plotly_chart(fig, use_container_width=True)

    get_info_and_display(title='Ban điều hành', question=f'Ban điều hành của công ty có mã cổ phiếu {ticker_and_name} (liệt kê, ngắn gọn)',getAnswer= getAnswer)
    
    get_info_and_display(title='Các mảng kinh doanh', question=f'Các mảng kinh doanh của công ty có mã cổ phiếu {ticker_and_name} (liệt kê, ngắn gọn)',getAnswer= getAnswer)

    get_info_and_display(title='Đầu ra (sản phẩm/dịch vụ)', question=f'Đầu ra (sản phẩm/dịch vụ) của công ty có mã cổ phiếu {ticker_and_name} (liệt kê, ngắn gọn)',getAnswer= getAnswer)
    
    get_info_and_display(title='Đầu ra (thị trường)', question=f'Đầu ra (thị trường) của công ty có mã cổ phiếu {ticker_and_name} (liệt kê, ngắn gọn)',getAnswer= getAnswer)

    get_info_and_display(title='Đầu vào (nguyên vật liệu)', question=f'Đầu vào (nguyên vật liệu) của công ty có mã cổ phiếu {ticker_and_name} (liệt kê, ngắn gọn)',getAnswer= getAnswer)

    get_info_and_display(title='Đối thủ cạnh tranh', question=f'Đối thủ cạnh tranh của công ty có mã cổ phiếu {ticker_and_name} (liệt kê, ngắn gọn)',getAnswer= getAnswer)

    get_info_and_display(title='Năng lưc cạnh tranh/Lợi thế cạnh tranh', question=f'Năng lưc cạnh tranh/Lợi thế cạnh tranh của công ty có mã cổ phiếu {ticker_and_name} (liệt kê, ngắn gọn)',getAnswer= getAnswer)

    get_info_and_display(title='Lý do/Cơ hội tăng trưởng cho doanh nghiệp', question=f'Lý do/Cơ hội tăng trưởng cho doanh nghiệp của công ty có mã cổ phiếu {ticker_and_name} (liệt kê, ngắn gọn)',getAnswer= getAnswer)

    get_info_and_display(title='Lưu ý khác', question=f'Những lưu ý khi đầu tư vào công ty có mã cổ phiếu {ticker_and_name} (liệt kê, ngắn gọn)',getAnswer= getAnswer)

    get_info_and_display(title='Đối thủ cạnh tranh', question=f'Đối thủ cạnh tranh của công ty có mã cổ phiếu {ticker_and_name} (liệt kê, ngắn gọn)',getAnswer= getAnswer)


    get_info_and_display(title='Đối thủ cạnh tranh', question=f'Đối thủ cạnh tranh của công ty có mã cổ phiếu {ticker_and_name} (liệt kê, ngắn gọn)',getAnswer= getAnswer)
