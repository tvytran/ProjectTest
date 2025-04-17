from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from VSA Website! This is a basic test."

# This is crucial for Vercel
index = app.wsgi_app