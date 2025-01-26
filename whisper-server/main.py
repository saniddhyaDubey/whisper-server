from fastapi import FastAPI, UploadFile
import whisper
import tempfile     # To temporary store the file, so that whisper can access!

app = FastAPI()

model = whisper.load_model("tiny")

async def whisper_call(file: UploadFile):

    # TODO: Do we have to save the file to the server ?
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_file:
        temp_file.write(await file.read())  # Read and save the file
        temp_file_path = temp_file.name

    # Generating the Transcribe!
    result = model.transcribe(temp_file_path)   # TODO: Create a .txt file and save in a directory on server!

    temp_file.close()
    return result

@app.get("/healthCheck")
def health_check_endpoint():
    return {"message": "Server running fine!"}

@app.post("/uploadFile")
async def handle_upload_file(file: UploadFile):
    transcription_result = await whisper_call(file)
    return {"file": file.filename, "transcription": transcription_result["text"]}
