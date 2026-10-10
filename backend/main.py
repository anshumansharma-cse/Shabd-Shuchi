# Fast API Testing

from fastapi import FastAPI
import uvicorn

app = FastAPI(
    title="Shabd-Shuchi",
    description=(
        "Testing Backend Module for Shabd-Shuchi"
        "Cheers!"
    ),
    version="0.0.1",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

@app.get("/")
def get_root():
    """Root Emdpoint"""
    return{
        "Purpose": "Testing module"
    }

if __name__== "__main__":
     uvicorn.run("main:app",host="127.0.0.1", port=8080, reload=True)