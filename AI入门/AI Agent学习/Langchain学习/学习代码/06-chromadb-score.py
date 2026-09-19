'''
Author: shaoting0730 510738319@qq.com
Date: 2026-09-15 17:08:28
LastEditors: shaoting0730 510738319@qq.com
LastEditTime: 2026-09-15 20:35:49
FilePath: /ollama_local_model/06-chromadb-score.py
Description: 搞不懂
'''
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
# 嵌入模型:#
embedding=OllamaEmbeddings(model="qwen3-embedding:4b")

#评分方式
score_measures=[
   "default",
   "cosine",  # 用两个向量的夹角度量相似度，
   "12",      # 用两个向量的距离度量相似度，
   "ip"    #用两个向量的内积/点积度量相似度，
]

#创建向量库和4个collection
persist_dir="./chroma_score_db"
vector_stores=[]
for score_measure in score_measures:
    collection_metadata={"hnsw:space": score_measure}
    if score_measure == "default":
       collection_metadata = None

    collection_name = f"my_collection_{score_measure}"
    vector_stores.append(Chroma(
        collection_name=collection_name,
        embedding_function=embedding,
        persist_directory=persist_dir,
        collection_metadata=collection_metadata
    ))

def indexing(docs):
    print("\n加入文档:")
    for vector_store in vector_stores:
        ids=vector_store.add_documents(docs)
        print("\n集合{vector_store._document.name}")
        print(ids)   


def query_with_score(query):
    for i in range(len(score_measures)):
        results=vector_stores[i].similarity_search_with_score(query)
        print(f"\n搜索{query}")
        for doc, score in results:
            print (doc.page_content, end='')
            print (f"{score_measures[i]}: {score}")


docs=[
   Document(page_content="这个小米手机很好用"),
   Document(page_content="我国陕西地区盛产小米"),
]

indexing(docs);


# query_with_score("我刚和朋友通完话")