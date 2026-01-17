from app.common.logger import get_logger
from app.common.custom_exception import CustomException
import os
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from app.config.path_config import *

logger = get_logger("llm.py")

def load_llm(repo_id:str,HF_TOKEN:str):
    try:
        logger.info("Loading LLM Model")
        llm = ChatHuggingFace(
            llm=HuggingFaceEndpoint(
            repo_id=repo_id,
            task="conversational",
            temperature=0.1,
            max_new_tokens=256,
            huggingfacehub_api_token=HF_TOKEN
        )
    )
        logger.info("LLM loaded successfully....")
        return llm

    except Exception as e:
        logger.exception("Error while loading LLM")
        raise CustomException("Error in Load LLM ")

