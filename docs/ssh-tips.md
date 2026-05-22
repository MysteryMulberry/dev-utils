# SSH实用技巧

## 配置
```bash
Host myserver
    HostName 1.2.3.4
    User root
    Port 22
    IdentityFile ~/.ssh/id_rsa
```

## 免密登录
```bash
ssh-keygen -t ed25519
ssh-copy-id user@host
```

## 端口转发
- 本地: `ssh -L 8080:localhost:80 host`
- 远程: `ssh -R 8080:localhost:80 host`
- 动态: `ssh -D 1080 host`

## 文件传输
- 上传: `scp file host:/path`
- 下载: `scp host:/path/file .`
- 同步: `rsync -avz src/ host:/dst/`
