import asyncio
import websockets

async def hello(websocket, path):
    name = await websocket.recv()
    print(f"<<< {name}")
    greeting = f"Hello {name}!"
    await websocket.send(greeting)
    print(f">>> {greeting}")


async def main():
    async with websockets.serve(hello, "10.2.2.2", 8888): 
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
