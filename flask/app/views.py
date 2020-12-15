from app import app
from app import test_model_load
from flask import render_template
from flask import request, redirect

@app.route("/")
def index():
    test_predictions = test_model_load.get_test_predictions()
    return render_template("index.html", test_predictions=test_predictions)

@app.route("/upload_image", methods=["GET", "POST"])
def upload_image():
    if request.method == "POST":
        if request.files:
            image = request.files["image"]
            print(image)
            #return redirect(request.url)
            return render_template("upload_image.html", prediction=test_model_load.predict_uploaded_image(image))

    return render_template("upload_image.html")