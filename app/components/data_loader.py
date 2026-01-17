from app.common.logger import get_logger
from app.common.custom_exception import CustomException
import os
from app.components.docs_loader import load_pdfs
from app.components.text_splitter import text_splitting_of_docs
from app.components.text_embeddings import get_embedding_model
from app.components.vectorstore import create_vector_store, load_vector_store
from langchain_community.vectorstores import FAISS
from app.config.path_config import *
from langchain_core.documents import Document


logger = get_logger("data_loader.py")

def process_all_components():
    try:
        logger.info("Processin all components till vector store")
        documents = load_pdfs(docs_path=DOCS_DIR)
        text_chunks = text_splitting_of_docs(documents=documents)
        create_vector_store(vectorstore_path=DB_FAISS_PATH,documents=text_chunks)
        logger.info("All components process completed...")
    except Exception as e:
        logger.exception("Error while running all components till vector store creation")
        raise CustomException("Error While process Compoenents",e)
        
if __name__=="__main__":
    process_all_components()