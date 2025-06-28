import os

def human_review(content):
    os.makedirs("data/edited", exist_ok=True)
    input_path = "data/edited/chapter_1_edited.txt"
    with open(input_path, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"Please edit the file at {input_path} and save changes.")
    input("Press Enter after editing the file...")
    
    with open(input_path, "r", encoding="utf-8") as f:
        edited_content = f.read()
    
    os.makedirs("data/final", exist_ok=True)
    with open("data/final/chapter_1_final.txt", "w", encoding="utf-8") as f:
        f.write(edited_content)
    
    return edited_content