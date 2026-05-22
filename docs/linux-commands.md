# Linux常用命令速查

## 文件操作
- 查找: `find / -name '*.log' 2>/dev/null`
- 权限: `chmod 755 file && chown user:group file`
- 磁盘: `du -sh * | sort -h`

## 进程管理
- 查看: `ps aux | grep process`
- 终止: `kill -9 PID`
- 后台: `nohup command &`

## 网络
- 连接: `ss -tulpn`
- 抓包: `tcpdump -i eth0 port 80`
- 下载: `wget -c URL`

## 系统监控
- 资源: `htop`
- IO: `iotop`
- 网络流: `nethogs`
