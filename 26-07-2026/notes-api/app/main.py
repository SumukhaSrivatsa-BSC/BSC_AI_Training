from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Notes API", version="0.1.0")


class Note(BaseModel):
    id: int
    title: str
    body: str


# Simple in-memory store for the demo (not for production)
_notes: dict[int, Note] = {}


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/notes", response_model=Note, status_code=201)
def create_note(note: Note) -> Note:
    if note.id in _notes:
        raise HTTPException(status_code=409, detail="Note already exists")
    _notes[note.id] = note
    return note


@app.get("/notes/{note_id}", response_model=Note)
def get_note(note_id: int) -> Note:
    note = _notes.get(note_id)
    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return note
