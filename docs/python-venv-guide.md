# Python虚拟环境指南

## 创建虚拟环境

python -m venv myenv

## 激活虚拟环境

### Windows
myenv\Scripts\activate

### Linux/macOS
source myenv/bin/activate

## 包管理

### 安装依赖
pip install -r requirements.txt

### 导出依赖
pip freeze > requirements.txt

### 升级pip
pip install --upgrade pip

## 常见问题

1. 虚拟环境激活后命令找不到
   - 确认activate脚本正确执行

2. pip安装超时
   - 使用镜像源: pip install -i https://pypi.tuna.tsinghua.edu.cn/simple package

3. 多版本Python共存
   - 使用pyenv或指定完整路径创建虚拟环境
