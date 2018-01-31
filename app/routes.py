from flask import Flask

def create_app():
    return Flask(__name__)

app = create_app()

@app.route('/')
def index():
    return "Word Count"
