import asyncio
from websockets import connect
from aioconsole import ainput

async def send_message(ws):
    while True:
        message = await ainput("\rVous : ")
        if message.strip():
            await ws.send(message)

async def receive_message(ws):
    try:
        async for message in ws:
            print(f"\r{message}\n", end="")
            print("\rVous : ", end="", flush=True)
    except asyncio.CancelledError:
        pass

async def main():
    server_uri = "ws://10.2.2.2:8888"
    print(f"Connexion au serveur WebSocket {server_uri}...")

    try:
        async with connect(server_uri) as websocket:
            pseudo = input("Entrez votre pseudo : ").strip()
            if not pseudo:
                print("Il vous faut un pseudo.")
                pseudo = "Anonyme"
            
            await websocket.send(f"Hello|{pseudo}")
            print(f"Vous êtes connecté en tant que '{pseudo}'. Entrez votre message !")

            send_task = asyncio.create_task(send_message(websocket))
            receive_task = asyncio.create_task(receive_message(websocket))

            done, pending = await asyncio.wait(
                [send_task, receive_task],
                return_when=asyncio.FIRST_COMPLETED
            )

            for task in pending:
                task.cancel()

    except ConnectionRefusedError:
        print(f"Impossible de se connecter au serveur {server_uri}")
    except Exception as e:
        print(f"Erreur : {e}")

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nFermeture de la connexion.")
