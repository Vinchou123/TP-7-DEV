import asyncio
import websockets

# Gestionnaire des connexions clients
async def handle_client(websocket, path):  # 'path' est requis, même s'il n'est pas utilisé
    print(f"Connexion établie avec : {websocket.remote_address}")
    try:
        while True:
            # Réception du message du client
            message = await websocket.recv()
            print(f"Message reçu : {message}")

            # Réponse au client
            response = f"Hello client! Received \"{message}\""
            await websocket.send(response)
    except websockets.ConnectionClosedOK:
        print(f"Connexion fermée par le client : {websocket.remote_address}")
    except Exception as e:
        print(f"Erreur dans handle_client : {e}")

# Fonction principale
async def main():
    # Création du serveur WebSocket
    server = await websockets.serve(
        handle_client,       # Fonction de gestion des connexions
        "10.2.2.2",          # Adresse IP du serveur
        8888                 # Port
    )
    print("Serveur WebSocket démarré sur ws://10.2.2.2:8888")
    await asyncio.Future()  # Garde le serveur actif

if __name__ == "__main__":
    asyncio.run(main())
