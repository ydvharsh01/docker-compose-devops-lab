from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "🚀 Docker Compose Magic: Flask App aur PostgreSQL Database ek sath chal rahe hain!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)