# from flask import Flask, request, jsonify
# from main import agent  # Assuming your agent is defined in the main.py

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return 'Hello, World!'

# @app.route('/chat', methods=['POST'])
# def chat():
#     data = request.json
#     user_message = data['message']
#     response = agent(user_message)  # Use the agent from your main.py
#     return jsonify({'response': response['output']})

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask
from flask import Blueprint, render_template, request, jsonify
from flask_cors import CORS
from main import agent

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/send-message', methods=['POST'])
def send_message():
    data = request.get_json()
    user_message = data.get('message')
    
    # Process the user's message as needed here
    
    response_message = agent(user_message)
    response = response_message['output']
    
    return jsonify({"response": response})


if __name__ == "__main__":
   app.run(debug=True, port=8001)
   #app.run(debug=True, host='0.0.0.0', port=8000)