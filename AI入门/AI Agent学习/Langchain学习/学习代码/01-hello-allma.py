# from langchain_ollama import ChatOllama
  
# model = ChatOllama(
#     model="deepseek-r1:1.5b",
#     base_url="http://localhost:11434",
#     temperature=0.7,
# )

# response = model.stream("来一段唐诗宋词让我欣赏一下")

# for chunk in response:
#     print(chunk.content, end="", flush=True)


# langchain1.0

from langchain.chat_models import init_chat_model

model = init_chat_model(
    model="ollama:deepseek-r1:1.5b",
    base_url="http://localhost:11434",
    temperature=0.7,
)

response = model.stream("来一段唐诗宋词让我欣赏一下")

for chunk in response:
    print(chunk.content, end="", flush=True)