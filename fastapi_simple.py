from fastapi import FastAPI
import uvicorn

app = FastAPI(title="Simple fastapi tutorial")

if __name__ == "__main__":
    uvicorn.run("fastapi_simple:app" , host="0.0.0.0", port=8000, reload=True)