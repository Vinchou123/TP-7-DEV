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
    async with websockets.serve(echo, "10.2.2.2", 8888) as server:
        print("Server started and listening on 10.2.2.2:8888")
        await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())
