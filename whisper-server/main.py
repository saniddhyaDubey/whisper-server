from fastapi import FastAPI, UploadFile, Response
import whisper
import tempfile
import os

app = FastAPI()

model = whisper.load_model("tiny")

async def whisper_call(file: UploadFile):
    # Save the uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_file:
        temp_file.write(await file.read())  # Read and save the file
        temp_file_path = temp_file.name

    # Generate the transcription
    result = model.transcribe(temp_file_path)

    # Clean up the temporary file
    os.unlink(temp_file_path)

    return result["text"]

@app.get("/healthCheck")
def health_check_endpoint():
    return {"message": "Server running fine!"}

@app.post("/uploadFile")
async def handle_upload_file(file: UploadFile):
    transcription_text = await whisper_call(file)

    # Create a temporary .txt file with the transcription
    with tempfile.NamedTemporaryFile(delete=False, suffix=".txt") as temp_txt_file:
        temp_txt_file.write(transcription_text.encode('utf-8'))
        temp_txt_file_path = temp_txt_file.name

    # Read the .txt file content
    with open(temp_txt_file_path, "rb") as f:
        transcription_content = f.read()

    # Clean up the temporary .txt file
    os.unlink(temp_txt_file_path)

    # Return the .txt file as a response
    return Response(
        content=transcription_content,
        media_type="text/plain",
        headers={"Content-Disposition": f"attachment; filename={file.filename}.txt"}
    )