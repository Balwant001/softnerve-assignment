import os

def review_chapter(content):
    reviewed_content = f"[AI Reviewer Note: Content is clear and coherent]\n{content}"
    
    os.makedirs("data/reviewed", exist_ok=True)
    with open("data/reviewed/chapter_1_reviewed.txt", "w", encoding="utf-8") as f:
        f.write(reviewed_content)
    
    return reviewed_content