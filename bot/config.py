# config.py
import os
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("TOKEN")
