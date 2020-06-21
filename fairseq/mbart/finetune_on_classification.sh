#!/bin/bash

TOTAL_NUM_UPDATES=11261  # 10 epochs through RTE for bsz 16
WARMUP_UPDATES=676       # 6 percent of the number of updates
LR=1e-5                  # Peak LR for polynomial LR scheduler.
NUM_CLASSES=8
MAX_SENTENCES=1         # Batch size.
MBART_PATH=mbart.cc25

fairseq-train jfckb-bin/ \
    --restore-file $MBART_PATH \
    --max-sentences $MAX_SENTENCES \
    --max-tokens 256 \
    --task sentence_prediction \
    --add-prev-output-tokens \
    --layernorm-embedding \
    --share-all-embeddings \
    --share-decoder-input-output-embed \
    --reset-optimizer --reset-dataloader --reset-meters \
    --required-batch-size-multiple 1 \
    --init-token 0 \
    --arch mbart_large \
    --criterion sentence_prediction \
    --num-classes $NUM_CLASSES \
    --dropout 0.1 --attention-dropout 0.1 \
    --weight-decay 0.01 --optimizer adam --adam-betas '(0.9, 0.98)' --adam-eps 1e-08 \
    --clip-norm 0.0 \
    --lr-scheduler polynomial_decay --lr $LR --total-num-update $TOTAL_NUM_UPDATES --warmup-updates $WARMUP_UPDATES \
    --fp16 --fp16-init-scale 4 --threshold-loss-scale 1 --fp16-scale-window 128 \
    --max-epoch 10 \
    --find-unused-parameters \
    --best-checkpoint-metric accuracy --maximize-best-checkpoint-metric \
    --update-freq 16 \
    --save-dir jfckb_checkpoints
