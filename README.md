# bot-telegram

## Description

Ce projet est un bot Telegram écrit en Python. Il peut envoyer des messages à un chat spécifique et de lancer/arrêter une action à distance.

## Prérequis

- Python 3.12
- Docker (optionnel)
- Un compte Telegram et un bot créé

## Installation

Clonez le dépôt :
    
```bash
git clone https://github.com/llarboullet/bot-telegram.git
```

## Configuration

### Configuration du bot Telegram

#### Création du bot

1. Ouvrez Telegram et recherchez le bot `@BotFather`.
2. Cliquez sur `Start` pour commencer à discuter avec le bot `@BotFather`.
3. Tapez `/newbot` pour créer un nouveau bot.
4. Suivez les instructions pour donner un nom à votre bot et un nom d'utilisateur.
5. Une fois le bot créé, vous recevrez un token d'authentification ou envoyé /token au bot `@BotFather` pour obtenir le token.

#### Ajout du bot à un groupe

1. Coller le lien suivant dans votre navigateur en remplaçant `<votre_token_bot_telegram>` par le token de votre bot : `https://api.telegram.org/bot<votre_token_bot_telegram>/getUpdates?offset=0`
2. Envoyez un message dans le groupe où vous souhaitez ajouter le bot.
3. Rafraîchissez la page du navigateur pour voir les informations sur le message envoyé.
4. Recherchez le champ `chat` et copiez la valeur de `id` qui est votre `chat_id`.


### Variables d'environnement

Créez un fichier `.env` à la racine du projet et ajoutez les variables suivantes :

```bash
cd bot-telegram
nano .env
```

```env 
TELEGRAM_BOT_TOKEN=<votre_token_bot_telegram>
TELEGRAM_CHAT_ID=<votre_chat_id>
```

## Exécution

### Sans Docker

1. Accédez au dossier du projet :

```bash
cd bot-telegram
```

2. Installez les dépendances :
    
```bash
pip install -r requirements.txt
```

3. Exécutez le script principal :

```bash
python main.py
```

### Avec Docker

Si vous préférez utiliser Docker, vous pouvez construire et exécuter le conteneur avec les commandes suivantes :

```bash
docker build -t bot-telegram .
docker run -d --restart=always --name bot-telegram bot-telegram
```
