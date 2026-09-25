#Este archivo toma las claves generadas en test y las protege
import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(dotenv_path=BASE_DIR / ".env")

class Config:
    API_KEY= os.getenv("API_KEY")