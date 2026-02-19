from setuptools import setup, find_packages

setup(
    name="neural",
    version="0.1.0",
    description="A low-latency thought buffer for the terminal with Whisper, Llama 3 on Groq, and Notion integration.",
    author="hyusband",
    packages=find_packages(),
    install_requires=[
        "typer[all]",
        "python-dotenv",
        "pydantic-settings",
        "sounddevice",
        "scipy",
        "numpy",
        "groq",
        "notion-client",
        "sqlmodel",
        "rich",
    ],
    entry_points={
        "console_scripts": [
            "neural=app.cli:app",
        ],
    },
    python_requires=">=3.11",
)