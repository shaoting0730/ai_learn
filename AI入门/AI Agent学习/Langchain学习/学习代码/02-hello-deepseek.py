# from langchain_deepseek import ChatDeepSeek

# from dotenv import load_dotenv
# load_dotenv()

# model = ChatDeepSeek(
#     model="deepseek-reasoner", # deepseek-chat 深度思考，deepseek-reasoner 深度思考+推理
#     temperature=0.1,
#     max_tokens=2000,
#     timeout=None,
#     max_retries=2
# )



from langchain.chat_models import init_chat_model

from dotenv import load_dotenv
load_dotenv()

model = init_chat_model(
    model="deepseek-reasoner",
    temperature=0.1,
    max_tokens=2000,
    timeout=None,
    max_retries=2
)

for chunk in model.stream("今天是星期几"):
    print(chunk.content, end="", flush=True)
