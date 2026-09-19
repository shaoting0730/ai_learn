'''
Author: shaoting0730 510738319@qq.com
Date: 2026-09-17 14:40:45
LastEditors: shaoting0730 510738319@qq.com
LastEditTime: 2026-09-17 18:05:58
FilePath: /ollama_local_model/07-agent-basic.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AEANG
'''
from langchain.agents import create_agent


from dotenv import load_dotenv
load_dotenv()

agent = create_agent(
    model="deepseek:deepseek-chat"
)

# print(agent)
# <langgraph.graph.state.CompiledStateGraph object at 0x1101671c0>

results =  agent.invoke({"messages":[{"role":"user","content":"你是什么模型"}]})
print(results)
# {'messages': [
# HumanMessage(content='你是什么模型', additional_kwargs={}, response_metadata={}, id='a724f882-3bce-41f6-9257-2f96eb38f006'),
# AIMessage(content='我是 DeepSeek 最新版模型！🤗\n\n具体来说，我是由深度求索公司开发的 DeepSeek 系列模型的最新版本。如果你想了解更详细的版本号信息，建议查阅 DeepSeek 官方文档和公告哦～\n\n有什么我可以帮你的吗？无论是回答问题、创作内容还是分析问题，我都很乐意帮忙！😊', additional_kwargs={'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 73, 'prompt_tokens': 7, 'total_tokens': 80, 'completion_tokens_details': None, 'prompt_tokens_details': {'audio_tokens': None, 'cache_write_tokens': None, 'cached_tokens': 0}, 'prompt_cache_hit_tokens': 0, 'prompt_cache_miss_tokens': 7}, 'model_provider': 'deepseek', 'model_name': 'deepseek-flash', 'system_fingerprint': 'aeb56401ca74e127821c4f9126dcb669', 'id': '93afe3ce-e354-4a91-886e-1f631a041141', 'finish_reason': 'stop', 'logprobs': None}, id='lc_run--01a0aed0-a177-7e43-b994-d45b7cf4bda1-0', tool_calls=[], invalid_tool_calls=[], usage_metadata={'input_tokens': 7, 'output_tokens': 73, 'total_tokens': 80, 'input_token_details': {'cache_read': 0}, 'output_token_details': {}})
# ]}

messages = results["messages"]
print(f"历史消息：{len(messages)}条")
for message in messages:
    message.pretty_print()