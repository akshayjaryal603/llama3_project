from transformers import pipeline

# Initialize model (replace with the specific model you're using)
summarizer = pipeline('summarization', model='Llama3')

def generate_summary(text):
    summary = summarizer(text, max_length=150, min_length=30, do_sample=False)
    return summary[0]['summary_text']
