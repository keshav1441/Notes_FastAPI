from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient

app = FastAPI()
templates = Jinja2Templates(directory="templates")

conn = MongoClient("mongodb+srv://keshavsharma1441:BvLxHXwiNUq5ioyO@cluster0.2sfep.mongodb.net/notes")


@app.get("/", response_class=HTMLResponse)
async def read(request: Request):
    newdoc=[]
    docs=conn.notes.notes.find({})
    for doc in docs:
        newdoc.append({
            "id":doc["_id"],
            "notes":doc["notes"]
        })
    return templates.TemplateResponse("index.html", {"request": request, "newdoc":newdoc})

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str | None = None):
    return {"item_id":item_id, "q": q}
