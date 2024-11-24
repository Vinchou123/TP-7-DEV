import asyncio
import websockets

async def handle_client(websocket):
    print(f"Connexion établie avec : {websocket.remote_address}")
    try:
        while True:
            message = await websocket.recv()
            print(f"Message reçu : {message}")

            response = f"Hello client! Received \"{message}\""
            await websocket.send(response)
    except websockets.ConnectionClosedOK:
        print(f"Connexion fermée par le client : {websocket.remote_address}")
    except Exception as e:
        print(f"Erreur dans handle_client : {e}")

async def main():
    server = await websockets.serve(
        lambda ws, _: handle_client(ws),
        "10.2.2.2",                     
        8888                            
    )
    print("Serveur WebSocket démarré sur ws://10.2.2.2:8888")
    await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())