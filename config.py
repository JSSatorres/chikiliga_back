import os
from dotenv import load_dotenv

load_dotenv()

COMUNIO_USER = os.getenv("COMUNIO_USER")
COMUNIO_PASSWORD = os.getenv("COMUNIO_PASSWORD")

