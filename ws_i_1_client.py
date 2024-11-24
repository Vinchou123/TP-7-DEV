import asyncio
import websockets

async def send_message():
    try:
        async with websockets.connect("ws://10.2.2.2:8888") as websocket:
            print("Connexion établie avec le serveur.")
            while True:
                message = input("Entrez un message à envoyer au serveur (ou 'quit' pour terminer) : ")
                
                if message.lower() == 'quit':
                    print("Fermeture du client.")
                    break
                
                await websocket.send(message)
                print(f"Message envoyé : {message}")

                response = await websocket.recv()
                print(f"Réponse du serveur : {response}")
    except Exception as e:
        print(f"Erreur : {e}")

if __name__ == "__main__":
    asyncio.run(send_message())
