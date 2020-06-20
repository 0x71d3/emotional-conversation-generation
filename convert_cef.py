import os
import sys

features = [
    'joy', 'trust', 'fear', 'surprise',
    'sadness', 'disgust', 'anger', 'anticipation'
]
changes = ['inc', 'dec', 'unc']

cef_dir = sys.argv[1]
dst_path = sys.argv[2]

cef_verb_path = cef_dir + 'bind/cef_verb_2017-10-13_17:56:13.001454.tsv'
cef_adj_path = cef_dir + 'bind/cef_adj_bind_2017-11-09_16:27:04.990752.tsv'

cef_verb_dict = {}
with open(cef_verb_path, encoding='utf-8') as f:
    header = next(f).strip().split('\t')
    
    for line in f:
        row = line.strip().split('\t')
        row_dict = dict(zip(header, row))

        sentence = row_dict['SENTENCE']

        sentence_dict = {}
        for feature in features:
            change_dict = {}
            for change in changes:
                key = '/'.join(['os', feature, change])
                change_dict[change] = float(row_dict[key])
            sentence_dict[feature] = tuple(change_dict.values())
        
        cef_verb_dict[sentence] = sentence_dict

cef_adj_dict = {}
with open(cef_adj_path, encoding='utf-8') as f:
    header = next(f).strip().split('\t')

    for line in f:
        row = line.strip().split('\t')
        row_dict = dict(zip(header, row))

        sent = row_dict['sent']

        sent_dict = {}
        for feature in features:
            change_dict = {}
            for change in changes:
                key = '/'.join(['os', feature, change])
                change_dict[change] = float(row_dict[key])
            sent_dict[feature] = tuple(change_dict.values())
        
        cef_adj_dict[sent] = sent_dict

labeled = {}
for cef_dict in [cef_verb_dict, cef_adj_dict]:
    for sentence, sentence_dict in cef_dict.items():
        exp_vals = {}
        for feature, change_tuple in sentence_dict.items():
            # 1 * inc + (-1) * dec + 0 * unc
            exp_vals[feature] = change_tuple[0] - change_tuple[1]

        max_features = [
            feature for feature, exp_val in exp_vals.items()
            if exp_val == max(exp_vals.values())
        ]

        if len(max_features) > 1:
            continue

        max_feature = max_features[0]
        if exp_vals[max_feature] <= 0:
            print(exp_vals)

        labeled[sentence] = max_feature

with open(dst_path, 'w', encoding='utf-8') as f:
    for sentence, label in labeled.items():
        f.write('{}\t{}\n'.format(sentence, features.index(label)))
