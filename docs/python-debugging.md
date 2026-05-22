# Python调试技巧

## pdb调试
```python
import pdb; pdb.set_trace()
```

## 常用pdb命令
- n: 下一行
- s: 进入函数
- c: 继续执行
- p var: 打印变量
- l: 查看代码

## logging配置
```python
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')
```

## 性能分析
```python
import cProfile
cProfile.run('function()')
```

## 内存分析
```python
import tracemalloc
tracemalloc.start()
```
