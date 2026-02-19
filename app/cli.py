import typer
from rich.console import Console
from app.core.processor import Processor
from app.data.repository import init_db, get_recent_notes, get_unsynced_notes, mark_as_synced
from app.services.notion import NotionService
from app.core.i18n import t

app = typer.Typer()
console = Console()

@app.command()
def record():
    """
    {help}
    """.format(help=t["record_help"])
    processor = Processor()
    processor.process_voice_command()

@app.command()
def init():
    """
    {help}
    """.format(help=t["init_help"])
    init_db()
    console.print(t["db_init"])

@app.command()
def list(limit: int = 10):
    """
    {help}
    """.format(help=t["list_help"])
    notes = get_recent_notes(limit)
    for note in notes:
        status = t["synced"] if note.synced else t["unsynced"]
        console.print(f"[{note.id}] {note.created_at.strftime('%Y-%m-%d %H:%M')} [{note.category.value}] - {note.content} {status}")

@app.command()
def sync():
    """
    {help}
    """.format(help=t["sync_help"])
    notes = get_unsynced_notes()
    if not notes:
        console.print(t["all_synced"])
        return
        
    notion = NotionService()
    for note in notes:
        try:
            console.print(t["syncing"].format(note.id))
            notion.create_page(note.content, note.category)
            mark_as_synced(note.id)
            console.print(t["note_synced"].format(note.id))
        except Exception as e:
            console.print(t["sync_error"].format(note.id, e))

if __name__ == "__main__":
    app()
