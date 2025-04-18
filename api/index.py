from flask import Flask, render_template

# Tell Flask where to look for templates and static assets
app = Flask(__name__, static_folder="../static", template_folder="../templates")

@app.route('/')
def home():
    return render_template("home.html")

index = app.wsgi_app
