# Pydantic数据验证

## 基本模型
```python
from pydantic import BaseModel, field_validator
from datetime import datetime

class User(BaseModel):
    name: str
    email: str
    age: int
    created_at: datetime = datetime.now()

    @field_validator('email')
    @classmethod
    def validate_email(cls, v):
        if '@' not in v:
            raise ValueError('Invalid email')
        return v
```

## 嵌套模型
```python
class Address(BaseModel):
    city: str
    country: str = "CN"

class UserProfile(BaseModel):
    user: User
    address: Address
    tags: list[str] = []
```

## 配置
```python
class Config:
    str_strip_whitespace = True
    str_min_length = 1
    json_schema_extra = {"example": {"name": "test"}}
```

---
*编号: R013-#0114 | 更新时间: 2026-05-22T07:18:40Z | 仓库: dev-utils*
