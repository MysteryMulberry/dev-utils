<div align="center">

# 🧰 Dev Utils

**开发者瑞士军刀 | 80+ 实用脚本 · 配置模板 · 速查文档**

[![Stars](https://img.shields.io/github/stars/MysteryMulberry/dev-utils?style=social)](https://github.com/MysteryMulberry/dev-utils/stargazers)
[![Forks](https://img.shields.io/github/forks/MysteryMulberry/dev-utils?style=social)](https://github.com/MysteryMulberry/dev-utils/network/members)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Shell](https://img.shields.io/badge/Shell-Bash-green.svg)](https://www.gnu.org/software/bash/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

*告别重复劳动 —— 命令行一键搞定日常开发任务*

[⚡ 脚本一览](#-脚本一览) · [📁 配置模板](#-配置模板) · [📖 速查文档](#-速查文档) · [🚀 安装](#-安装使用)

</div>

---

## ✨ 项目亮点

- 🎯 **即拿即用** — 每个脚本独立运行，零依赖安装（核心脚本）
- 📦 **80+工具** — 覆盖文件处理、API测试、数据分析、系统运维
- 📋 **配置模板** — .gitignore、Docker Compose、Makefile等开箱即用
- 📚 **速查文档** — Git/Linux/Docker/SSH/Python命令速查卡
- 🐍 **Python优先** — 充分利用Python生态，类型提示+PEP 8规范

## ⚡ 脚本一览

### 📁 文件与数据处理

| 脚本 | 功能 | 用法 |
|------|------|------|
| `json-formatter.py` | JSON格式化/美化 | `python json-formatter.py file.json` |
| `json-to-csv.py` | JSON转CSV | `python json-to-csv.py data.json out.csv` |
| `csv-to-json.py` | CSV转JSON | `python csv-to-json.py data.csv out.json` |
| `csv-merge.py` | 多CSV按列合并 | `python csv-merge.py a.csv b.csv key out.csv` |
| `markdown-toc.py` | 生成Markdown目录 | `python markdown-toc.py README.md` |
| `batch-rename.py` | 正则批量重命名 | `python batch-rename.py dir pattern replace` |
| `duplicate-finder.py` | 重复文件查找(MD5) | `python duplicate-finder.py /path` |
| `directory-tree.py` | 目录树可视化 | `python directory-tree.py /path` |
| `text-stats.py` | 文本统计(词频/行数) | `python text-stats.py file.txt` |
| `pdf-merger.py` | PDF文件合并 | `python pdf-merger.py a.pdf b.pdf -o out.pdf` |

### 🌐 网络与API

| 脚本 | 功能 | 用法 |
|------|------|------|
| `api-tester.py` | HTTP端点测试 | `python api-tester.py https://api.example.com` |
| `port-scanner.py` | 端口扫描 | `python port-scanner.py 127.0.0.1` |
| `regex-tester.py` | 正则表达式测试 | `python regex-tester.py "p\d+" "p123"` |
| `password-gen.py` | 安全密码生成 | `python password-gen.py 20` |
| `timestamp-tool.py` | 时间戳转换 | `python timestamp-tool.py 1700000000` |

### 🔧 开发辅助

| 脚本 | 功能 | 用法 |
|------|------|------|
| `git-batch-clone.sh` | 批量Git克隆 | `./git-batch-clone.sh repos.txt ./dir` |
| `git-stats.py` | Git提交统计 | `python git-stats.py /repo` |
| `backup-tool.py` | 目录打包备份 | `python backup-tool.py /src /backups` |
| `env-check.py` | 开发环境检查 | `python env-check.py` |
| `log-analyzer.py` | 日志分析统计 | `python log-analyzer.py app.log` |

### 🖥️ 系统运维

| 脚本 | 功能 | 用法 |
|------|------|------|
| `sys-monitor.py` | 系统资源监控 | `python sys-monitor.py` |
| `image-compressor.py` | 图片压缩 | `python image-compressor.py photo.jpg` |

## 📁 配置模板

开箱即用的项目配置，复制即用：

### .gitignore 模板
| 模板 | 适用项目 |
|------|---------|
| `configs/gitignore-templates/python.gitignore` | Python项目 |
| `configs/gitignore-templates/node.gitignore` | Node.js项目 |

### Docker Compose 模板
| 模板 | 技术栈 |
|------|--------|
| `configs/docker-compose-templates/python.yml` | Python + Redis |
| `configs/docker-compose-templates/node.yml` | Node.js + PostgreSQL |

### 代码规范模板
| 模板 | 说明 |
|------|------|
| `configs/editorconfig-template` | EditorConfig统一缩进/编码 |
| `configs/prettierrc-template.json` | Prettier代码格式化 |
| `configs/eslintrc-template.json` | ESLint代码检查 |

### Makefile 模板
| 模板 | 语言 |
|------|------|
| `configs/Makefile-templates/python.mk` | Python项目 |
| `configs/Makefile-templates/go.mk` | Go项目 |

## 📖 速查文档

### 命令速查
| 文档 | 内容 |
|------|------|
| [Git实用技巧](docs/git-tips.md) | 分支/撤销/变基/Stash |
| [Linux常用命令](docs/linux-commands.md) | 文件/进程/网络/监控 |
| [Docker命令速查](docs/docker-commands.md) | 容器/镜像/Compose/清理 |
| [SSH实用技巧](docs/ssh-tips.md) | 配置/免密/端口转发/ rsync |
| [Shell脚本片段](docs/shell-snippets.md) | 批量重命名/文本处理/下载 |

### 开发指南
| 文档 | 内容 |
|------|------|
| [VS Code扩展推荐](docs/vscode-extensions.md) | 通用/Python/前端/AI扩展 |
| [Python调试技巧](docs/python-debugging.md) | pdb/logging/cProfile/内存分析 |
| [Python虚拟环境](docs/python-venv-guide.md) | venv创建/激活/镜像源配置 |
| [Python打包发布](docs/python-packaging.md) | pyproject.toml/hatch/poetry |
| [npm实用技巧](docs/npm-tricks.md) | 换源/审计/脚本/锁定依赖 |
| [Git工作流对比](docs/git-workflows.md) | GitFlow/GitHubFlow/Trunk-Based |
| [数据库技巧](docs/database-tips.md) | PostgreSQL/Redis/MongoDB |
| [CI/CD快速指南](docs/ci-cd-guide.md) | GitHub Actions/缓存优化 |

## 🚀 安装使用

```bash
# 克隆仓库
git clone https://github.com/MysteryMulberry/dev-utils.git
cd dev-utils

# 直接运行任意脚本
python scripts/json-formatter.py yourfile.json
python scripts/directory-tree.py /your/project

# 或使用Shell脚本
bash scripts/git-batch-clone.sh repos.txt ./projects
```

### 依赖安装（部分脚本需要）

```bash
pip install psutil        # sys-monitor.py
pip install Pillow        # image-compressor.py
pip install PyPDF2        # pdf-merger.py
pip install requests      # api-tester.py
```

## 📊 项目统计

| 类别 | 数量 |
|------|------|
| Python脚本 | 83 |
| Shell工具 | 30 |
| 配置模板 | 9 |
| 速查文档 | 130 |
| **总计** | **261** |

## 🗂️ 项目结构

```
dev-utils/
├── scripts/                 # Python & Shell 脚本
│   ├── json-formatter.py
│   ├── api-tester.py
│   ├── git-stats.py
│   └── ...
├── configs/                 # 配置模板
│   ├── gitignore-templates/
│   ├── docker-compose-templates/
│   ├── Makefile-templates/
│   └── ...
├── tools/                   # Shell工具集
├── docs/                    # 速查文档与指南
└── README.md
```

## 🤝 贡献

欢迎提交新工具或改进现有脚本！

1. Fork → Feature Branch → Commit → PR
2. 脚本需包含：shebang、docstring、`if __name__ == '__main__'` 入口
3. 遵循PEP 8，添加类型提示

## 📄 许可证

[MIT License](LICENSE)

---

<div align="center">

**觉得好用？给个 ⭐ Star 让更多人看到！**

Made with ❤️ by [@MysteryMulberry](https://github.com/MysteryMulberry)

</div>
