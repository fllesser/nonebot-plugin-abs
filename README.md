<div align="center">
    <a href="https://v2.nonebot.dev/store">
    <img src="https://raw.githubusercontent.com/fllesser/nonebot-plugin-template/refs/heads/resource/.docs/NoneBotPlugin.svg" width="310" alt="logo"></a>

## ✨ nonebot-plugin-abs ✨

<a href="./LICENSE">
    <img src="https://img.shields.io/github/license/fllesser/nonebot-plugin-abs.svg" alt="license">
</a>
<a href="https://pypi.python.org/pypi/nonebot-plugin-abs">
    <img src="https://img.shields.io/pypi/v/nonebot-plugin-abs.svg" alt="pypi">
</a>
<img src="https://img.shields.io/badge/python-3.10+-blue.svg" alt="python">
<a href="https://github.com/astral-sh/ruff">
    <img src="https://img.shields.io/badge/code%20style-ruff-black?style=flat-square&logo=ruff" alt="ruff">
</a>
<a href="https://github.com/astral-sh/uv">
    <img src="https://img.shields.io/badge/package%20manager-uv-black?style=flat-square&logo=uv" alt="uv">
</a>
<a href="https://results.pre-commit.ci/latest/github/fllesser/nonebot-plugin-abs/master">
    <img src="https://results.pre-commit.ci/badge/github/fllesser/nonebot-plugin-abs/master.svg" alt="pre-commit" />
</a>
</div>

## 📖 介绍

抽象化消息，将消息中的中文、数字、英文、拼音等转换为对应的emoji

## 💿 安装

<details open>
<summary>使用 nb-cli 安装</summary>
在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

    nb plugin install nonebot-plugin-abs --upgrade
使用 **pypi** 源安装

    nb plugin install nonebot-plugin-abs --upgrade -i "https://pypi.org/simple"
使用**清华源**安装

    nb plugin install nonebot-plugin-abs --upgrade -i "https://pypi.tuna.tsinghua.edu.cn/simple"


</details>

<details>
<summary>使用包管理器安装</summary>
在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令

<details open>
<summary>uv</summary>

    uv add nonebot-plugin-abs
安装仓库 master 分支

    uv add git+https://github.com/fllesser/nonebot-plugin-abs@master
</details>

<details>
<summary>pdm</summary>

    pdm add nonebot-plugin-abs
安装仓库 master 分支

    pdm add git+https://github.com/fllesser/nonebot-plugin-abs@master
</details>
<details>
<summary>poetry</summary>

    poetry add nonebot-plugin-abs
安装仓库 master 分支

    poetry add git+https://github.com/fllesser/nonebot-plugin-abs@master
</details>

打开 nonebot2 项目根目录下的 `pyproject.toml` 文件, 在 `[tool.nonebot]` 部分追加写入

    plugins = ["nonebot_plugin_abs"]

</details>

<details>
<summary>使用 nbr 安装(使用 uv 管理依赖可用)</summary>

[nbr](https://github.com/fllesser/nbr) 是一个基于 uv 的 nb-cli，可以方便地管理 nonebot2

    nbr plugin install nonebot-plugin-abs --upgrade
使用 **pypi** 源安装

    nbr plugin install nonebot-plugin-abs --upgrade -i "https://pypi.org/simple"
使用**清华源**安装

    nbr plugin install nonebot-plugin-abs --upgrade -i "https://pypi.tuna.tsinghua.edu.cn/simple"

</details>

## 🎉 使用
### 指令表
|   指令   | 权限  | 需要@ | 范围  |           说明           |
| :------: | :---: | :---: | :---: | :----------------------: |
| abs/抽象 |   -   |  否   |   -   | 抽象化消息, 只是回复消息 |

### 🎨 效果图
懒得截捏
