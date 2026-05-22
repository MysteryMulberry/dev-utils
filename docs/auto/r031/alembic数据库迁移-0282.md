# Alembic数据库迁移

## 初始化
```bash
alembic init migrations
```

## 创建迁移
```bash
alembic revision --autogenerate -m "add users table"
```

## 迁移文件
```python
def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('email', sa.String(100), unique=True),
    )

def downgrade():
    op.drop_table('users')
```

## 执行迁移
```bash
alembic upgrade head
alembic downgrade -1
alembic current
alembic history
```

---
*编号: R031-#0282 | 更新时间: 2026-05-22T07:39:54Z | 仓库: dev-utils*
