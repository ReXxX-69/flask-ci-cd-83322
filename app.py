from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Kacper_Jamrozinski_83322'

if __name__ == '__main__':
    app.run(debug=True)
