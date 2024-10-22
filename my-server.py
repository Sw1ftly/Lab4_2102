from flask import Flask, request, jsonify

app = Flask(__name__)
stored_token = None

@app.route('/login', methods=['POST'])
def login():
    global stored_token
    data = request.form
    if data.get('id') == 'yasin.ahmed@uconn.edu' and data.get('token') == 'f99aa8b8573062e9802f4fc0807ae1cb':
        stored_token = data.get('token')
        return jsonify({"message": "Login successful"}), 200
    return jsonify({"message": "Invalid credentials"}), 401

@app.route('/some_protected_endpoint', methods=['GET'])
def protected():
    token = request.headers.get('Authorization', '').replace('Bearer ', '')
    if token == stored_token:
        return jsonify({"message": "You said: Hello Yasin. The lab demo seems to work :)"}), 200
    return jsonify({"message": "Unauthorized"}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)