from flask import Flask, jsonify, request
import RPi.GPIO as GPIO

app = Flask(__name__)

# Set up GPIO
LED_PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

@app.route('/led', methods=['POST'])
def control_led():
    data = request.get_json()
    if not data or 'state' not in data:
        return jsonify({'error': 'Invalid request'}), 400

    state = data['state']
    if state == 'on':
        GPIO.output(LED_PIN, GPIO.HIGH)
        return jsonify({'status': 'LED turned on'}), 200
    elif state == 'off':
        GPIO.output(LED_PIN, GPIO.LOW)
        return jsonify({'status': 'LED turned off'}), 200
    else:
        return jsonify({'error': 'Invalid state'}), 400

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000)
    finally:
        GPIO.cleanup()

