#!/bin/bash

model=btsj_nucc_chechpoints/checkpoint_best.pt
langs=ar_AR,cs_CZ,de_DE,en_XX,es_XX,et_EE,fi_FI,fr_XX,gu_IN,hi_IN,it_IT,ja_XX,kk_KZ,ko_KR,lt_LT,lv_LV,my_MM,ne_NP,nl_XX,ro_RO,ru_RU,si_LK,tr_TR,vi_VN,zh_CN

fairseq-generate btsj_nucc-bin \
    --path $model \
    --task translation_from_pretrained_bart \
    --gen-subset test \
    -t ja_tgt \
    -s ja_src \
    --bpe 'sentencepiece' \
    --sentencepiece-vocab mbart.cc25/sentence.bpe.model \
    --sacrebleu \
    --remove-bpe 'sentencepiece' \
    --max-sentences 32 \
    --langs $langs \
    > ja_ja

# cat en_ro | grep -P "^H" | sort -V | cut -f 3- | sed 's/\[ro_RO\]//g' | $TOKENIZER ro > en_ro.hyp
# cat en_ro | grep -P "^T" | sort -V | cut -f 2- | sed 's/\[ro_RO\]//g' | $TOKENIZER ro > en_ro.ref
# sacrebleu -tok 'none' -s 'none' en_ro.ref < en_ro.hyp
