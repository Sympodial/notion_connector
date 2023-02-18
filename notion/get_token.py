import os
import requests, json
from dotenv import load_dotenv

load_dotenv()

def get_token():
    return os.environ.get("NOTION_TOKEN")
