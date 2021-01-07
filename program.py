from flask import Flask 
from flask import jsonify
import time
from datetime import datetime
import board
from busio import I2C
import adafruit_bme680


i2c = I2C(board.SCL, board.SDA)
bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c, debug=False)

bme680.sea_level_pressure = 1012.0

def getData():
    return {
        'time': datetime.utcnow().isoformat(),
                'temperature': bme680.temperature,
                'gas': bme680.gas,
                'humidity': bme680.relative_humidity,
                'pressure': bme680.pressure,
                'altitude': bme680.altitude
        } 


app = Flask(__name__)

@app.route('/')
def index() : 
    return jsonify(getData())
    

if __name__ == '__main__':
    app.run(host='0.0.0.0.', port=5000)