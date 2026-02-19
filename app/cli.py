import typer
from rich.console import Console
from app.core.processor import Processor
from app.data.repository import init_db, get_recent_notes, get_unsynced_notes, mark_as_synced
from app.services.notion import NotionService

app = typer.Typer()
console = Console()

@app.command()
def record():
    """
    Grabar la Sesion
    """
    processor = Processor()
    processor.process_voice_command()

@app.command()
def init():
    """
    Iniciar la DB
    """
    init_db()
    console.print("[green]Database initialized.[/green]")

@app.command()
def list(limit: int = 10):
    """
    List recent notes.
    """
    notes = get_recent_notes(limit)
    for note in notes:
        status = "[green]SYNCED[/green]" if note.synced else "[red]UNSYNCED[/red]"
        console.print(f"[{note.id}] {note.created_at.strftime('%Y-%m-%d %H:%M')} [{note.category.value}] - {note.content} {status}")

@app.command()
def sync():
    """
    Tratando de escribr las notas
    """
    notes = get_unsynced_notes()
    if not notes:
        console.print("[green]All notes are already synced.[/green]")
        return
        
    notion = NotionService()
    for note in notes:
        try:
            console.print(f"Syncing note {note.id}...")
            notion.create_page(note.content, note.category)
            mark_as_synced(note.id)
            console.print(f"[green]Note {note.id} synced.[/green]")
        except Exception as e:
            console.print(f"[red]Failed to sync note {note.id}:[/red] {e}")

if __name__ == "__main__":
    app()
