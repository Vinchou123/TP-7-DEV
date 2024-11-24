import asyncio
import websockets

async def send_message():
    uri = "ws://10.2.2.2:8888"
    async with websockets.connect(uri) as websocket:
        try:
            while True:
                message = input("Entrez un message à envoyer au serveur: ")
                await websocket.send(message)
                print(f"Message envoyé: {message}")

                response = await websocket.recv()
                print(f"Réponse reçue: {response}")
        except websockets.exceptions.ConnectionClosedError as e:
            print(f"Erreur de fermeture de connexion: {e}")
        except Exception as e:
            print(f"Une erreur est survenue: {e}")

if __name__ == "__main__":
    asyncio.run(send_message())
