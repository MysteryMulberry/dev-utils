# Celery任务队列

## 基本配置
```python
from celery import Celery

app = Celery('tasks', broker='redis://localhost:6379/0')

@app.task
def process_data(data_id):
    result = heavy_computation(data_id)
    return result
```

## 定时任务
```python
app.conf.beat_schedule = {
    'cleanup-every-hour': {
        'task': 'tasks.cleanup',
        'schedule': crontab(minute=0),
    },
}
```

## 任务链
```python
from celery import chain

workflow = chain(process.s(data), validate.s(), notify.s())
workflow.apply_async()
```

## 监控
```bash
celery -A tasks flower
```

---
*编号: R049-#0442 | 更新时间: 2026-05-22T07:55:19Z | 仓库: dev-utils*
