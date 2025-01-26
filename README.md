# Whisper Server

This project is a FastAPI server wrapper around the OpenAI Whisper model for transcribing audio files. It uses the tiny Whisper model for demonstration.

---

## **Table of Contents**
1. [Prerequisites](#prerequisites)
2. [Setup Instructions](#setup-instructions)
   - [Clone the Repository](#1-clone-the-repository)
   - [Create a Virtual Environment](#2-create-a-virtual-environment)
   - [Activate the Virtual Environment](#3-activate-the-virtual-environment)
   - [Install Dependencies](#4-install-dependencies)
   - [Run the Server](#5-run-the-server)
3. [API Endpoints](#api-endpoints)
   - [Health Check](#1-health-check)
   - [Upload File](#2-upload-file)
4. [Notes](#notes)
5. [License](#license)

---

## **Prerequisites**
- Python 3.8+ installed
- [Git](https://git-scm.com/downloads) installed

---

## **Setup Instructions**

### 1. Clone the Repository
```bash
git clone <repository-url>
cd whisper-server
```

### 2. Create a Virtual Environment
```bash
python -m venv whisper-env
```

### 3. Activate the Virtual Environment
- Windows
```bash
whisper-env\Scripts\activate
```

- macOS/Linux
```bash
source whisper-env/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Run the Server
```bash
uvicorn main:app --host 0.0.0.0 --port 8089
```
The server will start on http://0.0.0.0:8089

## **API Endpoints**

### 1. Health Check
URL: GET /healthCheck
Description: Returns a simple message to confirm the server is running.

### 2. Upload File
URL: POST /uploadFile
Description: Accepts an audio file for transcription and returns the transcribed text.
Request:
 - Content-Type: multipart/form-data
 - Form field: file (audio file)

## **Notes**
 1. Ensure the audio file is in a supported format, such as .wav or .mp3.
 2. The current implementation uses the Whisper tiny model. You can modify main.py to use other Whisper models as needed.
