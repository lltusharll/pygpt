from flask import Flask, request, jsonify
import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel

app = Flask(__name__)

# Load the GPT-2 model and tokenizer
model = GPT2LMHeadModel.from_pretrained('gpt2')
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')

@app.route('/api', methods=['POST'])
def generate_text():
  # Get the input text from the request body
  input_text = request.json['input']

  # Encode the input text and generate text
  input_ids = torch.tensor(tokenizer.encode(input_text)).unsqueeze(0)
  output = model.generate(input_ids)
  output_text = tokenizer.decode(output[0], skip_special_tokens=True)

  # Return the generated text as a response
  return jsonify({ 'output': output_text })

if __name__ == '__main__':
  app.run()
  
 #nothing
