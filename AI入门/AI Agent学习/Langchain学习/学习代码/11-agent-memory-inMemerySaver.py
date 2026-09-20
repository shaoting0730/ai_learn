'''
Author: shaoting0730 510738319@qq.com
Date: 2026-09-20 13:55:35
LastEditors: shaoting0730 510738319@qq.com
LastEditTime: 2026-09-20 16:11:47
FilePath: /学习代码/11-agent-memory-inMemerySaver.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''


from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver


from dotenv import load_dotenv
load_dotenv()

checkpointer = InMemorySaver()

agent = create_agent(
    model="deepseek:deepseek-chat",
    checkpointer=checkpointer
)

config = {"configurable":{"thread_id":1}}

results =  agent.invoke(
    {"messages":[{"role":"user","content":"来首唐诗"}]},
    config=config
    )
messages = results["messages"]
for message in messages:
    message.pretty_print()    

results =  agent.invoke(
    {"messages":[{"role":"user","content":"再来"}]},
    config=config
    )
messages = results["messages"]
for message in messages:
    message.pretty_print()    

