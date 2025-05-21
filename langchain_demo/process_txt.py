from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import CharacterTextSplitter


def load_documents(directory="books"):
        loader = DirectoryLoader(directory)
        documents = loader.load()
        text_spliter = CharacterTextSplitter(chunk_size=256, chunk_overlap=0)
        split_docs = text_spliter.split_documents(documents)
        print(split_docs[:2])
        return split_docs
            
    
load_documents("books")
"""
window第一次
"""