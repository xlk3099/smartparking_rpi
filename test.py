import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
input_chan_list = [8, 10, 12]
GPIO.setup(input_chan_list, GPIO.IN)

ir_prev_values = [1, 1, 1]
# Define the GPIO output ports for controllering LEDS
output_chan_list = [22, 24, 26]

GPIO.setup(output_chan_list, GPIO.OUT, initial=GPIO.HIGH)

while True:
        # Update the status of LED
        if GPIO.input(8) == 0:
            GPIO.output(22, GPIO.LOW)
        else:
            GPIO.output(, GPIO.HIGH)
        # update the status of car slots available or not 
        data[index+1]["available"] = True if GPIO.input(chan) == 1 else False
