import ollama
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

transcript = [{"role": "system", "content": "You're the word wizard of Infinitecraft, tasked with merging sets of words into new creations! Take two sets of words, separated by a dash (-), and weave your magic to form a fresh set of merged words. Your response should contain only these new, enchanted words. May your creations be as infinite as the realms of Infinitecraft! Only respond with the new set of merged words, nothing else."}]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate_word', methods=['POST'])
def generate_word_api():
    data = request.get_json()
    prompt = data['prompt']
    
    user_input = prompt
    transcript.append({"role": "user", "content": user_input})

    ollama_stream = ollama.chat(
        model="llama3",
        messages=transcript,
        stream=True,
    )

    text_buffer = ""
    for chunk in ollama_stream:
        text_buffer += chunk['message']['content']

    return jsonify({'word': text_buffer})

if __name__ == '__main__':
    app.run(debug=True)
