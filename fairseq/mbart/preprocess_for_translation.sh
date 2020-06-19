#!/bin/bash

SRC=ja_src
TGT=ja_tgt

DATA=btsj_nucc

TRAIN=train
VALID=valid
TEST=test

DEST=.
NAME=btsj_nucc-bin

DICT=mbart.cc25/dict.txt

fairseq-preprocess \
--source-lang ${SRC} \
--target-lang ${TGT} \
--trainpref ${DATA}/${TRAIN}.spm \
--validpref ${DATA}/${VALID}.spm \
--testpref ${DATA}/${TEST}.spm  \
--destdir ${DEST}/${NAME} \
--thresholdtgt 0 \
--thresholdsrc 0 \
--srcdict ${DICT} \
--tgtdict ${DICT} \
--workers 70
