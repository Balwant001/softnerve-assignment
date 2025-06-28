Automated Book Publication Workflow
## Setup

1. **Clone the repository:**  
    ```bash
    git clone <your-repo-url>
    ```

2. **Install dependencies:**  
    ```bash
    pip install -r requirements.txt
    ```

3. **Install Playwright browsers:**  
    ```bash
    playwright install
    ```

## Run

1. **Start the workflow:**  
    ```bash
    python main.py
    ```

2. **Edit the file**  
    When prompted, edit `data/edited/chapter_1_edited.txt`.

3. **Continue the workflow**  
    Press Enter after editing to proceed.

4. **Access the API**  
    Visit [http://localhost:8000](http://localhost:8000) for agent communication.

## Notes

- Screenshots are saved in `data/screenshots`.
- Final content is stored in `data/final` and ChromaDB.
- Submit your code using a public Git repository and include a recorded video.
