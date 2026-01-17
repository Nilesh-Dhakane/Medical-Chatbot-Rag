from app.common.logger import get_logger
from app.common.custom_exception import CustomException
import os
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from app.config.path_config import *
from langchain_core.prompts import PromptTemplate
from app.components.vectorstore import load_vector_store
from app.components.llm import load_llm

logger= get_logger("retriever.py")

custom_prompt_template = """
    You are a helpful medical expert. 
    Answer the follwing medical question in one line, using only the information provided in the context.
    If context is not enough then just say: Not enough information.

    Context:
    {context}

    Question:
    {question}

    Answer:

"""

def set_custom_prompt():
    return PromptTemplate(template=custom_prompt_template, input_variables=["context","question"])


def create_qa_chain():
    try:
        logger.info("Loading Vector Store for context")
        db = load_vector_store(DB_FAISS_PATH)
        if db is None:
            raise CustomException("Vector Store is not present of empty.")
        llm = load_llm(repo_id=HUGGINGFACE_REPO_ID,HF_TOKEN=HF_TOKEN)
        if llm is None:
            raise CustomException("LLM is not loaded.")

        prompt = set_custom_prompt()
        retriever = db.as_retriever(search_kwargs={"k":1})

        rag_chain = (
        {
            "context": retriever,
            "question": RunnablePassthrough()
        }
        | prompt
        | llm
        | StrOutputParser()
        )

        # document_chain = create_stuff_documents_chain(
        # llm=llm,
        # prompt=prompt
        # )

        # retrieval_chain = create_retrieval_chain(
        #     retriever,
        #     document_chain
        # )

        
        # # qa_chain = RetrievalQA.from_chain_type(
        # #     chain_type="stuff",
        # #     llm = llm,
        # #     retriever=retriever,
        # #     return_source_documents = False,
        # #     chain_type_kwargs={"prompt":prompt}
        # # )
        logger.info("Sucessfully created qa chain")
        return rag_chain
        
    except Exception as e:
        logger.exception("Error in qa chain creation")
        raise CustomException("Error in Qa chain")
