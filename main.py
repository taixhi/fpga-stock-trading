import RPi.GPIO as GPIO
import time
import random
import math
import matplotlib.pyplot as plt

# Choose a GPIO pin number
clock_pin = 21

# Set up the GPIO pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(clock_pin, GPIO.OUT)

# Set up GPIO pins for output
GPIO.setmode(GPIO.BCM)
output_pins = list(reversed([2, 3, 4, 17, 27, 22, 10, 9]))  # Output GPIO pins
for pin in output_pins:
    GPIO.setup(pin, GPIO.OUT)

# Set up GPIO pins for input (replace these pin numbers with your actual input pin numbers)
input_pins = list(reversed([11, 5, 13, 19, 26, 14, 15, 18]))  # Input GPIO pins
for pin in input_pins:
    GPIO.setup(pin, GPIO.IN)

def send_integer(integer):
    binary_representation = format(integer, '08b')  # Adjusted for 8-bit binary format
    # print(f"Sending: {binary_representation} -> {integer}")
    for i, bit in enumerate(binary_representation):
        GPIO.output(output_pins[i], int(bit))

def read_gpio_state():
    # Read the state of each input pin and form a binary string
    state = ''.join(['1' if GPIO.input(pin) else '0' for pin in input_pins])
    # Convert binary string to integer
    value = int(state, 2)
    # print(f"Reading: {state} -> {value}")
    return value
    
def generate_clock_signal():
    GPIO.output(clock_pin, GPIO.LOW)
    # time.sleep(0.1)
    GPIO.output(clock_pin, GPIO.HIGH)
    # Wait for half the period
    # Set the pin low

    

# Example: Sending and reading a series of 8-bit integers
input_readings = []
output_readings = []

# Initialize the plot
plt.ion()
fig, ax = plt.subplots()
x = []
input_y = []
output_y = []
input_line, = ax.plot(x, input_y, label='FPGA Output')
output_line, = ax.plot(x, output_y, label='FPGA Input')
ax.legend()
prev_val = 0
t = 0
try:
    while True:
        t += 3.14/180
        val = int(abs(128*random.random()))
#    for val in [0x20, 0x12,0x00] * 2:
#    for val in [0x00,0x02,0x04,0x08,0X08,0x10,0x20,0x40,0x80]:
        print("===")
        # val = 0x00

        send_integer(val)
        generate_clock_signal()  # Generate a clock pulse
        input_value = read_gpio_state()
        
        output_value = val
        
        print("Sent: " + str(bin(output_value)) + ", Received: " + str(bin(input_value)))
        
        input_readings.append(input_value)
        output_readings.append(output_value)

        # Keep only the most recent 50 readings
        if len(input_readings) > 50:
            input_readings.pop(0)
            output_readings.pop(0)

        # Update the x-axis
        x = list(range(len(input_readings)))

        # Update the input and output lines
        input_line.set_xdata(x)
        input_line.set_ydata(input_readings)
        output_line.set_xdata(x)
        output_line.set_ydata(output_readings)

        ax.relim()
        ax.autoscale_view()

        # plt.pause(0.1)  # Add some delay to observe the plot
except KeyboardInterrupt:
    pass
finally:
    # Cleanup GPIO pins
    GPIO.cleanup()
    plt.ioff()
    plt.show()
