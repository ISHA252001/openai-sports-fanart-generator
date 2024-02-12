import streamlit as st
from pages import page1, page2, page3

pages = {
    "Home": page1,
    "UCL Fan Art Generator": page2,
    "IPL Fan Art Generator": page3,
}

page = st.sidebar.selectbox("Select a page", list(pages.keys()))

pages[page]()

