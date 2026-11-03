#!/usr/bin/env python3
"""Fail if README.md and README.zh.md list different repos (bilingual drift guard)."""
import re
import sys


def urls(path):
    found = {}
    with open(path, encoding='utf-8') as fh:
        for line in fh:
            m = re.match(r'^- \[([^\]]+)\]\((https://github\.com/[^)]+)\)', line)
            if m:
                found[m.group(2).rstrip('/').lower()] = m.group(1)
    return found


en = urls('README.md')
zh = urls('README.zh.md')
only_en = sorted(set(en) - set(zh))
only_zh = sorted(set(zh) - set(en))

print(f'en {len(en)} entries / zh {len(zh)} entries')
for url in only_en:
    print(f'missing in README.zh.md: {en[url]} {url}')
for url in only_zh:
    print(f'missing in README.md: {zh[url]} {url}')

if only_en or only_zh:
    sys.exit(1)
print('in sync')
