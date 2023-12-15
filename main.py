import RPi.GPIO as GPIO
import time
import random
import math
import matplotlib.pyplot as plt
import pandas as pd

class TradingSimulation:
    def __init__(self, initial_cash):
        self.cash = initial_cash
        self.eth_holding = 0
        self.btc_holding = 0
        self.current_price = {'eth': 0, 'btc': 0}

    def update_price(self, eth_price, btc_price):
        self.current_price['eth'] = eth_price
        self.current_price['btc'] = btc_price

    def buy(self, currency, amount_in_usd):
        if amount_in_usd > self.cash:
            print("Not enough cash to buy.")
            return
        units = amount_in_usd / self.current_price[currency]
        self.cash -= amount_in_usd
        if currency == 'eth':
            self.eth_holding += units
        elif currency == 'btc':
            self.btc_holding += units

    def sell(self, currency, amount_in_usd):
        units = amount_in_usd / self.current_price[currency]
        if currency == 'eth' and units > self.eth_holding or \
           currency == 'btc' and units > self.btc_holding:
            print("Not enough holdings to sell.")
            return
        self.cash += amount_in_usd
        if currency == 'eth':
            self.eth_holding -= units
        elif currency == 'btc':
            self.btc_holding -= units
# =========================== # 



# Import Data
single_price = False
prices = []
if(single_price):
    # Load Lockheed CSV file
    df = pd.read_csv('/home/pi/final-project/prices.csv')  #

    # Extract a column (for example, a column named 'ColumnName')
    prices = [(x) for x in [int(df['Close'].values[0]/2)] * 32 + [int(x/2) for x in list(df['Close'].values)]]  #
else:
    # Load ETH, USD file
    df = pd.read_csv('/home/pi/final-project/data/raw_merge.csv') 
    df['eth_btc_ratio'] = (df['Open_eth'] / df['Open_btc'] - 0.022) * 100000
    df['eth_btc_ratio'] = df['eth_btc_ratio'].apply(lambda x: int(x)) # Quantize the ratio, assuming eth never goes above btc
    # Extract the tuples
    prices = list(df[['eth_btc_ratio','Open_eth', 'Open_btc']].itertuples(index=False, name=None))



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

# Set up GPIO pins for input
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

    

input_readings = [0,0]
output_readings = [0,0]
eth_readings = [0,0]
btc_readings = [0,0]


# Initialize the plot
plt.ion()
# Create a figure and a set of subplots
fig, (ax1, ax2, ax3) = plt.subplots(3, 1)  # 2 rows, 1 column

plt.tight_layout()  # Adjusts the plots to fit into the figure area.
plt.show()

x = []
input_y = []
output_y = []
input_line, = ax1.plot(x, input_y, label='FPGA Output')
output_line, = ax1.plot(x, output_y, label='FPGA Input')


btc = []
eth = []
eth_line, = ax2.plot(x, btc, label='ETH/USD')
btc_line, = ax2.plot(x, eth, label='BTC/USD')
ax2.legend()
ax1.legend()


x_pnl = []
pnl = []
pnl_line, = ax3.plot(x_pnl, pnl, label='PnL')

# Create a secondary y-axis for ax2
ax2_twin = ax2.twinx()  # This is the new y-axis with a different scale

prev_val = 0


prev_diff = 0
directions = []

