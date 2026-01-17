import os


HF_TOKEN=os.environ.get("HF_TOKEN")
HUGGINGFACE_REPO_ID="HuggingFaceH4/zephyr-7b-beta"
CHUNK_SIZE=500
CHUNK_OVERLAP=50
DB_FAISS_PATH="vectorstore/db_faiss"

DOCS_DIR = "data"
DOC_FILES_PATH = os.path.join(DOCS_DIR,"*.pdf")