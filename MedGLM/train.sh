CUDA_VISIBLE_DEVICES=6 python src/train_sft.py \
    --do_train \
    --dataset xiaohongshu \
    --finetuning_type lora \
    --output_dir /home/songbo/songbo/NLP_dev/project/xiaohongshu/ChatGLM-Efficient-Tuning/saved_model/ft_v1  \
    --per_device_train_batch_size 4 \
    --gradient_accumulation_steps 4 \
    --lr_scheduler_type cosine \
    --logging_steps 10 \
    --save_steps 1000 \
    --learning_rate 5e-5 \
    --num_train_epochs 5.0 \
    --fp16


