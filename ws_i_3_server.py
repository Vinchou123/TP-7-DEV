import asyncio
from websockets import WebSocketServerProtocol, serve

CLIENTS = {}

async def broadcast_message(sender, message, include_sender=False):
    for client, info in CLIENTS.items():
        if not include_sender and client == sender:
            continue
        try:
            await client.send(message)
        except Exception as e:
            print(f"Erreur d'envoi vers {info['pseudo']}: {e}")

async def handle_client(websocket: WebSocketServerProtocol, path):
    addr = websocket.remote_address
    print(f"Nouvelle connexion de {addr}")

    try:
        data = await websocket.recv()
        if not data.startswith("Hello|"):
            print(f"Connexion refusée par {addr} (format invalide).")
            return

        pseudo = data.split("|", 1)[1].strip() or "Anonyme"
        CLIENTS[websocket] = {"pseudo": pseudo}
        print(f"{addr} connecté avec le pseudo '{pseudo}'.")

        join_announcement = f"Annonce : {pseudo} a rejoint la chatroom."
        await broadcast_message(sender=None, message=join_announcement)

        async for message in websocket:
            print(f"Message de {pseudo} ({addr}): {message}")
            redistrib_message = f"{pseudo} a dit : {message}"
            await broadcast_message(sender=websocket, message=redistrib_message)

    except Exception as e:
        print(f"Erreur avec {addr}: {e}")
    finally:
        pseudo = CLIENTS.get(websocket, {}).get("pseudo", "Inconnu")
        CLIENTS.pop(websocket, None)
        print(f"Déconnexion de {addr} ({pseudo})")

        leave_announcement = f"Annonce : {pseudo} a quitté la chatroom."
        await broadcast_message(sender=None, message=leave_announcement)

        await websocket.close()

async def main():
    server_host = "10.2.2.2"
    server_port = 8888

    server = await serve(handle_client, server_host, server_port)
    print(f"Serveur WebSocket lancé sur {server_host}:{server_port}")

    async with server:
        await asyncio.Future()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nServeur arrêté manuellement.")
