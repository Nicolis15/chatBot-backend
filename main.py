from backend import app
from dotenv import load_dotenv
import uvicorn
import os

if __name__ == "__main__":
    load_dotenv()
    uvicorn.run(
        app.app, host="0.0.0.0", port = int(os.environ.get("PORT", 8000)), log_level="info") #os.getenv('HOST')