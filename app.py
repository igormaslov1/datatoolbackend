from flask import Flask, request
import analysys_service
import pandas as pd

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/convertFromExcelToPandas", methods=['GET', 'POST'])
def convertFromExcelToPandas():
    if request.method == 'POST':
        file = request.files['file']
        return analysys_service.convertFromExcelToPandas(file)

if __name__ == "__main__":
    app.run()