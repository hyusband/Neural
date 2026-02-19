import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import tempfile
import os
from typing import Optional
from app.core.config import settings
from rich.console import Console

console = Console()

class AudioRecorder:
    def __init__(self):
        self.sample_rate = settings.SAMPLE_RATE
        self.channels = settings.CHANNELS
        self.temp_file = tempfile.NamedTemporaryFile(suffix=".wav", delete=False).name


    def record_until_enter(self):
        """
        Grabar despues de presionar enter y detenerse cuando se presiona enter
        """
        console.print("[red]Recording... Press Enter to stop.[/red]")
        recording = []
        
        def callback(indata, frames, time, status):
            if status:
                console.print(status)
            recording.append(indata.copy())
            
        with sd.InputStream(samplerate=self.sample_rate, channels=self.channels, callback=callback):
            input()
            
        recording = np.concatenate(recording, axis=0)
        wav.write(self.temp_file, self.sample_rate, recording)
        return self.temp_file
