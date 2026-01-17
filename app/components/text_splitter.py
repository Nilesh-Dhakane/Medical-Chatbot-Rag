from app.common.logger import get_logger
from app.common.custom_exception import CustomException
import os
from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.config.path_config import *
from langchain_core.documents import Document

logger = get_logger("text_splitter.py")


def text_splitting_of_docs(documents:Document)->Document:
    try:
        logger.info("Text Splitting started for chunking")
        print(f"Type of Document:---{type(documents)}")
        if not documents:
            raise CustomException(f"Documnets are empty. No. of documents:= {len(documents)}")
        splitter = RecursiveCharacterTextSplitter(
            chunk_size = CHUNK_SIZE,
            chunk_overlap = CHUNK_OVERLAP
        )
        text_chunks = splitter.split_documents(documents=documents)
        logger.info(f"Text Chunking successfully.")
        logger.info(f"Smaple Text Chunk metadata := {text_chunks[0].metadata}")
        return text_chunks

    except Exception as e:
        logger.exception(f"Error while splitting the documents into chunks. {e}")
        raise CustomException("Error in split documents",e)