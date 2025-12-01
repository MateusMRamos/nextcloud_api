import os
from dotenv import load_dotenv

load_dotenv()

NEXTCLOUD_URL = os.getenv('NEXTCLOUD_URL')
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')
