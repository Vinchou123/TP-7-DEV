import asyncio
import websockets

async def handle_client(websocket, path):
    try:
        message = await websocket.recv()
        print(f"Message reçu du client: {message}")
        
        response = f"Hello client! Received \"{message}\""
        await websocket.send(response)
    except Exception as e:
        print(f"Erreur: {e}")

async def main():
    server = await websockets.serve(handle_client, "localhost", 8888)
    print("Serveur WebSocket démarré sur ws://localhost:8888")
    await server.wait_closed()

asyncio.run(main())
