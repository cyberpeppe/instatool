# syntax=docker/dockerfile:1

# Imposta la versione di Python
ARG PYTHON_VERSION=3.11.9
FROM python:${PYTHON_VERSION}-slim as base

# Evita la scrittura dei file .pyc e disabilita il buffering
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Imposta la cartella di lavoro
WORKDIR /app

# Crea un utente non privilegiato
ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    appuser

# Copia tutto il codice sorgente prima di cambiare utente
COPY . .

# Converti line endings Windows -> Linux e rendi eseguibile lo script
RUN sed -i 's/\r$//' instatool.sh && chmod +x instatool.sh

# Installa le dipendenze Python
RUN --mount=type=cache,target=/root/.cache/pip \
    python -m pip install --upgrade pip && \
    python -m pip install -r requirements.txt



# Espone la porta dell’applicazione
EXPOSE 8000

# Avvia lo script con sh (evita problemi di eseguibilità)
CMD ["sh", "./instatool.sh"]
