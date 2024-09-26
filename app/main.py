from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.api import inventory  # Import your inventory routes
from starlette.requests import Request

app = FastAPI()

# Serve static files from the frontend/static directory
app.mount("/static", StaticFiles(directory="frontend/static"), name="static")

# Set up Jinja2 templates (optional if you are rendering HTML using templates)
templates = Jinja2Templates(directory="frontend/templates")

# Include the inventory routes from the inventory.py file
app.include_router(inventory.router)

# Route to serve the index.html file using Jinja2 templates (or you can use a static HTML file)
@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})