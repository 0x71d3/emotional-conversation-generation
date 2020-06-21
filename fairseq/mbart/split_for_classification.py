import random
import sys

src_path = sys.argv[1]
dst_dir = '.'

with open(src_path, encoding='utf-8') as f:
    data = [line.split() for line in f]

random.shuffle(data)

data_len = len(data)

test_size = data_len // 10
dev_size = data_len // 10
train_size = data_len - (dev_size + test_size)

with open('test.input0', 'w', encoding='utf-8') as f1, \
        open('test.label', 'w', encoding='utf-8') as f2:
    for input0, label in data[:test_size]:
        f1.write(input0 + '\n')
        f2.write(label + '\n')

with open('dev.input0', 'w', encoding='utf-8') as f1, \
        open('dev.label', 'w', encoding='utf-8') as f2:
    for input0, label in data[test_size:test_size+dev_size]:
        f1.write(input0 + '\n')
        f2.write(label + '\n')

with open('train.input0', 'w', encoding='utf-8') as f1, \
        open('train.label', 'w', encoding='utf-8') as f2:
    for input0, label in data[test_size+dev_size:]:
        f1.write(input0 + '\n')
        f2.write(label + '\n')
