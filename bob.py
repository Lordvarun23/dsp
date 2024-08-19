from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

e = 7
n = 143

@app.route('/send', methods=['POST'])
def send():
    P = int(request.json['P'])
    C = pow(P, e, n)
    
    response = requests.post('http://localhost:5003/intercept', json={"C": C})
    return response.json()

if __name__ == '__main__':
    app.run(port=5002)
