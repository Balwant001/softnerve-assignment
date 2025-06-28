import os

def spin_chapter(content):
    spun_content = content.replace("morning", "dawn").replace("sea", "ocean")
    
    os.makedirs("data/spun", exist_ok=True)
    with open("data/spun/chapter_1_spun.txt", "w", encoding="utf-8") as f:
        f.write(spun_content)
    
    return spun_content