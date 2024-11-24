import asyncio
import websockets

async def handle_client(websocket, path):
    try:
        while True:
            message = await websocket.recv()
            print(f"Message reçu du client: {message}")
            
            response = f"Hello client! Received \"{message}\""
            await websocket.send(response)
    except websockets.ConnectionClosedOK:
        print("Connexion fermée par le client.")
    except Exception as e:
        print(f"Erreur dans le gestionnaire de connexion : {e}")

async def main():
    async with websockets.serve(handle_client, "10.2.2.2", 8888):
        print("Serveur WebSocket démarré sur ws://10.2.2.2:8888")
        await asyncio.Future()

asyncio.run(main())
