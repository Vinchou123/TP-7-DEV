import asyncio
import redis.asyncio as redis
from websockets import serve
from websockets.server import WebSocketServerProtocol

redis_client = redis.Redis(host="10.2.2.2", port=6379, db=0)

async def broadcast_message(sender, message, include_sender=False):
    clients = await redis_client.keys("client:*")
    for client in clients:
        pseudo = await redis_client.hget(client, "pseudo")
        if not include_sender and client == sender:
            continue
        try:
            await client.send(message)
        except Exception as e:
            print(f"Erreur d'envoi vers {pseudo.decode()}: {e}")

async def handle_client(websocket: WebSocketServerProtocol):
    addr = websocket.remote_address
    print(f"Nouvelle connexion de {addr}")

    try:
        data = await websocket.recv()
        if not data.startswith("Hello|"):
            print(f"Connexion refusée par {addr} (format invalide).")
            return

        pseudo = data.split("|", 1)[1].strip() or "Anonyme"

        client_id = f"client:{addr[0]}:{addr[1]}"
        await redis_client.hset(client_id, mapping={"pseudo": pseudo})
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
        pseudo = await redis_client.hget(f"client:{addr[0]}:{addr[1]}", "pseudo")
        await redis_client.delete(f"client:{addr[0]}:{addr[1]}")
        print(f"Déconnexion de {addr} ({pseudo.decode() if pseudo else 'Inconnu'})")

        leave_announcement = f"Annonce : {pseudo.decode() if pseudo else 'Inconnu'} a quitté la chatroom."
        await broadcast_message(sender=None, message=leave_announcement)

        await websocket.close()

async def main():
    server = await serve(handle_client, '10.2.2.2', 8888)
    print(f"Serveur WebSocket lancé sur ws://10.2.2.2:8888")

    async with server:
        await asyncio.Future()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nServeur arrêté manuellement.")
