from flask import Flask, request, jsonify
app = Flask(__name__)

# Bob's RSA private key
d = 103
n = 143

@app.route('/decrypt', methods=['POST'])
def decrypt():
    Y = int(request.json['Y'])
    Z = pow(Y, d, n)
    return jsonify({"Z": Z})

if __name__ == '__main__':
    app.run(port=5001)
