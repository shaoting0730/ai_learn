from langchain_core import documents
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma

file_path = "happy.pdf"

loader = PyPDFLoader(file_path)

doc = loader.load()

# print(doc)
# print(len(doc))
# print(doc[0])
# print(type(doc[0]))

text_splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=50,add_start_index=True)

all_splits = text_splitter.split_documents(doc)

# print(len(all_splits))
# print(all_splits[0])
# print(type(all_splits[0]))

embeddings = OllamaEmbeddings(model="nomic-embed-text")
# vecor_0 = embeddings.embed_query(all_splits[0].page_content)

# print(len(vecor_0))
# print(vecor_0)

vecor_store = Chroma(
    collection_name = "example_collection",
    embedding_function=embeddings,
    persist_directory="./chroma_langchain_db"
)

ids = vecor_store.add_documents(documents=all_splits)

print(len(ids))
print(ids)