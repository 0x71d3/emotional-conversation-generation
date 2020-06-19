#!/usr/bin/env python3

import random

tsv_paths = ['btsj_pairs.tsv', 'nucc_pairs.tsv']

pairs = []
for tsv_path in tsv_paths:
    with open(tsv_path, encoding='utf-8') as f:
        for line in f:
            pair = line.strip().split('\t')
            pairs.append(pair)

random.shuffle(pairs)

pairs_len = len(pairs)

test_len = pairs_len // 10
valid_len = pairs_len // 10
train_len = pairs_len - (valid_len + test_len)

with open('btsj_nucc/train.ja_src', 'w', encoding='utf-8') as f1, \
        open('btsj_nucc/train.ja_tgt', 'w', encoding='utf-8') as f2:
    for src, tgt in pairs[:train_len]:
        f1.write(src + '\n')
        f2.write(tgt + '\n')

with open('btsj_nucc/valid.ja_src', 'w', encoding='utf-8') as f1, \
        open('btsj_nucc/valid.ja_tgt', 'w', encoding='utf-8') as f2:
    for src, tgt in pairs[train_len:train_len+valid_len]:
        f1.write(src + '\n')
        f2.write(tgt + '\n')

with open('btsj_nucc/test.ja_src', 'w', encoding='utf-8') as f1, \
        open('btsj_nucc/test.ja_tgt', 'w', encoding='utf-8') as f2:
    for src, tgt in pairs[train_len+valid_len:]:
        f1.write(src + '\n')
        f2.write(tgt + '\n')
