# SQLAlchemy 2.0新特性

## 声明式模型
```python
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(unique=True)
```

## 2.0风格查询
```python
stmt = select(User).where(User.name == "Alice")
result = session.execute(stmt)
users = result.scalars().all()
```

## 异步支持
```python
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

engine = create_async_engine("postgresql+asyncpg://...")
async with AsyncSession(engine) as session:
    result = await session.execute(select(User))
```

---
*编号: R044-#0394 | 更新时间: 2026-05-22T07:51:04Z | 仓库: dev-utils*
