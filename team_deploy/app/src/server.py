import pandas as pd
from flask import Flask, jsonify, request
import pickle
from swagger.app import blueprint as app_endpoints
import base64
from datetime import datetime

import tensorflow as tf
import numpy as np
from keras import backend
from tensorflow.keras import models
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array

# app
app = Flask(__name__)
app.config['RESTPLUS_MASK_SWAGGER'] = False
app.register_blueprint(app_endpoints)

# routes
@app.route('/prediction', methods=['GET', 'POST'])

def predict():

    if request.method == "GET":
        return {
            'message': 'This endpoint should return past predictions',
            'method': request.method
        }
    
    if request.method == "POST":
        
        # get data
        data = request.get_json(force=True)

        img = data["message"]

        base64_img_bytes = img.encode('utf-8')
        now = datetime.now()
        file_name_st = now.strftime("%d%m%Y%H%M%S")
        with open('../../bucket_images/'+file_name_st+'.png', 'wb') as file_to_save:
            decoded_image_data = base64.decodebytes(base64_img_bytes)
            file_to_save.write(decoded_image_data)

        #Output prediction
        # calculate fbeta score for multi-class/label classification
        def fbeta(y_true, y_pred, beta=2):
            # clip predictions
            y_pred = backend.clip(y_pred, 0, 1)
            # calculate elements
            tp = backend.sum(backend.round(backend.clip(y_true * y_pred, 0, 1)), axis=1)
            fp = backend.sum(backend.round(backend.clip(y_pred - y_true, 0, 1)), axis=1)
            fn = backend.sum(backend.round(backend.clip(y_true - y_pred, 0, 1)), axis=1)
            # calculate precision
            p = tp / (tp + fp + backend.epsilon())
            # calculate recall
            r = tp / (tp + fn + backend.epsilon())
            # calculate fbeta, averaged across each class
            bb = beta ** 2
            fbeta_score = backend.mean((1 + bb) * (p * r) / (bb * p + r + backend.epsilon()))
            return fbeta_score

        # predictions
        #Load Model
        new_model = tf.keras.models.load_model('./models/score_3249.h5', custom_objects={'fbeta': fbeta})

        #Load image
        photo = load_img('../../bucket_images/'+file_name_st+'.png', target_size=(128,128))
        # convert to numpy array
        photo = img_to_array(photo, dtype='uint8')

        X = np.reshape(photo, (1,128,128,3))

        # output
        tags = new_model.predict(X)
        tags.argmax()
        list_emotions = ['Affection','Anger','Annoyance', 'Anticipation', 'Aversion', 'Confidence', 'Disapproval', 'Disconnection', 'Disquietment', 'Doubt/Confusion', 'Embarrassment', 'Engagement', 'Esteem', 'Excitement', 'Fatigue', 'Fear', 'Happiness', 'Pain', 'Peace', 'Pleasure', 'Sadness', 'Sensitivity', 'Suffering', 'Surprise', 'Sympathy', 'Yearning']
        output = {'emotions': list_emotions[tags.argmax()], "score": 0.3249}

        # return data
        return jsonify(results=output)

if __name__ == '__main__':
    app.run(port = 5000, debug=True, host='0.0.0.0')