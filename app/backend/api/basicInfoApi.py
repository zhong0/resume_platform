from fastapi import APIRouter, HTTPException, Form
from backend.service.basicInfoSvc import basicInfoSvc

router = APIRouter()
service = basicInfoSvc()

@router.post("/upload_resume")
def register(data:  str = Form(...)):
    if not service.updateResume(data):
        raise HTTPException(status_code=400, detail="Update Resume Fail")
    return {"message": "User registered successfully"}

@router.post("/get_basicInfo")
def register(data: str = Form(...)):
    result = service.getUserBasicInfo(data)
    if not result:
        raise HTTPException(status_code=400, detail="Get Basic Info Fail")
    return result