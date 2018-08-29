import random
import asyncio
from aiohttp import ClientSession
import time
from concurrent.futures import ProcessPoolExecutor

async def fetch(sem,url, session):
    async with sem:
        async with session.get(url) as response:
            return await response.read()
async def run(r):
    url = "http://www.example.com/"
    tasks = []
    sem = asyncio.Semaphore(1000)
    async with ClientSession() as session:
        for i in range(r):
            task = asyncio.ensure_future(fetch(sem, url.format(i), session)) #return a task
            tasks.append(task)
        responses = asyncio.gather(*tasks)
        await responses
if __name__ == "__main__":
    number = 10000
    loop = asyncio.get_event_loop()
    start = time.time()
    loop.run_until_complete(run(number))
    end = time.time() - start
    print (end)