#Import necessary libraries
from flask import Flask, render_template, Response, send_file, redirect, url_for, request
import cv2
from camera import Camera


#Initialize the Flask app
app = Flask(__name__)
camera = None


def get_camera():
    global camera
    if not camera:
        camera = Camera()

    return camera


@app.route("/")
def root():
    return redirect(url_for('index'))


@app.route('/index/')
def index():
    return render_template('index.html', title="page")

def gen(camera):
    while True:
        frame = camera.get_feed()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed/')
def video_feed():
    camera = get_camera()
    return Response(gen(camera),
        mimetype='multipart/x-mixed-replace; boundary=frame')


# route for capturing picture
@app.route('/capture/')

def capture():
    camera = get_camera()
    stamp = camera.capture()
    return redirect(url_for('show_capture', timestamp=stamp))

def stamp_file(timestamp):
    return 'captures/' + timestamp +".jpg"


@app.route('/capture/image/<timestamp>', methods=['POST', 'GET'])
def show_capture(timestamp):
    path = stamp_file(timestamp)
    
    email_msg = None
    if request.method == 'POST':
        if request.form.get('email'):
            email = get_mail_server()
            email_msg = email.send_email('static/{}'.format(path), 
                request.form['email'])
        else:
            email_msg = "Email field empty!"


    return render_template('capture.html',
        stamp=timestamp, path=path, email_msg=email_msg)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')