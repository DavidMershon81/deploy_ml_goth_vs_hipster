from app import app
from app import test_model_load
from flask import render_template

@app.route("/")
def index():
    test_predictions = test_model_load.get_test_predictions()
    return render_template("index.html", test_predictions=test_predictions)