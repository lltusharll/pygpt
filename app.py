from flask import Flask, request
import torch
import transformers

app = Flask(__name__)

# Load the pretrained model and tokenizer
model = transformers.GPT2LMHeadModel.from_pretrained('gpt2')
tokenizer = transformers.GPT2Tokenizer.from_pretrained('gpt2')

@app.route('/api', methods=['GET'])  # Allow the GET method
def handle_request():
    # Get the input text from the query string
    input_text = request.args.get('input')
    # Tokenize the input text and generate the response
    input_ids = torch.tensor([tokenizer.encode(input_text, return_tensors='pt')])
    output = model.generate(input_ids)
    output_text = tokenizer.decode(output[0], skip_special_tokens=True)
    # Return the generated text as a JSON response
    return {'output': output_text}

if __name__ == '__main__':
    app.run()
