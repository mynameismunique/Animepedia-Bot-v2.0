from flask import Flask, render_template, request, jsonify
import json
import random

app = Flask(__name__)

def load_intents(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def get_response(user_input, intents_data):
    user_input = user_input.lower()
    
    for intent in intents_data['intents']:
        for pattern in intent['patterns']:
            if pattern.lower() in user_input:
                return random.choice(intent['responses'])
    
    for intent in intents_data['intents']:
        if intent['tag'] == 'default':
            return random.choice(intent['responses'])
    
    return {"text": "Gomen... saya tidak mengerti.", "image": None} 

intents = load_intents('data.json')


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def chat_response():
    user_message = request.json["message"]
    bot_response = get_response(user_message, intents)
    
    with open('chat_log.txt', 'a', encoding='utf-8') as f:
        f.write(f"USER: {user_message}\n")
        f.write(f"BOT: {bot_response['text']}\n---\n")
    
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)