import RPi.GPIO as GPIO
import time

# Set up GPIO pins
GPIO.setmode(GPIO.BCM)
data_pins = [2, 3, 4, 17, 27, 22, 10, 9, 11, 5, 6, 13, 19, 26, 14, 15]  # Example GPIO pins
for pin in data_pins:
    GPIO.setup(pin, GPIO.OUT)

def send_integer(integer):
    binary_representation = format(integer, '016b')
    # print(binary_representation)
    for i, bit in enumerate(binary_representation):
        GPIO.output(data_pins[i], int(bit))

# Example: Sending a series of 16-bit integers
integers = [1023, 2048, 4096, 8192]  # Example array of integers
for integer in integers:
    send_integer(integer)
    time.sleep(0.001)  # Adjust timing based on your requirements

# Cleanup GPIO pins
GPIO.cleanup()
