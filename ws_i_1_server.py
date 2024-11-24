import asyncio
import websockets

async def echo(websocket, path):
    try:
        async for message in websocket:
            print(f"Received message: {message}")
            response = f"Hello client! Received \"{message}\""
            await websocket.send(response)
            print(f"Sent response: {response}")
    except websockets.exceptions.ConnectionClosedError as e:
        print(f"Connection closed error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

async def main():
    async with websockets.serve(echo, "10.2.2.223", 8888) as server:
        await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())
