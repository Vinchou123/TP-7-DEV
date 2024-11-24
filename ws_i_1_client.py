import asyncio
import websockets

async def send_message():
    try:
        async with websockets.connect("ws://10.2.2.2:8888") as websocket:
            message = input("Entrez une message à envoyer au serveur: ")

            await websocket.send(message)
            
            response = await websocket.recv()
            print(f"Réponse du serveur: {response}")
    except Exception as e:
        print(f"Erreur: {e}")

asyncio.run(send_message())
