import time
from datetime import datetime
import board
from busio import I2C
import adafruit_bme680

i2c = I2C(board.SCL, board.SDA)
bme680 = adafruit_bme680.adafruit_BME680_I2C(i2c, debug=False)

print("Temperatur: " + bme680.temperature + " °C") # Grad Celsius
print("Gas: " + bme680.gas + "Ohm") # Ohm
print("Relative Luftfeuchtigkeit: " + relative_humidity + " %") # %
print("Luftdruck: " + bme680.pressure + " hPa") # hPa
print("Meter: " + bme680.altitude + " m") # m 
