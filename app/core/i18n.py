from app.core.config import settings

STRINGS = {
    "en": {
        "record_help": "Record a new voice note.",
        "init_help": "Initialize the local database.",
        "list_help": "List recent notes.",
        "sync_help": "Sync pending notes to Notion.",
        "db_init": "[green]Database initialized.[/green]",
        "synced": "[green]SYNCED[/green]",
        "unsynced": "[red]UNSYNCED[/red]",
        "all_synced": "[green]All notes are already synced.[/green]",
        "syncing": "Syncing note {}...",
        "note_synced": "[green]Note {} synced.[/green]",
        "sync_error": "[red]Failed to sync note {}:[/red] {}",
    },
    "es": {
        "record_help": "Grabar una nueva nota de voz.",
        "init_help": "Inicializar la base de datos local.",
        "list_help": "Listar notas recientes.",
        "sync_help": "Sincronizar notas pendientes con Notion.",
        "db_init": "[green]Base de datos inicializada.[/green]",
        "synced": "[green]SINCRONIZADO[/green]",
        "unsynced": "[red]NO SINCRONIZADO[/red]",
        "all_synced": "[green]Todas las notas están sincronizadas.[/green]",
        "syncing": "Sincronizando nota {}...",
        "note_synced": "[green]Nota {} sincronizada.[/green]",
        "sync_error": "[red]Error al sincronizar nota {}:[/red] {}",
    }
}

t = STRINGS.get(settings.LANGUAGE, STRINGS["en"])
