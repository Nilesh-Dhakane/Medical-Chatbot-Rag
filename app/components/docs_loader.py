from app.common.logger import get_logger
from app.common.custom_exception import CustomException
import os
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from app.config.path_config import *
from langchain_core.documents import Document

logger = get_logger("data_loader.py")

def load_pdfs(docs_path:str)->Document:
    try:
        logger.info("Loading PDf files")
        if not docs_path:
            raise CustomException(f"{docs_path}File path is not found")
        loader = DirectoryLoader(
            path=docs_path,
            glob="*.pdf",
            loader_cls=PyPDFLoader
        )
        doc_files = loader.load()
        logger.info(f"All pdf files are loaded successfully")
        return doc_files

    except Exception as e:
        logger.exception(f"Error while Loading the pdf files {e}")
        raise CustomException(f"Error while loading the pdf files from {docs_path}",e)

