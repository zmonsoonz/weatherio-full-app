from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

links_data = [
    {
        "id": 1,
        "title": "GitHub",
        "url": "https://github.com/zmonsoonz",
    },
    {
        "id": 2,
        "title": "Telegram",
        "url": "https://t.me/@d.mokrov",
    },
    {
        "id": 3,
        "title": "Mail",
        "url": "mailto:mok-danil28@mail.ru",
    }
]

@app.get("/links")
def get_links():
    return links_data

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)