past = []
accelerate = False
try:
    sim = TradingSimulation(10000)
    for data in prices:
        sim.update_price(data[1],data[2])
        val = data[0]
        def ma(val):
            if accelerate:
                print("===")        
                start = time.time()
                send_integer(val)
                ## elapsed_sent = (time.time() - start)
                ## print("TIME TOOK FOR SENDING DATA :" + str(elapsed_sent))
                generate_clock_signal()  # Generate a clock pulse
                start_read = time.time()
                moving_average = read_gpio_state()
                ## elasped_read = (time.time() - start_read)
                ## print("TIME TOOK FOR READING DATA:" + str(elasped_read))
                total_time = time.time() - start
                # print("TIME TOOK FOR COMPUTATION" + str(total_time))
                return moving_average
            else:
                if len(past) > 15:
                    past.pop(0)
                    past.append(val)
                else:
                    past.append(val)
                return int(sum(past)/len(past))
        moving_average = ma(val)
        output_value = val
        # print("Sent: " + str(bin(output_value)) + ", Received: " + str(bin(moving_average)))
        
        # Populate lists for visualization
        input_readings.append(moving_average)
        output_readings.append(output_value)
        eth_readings.append(data[1])
        btc_readings.append(data[2])
        
        # Keep only the most recent 50 readings
        if len(input_readings) > 50:
            input_readings.pop(0)
            output_readings.pop(0)
            btc_readings.pop(0)
            eth_readings.pop(0)
            
        # Compute diffs
        diff = input_readings[-1]-input_readings[-2]
        if diff > prev_diff:
            directions.append(1)  # Upward trend
        elif diff < prev_diff:
            directions.append(-1) # Downward trend
        else:
            directions.append(0)  # No significant change
        prev_diff = diff
        direction = directions[-1]

        # Update the x-axis
        x = list(range(len(input_readings)))

        # Update the input and output lines
        input_line.set_xdata(x)
        input_line.set_ydata(input_readings)
        output_line.set_xdata(x)
        output_line.set_ydata(output_readings)

        ax1.relim()
        ax1.autoscale_view()
        
        
        # Update the input and output lines
        btc_line.set_xdata(x)
        btc_line.set_ydata(btc_readings)
        eth_line.set_xdata(x)
        eth_line.set_ydata(eth_readings)

        ax2.relim()
        ax2.autoscale_view()

        # Trading logic
        threshold = 0.01  # Example: 1% threshold
        ratio_ma = moving_average
        ratio = val
    
        if ratio > ratio_ma * (1 + threshold):
            sim.sell('eth', 1000)  # Sell ETH worth 1000 USD
            sim.buy('btc', 1000)  # Buy BTC with 1000 USD
            print("SHORT ETH")
        elif ratio < ratio_ma * (1 - threshold):
            sim.buy('eth', 1000)  # Sell ETH worth 1000 USD
            sim.sell('btc', 1000)  # Buy BTC with 1000 USD
            print("LONG ETH")    
        print("RATIO:",data[0],",ETH/USD:",data[1],",BTC/USD:",data[2],", ETH HOLDING:",sim.eth_holding,", BTC HOLDING:",sim.btc_holding)
        

        # Update net worth
        net_worth = sim.cash + sim.eth_holding * sim.current_price['eth'] + \
                      sim.btc_holding * sim.current_price['btc']
        print("Net Worth: $" + str(net_worth))
        pnl.append(net_worth)
        
        # Update the graph with input and output readings
        ax1.clear()
        ax2.clear()
        ax2_twin.clear()
        input_line, = ax1.plot(x, input_readings, label='32t Moving Average (ETH/BTC)')
        output_line, = ax1.plot(x, output_readings, label='ETH/BTC ratio at t (ETH/BTC)')
        
        ax3.clear()
        pnl.append(net_worth)
        x_pnl = list(range(len(pnl)))
        pnl_line,  = ax3.plot(x_pnl, pnl, label="PnL")

        # Plot on the secondary axis
        btc_line, = ax2.plot(x, btc_readings, 'r-', label='BTC/USD')  # Plotting on the original axis
        eth_line, = ax2_twin.plot(x, eth_readings, 'b-', label='ETH/USD')  # Plotting on the secondary axis
        
        # Set labels for the axes
        ax2.set_xlabel('Time')
        ax2.set_ylabel('BTC/USD', color='r')
        ax2_twin.set_ylabel('ETH/USD', color='b')

        # Add legends
        ax2.legend(loc='upper left')
        ax2_twin.legend(loc='upper right')


        # Display net worth on the graph
        # ax1.set_title('ETH/BTC Ratio, MA')
        # Adjust plot limits and draw the plot
        ax3.relim()
        ax3.autoscale_view()
        ax3.legend()
        ax1.relim()
        ax1.autoscale_view()
        ax2.relim()
        ax2.autoscale_view()
        ax2.legend()
        ax1.text(0.5, 1.05, "FPGA Net Worth: USD" + str(net_worth), ha='center', va='center', transform=ax1.transAxes, fontsize=16)
        ax1.legend()
        plt.pause(0.1)  # Add some delay to observe 
except KeyboardInterrupt:
    pass
finally:
    # Cleanup GPIO pins
    GPIO.cleanup()
    plt.ioff()
    plt.show()
