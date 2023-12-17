from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.staticfiles import StaticFiles
from starlette.responses import HTMLResponse

from core import templates
from core.paths import setup_path

app = FastAPI()
app.mount("/static", StaticFiles(directory=setup_path("static")), name="static")

posts = [{"title": f"Title {i}", "content": "asdasdasdasdasdasdad" * 100} for i in range(24)]  # just developing mock


@app.get("/", response_class=HTMLResponse)
async def home_page(request: Request):
    return templates.TemplateResponse("home/index.html", {"request": request, "posts": posts})


@app.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})
