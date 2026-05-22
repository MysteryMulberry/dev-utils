#!/bin/bash
# Docker资源清理工具
case "$1" in
  "images") docker image prune -a -f ;;
  "containers") docker container prune -f ;;
  "volumes") docker volume prune -f ;;
  "all") docker system prune -a --volumes -f ;;
  "size") docker system df ;;
  *) echo "Usage: docker-clean {images|containers|volumes|all|size}" ;;
esac
