from fastapi import FastAPI
from bot import bot
import uvicorn
import asyncio
import threading

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Discord Fun Bot API is running!"}

def run_bot():
    bot.run(DISCORD_TOKEN)

@app.on_event("startup")
async def startup_event():
    bot_thread = threading.Thread(target=run_bot)
    bot_thread.start()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
