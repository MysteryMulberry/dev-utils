# Shell脚本片段集

## 文件操作

### 批量重命名
for f in *.jpg; do mv "$f" "prefix_$f"; done

### 查找大文件
find . -type f -size +100M -exec ls -lh {} \;

### 统计文件行数
find . -name "*.py" | xargs wc -l

## 文本处理

### 替换文本
sed -i 's/old/new/g' file.txt

### 提取列
awk -F',' '{print $1,$3}' data.csv

### 去重排序
sort file.txt | uniq

## 网络操作

### 下载并解压
curl -sL URL | tar xz

### 端口检查
lsof -i :PORT

### HTTP请求
curl -X POST -H "Content-Type: application/json" -d '{"key":"value"}' URL
