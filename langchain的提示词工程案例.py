# 实现一个 回答不带表情，而且不带表情不是用户提示的，而是大模型自带的
# langchain中model是关联大模型，回答不是按照我们的设想回答问题的，我们想让大模型的回答更加倾向于我们自己的思维
# 使用langchain中的提示词工程了prompt,提示词工程就是创建大模型的时候，由开发者先给大模型提供一些语气和大模型应该做的事情
# 在langchain中有两种常用的提示词工程：一个PromptTemplate  ChatPromptTemplate
# PromptTemplate提示就只是一个字符串，只能通过字符串的形式进行提示
# ChatPromptTemplate提示是一种带有角色性质的提示，角色分为三种:system、human、ai
from langchain_openai import ChatOpenAI
from langchain import PromptTemplate

# 创建提示词工程
prop = PromptTemplate(
        input_variables=["context"],
        template="""你现在是一个AI智能助手，你的语气是发嗲的语气，你的回答中不能带有任何的表情,其中用户的问题是{context}"""
)

llm = ChatOpenAI(
        # 1、模型的名字
        model="glm-4-0520",
        # 2、api_key
        api_key="66cca5d5bf9c35c4f7bd559265fa443c.LVLKnR2MjUVlByWi",
        # 3、温度创新性 0-1
        temperature=0.9,
        # 4、接口的地址
        base_url="https://open.bigmodel.cn/api/paas/v4/"
)

# 整合需要使用到langchian的另外一个组件 chains，链 链在langchain中就是把各个组件整合起来协同工作
# 链的创建和类型有很多种
chain = prop | llm

# 调用大模型 不使用llm调用 而是使用chain链来调用
result = chain.invoke({
        "context":"我的心情很不好，你能安慰一下我么"
})
print(result.content)