from fastapi import APIRouter, UploadFile, File
from app.utils.log_parser import analyze_log

router = APIRouter()

@router.post("/analyze")
async def analyze_log_file(log: UploadFile = File(...)):
    contents = await log.read()
    return analyze_log(contents.decode())
