from db import database, notes
from fastapi import FastAPI
from models import Note, NoteIn, NoteDl, NoteUp
app = FastAPI()



@app.post("/notes/", response_model=Note)
async def create_note(note: NoteIn):
    query = notes.insert().values(text=note.text, completed=note.completed)
    last_record_id = await database.execute(query)
    return {**note.dict(), "id": last_record_id}