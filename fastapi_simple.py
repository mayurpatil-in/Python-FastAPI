from fastapi import FastAPI
import uvicorn

app = FastAPI(title="Simple fastapi tutorial")

@app.get("/") #path
def hello_world():
    return {"message": "hello world"}

@app.get("/hello/{name}") #path
def hello_name(name: str):
    return{"message": f"hello {name}"}

if __name__ == "__main__":
    uvicorn.run("fastapi_simple:app" , host="0.0.0.0", port=8000, reload=True)