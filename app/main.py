import datetime

from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.staticfiles import StaticFiles
from starlette.responses import HTMLResponse

from core import templates
from core.paths import setup_path

app = FastAPI()
app.mount("/static", StaticFiles(directory=setup_path("static")), name="static")

posts = [
    {"id": i, "title": f"Title {i}", "content": "asdasdasdasdasdasdad" * 100, "created": datetime.datetime.now(tz=datetime.timezone.utc)} for i in range(1, 6)
]  # just developing mock


@app.get("/", response_class=HTMLResponse)
async def home_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "posts": posts})


@app.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})


@app.get("/posts/{post_id}", response_class=HTMLResponse)
async def post_detail(request: Request, post_id: int):
    post = next(post for post in posts if post["id"] == post_id)
    return templates.TemplateResponse("post_detail.html", {"request": request, "post": post})
