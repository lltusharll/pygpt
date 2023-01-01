# # First, let's install the necessary packages
# !pip install flask
# !pip install torch
# !pip install transformers

# Next, let's import the necessary modules
import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel
from flask import Flask, request, jsonify

# Set the device to run on (either CPU or GPU)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Set the model and tokenizer names
model_name = 'gpt2'

# Download the model and tokenizer from the Hugging Face model repository
model = GPT2LMHeadModel.from_pretrained(model_name).to(device)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Define a function to generate text based on a user's input
def generate_text(prompt):
  # Encode the prompt
  encoded_prompt = tokenizer.encode(prompt, return_tensors='pt').to(device)

  # Set the attention mask and pad token ID
  attention_mask = encoded_prompt.ne(0).int()
  pad_token_id = tokenizer.eos_token_id

  # Generate text
  output = model.generate(input_ids=encoded_prompt, attention_mask=attention_mask, pad_token_id=pad_token_id, max_length=200, top_k=5, top_p=0.95, temperature=0.5)
  
  # Decode the output and remove the start token
  generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

  return generated_text

# Set up the Flask server
app = Flask(__name__)

# Define the API endpoint
@app.route('/api', methods=['POST'])
def generate_text_endpoint():
  # Get the input from the request
  input = request.json['input']

  # Generate text
  output = generate_text(input)

  # Return the output as a JSON response
  return jsonify({ 'output': output })

# Run the Flask server
if __name__ == '__main__':
  app.run()
