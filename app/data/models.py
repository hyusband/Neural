from datetime import datetime
from enum import Enum
from typing import Optional
from sqlmodel import Field, SQLModel

class Category(str, Enum):
    TASK = "TASK"
    IDEA = "IDEA"
    LOG = "LOG"

class Note(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    content: str
    category: Category
    created_at: datetime = Field(default_factory=datetime.now)
    synced: bool = Field(default=False)
