#!/bin/bash

SPM=spm_encode
MODEL=mbart.cc25/sentence.bpe.model

DATA=jfckb
LANG=input0

for SPLIT in train dev test
do
    $SPM --model=$MODEL < $DATA/$SPLIT.$LANG > $DATA/$SPLIT.spm.$LANG &
done
