from flask import Flask, request, jsonify, render_template
from llama import create_llm, generate_output

llm = create_llm()
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get("message")
    print(user_message)
    response_message = generate_output(user_message, llm)
    print(response_message)
    return jsonify({"response": response_message})

if __name__ == '__main__':
    app.run(threaded=True)
