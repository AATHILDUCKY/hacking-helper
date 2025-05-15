# backend/main.py

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from utils import search_notes

app = FastAPI()

# Enable CORS for frontend access (adjust origins if needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/search")
def search(keywords: str = Query(..., description="Comma-separated keywords")):
    results = search_notes(keywords)
    return {"results": results}
