from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/rehareha261/rehareha261')
def rehareha261_endpoint():
    return jsonify({
        "message": "Welcome to the rehareha261 endpoint",
        "status": "success"
    })

if __name__ == '__main__':
    app.run()