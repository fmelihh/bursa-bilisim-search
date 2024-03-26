from fastapi import APIRouter, UploadFile, File

from ...services.search import SearchService

search_router = APIRouter()


@search_router.get("/hello-world")
def hello_world():
    return "hello world"


@search_router.post("/upload")
async def upload(file: UploadFile = File(...)):
    file_content = await file.read()
    return SearchService.upload(file_content)
