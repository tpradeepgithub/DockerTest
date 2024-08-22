from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <h1>About MyIntro</h1>
        <p>Name: Pradeep</p>
        <p>email: pradeep1@gmail.com </p>
        <p>Developer: PY</p>
        <p>Description: This is my sample Docker page.</p>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

