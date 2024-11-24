import asyncio
import websockets

async def echo(websocket, path):
    try:
        async for message in websocket:
            print(f"Message reçu: {message}")
            response = f"Bonjour client! Message reçu: \"{message}\""
            await websocket.send(response)
            print(f"Réponse envoyée: {response}")
    except websockets.exceptions.ConnectionClosedError as e:
        print(f"Erreur de fermeture de connexion: {e}")
    except Exception as e:
        print(f"Une erreur est survenue: {e}")

async def main():
    async with websockets.serve(echo, "10.2.2.2", 8888) as server:
        print("Serveur démarré et en écoute sur 10.2.2.2:8888")
        await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())
