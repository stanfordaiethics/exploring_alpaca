# This is an example of async query, which avoids have the program block on `requests.post`.
# Please be mindful of the usage of this pattern, and don't use this as way to flood the server.
import asyncio

from httpx import AsyncClient

API_KEY = None  # Your API key.


async def query():
    prompt = "Tell me something about Alpacas."
    async with AsyncClient() as cli:
        response = await cli.post(
            "https://alpaca-internal.ngrok.io/run/predict_instruction_box",
            json={
                "data": [prompt, API_KEY]
            },
            timeout=100
        )
    return response.json()


async def main():
    tasks = [asyncio.ensure_future(query()) for _ in range(8)]
    responses = await asyncio.gather(*tasks)
    print(responses)


if __name__ == '__main__':
    asyncio.run(main())
