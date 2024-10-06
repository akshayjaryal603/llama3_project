import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from flask import Flask, request, jsonify

# Load the Llama3 model and tokenizer from Hugging Face
model_name = "princeton-nlp/Llama-3-8B-ProLong-512k-Instruct"  # Replace this with the appropriate model
tokenizer = AutoTokenizer.from_pretrained(model_name, use_auth_token=True)
model = AutoModelForCausalLM.from_pretrained(model_name, use_auth_token=True)

# Check if CUDA is available for faster processing
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

def generate_summary(text, max_length=150):
    """
    Function to generate summary based on input text.
    """
    inputs = tokenizer(text, return_tensors="pt").to(device)
    summary_ids = model.generate(inputs['input_ids'], max_length=max_length, num_beams=5, early_stopping=True)
    return tokenizer.decode(summary_ids[0], skip_special_tokens=True)\

app = Flask(__name__)

@app.route("/generate-summary", methods=["POST"])
def generate_summary_api():
    """
    API endpoint to generate a summary for the given book content.
    The request body should contain JSON with a 'text' field.
    """
    data = request.get_json()
    if 'text' not in data:
        return jsonify({"error": "Please provide text to summarize"}), 400
    
    text = data['text']
    try:
        # Generate summary using the model
        summary = generate_summary(text)
        return jsonify({"summary": summary})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
