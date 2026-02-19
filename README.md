# 🧠 NEURAL
> **Direct Intelligence Pipeline for the Terminal.**

![License](https://img.shields.io/badge/License-MIT-000000?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Fedora](https://img.shields.io/badge/OS-Fedora_Linux-51A2DA?style=for-the-badge&logo=fedora&logoColor=white)
![Groq](https://img.shields.io/badge/Inference-Llama3_on_Groq-f3d03e?style=for-the-badge)

**Neural** es un "buffer" de pensamiento de baja latencia diseñado para desarrolladores. Captura ráfagas de voz, las transcribe mediante Whisper y las organiza semánticamente usando **Groq (Llama 3)**. Sin fricción, sin interfaces pesadas, solo tú y tu terminal.

---

## ⚡ Core Features

- **Voice-to-Data:** Captura instantánea de audio desde la terminal.
- **Neural Classification:** Categorización automática mediante IA en:
    - `[TASK]` - Tareas accionables y pendientes.
    - `[IDEA]` - Conceptos de negocio y proyectos futuros.
    - `[LOG]` - Registros personales y diarios emocionales.
- **Local-First:** Persistencia en SQLite. Tus pensamientos se quedan en tu máquina.
- **Latency Optimized:** Inferencia ultrarrápida para que el flujo de trabajo no se detenga.

---

## 🏗️ System Architecture

El sistema opera bajo un patrón de **Neural Layering**, separando la captura física del procesamiento cognitivo:

1.  **Aural Stage:** Stream de audio crudo optimizado para frecuencias de voz humana.
2.  **Transcription Stage:** Transformación Speech-to-Text de alta fidelidad vía Whisper.
3.  **Synthesis Stage:** Motor de inferencia (Llama 3) para estructurar el caos en datos.

---

## 🛠️ Installation (Fedora Workstation)

Para garantizar el funcionamiento del procesamiento de audio, instala las dependencias de sistema:

```bash
# 1. Dependencias de sistema
sudo dnf install portaudio-devel python3-devel -y

# 2. Setup del entorno
git clone [https://github.com/hyusband/Neural.git](https://github.com/hyusband/Neural.git) && cd Neural
python3 -m venv venv && source venv/bin/activate

# 3. Instalación en modo desarrollo
pip install -e .```
