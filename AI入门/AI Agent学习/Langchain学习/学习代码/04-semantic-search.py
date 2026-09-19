'''
Author: shaoting0730 510738319@qq.com
Date: 2026-09-15 13:14:48
LastEditors: shaoting0730 510738319@qq.com
LastEditTime: 2026-09-15 16:23:18
FilePath: /ollama_local_model/04-semantic-search.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma

# 嵌入模型
embedding = OllamaEmbeddings(model="nomic-embed-text")

# 向量库
vecor_store = Chroma(
    collection_name = "example_collection",
    embedding_function=embedding,
    persist_directory="./chroma_langchain_db"
)

print("--------------相似度查询-------------------")
# 相似度查询
results = vecor_store.similarity_search("小林吃饭时，遇见的搞笑事件")

for index, result in enumerate(results):
    print(index)
    print(result.page_content)

print("--------------带分数的相似度查询-------------------")
# 带分数的相似度查询
results = vecor_store.similarity_search_with_score("小林吃饭时，遇见的搞笑事件")

for (doc, scode)  in results:
    print(scode)
    print(doc.page_content)

# 用向量进行相似度查询
print("--------------用向量进行相似度查询-------------------")
vector = embedding.embed_query(
    "小林吃饭时，遇见的搞笑事件"
)    

results = vecor_store.similarity_search_by_vector(vector)

for index, result in enumerate(results):
    print(index)
    print(result.page_content)

print("--------------用检索器查询-------------------")
# chain: LangChain: 大模型、提示词模版、toos、output, Runnable

from typing import List 

from langchain_core.documents import Document
from langchain_core.runnables import chain

@chain
def retriever(query: str) -> List[Document]:
    return vecor_store.similarity_search(query,k=1)

result = retriever.invoke("小林吃饭时，遇见的搞笑事件")      

for index, result in enumerate(results):
    print(index)
    print(result.page_content)