from fastapi import APIRouter
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from models.note import Note
from config.db import conn
from schemas.note import noteEntities,noteEntity

Notes=APIRouter()
templates = Jinja2Templates(directory="templates")

@Notes.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    docs = conn.notes.notes.find({})
    newdoc = []
    for doc in docs:
        newdoc.append({
            "id": doc.get("_id"),
            "title": doc.get("title", "Untitled"),  # Provide a default value if title is missing
            "description": doc.get("description", "No description"),  # Provide a default value if description is missing
            "important": doc.get("important", False)  # Default to False if 'important' is missing
        })
    return templates.TemplateResponse("index.html", {"request": request, "newdoc": newdoc})



@Notes.post("/")
async def create_item(request: Request):
    form = await request.form()
    form_dict = dict(form)
    form_dict["important"] = True if form_dict["important"] == "on" else False
    inserted_note = conn.notes.notes.insert_one(form_dict)    
    return {"success": True}

