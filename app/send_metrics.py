import os
import time
from opentelemetry import metrics
from opentelemetry.exporter.otlp.proto.grpc.metric_exporter import OTLPMetricExporter
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader

otel_endpoint = os.getenv("OTEL_COLLECTOR_ENDPOINT", "localhost:4317")

exporter = OTLPMetricExporter(endpoint=otel_endpoint, insecure=True)
reader = PeriodicExportingMetricReader(exporter, export_interval_millis=5000)

provider = MeterProvider(metric_readers=[reader])
metrics.set_meter_provider(provider)
meter = metrics.get_meter(__name__)

counter = meter.create_counter(
    name="example_counter",
    description="Пример счетчика",
    unit="1",
)

while True:
    counter.add(1, {"environment": "test"})
    print("Отправлена метрика")
    time.sleep(5)