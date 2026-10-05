"""seo-meta-gen 命令行入口。

用法示例：
    python3 cli.py --keyword "空气炸锅选购"
    python3 cli.py --keyword "空气炸锅选购" --all
"""

from __future__ import annotations

import argparse
import sys

from seo_meta import (DESC_TEMPLATES, TITLE_TEMPLATES, generate,
                      gen_description, gen_title, validate)


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="seo-meta-gen",
        description="按关键词生成长度合规的 SEO title / description",
    )
    p.add_argument("--keyword", required=True, help="目标关键词")
    p.add_argument("--all", action="store_true", help="列出全部模板组合")
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)

    if args.all:
        for i, tt in enumerate(TITLE_TEMPLATES):
            t = gen_title(args.keyword, i)
            for j, dt in enumerate(DESC_TEMPLATES):
                d = gen_description(args.keyword, j)
                v = validate(t, d)
                print(f"[组合 {i+1}-{j+1}]")
                print(f"  title({v['title_len']}): {t}")
                print(f"  desc({v['description_len']}): {d}")
        return 0

    res = generate(args.keyword)
    v = res["validation"]
    print(f"title ({v['title_len']} 字, ok={v['title_ok']}):")
    print(res["title"])
    print(f"\ndescription ({v['description_len']} 字, ok={v['description_ok']}):")
    print(res["description"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
