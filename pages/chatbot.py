import streamlit as st
import pages.bg as bg
st.title('AI应用产品网👏')

col,col1,col2,col3 = st.columns(4)
with col:
    st.image("4.png")
    bt = st.button("小白助手")
    if bt:
        st.switch_page("pages/xiaobaibot.py")
with col1:
    st.image("2.png")
    bt1 = st.button("IT百科")
    if bt1:
        st.switch_page("pages/dfswbot.py")
with col2:
    st.image("5.png")
    bt2 = st.button("知心朋友")
    if bt2:
        st.switch_page("pages/friend.py")
with col3:
    st.image("3.png")
    bt3 = st.button("宠物顾问")
    if bt3:
        st.switch_page("pages/pet.py")
bg.main_bg('1.png')