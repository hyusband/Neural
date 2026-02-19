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
            result = self.groq.process_text(transcript)
            category_str = result.get("category", "LOG").upper()
            refined_text = result.get("refined_text", transcript)
            
            try:
                category = Category(category_str)
            except ValueError:
                if "TASK" in category_str: category = Category.TASK
                elif "IDEA" in category_str: category = Category.IDEA
                else: category = Category.LOG
                
            console.print(f"[blue]Category:[/blue] {category.value}")
            console.print(f"[bold]Refined:[/bold] {refined_text}")
        except Exception as e:
            console.print(f"[bold red]Processing failed:[/bold red] {e}, using raw transcript")
            category = Category.LOG
            refined_text = transcript

        note = save_note(refined_text, category)
        console.print(f"[green]Saved to local DB[/green] (ID: {note.id})")

        try:
            self.notion.create_page(refined_text, category)
            mark_as_synced(note.id)
            console.print("[bold green]Synced to Notion![/bold green]")
        except Exception as e:
            console.print(f"[yellow]Notion sync failed:[/yellow] {e}")
