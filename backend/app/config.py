import os
from pathlib import Path
from dotenv import load_dotenv

# Load .env from backend/
BACKEND_DIR = Path(__file__).resolve().parent.parent
PROJECT_DIR = BACKEND_DIR.parent
load_dotenv(BACKEND_DIR / ".env")

# Suppress HuggingFace warnings
os.environ.setdefault("HF_HUB_DISABLE_SYMLINKS_WARNING", "1")
os.environ.setdefault("HF_HUB_DISABLE_IMPLICIT_TOKEN", "1")

# OpenAI
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

# LLM
LLM_MODEL = os.getenv("LLM_MODEL", "gpt-3.5-turbo")

# Embeddings
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "paraphrase-multilingual-MiniLM-L12-v2")

# ChromaDB
CHROMA_PERSIST_DIR = str(PROJECT_DIR / os.getenv("CHROMA_PERSIST_DIR", "./chroma_db"))

# RAG Settings
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", "500"))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", "50"))
TOP_K = int(os.getenv("TOP_K", "5"))

# Data Paths
DATASET_DIR = PROJECT_DIR / os.getenv("DATASET_DIR", "./dataset")
INVESTORS_PATH = DATASET_DIR / "investors" / "investors.json"
GRANTS_PATH = DATASET_DIR / "grants" / "grants.json"
METRICS_PATH = DATASET_DIR / "metrics" / "metrics_reference.json"
FAQ_PATH = DATASET_DIR / "faq" / "faq.json"
FUNDRAISING_GUIDE_DIR = DATASET_DIR / "fundraising_guide"
REGULATIONS_DIR = DATASET_DIR / "regulations"
