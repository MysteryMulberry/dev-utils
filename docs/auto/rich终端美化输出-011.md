# Rich终端美化输出

## 基本输出
```python
from rich import print
print("[bold green]Success![/] Operation completed.")
```

## 表格
```python
from rich.table import Table

table = Table(title="Results")
table.add_column("Name", style="cyan")
table.add_column("Score", justify="right", style="green")
table.add_row("Alice", "95")
table.add_row("Bob", "87")
console.print(table)
```

## 进度条
```python
from rich.progress import track

for item in track(items, description="Processing..."):
    process(item)
```

## Live更新
```python
from rich.live import Live

with Live(console=console) as live:
    for i in range(100):
        live.update(generate_display(i))
        time.sleep(0.1)
```

---
*编号: #011 | 更新时间: 2026-05-22T05:52:22Z | 仓库: dev-utils*
