import torch
from transformers import BartForConditionalGeneration, BartTokenizer

# Use a fine-tuned model for better results
MODEL_NAME = "facebook/bart-large-cnn" 
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

tokenizer = BartTokenizer.from_pretrained(MODEL_NAME)
model = BartForConditionalGeneration.from_pretrained(MODEL_NAME).to(device)
model.eval()

def summarize_text(text, max_len=150, min_len=40):
    if not text.strip():
        return "No content available for summarization."

    # Using larger token limit for the fine-tuned model
    inputs = tokenizer([text], max_length=1024, truncation=True, return_tensors="pt").to(device)
    with torch.no_grad():
        summary_ids = model.generate(
            inputs["input_ids"],
            num_beams=4,
            min_length=min_len,
            max_length=max_len,
            early_stopping=True
        )
    return tokenizer.decode(summary_ids[0], skip_special_tokens=True)

def summarize_csv(processed_csv, text_col="content", limit=10000):
    import pandas as pd
    df = pd.read_csv(processed_csv)
    if text_col not in df.columns:
        return "CSV has no content column."
    full_text = " ".join(df[text_col].astype(str).tolist())[:limit]
    return summarize_text(full_text)