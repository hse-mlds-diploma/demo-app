from fastapi import FastAPI
import os

app = FastAPI()

API_KEY = os.getenv("API_KEY")

print(f"API_KEY: {API_KEY}")

@app.get("/")
def read_root():
    return {"Hello": "World app updated"}