'''
Author: shaoting0730 510738319@qq.com
Date: 2026-09-15 16:30:44
LastEditors: shaoting0730 510738319@qq.com
LastEditTime: 2026-09-15 17:05:01
FilePath: /ollama_local_model/05-chromadb-tool.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AEm
'''
import chromadb


# 列出向量库的collections和记录

def list_collection(db_path):
    client = chromadb.PersistentClient(db_path)
    collections = client.list_collections()
    print(f"chromadb:{db_path} 有 {len(collections)} 个collections");

    for i,collection in enumerate(collections):
        print(f"collection{i}:{collection.name},共有 {collection.count()}条记录")


def delete_collection(db_path, collection_name):
    try:
         client = chromadb.Persistentclient(db_path)
         client.delete_collection(collection_name)
    except Exception as e:
        print(f"删除{collection_name}是出错,{e}")

db_path="./chroma_langchain_db"
list_collection(db_path)
