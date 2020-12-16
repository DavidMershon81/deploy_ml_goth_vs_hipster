#This script loads in a fast.ai classifier that I trained on colab
#Then it returns some predictions about if an image is goth or hipster
#This was modified off the original test script to work with a flask web app

from collections import namedtuple
from fastai.vision.all import *
load_path = Path(__file__).parent
classifier_save_filename = 'subculture_classifier.pkl'
loaded_subculture_learn = load_learner(load_path/classifier_save_filename)

PredictionInfo = namedtuple("PredictionInfo", "prediction probability description img_filename")

def predict_uploaded_image(uploaded_image):
    test_img = PILImage.create(uploaded_image)
    prediction,p_index,probabilities = loaded_subculture_learn.predict(test_img)
    image_file_name = str(uploaded_image)
    return PredictionInfo(prediction=prediction, probability=probabilities[p_index], description="Uploaded Image", img_filename=image_file_name)

def get_prediction_info(img_filename, description):
    full_path = image_path = load_path/'static'/'images'/img_filename
    prediction,p_index,probabilities = loaded_subculture_learn.predict(full_path)
    return PredictionInfo(prediction=prediction, probability=probabilities[p_index], description=description, img_filename=img_filename)

def get_test_predictions():
  return [ get_prediction_info('david_and_julie.jpg', 'David and Julie'), \
    get_prediction_info('david_solo.jpg', 'David Solo'), \
    get_prediction_info('james_hoffmann.jpg', 'James Hoffmann')]
