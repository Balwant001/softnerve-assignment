from fastapi import FastAPI
import uvicorn
from scraper import scrape_content
from ai_writer import spin_chapter
from ai_reviewer import review_chapter
from storage import store_version

app = FastAPI()

@app.get("/scrape/{url:path}")
async def scrape(url: str):
    content = await scrape_content(url)
    return {"content": content}

@app.post("/spin")
async def spin(content: str):
    spun_content = spin_chapter(content)
    return {"spun_content": spun_content}

@app.post("/review")
async def review(content: str):
    reviewed_content = review_chapter(content)
    return {"reviewed_content": reviewed_content}

@app.post("/store/{chapter_id}")
async def store(content: str, chapter_id: str):
    version_id = store_version(content, chapter_id)
    return {"version_id": version_id}

def start_api():
    uvicorn.run(app, host="0.0.0.0", port=8000)