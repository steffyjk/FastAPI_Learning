from fastapi import FastAPI
from sqlalchemy.ext.asyncio import async_sessionmaker
from crud import CRUD
from db import engine
from schemas import NoteModel, NoteCreateModel
from http import HTTPStatus
from typing import List
from models import Note
import uuid

app = FastAPI(
    title="Noted API", description="This is a simple note taking service", docs_url="/"
)

session = async_sessionmaker(
    bind=engine,
    expire_on_commit=False
)
db = CRUD()


@app.get("/notes")
async def get_all_notes():
    notes = await db.get_all(session)
    return notes


@app.post("/notes", status_code=HTTPStatus.CREATED )
async def create_note(note_data: NoteCreateModel):
    new_note = Note(
        id=str(uuid.uuid4()),
        title=note_data.title,
        content=note_data.content,
    )
    note = await db.add(session, new_note)

    return note


@app.get("/note/{note_id}")
async def get_note_by_id(note_id) -> dict:
    note = await db.get_by_id(async_session=session,note_id="066a7046-7dba-4066-a181-28661ebea0fc")

    return note


@app.patch("/note/{note_id}")
async def update_note(note_id):
    pass


@app.delete("/note/{note_id}")
async def delete_note(note_id):
    pass
