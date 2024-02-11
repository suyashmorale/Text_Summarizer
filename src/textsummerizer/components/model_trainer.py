from transformers import TrainingArguments, Trainer
from transformers import DataCollatorForSeq2Seq
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from textsummerizer.entity import ModelTrainingConfig
from datasets import load_dataset, load_from_disk
import torch

class ModelTrainer:
    def __init__(self, config: ModelTrainingConfig):
        self.config = config
    
    def train(self):
        device = "cuda" if torch.cuda.is_available() else "cpu"
        model_ckpt = "google/pegasus-cnn_dailymail"
        tokenizer = AutoTokenizer.from_pretrained(model_ckpt)
        model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(model_ckpt).to(device)
        seq2seq_data_collator = DataCollatorForSeq2Seq(tokenizer, model=model_pegasus)

        # Load the dataset
        dataset_samsum_pt = load_from_disk(self.config.data_path)

        trainer_args = TrainingArguments(
            output_dir=self.config.root_dir,
            num_train_epochs=self.config.num_train_epochs,
            per_device_train_batch_size=self.config.per_device_train_batch_size,
            per_device_eval_batch_size=self.config.per_device_eval_batch_size,
            warmup_steps=self.config.warmup_steps,
            weight_decay=self.config.weight_decay,
            logging_steps=self.config.logging_steps,
            evaluation_strategy=self.config.evaluation_strategy,
            eval_steps=self.config.eval_steps,
            save_steps=self.config.save_steps,
            gradient_accumulation_steps=self.config.gradient_accumulation_steps,
        )

        trainer = Trainer(model=model_pegasus, args=trainer_args,
                  tokenizer=tokenizer, data_collator=seq2seq_data_collator,
                  train_dataset = dataset_samsum_pt["test"],
                  eval_dataset = dataset_samsum_pt["validation"])
        
        trainer.train()

        # Save the model and tokenizer
        model_pegasus.save_pretrained(os.path.join(self.config.root_dir, "pegasus_samsum_model"))
        tokenizer.save_pretrained(os.path.join(self.config.root_dir, "pegasus_samsum_tokenizer"))