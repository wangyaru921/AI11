import streamlit as st
import pages.pets as pp
import data.data as dd
import model.model as mm
import pages.bg as bg
# 全新的AI助手，专用负责翻译

user_id = st.session_state.user_id  # 用户id就是某一个用户的唯一标识
username = st.session_state.username

# streamlit的session_state缓存器进行处理 新数据覆盖旧数据的问题
if "messages" not in st.session_state:
    # 缓存的数据以字典类型的数组来缓存
    # [{"role":user,context:xxx},{}]
    st.session_state.messages = []

# 需要从缓存中获取数据进行界面的渲染
list = dd.query_message_by_user_id_pet(user_id=user_id)
if list:
    # {"message_id":xx,"user_id":xx,message:xxx,role:xxx,message_time:xxx"}
    for msg in list:
        with st.chat_message(msg["role"]):
            st.write(msg["message"])
else:
    # 如果当前用户和AI助手没有任何的聊天记录，需要给他一个默认的助手欢迎语
    with st.chat_message("assistant"):
        st.write("我是你的智能AI助手，可以回答你相关宠物的问题，请问你有什么问题？")


if len(st.session_state.messages) <=0 :
    with st.chat_message("assistant"):
        st.write("你好，我是你的专属宠物助手，可以回答你的任何的宠物问题")

input = st.chat_input("请输入你要咨询的宠物问题")
if input:
    with st.chat_message("user"):
        st.write(input)
        dd.add_chat_message_pet(user_id, input, "user")
        res = mm.invoke(input)
    st.session_state.messages.append({"role":"user","context":input})
    result = (pp.chain_invoke({"context":input}))
    with st.chat_message("assistant"):
        st.write(result)
        dd.add_chat_message_pet(user_id, res, "assistant")
    st.session_state.messages.append({"role": "assistant", "context": result})
bg.main_bg('1.png')

