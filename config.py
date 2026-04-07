import os
from dotenv import load_dotenv

load_dotenv()

# API Keys
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Model name (important for flexibility)
GEMINI_MODEL = "gemini-2.5-flash"

# Safety checks
if not OPENWEATHER_API_KEY:
    raise ValueError("OPENWEATHER_API_KEY missing in .env")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY missing in .env")