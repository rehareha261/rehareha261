from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/github")
async def get_main_content():
    try:
        with open("main.txt", "r") as file:
            content = file.read()
        return {"content": content}
    except FileNotFoundError:
        return {"error": "File not found"}

@app.get("/rehareha261/rehareha261")
async def get_readme_content():
    url = "https://raw.githubusercontent.com/rehareha261/rehareha261/main/README.md"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return {"content": response.text}
    except Exception as e:
        return {"error": str(e)}