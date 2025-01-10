FROM python:3.9-slim

WORKDIR /app
COPY send_metrics.py .

RUN pip install opentelemetry-api opentelemetry-sdk opentelemetry-exporter-otlp

CMD ["python", "send_metrics.py"]