import asyncio
import websockets

async def send_message():
    uri = "ws://10.2.2.223:8888"
    async with websockets.connect(uri) as websocket:
        try:
            while True:
                message = input("Enter a message to send to the server: ")
                await websocket.send(message)
                print(f"Sent message: {message}")

                response = await websocket.recv()
                print(f"Received response: {response}")
        except websockets.exceptions.ConnectionClosedError as e:
            print(f"Connection closed error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    asyncio.run(send_message())
