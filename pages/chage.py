import streamlit as st
import re
import data.data as dd
import time
import pages.bg as bg

# 设置注册的标签页
st.set_page_config(
    page_title="AI智能聊天修改密码页面",
    page_icon="😀"
)
# 设置页面的标题
st.title("AI智能聊天修改密码页面 👏")

# 设置注册页面的组件
username = st.text_input("请输入手机号")
oldpassword = st.text_input("请输入原密码",type="password")
password = st.text_input("请输入新密码密码",type="password")
repass = st.text_input("请再次输入新密码密码",type="password")
loginFlag = st.button("确认修改")



# 定义一个注册函数
def change_password(username,oldpassword,password,repass):
    # 1、校验三个信息是否填写
    if username and oldpassword and password and repass:
        #2、校验用户名的长度是否为11位 并且是否为手机号 正则表达式
        if re.match('^(13|15|17|18|19)[0-9]{9}$', username):
            #3、查看两次密码是否一致 并且密码长度必须大于等于8位
            if password == repass and len(password) >=8:
                # 4、查询数据库是否有重复信息
                if dd.query_user_by_username(username) is not None:
                    result=dd.change_password(username,password)
                    st.success("修改成功")
                    time.sleep(2)
                    st.switch_page("login.py")
                else:
                    st.error("用户未注册，请先注册！")
            else:
                st.error("两次密码不一致或者密码长度字段不足8位")
        else:
            st.error("手机号格式不正确")

    else:
        st.error("请务必填写相关修改信息")




# 这是是当点击登录按钮之后需要跳转到登录界面
if loginFlag:
    change_password(username,oldpassword,password,repass)

bg.main_bg('1.png')
