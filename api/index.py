from flask import Flask, render_template

# Tell Flask explicitly where to find static files
app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def home():
    return render_template("home.html")

index = app.wsgi_app
