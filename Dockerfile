# syntax=docker/dockerfile:1

# -------- Base: dependencias runtime --------
FROM python:3.12-slim AS base
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# -------- Test: ejecuta pytest (opcional pero recomendado para máxima nota) --------
FROM base AS test
COPY requirements-dev.txt .
RUN pip install --no-cache-dir -r requirements-dev.txt

COPY app.py ./app.py
COPY tests ./tests
RUN pytest -q

# -------- Final: imagen mínima para ejecutar la app --------
FROM base AS final
COPY app.py ./app.py

EXPOSE 5000

# Ejecuta Flask vía Gunicorn (WSGI) en el puerto 5000
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
