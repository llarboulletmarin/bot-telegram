# Utilise l'image Python 3.12 comme base
FROM python:3.12
# Définit le répertoire de travail dans le conteneur
WORKDIR /app
# Copie le contenu du répertoire actuel dans le conteneur
COPY . /app
# Installe les dépendances
RUN pip install --no-cache-dir -r requirements.txt
# Exécute main.py lorsque le conteneur démarre
CMD ["python", "main.py"]