from app.common.logger import get_logger
from app.common.custom_exception import CustomException
import os
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from app.config.path_config import *
from langchain_core.documents import Document

logger = get_logger("text_embedding.py")


def get_embedding_model()->HuggingFaceEmbeddings:
    try:
        logger.info("Creating embedding model")
        embedding_model = HuggingFaceEmbeddings(
            model="sentence-transformers/all-MiniLM-L6-v2"
        )
        logger.info("Embedding Model Creation successfully")
        return embedding_model
    except Exception as e:
        logger.info(f"Error occured while creating embedding model")
        raise CustomException("Error while get_embedding model",e)

# def create_text_embeddings(documents:Document):
#     try:
#         logger.ino("Embeddings creation started")
#         if not documents:
#             raise CustomException("Documents are empty.")
        
#         embeddings = get_embedding_model()
        
#     except:
#         pass