from typing import List, Optional
from sqlmodel import Session, create_engine, select
from app.core.config import settings
from app.data.models import Note, Category

engine = create_engine(f"sqlite:///{settings.SQLITE_DB_PATH}")

def init_db():
    from sqlmodel import SQLModel
    SQLModel.metadata.create_all(engine)

def save_note(content: str, category: Category) -> Note:
    with Session(engine) as session:
        note = Note(content=content, category=category)
        session.add(note)
        session.commit()
        session.refresh(note)
        return note

def get_unsynced_notes() -> List[Note]:
    with Session(engine) as session:
        statement = select(Note).where(Note.synced == False)
        return list(session.exec(statement).all())

def mark_as_synced(note_id: int):
    with Session(engine) as session:
        note = session.get(Note, note_id)
        if note:
            note.synced = True
            session.add(note)
            session.commit()

def get_recent_notes(limit: int = 10) -> List[Note]:
    with Session(engine) as session:
        statement = select(Note).order_by(Note.created_at.desc()).limit(limit)
        return list(session.exec(statement).all())
