# api/Dockerfile

# 1) Choix d'une image Python officielle
FROM python:3.10-slim

# 2) Création d'un répertoire de travail
WORKDIR /app

# 3) Copie des requirements et installation
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# 4) Copie du code et du modèle
COPY . /app

# 5) Exposition du port
EXPOSE 8000

# 6) Commande de lancement
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]