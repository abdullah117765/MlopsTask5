from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/data')
def get_data():
    data = {'message': 'Hello from Flask!'}
    return jsonify(data)

@app.route('/api/user', methods=['POST'])
def add_user():
    data = request.json
    if 'name' in data and 'email' in data:
        # Here you can process the received data, such as saving it to a database
        print("Received data:", data)
        return jsonify({'message': 'User data received successfully'}), 200
    else:
        return jsonify({'error': 'Name and email are required fields'}), 400

if __name__ == '__main__':
    app.run(debug=True)
