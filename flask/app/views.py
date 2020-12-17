from app import app, test_model_load
from flask import request, jsonify, render_template


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if request.files:
            image = request.files["image"]
            prediction = test_model_load.predict_uploaded_image(image)
            #print(f"prediction: {prediction.prediction} probability: {prediction.probability}")
            prediction_display_html = render_template("prediction_display.html", prediction=prediction)
            return jsonify({"prediction_display_html" : prediction_display_html })
    else:
        return render_template("index.html")
