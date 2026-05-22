# 数据库实用技巧

## PostgreSQL
- 连接: `psql -h host -U user -d dbname`
- 备份: `pg_dump dbname > backup.sql`
- 还原: `psql dbname < backup.sql`
- 慢查询: `EXPLAIN ANALYZE SELECT ...`

## Redis
- 连接: `redis-cli -h host -p 6379`
- 查看内存: `INFO memory`
- 查看键: `SCAN 0 MATCH prefix:* COUNT 100`
- 大键分析: `redis-cli --bigkeys`

## MongoDB
- 连接: `mongosh 'mongodb://host:27017'`
- 备份: `mongodump --db dbname`
- 慢查询: `db.collection.explain('executionStats').find(...)`
