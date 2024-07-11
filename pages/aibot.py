# 女朋友
# 1、ai得知道他是你的女朋友 langchain中提示词模块来限定
#    女朋友的性格和类型由用户选择
# 2、ai还能能记住用户和它聊天的记录
#    langchain的memory记忆模块来实现
# 3、需要使用langchain的chain链，链把提示词+模型+记忆连接起来
# 构建我们的提示词，通过提示词来给大模型定义规则
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory # 在内存中保存历史记忆的模块
from langchain.chains import ConversationChain
import data.data as dd
import model.model as mm
import pages.bg as bg

user_id = st.session_state.user_id  # 用户id就是某一个用户的唯一标识
username = st.session_state.username
st.title('我的知心朋友❤️❤️💕❤️💕')
st.subheader("原来是你，高山流水觅知音")
if "gms" not in st.session_state:
    st.session_state.gms =[]

for gm in st.session_state.gms:
    with st.chat_message(gm["role"]):
        st.write(gm["context"])

list = dd.query_message_by_user_id_friends(user_id=user_id)
if list:
    # {"message_id":xx,"user_id":xx,message:xxx,role:xxx,message_time:xxx"}
    for msg in list:
        with st.chat_message(msg["role"]):
            st.write(msg["message"])
else:
    # 如果当前用户和AI助手没有任何的聊天记录，需要给他一个默认的助手欢迎语
    with st.chat_message("assistant"):
        st.write("我是你的智能AI助手，可以像朋友一样和你聊天？")

# 构建的大模型
llm = ChatOpenAI(
    model="glm-4-0520",
    api_key="4e8359731127a629e7d20d4cfe2ffe23.rtG99jESZmNdEA7K",
    temperature=0.99,
    base_url="https://open.bigmodel.cn/api/paas/v4/"
)
# 构建记忆模块
if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory()
# 通过链把三个模块给连接起来
# ConversationChain链之所以能所以历史记忆存储，主要是因为会做一件事情，会把memory记忆模块中的数据以history参数名的形式
# 封装到链的PromptTemplate提示词模板当中
temp = "现在你要扮演一个朋友的角色，你的性格是"+st.session_state.xingge+"，你只需要回答你朋友的话即可，不需要重复用户的话，也不要加表情，也不需要将你的角色和性格进行展示。你的朋友说的话是:{input},你们的以前的对话是{history}"
prompt = PromptTemplate(
    input_variables=["input","history"],
    template=temp
)
chain = ConversationChain(
    prompt=prompt,
    llm=llm,
    memory=st.session_state.memory
)

input = st.chat_input("和你的朋友说点话吧")
if input:
    with st.chat_message("user"):
        st.write(input)
        dd.add_chat_message_friends(user_id, input, "user")
        res = mm.invoke(input)
    st.session_state.gms.append({"role":"user","context":input})
    # 调用大模型回答我们的问题
    result = chain.invoke(input)
    # 带有记忆的链result中没有content,
    with st.chat_message("assistant"):
        st.write(result["response"])
        dd.add_chat_message_friends(user_id, res, "assistant")
    st.session_state.gms.append({"role":"assistant","context":result["response"]})
bg.main_bg('1.png')
