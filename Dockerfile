FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN addgroup --system appgroup && adduser --system appuser --ingroup appgroup

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY myapp ./myapp

USER appuser

EXPOSE 5000

CMD ["python", "myapp/main.py"]