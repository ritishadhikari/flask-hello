from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Flask Hello world! Version 5'

@app.route('/test')
def test():
    return 'Testing hidden functionality, good luck ;)'

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')
