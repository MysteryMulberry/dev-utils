# OpenTelemetry可观测性

## 追踪
```python
from opentelemetry import trace

tracer = trace.get_tracer(__name__)

with tracer.start_as_current_span("process_request") as span:
    span.set_attribute("http.method", "GET")
    result = handle_request()
    span.set_attribute("result.count", len(result))
```

## 指标
```python
from opentelemetry import metrics

meter = metrics.get_meter(__name__)
counter = meter.create_counter("requests.total")

def handle_request():
    counter.add(1, {"endpoint": "/api/data"})
```

## 日志
```python
from opentelemetry import log as otel_log

logger = otel_log.get_logger(__name__)
logger.info("Processing request", extra={"user_id": user_id})
```

---
*编号: R044-#0398 | 更新时间: 2026-05-22T07:51:04Z | 仓库: dev-utils*
