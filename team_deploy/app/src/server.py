import pandas as pd
from flask import Flask, jsonify, request
from swagger.app import blueprint as app_endpoints
import base64
from datetime import datetime
from skimage import color
from skimage import io

import cv2
import tensorflow as tf
import numpy as np
from PIL import Image


# app
app = Flask(__name__)
app.config["RESTPLUS_MASK_SWAGGER"] = False
app.register_blueprint(app_endpoints)

# routes
@app.route("/prediction", methods=["GET", "POST"])

# def fbeta(y_true, y_pred, beta=2):
#            # clip predictions
#            y_pred = backend.clip(y_pred, 0, 1)
#            # calculate elements
#            tp = backend.sum(backend.round(backend.clip(y_true * y_pred, 0, 1)), axis=1)
#            fp = backend.sum(backend.round(backend.clip(y_pred - y_true, 0, 1)), axis=1)
#            fn = backend.sum(backend.round(backend.clip(y_true - y_pred, 0, 1)), axis=1)
#            # calculate precision
#            p = tp / (tp + fp + backend.epsilon())
#            # calculate recall
#            r = tp / (tp + fn + backend.epsilon())
#            # calculate fbeta, averaged across each class
#            bb = beta ** 2
#            fbeta_score = backend.mean((1 + bb) * (p * r) / (bb * p + r + backend.epsilon()))
#            return fbeta_score


def predict():

    if request.method == "GET":
        return {
            "message": "This endpoint should return past predictions",
            "method": request.method,
        }

    if request.method == "POST":

        # get data
        data = request.get_json(force=True)

        img = data["message"]

        base64_img_bytes = img.encode("utf-8")
        now = datetime.now()
        file_name_st = now.strftime("%d%m%Y%H%M%S")
        with open("./images/" + file_name_st + ".png", "wb") as file_to_save:  # bucket_
            decoded_image_data = base64.decodebytes(base64_img_bytes)
            file_to_save.write(decoded_image_data)

        # Output prediction

        # predictions
        # Load Model
        with open("./models/FacialExpression-model.json", "r") as json_file:
            json_savedModel = json_file.read()

            # Cargamos la arquitectura del modelo
        new_model = tf.keras.models.model_from_json(json_savedModel)
        new_model.load_weights("./models/FacialExpression_weights.hdf5")
        new_model.compile(
            optimizer="Adam", loss="categorical_crossentropy", metrics=["accuracy"]
        )

        # Load image
        def load_image(infilename):
            img = Image.open(infilename)
            img.load()
            data = np.asarray(img, dtype="int32")
            return data

        # photo = load_img('../../images/'+file_name_st+'.png', target_size=(128,128)) #bucket_
        photo = load_image(
            "./images/" + file_name_st + ".png"
        )  #'../../images/'+file_name_st+'.png'
        # convert to numpy array

        # Blanco y negro
        imgGray = color.rgb2gray(photo)

        # 1er redimensionado
        resize_img = cv2.resize(imgGray, (96, 96))

        # redimensionado
        resize_img2 = resize_img.reshape(1, 96, 96, 1)

        # Predecimos
        resultados = new_model.predict(resize_img2)

        # output
        list_emotions = {
            0: "Ira",
            1: "Odio",
            2: "Tristeza",
            3: "Felicidad",
            4: "Sorpresa",
        }

        output = {"emotions": list_emotions[resultados.argmax()], "score": -0.3249}

        # return data
        return jsonify(results=output)


if __name__ == "__main__":
    app.run(port=5000, debug=True, host="0.0.0.0")
