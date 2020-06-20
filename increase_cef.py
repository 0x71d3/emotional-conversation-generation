import sys
from itertools import permutations

from pyknp import KNP

src_path = sys.argv[1]
dst_path = sys.argv[2]

knp = KNP(option='-tab -dpnd')

data = []
with open(src_path, encoding='utf-8') as f:
    for line in f:
        sentence, label = line.split()

        result = knp.parse(sentence)
        bnst_midasis = [bnst.midasi for bnst in result.bnst_list()]

        for cases in permutations(bnst_midasis[:-1]):
            p_sentence = ''.join([*cases, bnst_midasis[-1]])
            data.append((p_sentence, label))

with open(dst_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join('\t'.join(line) for line in data) + '\n')
