from notion_client import Client
from app.core.config import settings
from app.data.models import Category

class NotionService:
    def __init__(self):
        self.client = Client(auth=settings.NOTION_TOKEN)
        self.database_id = settings.NOTION_DATABASE_ID

    def create_page(self, content: str, category: Category):
        properties = {
            "Name": {"title": [{"text": {"content": content}}]},
            "Category": {"select": {"name": category.value}},
            "Source": {"rich_text": [{"text": {"content": "Neural CLI"}}]}
        }
        
        self.client.pages.create(
            parent={"database_id": self.database_id},
            properties=properties
        )
