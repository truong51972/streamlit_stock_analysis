import streamlit as st
from vnstock import *
from app.bard_AI import bard_AI
import plotly.express as px

def get_info_and_display(title, question, getAnswer:bool= True, numOfAnswers = 1):
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
                    
                tabName = []
                for i in range(numOfAnswers):
                    tabName.append(f'Thông tin thứ {i+1}')
                tabs = st.tabs(tabName)
                
                for tab in tabs:
                    with tab:
                        if getAnswer:
                            bard_output = bardAI.getAnwser(prompt=question)
                            tab.markdown(bard_output, unsafe_allow_html=True)
                        else:
                            tab.markdown('Get answer is off', unsafe_allow_html=True)


def qualitative_tab_UI(ticker_and_name):
    
    getAnswer = False
    numOfAnswers = 2

    ticker = ticker_and_name[:3]
    industry = company_overview(ticker)['industry'].values[0]

    tab1, tab2, tab3 = st.tabs(['Tổng quan về ngành', 'Tổng quan về công ty', 'Thông tin khác'])
    global bardAI
    bardAI = bard_AI()
    with tab1:
        get_info_and_display(title='Đặc thù ngành', question=f'Đặc thù của cổ phiếu ngành {industry} là gì (liệt kê, ngắn gọn)',getAnswer= getAnswer, numOfAnswers= numOfAnswers)
        get_info_and_display(title='Triển vọng ngành', question=f'Triển vọng của cổ phiếu ngành {industry} là gì (liệt kê, ngắn gọn)',getAnswer= getAnswer, numOfAnswers= numOfAnswers)
        get_info_and_display(title='Chu kỳ ngành', question=f'Chu kỳ của cổ phiếu ngành {industry} là gì (liệt kê, ngắn gọn)',getAnswer= getAnswer, numOfAnswers= numOfAnswers)

    with tab2:
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

        get_info_and_display(title='Ban điều hành', question=f'Ban điều hành của công ty có mã cổ phiếu {ticker_and_name} (liệt kê, ngắn gọn)',getAnswer= getAnswer, numOfAnswers= numOfAnswers)
        get_info_and_display(title='Các mảng kinh doanh', question=f'Các mảng kinh doanh của công ty có mã cổ phiếu {ticker_and_name} (liệt kê, ngắn gọn)',getAnswer= getAnswer, numOfAnswers= numOfAnswers)
        get_info_and_display(title='Thị phần', question=f'Thị phần của công ty có mã cổ phiếu {ticker_and_name} so với các công ty cùng ngành (liệt kê, ngắn gọn)',getAnswer= getAnswer, numOfAnswers= numOfAnswers)
        get_info_and_display(title='Đầu ra (sản phẩm/dịch vụ)', question=f'Đầu ra (sản phẩm/dịch vụ) của công ty có mã cổ phiếu {ticker_and_name} (liệt kê, ngắn gọn)',getAnswer= getAnswer, numOfAnswers= numOfAnswers)
        get_info_and_display(title='Đầu ra (thị trường)', question=f'Đầu ra (thị trường) của công ty có mã cổ phiếu {ticker_and_name} (liệt kê, ngắn gọn)',getAnswer= getAnswer, numOfAnswers= numOfAnswers)
        get_info_and_display(title='Đầu vào (nguyên vật liệu)', question=f'Đầu vào (nguyên vật liệu) của công ty có mã cổ phiếu {ticker_and_name} (liệt kê, ngắn gọn)',getAnswer= getAnswer, numOfAnswers= numOfAnswers)
        get_info_and_display(title='Đối thủ cạnh tranh', question=f'Đối thủ cạnh tranh của công ty có mã cổ phiếu {ticker_and_name} (liệt kê, ngắn gọn)',getAnswer= getAnswer, numOfAnswers= numOfAnswers)
        get_info_and_display(title='Năng lưc cạnh tranh/Lợi thế cạnh tranh', question=f'Năng lưc cạnh tranh/Lợi thế cạnh tranh của công ty có mã cổ phiếu {ticker_and_name} so với các công ty cùng ngành(liệt kê, ngắn gọn)',getAnswer= getAnswer, numOfAnswers= numOfAnswers)
        get_info_and_display(title='Lý do/Cơ hội tăng trưởng cho doanh nghiệp', question=f'Lý do/Cơ hội tăng trưởng cho doanh nghiệp của công ty có mã cổ phiếu {ticker_and_name} so với các công ty cùng ngành(liệt kê, ngắn gọn)',getAnswer= getAnswer, numOfAnswers= numOfAnswers)
        get_info_and_display(title='Lưu ý khác', question=f'Những lưu ý khi đầu tư vào công ty có mã cổ phiếu {ticker_and_name} (liệt kê, ngắn gọn)',getAnswer= getAnswer, numOfAnswers= numOfAnswers)

    with tab3:
        
        get_info_and_display(title='Tin tức', question=f'Các tin tức nổi bật, đáng chú ý về cổ phiếu {ticker_and_name} (liệt kê, ngắn gọn)',getAnswer= getAnswer, numOfAnswers= numOfAnswers)
        get_info_and_display(title='Dự án tương lai', question=f'Các dự án trong tương lai của cổ phiếu {ticker_and_name} (liệt kê, ngắn gọn)',getAnswer= getAnswer, numOfAnswers= numOfAnswers)
