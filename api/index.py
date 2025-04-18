from flask import Flask, render_template
import os

base_dir = os.path.dirname(os.path.abspath(__file__))

app = Flask(
    __name__,
    static_folder=os.path.join(base_dir, '..', 'static'),
    template_folder=os.path.join(base_dir, '..', 'templates')
)

@app.route('/')
def home():
    return render_template("home.html")

index = app.wsgi_app
