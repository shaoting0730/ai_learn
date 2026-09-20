'''
Author: shaoting0730 510738319@qq.com
Date: 2026-09-20 13:38:33
LastEditors: shaoting0730 510738319@qq.com
LastEditTime: 2026-09-20 13:55:05
FilePath: /学习代码/10-agent-memory.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''

from langchain.agents import create_agent

# 简单实现

from dotenv import load_dotenv
load_dotenv()

agent = create_agent(
    model="deepseek:deepseek-chat"
)

results =  agent.invoke({"messages":[{"role":"user","content":"来首唐诗"}]})
messages = results["messages"]

his_message = messages

his_message.append({"role":"user","content":"再来"})
results =  agent.invoke({"messages":his_message})

messages = results["messages"]
print(f"历史消息：{len(messages)}条")
for message in messages:
    message.pretty_print()    