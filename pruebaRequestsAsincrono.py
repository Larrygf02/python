import asyncio
from aiohttp import ClientSession

async def hello(url):
	async with ClientSession() as session:
		async with session.get(url) as response:
			response = await response.read()
			print(response)
loop = asyncio.get_event_loop()
#loop.run_until_complete(hello("http://httpbin.org/headers"))
tasks = []
# I'm using test server localhost, but you can use any url
url = "https://apidocs.sendinblue.com/api-status/"
for i in range(5):
    task = asyncio.ensure_future(hello(url.format(i)))
    tasks.append(task)
loop.run_until_complete(asyncio.wait(tasks))