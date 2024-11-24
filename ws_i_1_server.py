import asyncio
import websockets

async def echo(websocket, path):
    async for message in websocket:
        print(f"Received message: {message}")
        response = f"Hello client! Received \"{message}\""
        await websocket.send(response)
        print(f"Sent response: {response}")

async def main():
    async with websockets.serve(echo, "10.2.2.2", 8888) as server:
        await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())