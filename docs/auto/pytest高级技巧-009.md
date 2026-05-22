# Pytest高级技巧

## 参数化测试
```python
@pytest.mark.parametrize("input,expected", [
    (1, 2),
    (2, 4),
    (3, 6),
])
def test_double(input, expected):
    assert double(input) == expected
```

## 异步测试
```python
@pytest.mark.asyncio
async def test_async_function():
    result = await async_operation()
    assert result is not None
```

## 临时目录
```python
def test_with_files(tmp_path):
    data_file = tmp_path / "data.json"
    data_file.write_text('{"key": "value"}')
    result = load_data(data_file)
    assert result["key"] == "value"
```

## 标记与跳过
```python
@pytest.mark.slow
def test_slow_operation():
    pass

@pytest.mark.skipif(sys.platform == "win32", reason="Unix only")
def test_unix_feature():
    pass
```

---
*编号: #009 | 更新时间: 2026-05-22T05:51:23Z | 仓库: dev-utils*
