import asyncio
import websockets

async def hello():
    uri = "ws://10.2.2.2:8888"
    async with websockets.connect(uri) as websocket:
        mess = input("Entrez un message : ")

        await websocket.send(mess) 
        print(f">>> {mess}")

        greeting = await websocket.recv() 
        print(f"<<< {greeting}")

if __name__ == "__main__":
    asyncio.run(hello())
