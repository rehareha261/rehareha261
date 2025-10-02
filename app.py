from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()

def read_main_txt():
    with open("main.txt", "r") as file:
        return file.read()

@app.get("/github", response_class=PlainTextResponse)
async def get_github():
    return read_main_txt()

@app.get("/rehareha261/rehareha261", response_class=PlainTextResponse)
async def get_profile():
    return read_main_txt()