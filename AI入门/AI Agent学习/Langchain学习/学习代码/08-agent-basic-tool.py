'''
Author: shaoting0730 510738319@qq.com
Date: 2026-09-19 14:03:05
LastEditors: shaoting0730 510738319@qq.com
LastEditTime: 2026-09-19 14:23:12
FilePath: /ollama_local_model/08-agent-basic-tool.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''

from langchain.agents import create_agent


from dotenv import load_dotenv
load_dotenv()

def get_weather(city:str) -> str:
    """查询天气如何"""
    return f"今天{city}天气是多云转晴"

agent = create_agent(
    model="deepseek:deepseek-chat",
    tools=[get_weather]
)


results =  agent.invoke({"messages":[{"role":"user","content":"杭州天气如何？"}]})

messages = results["messages"]
for message in messages:
    message.pretty_print()