from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()

#request Get method url: "/"
@app.get("/")
async def root():
    return {"message": "welcom to my api"}

@app.get("/posts")
def get_posts():
    return {"data": "This  is your posts"}

@app.post("/createposts")
def create_posts(payLoad: dict = Body(...)):
    print(payLoad)
    return {"New_post": f"title{payLoad['title']} content{payLoad['content']}"}

