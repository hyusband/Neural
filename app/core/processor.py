from rich.console import Console
from app.core.recorder import AudioRecorder
from app.services.groq_api import GroqService
from app.services.notion import NotionService
from app.data.repository import save_note, mark_as_synced
from app.data.models import Category

console = Console()

class Processor:
    def __init__(self):
        self.recorder = AudioRecorder()
        self.groq = GroqService()
        self.notion = NotionService()

    def process_voice_command(self):
        audio_file = self.recorder.record_until_enter()
        console.print(f"[green]Audio capture complete.[/green] Processing...")

        try:
            transcript = self.groq.transcribe_audio(audio_file)
            console.print(f"[bold]Transcript:[/bold] {transcript}")
        except Exception as e:
            console.print(f"[bold red]Transcription failed:[/bold red] {e}")
            return

        if not transcript:
            console.print("[yellow]No speech detected.[/yellow]")
            return

        try:
            category_str = self.groq.classify_text(transcript)
            category = Category(category_str)
            console.print(f"[blue]Category:[/blue] {category.value}")
        except Exception as e:
            console.print(f"[bold red]Classification failed:[/bold red] {e}, defaulting to LOG")
            category = Category.LOG

        note = save_note(transcript, category)
        console.print(f"[green]Saved to local DB[/green] (ID: {note.id})")

        try:
            self.notion.create_page(transcript, category)
            mark_as_synced(note.id)
            console.print("[bold green]Synced to Notion![/bold green]")
        except Exception as e:
            console.print(f"[yellow]Notion sync failed:[/yellow] {e}")
