from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

# This is crucial for Vercel
index = app.wsgi_app