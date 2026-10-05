"""seo-meta-gen：按关键词生成长度合规的 SEO title / description。

规则：
- title 建议 20~60 字符（中文按字符计），关键词尽量靠前；
- description 建议 70~160 字符，需自然包含关键词并带行动号召；
- 超长时在词边界处截断并补省略号；返回时附带长度校验结果。
"""

from __future__ import annotations

TITLE_MAX = 60
TITLE_MIN = 15
DESC_MAX = 160
DESC_MIN = 60

TITLE_TEMPLATES = [
    "{keyword}完整指南：从入门到精通",
    "{keyword}怎么选？2026 最新攻略与对比",
    "{keyword}教程：手把手教你快速上手",
    "一文读懂{keyword}：原理、方法与常见问题",
]

DESC_TEMPLATES = [
    "想搞懂{keyword}？本文用通俗的语言讲清{keyword}的核心概念、实操步骤和避坑要点，"
    "并附上常见问题解答，帮你少走弯路。马上阅读，快速掌握{keyword}。",
    "还在为{keyword}发愁？这篇攻略整理了关于{keyword}的实用经验、对比建议和最佳实践，"
    "无论你是新手还是有经验的用户，都能从中找到可落地的方法。",
]


def _truncate(text: str, limit: int) -> str:
    if len(text) <= limit:
        return text
    cut = text[: limit - 1]
    for sep in ("，", "。", "；", "、", " ", "："):
        idx = cut.rfind(sep)
        if idx > limit * 0.6:
            cut = cut[:idx]
            break
    return cut.rstrip("，。；、： ") + "…"


def gen_title(keyword: str, template_index: int = 0) -> str:
    keyword = keyword.strip()
    if not keyword:
        raise ValueError("关键词不能为空")
    tpl = TITLE_TEMPLATES[template_index % len(TITLE_TEMPLATES)]
    title = tpl.format(keyword=keyword)
    return _truncate(title, TITLE_MAX)


def gen_description(keyword: str, template_index: int = 0) -> str:
    keyword = keyword.strip()
    if not keyword:
        raise ValueError("关键词不能为空")
    tpl = DESC_TEMPLATES[template_index % len(DESC_TEMPLATES)]
    desc = tpl.format(keyword=keyword)
    return _truncate(desc, DESC_MAX)


def validate(title: str, description: str) -> dict:
    """返回长度合规校验结果。"""
    return {
        "title_len": len(title),
        "title_ok": TITLE_MIN <= len(title) <= TITLE_MAX,
        "description_len": len(description),
        "description_ok": DESC_MIN <= len(description) <= DESC_MAX,
    }


def generate(keyword: str) -> dict:
    """一次生成 title / description（各取一个模板）及校验结果。"""
    title = gen_title(keyword)
    desc = gen_description(keyword)
    return {
        "keyword": keyword.strip(),
        "title": title,
        "description": desc,
        "validation": validate(title, desc),
    }
