from fastapi import FastAPI
app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}

from fastapi import UploadFile, File

@app.post("/test-upload")
async def test_upload(file: UploadFile = File(...)):
    content = await file.read()
    return {"filename": file.filename, "size": len(content)}