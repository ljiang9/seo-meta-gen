# seo-meta-gen

零依赖的 **SEO 标题 / 描述生成器**：给定一个关键词，按内容规则自动生成包含关键词、长度合规的 `<title>` 与 `meta description`，并附带长度校验。无需任何 API。

## 功能简介

- title 控制在 15~60 字符，关键词靠前。
- description 控制在 60~160 字符，自然重复关键词并带行动号召。
- 超长时在标点处智能截断并补省略号。
- 多套模板，`--all` 可列出全部组合挑选。

## 快速开始

```bash
python3 cli.py --keyword "空气炸锅选购"

# 列出全部模板组合
python3 cli.py --keyword "空气炸锅选购" --all
```

输出形如：

```
title (24 字, ok=True):
空气炸锅选购完整指南：从入门到精通

description (78 字, ok=True):
想搞懂空气炸锅选购？本文用通俗的语言讲清空气炸锅选购的核心概念、实操步骤和避坑要点……
```

## 无 API key 如何运行

本项目**完全不需要 API key**，纯本地模板生成 + 长度校验。

## 目录说明

```
seo-meta-gen/
├── seo_meta.py     # 模板 + 截断 + 长度校验
├── cli.py         # 命令行入口
├── tests/
│   └── test_seo.py
├── README.md
├── LICENSE
└── .gitignore
```

## 运行测试

```bash
python3 -m unittest discover -s tests
```

## License

MIT License，Copyright (c) 2026 ljiang9。
