from flask import Flask
import analysys_service_ui
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"