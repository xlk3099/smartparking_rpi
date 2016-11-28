import RPi.GPIO as GPIO
import camera
import requests

# Set GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Define the GPIO input ports for IR sensors
input_chan_list = [8, 10, 12]
GPIO.setup(input_chan_list, GPIO.IN)

ir_prev_values = [1, 1, 1]
# Define the GPIO output ports for controllering LEDS
output_chan_list = [22, 24, 26]
GPIO.setup(output_chan_list, GPIO.OUT, initial=1)

# Data to send


data = {
    '1': {
        'id': 1,
        'available': True,
        'plateNo': ''
    },
    '2': {
        'id': 2,
        'available': True,
        'plateNo': ''
    },
    '3': {
        'id': 3,
        'available': True,
        'plateNo': ''
    }
}

camera = camera.Camera()

while True:
    for index, chan in enumerate(input_chan_list):
        if GPIO.input(chan) != ir_prev_values[index]:
            ir_prev_values[index] = GPIO.input(chan)
            # Take a capture
            plates = camera.recognizePlate()
            if GPIO.input(chan) == 0:
                # Update the status of LED
                GPIO.output(output_chan_list(index), GPIO.LOW)
            # Take photo and send request
            else:
                GPIO.output(output_chan_list(index), GPIO.HIGH)
            data[index]["available"] = True if GPIO.input(chan) == 1 else False
            data[index]["plateNo"] = plates[index]
    r = requests.put('http://10.148.75.58:8080/parking', json=data)

GPIO.cleanup()
