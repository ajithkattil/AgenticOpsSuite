from fastapi import FastAPI, UploadFile, File
from app.api_routes import router

app = FastAPI(title="AgenticOpsSuite")

app.include_router(router)

@app.get("/")
def root():
    return {"message": "AgenticOpsSuite is running"}
