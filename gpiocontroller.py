import RPi.GPIO as GPIO
import camera
import requests
import thread

# Set GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Define the GPIO input ports for IR sensors
input_chan_list = [8, 10, 12]
GPIO.setup(input_chan_list, GPIO.IN)

ir_prev_values = [1, 1, 1]
# Define the GPIO output ports for controllering LEDS
output_chan_list = [22, 24, 26]

GPIO.setup(output_chan_list, GPIO.OUT, initial=GPIO.HIGH)

# Data to send

data = {
    1: {
        'id': 1,
        'available': True,
        'plateNo': ''
    },
    2: {
        'id': 2,
        'available': True,
        'plateNo': ''
    },
    3: {
        'id': 3,
        'available': True,
        'plateNo': ''
    }
}

camera = camera.Camera()


def detect_parking():
    print("LED process started")
    while True:
        time.sleep(1)
        for index, chan in enumerate(input_chan_list):
            if GPIO.input(chan) != ir_prev_values[index]:
                ir_prev_values[index] = GPIO.input(chan)
                # Update the status of LED
                if GPIO.input(chan) == 0:
                    GPIO.output(output_chan_list[index], GPIO.LOW)
                else:
                    GPIO.output(output_chan_list[index], GPIO.HIGH)
            # update the status of car slots available or not 
            data[key]["available"] = True if GPIO.input(chan) == 1 else False


def take_snapshots():
    print("Camera process started")
    while True:
        plates = camera.recognizePlate()
        for key, value in plates.items():
            data[key]['plateNo'] = value
        r = requests.put('http://10.148.75.58:8080parking', json=data)
        print(r.)

try:
   thread.start_new_thread(detect_parking, ())
   thread.start_new_thread(take_snapshots, ())
except:
   print("Unable to start threads")
while 1:
    pass



