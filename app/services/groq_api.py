import os
from groq import Groq
from app.core.config import settings

class GroqService:
    def __init__(self):
        self.client = Groq(api_key=settings.GROQ_API_KEY)

    def transcribe_audio(self, file_path: str) -> str:
        with open(file_path, "rb") as file:
            transcription = self.client.audio.transcriptions.create(
                file=(file_path, file.read()),
                model="whisper-large-v3",
                response_format="json"
            )
            return transcription.text

    def process_text(self, text: str) -> dict:
        prompt = f"""
        You are an intelligent assistant for a developer's CLI tool. 
        Your job is to process the following raw voice transcription.

        1. **Refine**: Clean up the text. Remove filler words (like "eh", "um"), fix grammar, make it concise and professional. Keep the original meaning and language.
        2. **Classify**: Categorize it into one of:
           - [TASK]: Actionable items, to-dos.
           - [IDEA]: Business ideas, concepts.
           - [LOG]: Personal thoughts, journaling.

        Return the result in JSON format with two keys: "category" and "refined_text".

        Raw Text: "{text}"
        """
        
        completion = self.client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant that outputs JSON."
                },
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="llama-3.3-70b-versatile",
            response_format={"type": "json_object"}
        )
        
        try:
            import json
            content = completion.choices[0].message.content
            return json.loads(content)
        except Exception as e:
            return {"category": "LOG", "refined_text": text}
