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

    def classify_text(self, text: str) -> str:
        prompt = f"""
        Classify the following text into one of these categories:
        1. [TASK] - Actionable items, to-dos.
        2. [IDEA] - Business ideas, concepts, creative thoughts.
        3. [LOG] - Personal logs, journal entries, thoughts.

        Return ONLY the category tag (e.g. TASK, IDEA, or LOG). Do not include brackets in the output, just the word.
        
        Text: "{text}"
        """
        
        completion = self.client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="llama3-70b-8192",
        )
        
        category = completion.choices[0].message.content.strip().upper()
        if "TASK" in category: return "TASK"
        if "IDEA" in category: return "IDEA"
        if "LOG" in category: return "LOG"
        return "LOG" # Default
