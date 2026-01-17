from app.common.logger import get_logger
from app.common.custom_exception import CustomException
import os
from app.components.text_embeddings import get_embedding_model
from langchain_community.vectorstores import FAISS
from app.config.path_config import *
from langchain_core.documents import Document


logger = get_logger("vectorstore.py")


def create_vector_store(vectorstore_path, documents:Document):
    try:
        logger.info("Creating new vector store")
        embedding_model = get_embedding_model()
        if os.path.exists(vectorstore_path):
            logger.info("Vector Store already present")
        
        db = FAISS.from_documents(
            embedding=embedding_model,
            documents=documents
        )
        db.save_local(folder_path=vectorstore_path)
        logger.info(f"Vector Store Created at location:={vectorstore_path}")
        
    except Exception as e:
        logger.exception(f"Error while creating vector store")
        raise CustomException("Error while creating vector store.",e)

def load_vector_store(DB_PATH):
    try:
        logger.info("Loading Vector Store")
        embedding_model = get_embedding_model()
        if  os.path.exists(DB_PATH):
            logger.info("Loading existing vecor store")
            db = FAISS.load_local(folder_path=DB_PATH,embeddings=embedding_model,allow_dangerous_deserialization=True)
            return db
        logger.warning("No Vecor Store Found")
    except Exception as e:
        logger.exception("Error while loading the db")
        raise CustomException("Error in the loading vector store.",e)     
