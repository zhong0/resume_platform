from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from backend.api.router import api_router
import bootstrap

app = FastAPI()
app.include_router(api_router)

templates = Jinja2Templates(directory="frontend")

frontend_dir = Path(__file__).parent / "frontend"
app.mount("/frontend", StaticFiles(directory=frontend_dir), name="frontend")
backend_dir = Path(__file__).parent / "backend"
app.mount("/backend", StaticFiles(directory=backend_dir), name="backend")
resource_dir = Path(__file__).parent / "resource"
app.mount("/resource", StaticFiles(directory=resource_dir), name="resource")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("homepage.html", {"request": request})