#!/bin/bash

DATA=jfckb
DEST=$DATA-bin

DICT=mbart.cc25/dict.txt

fairseq-preprocess \
    --only-source \
    --trainpref $DATA/train.spm.input0 \
    --validpref $DATA/dev.spm.input0 \
    --testpref $DATA/dev.spm.input0 \
    --destdir $DEST/input0 \
    --workers 60 \
    --srcdict $DICT

fairseq-preprocess \
    --only-source \
    --trainpref $DATA/train.label \
    --validpref $DATA/dev.label \
    --testpref $DATA/test.label \
    --destdir $DEST/label \
    --workers 60
