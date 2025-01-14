from flask import Flask, jsonify
from flask_cors import CORS  # Import CORS

app = Flask(__name__)

# Enable CORS for all routes
CORS(app)
@app.route('/', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello from AWS EC2 Backend!'})
  
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
  
