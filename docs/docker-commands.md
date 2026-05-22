# Docker常用命令速查

## 容器操作
- 运行: `docker run -d --name myapp -p 8080:80 image`
- 列表: `docker ps -a`
- 停止: `docker stop <container>`
- 删除: `docker rm <container>`
- 日志: `docker logs -f <container>`
- 进入: `docker exec -it <container> /bin/bash`

## 镜像操作
- 构建: `docker build -t myapp .`
- 列表: `docker images`
- 删除: `docker rmi <image>`
- 拉取: `docker pull <image>:<tag>`
- 标签: `docker tag <image> <new-tag>`

## Docker Compose
- 启动: `docker compose up -d`
- 停止: `docker compose down`
- 日志: `docker compose logs -f`
- 重建: `docker compose up -d --build`

## 清理
- 清除悬空镜像: `docker image prune`
- 清除停止容器: `docker container prune`
- 全部清理: `docker system prune -a`
