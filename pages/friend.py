import streamlit as st
import pages.bg as bg
st.title("朋友性格选择页面")
if "xingge" not in st.session_state:
    st.session_state.xingge = ""
bt = st.button("温柔知性")
if bt:
    st.session_state.xingge="温柔知性"
    st.switch_page("pages/aibot.py")
bt1 = st.button("霸道冷漠")
if bt1:
    st.session_state.xingge="霸道冷漠"
    st.switch_page("pages/aibot.py")
bt2 = st.button("活泼可爱")
if bt2:
    st.session_state.xingge="活泼可爱"
    st.switch_page("pages/aibot.py")
bg.main_bg('1.png')