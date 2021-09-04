#!/bin/bash 
TASK_TYPE = $1
MODEL_NAME_PATH= $2

pip install transformers
pip install -r transformers/examples/legacy/seq2seq/requirements.txt

echo "Requirement are installed"


python transformers/examples/legacy/seq2seq/run_eval.py \
    $MODEL_NAME_PATH \
    Data/$TASK_TYPE/val.source generated_summary.txt \
    --reference_path Data/$TASK_TYPE/val.target \
    --score_path inference_score.txt \
    --bs 1

