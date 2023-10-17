CUDA_VISIBLE_DEVICES=7 python src/train_sft.py \
    --do_train \
    --dataset xiaohongshu_1 \
    --finetuning_type p_tuning \
    --output_dir /home/songbo/songbo/NLP_dev/project/xiaohongshu/ChatGLM-Efficient-Tuning/saved_model/pt2/ \
    --per_device_train_batch_size 4 \
    --gradient_accumulation_steps 4 \
    --lr_scheduler_type cosine \
    --logging_steps 10 \
    --save_steps 1000 \
    --learning_rate 5e-5 \
    --num_train_epochs 5.0 \
    --fp16


