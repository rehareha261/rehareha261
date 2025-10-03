from flask import Flask, send_file

app = Flask(__name__)

@app.route('/rehareha261/rehareha261')
def get_main_content():
    return send_file('main.txt', mimetype='text/plain')

if __name__ == '__main__':
    app.run()