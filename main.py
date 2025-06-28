import asyncio
from scraper import scrape_content
from ai_writer import spin_chapter
from ai_reviewer import review_chapter
from human_loop import human_review
from storage import store_version, search_content
from api import start_api

async def main():
    url = "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1"
    # Step 1: Scrape content
    raw_content = await scrape_content(url)
    
    # Step 2: AI Writer spins the chapter
    spun_content = spin_chapter(raw_content)
    
    # Step 3: AI Reviewer reviews the spun content
    reviewed_content = review_chapter(spun_content)
    
    # Step 4: Human-in-the-loop review and edit
    final_content = human_review(reviewed_content)
    
    # Step 5: Store final version in ChromaDB
    version_id = store_version(final_content, "chapter_1")
    
    # Step 6: Retrieve content using RL search
    retrieved_content = search_content("chapter_1")
    print(f"Retrieved content: {retrieved_content[:100]}...")
    
    # Start FastAPI for agent communication
    start_api()

if __name__ == "__main__":
    asyncio.run(main())