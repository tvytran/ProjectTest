from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")  # not base.html

# For Vercel compatibility
index = app.wsgi_app
