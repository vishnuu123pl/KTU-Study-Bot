import asyncio
import os
from aiohttp import web
from bot import app, main

async def handle(request):
    return web.Response(text="Bot is Running")

async def start_web():
    server = web.Application()
    server.router.add_get("/", handle)
    runner = web.AppRunner(server)
    await runner.setup()
    port = int(os.environ.get("PORT", 8000))
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()
    print(f"Flask Started")

async def run():
    await start_web()
    await main()

if __name__ == "__main__":
    asyncio.run(run())
