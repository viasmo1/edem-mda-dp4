import cv2 as cv
import base64
import requests
import datetime
from time import localtime, strftime
import json

class Camera(object):
    CAPTURES_DIR = "static/captures/"
    RESIZE_RATIO = 1.0

    state = ""

    def __init__(self):
        self.video = cv.VideoCapture(0)
    
    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, frame = self.video.read()
        if not success:
            return None

        if (Camera.RESIZE_RATIO != 1):
            frame = cv.resize(frame, None, fx=Camera.RESIZE_RATIO, \
                fy=Camera.RESIZE_RATIO)    
        return frame

    def get_feed(self):
        frame = self.get_frame()
        if frame is not None:
            ret, jpeg = cv.imencode('.jpg', frame)
            return jpeg.tobytes()

    def return_json(self, str_name, str_img):
        return '{"creationDate":'+'"'+str_name+'"'+','+'"message":'+'"'+str_img+'"'+'}'

    def post_method(self, image):
        base64_encoded_data = base64.b64encode(image)
        base64_message = base64_encoded_data.decode('utf-8')
        creationDate = str(datetime.datetime.now())
        data_in = self.return_json(creationDate, base64_message)
        r = requests.post("http://0.0.0.0:5000/prediction", data=data_in)
        return r

    def capture(self):
        frame = self.get_frame()
        timestamp = strftime("%d-%m-%Y-%Hh%Mm%Ss", localtime())
        if frame is not None:
            ret, jpeg = cv.imencode('.jpg', frame)
            jpeg.tobytes()
            result = self.post_method(jpeg.tobytes())
            ab = result.json()
            self.state=ab['results']['emotions']
        filename = Camera.CAPTURES_DIR + timestamp +".jpg"
        if not cv.imwrite(filename, frame):
            raise RuntimeError("Unable to capture image "+timestamp)
        return timestamp
    
    def emotion(self):
        return self.state