from playwright.async_api import async_playwright
import os

async def scrape_content(url):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto(url)
        
        content = await page.locator("div.mw-parser-output").inner_text()
        
        os.makedirs("data/screenshots", exist_ok=True)
        await page.screenshot(path="data/screenshots/chapter_1.png")
        
        await browser.close()
        
        os.makedirs("data/raw", exist_ok=True)
        with open("data/raw/chapter_1.txt", "w", encoding="utf-8") as f:
            f.write(content)
        
        return content