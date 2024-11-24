# TP7 DEV : Websockets et databases

## I. Websockets

### 1. First steps

🌞 ws_i_1_client.py

```bash
[vince@Client2TP6 TP-7-DEV]$ python3 ws_i_1_client.py
Entrez un message : Salut
>>> Salut
<<< Hello client ! Received "Salut"
```
🌞 ws_i_1_server.py

```bash
[vince@ServeurTP6 TP-7-DEV]$ python3 ws_i_1_server.py
<<< Salut
>>> Hello client ! Received "Salut"
```

### 2. Client JS

🌞 ws_i_2_client.js




### 3. Chatroom magueule

🌞 ws_i_3_server.py

```bash
[vince@ServeurTP6 TP-7-DEV]$ python ws_i_3_server.py
Serveur WebSocket lancé sur ws://10.2.2.2:8888
Nouvelle connexion de ('10.2.2.223', 44706)
('10.2.2.223', 44706) connecté avec le pseudo 'Vince'.
Message de Vince (('10.2.2.223', 44706)): Coucou
Nouvelle connexion de ('10.2.2.222', 43154)
('10.2.2.222', 43154) connecté avec le pseudo 'Léo'.
Message de Léo (('10.2.2.222', 43154)): salut
Message de Vince (('10.2.2.223', 44706)): Coucou
```

🌞 ws_i_3_client.py

```bash
[vince@Client2TP6 TP-7-DEV]$ python ws_i_3_client.py
Connexion au serveur WebSocket ws://10.2.2.2:8888...
Entrez votre pseudo : Vince
Vous êtes connecté en tant que 'Vince'. Entrez votre message !
Annonce : Vince a rejoint la chatroom.
Vous : Coucou
Annonce : Léo a rejoint la chatroom.
Léo a dit : salut
Vous : Coucou
```

```bash
[vince@ClientTP6 TP-7-DEV]$ python ws_i_3_client.py
Connexion au serveur WebSocket ws://10.2.2.2:8888...
Entrez votre pseudo : Léo
Vous êtes connecté en tant que 'Léo'. Entrez votre message !
Annonce : Léo a rejoint la chatroom.
Vous : salut
Vince a dit : Coucou
Vous :
```

## II. Base de données

🌞 ws_ii_2_server.py



