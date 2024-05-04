from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/hola", methods=['GET'])
def hola():
    return jsonify({'message':"Endpoint desde hola"})

if __name__ == "__main__":
    app.run(debug=True)