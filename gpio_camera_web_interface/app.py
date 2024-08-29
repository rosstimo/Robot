from flask import Flask, render_template, request
import RPi.GPIO as GPIO
from picamera import PiCamera
import time

app = Flask(__name__)

# Initialize GPIO and Camera
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)  # Example GPIO pin
camera = PiCamera()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gpio', methods=['POST'])
def gpio_control():
    state = request.form.get('state')
    if state == 'on':
        GPIO.output(18, GPIO.HIGH)
    else:
        GPIO.output(18, GPIO.LOW)
    return 'GPIO state changed'

@app.route('/capture', methods=['POST'])
def capture_image():
    camera.start_preview()
    time.sleep(2)  # Camera warm-up time
    camera.capture('/home/pi/image.jpg')
    camera.stop_preview()
    return 'Image captured'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

