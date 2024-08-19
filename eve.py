# eve.py
from flask import Flask, request, jsonify
import requests
from sympy import mod_inverse

app = Flask(__name__)

# Bob's public key
e = 7
n = 143

@app.route('/intercept', methods=['POST'])
def intercept():
    C = int(request.json['C'])
    
    # Eve chooses a random X in Z_n* (e.g., X = 2)
    X = 2
    
    # Eve computes Y = C * X^e mod n
    Y = (C * pow(X, e, n)) % n
    
    # Eve sends Y to Bob for decryption
    response = requests.post('http://localhost:5001/decrypt', json={"Y": Y})
    Z = response.json()["Z"]
    
    # Eve calculates P = Z * X^{-1} mod n
    X_inv = mod_inverse(X, n)  # Calculate the modular inverse of X mod n
    recovered_P = (Z * X_inv) % n
    
    return jsonify({"Recovered Plaintext": recovered_P})

if __name__ == '__main__':
    app.run(port=5003)

#curl -X POST -H "Content-Type: application/json" -d '{"P": 8}' http://localhost:5002/send
