from backend import app
from dotenv import load_dotenv
import uvicorn
import os

if __name__ == "__main__":
    load_dotenv()
    uvicorn.run(
        app.app, host=os.getenv('HOST'), port=5000, log_level="info")