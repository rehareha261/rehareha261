from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/github')
def github_endpoint():
    return jsonify({
        "message": "Welcome to the GitHub endpoint",
        "status": "success"
    })

if __name__ == '__main__':
    app.run()