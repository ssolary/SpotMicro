import board
import digitalio
import busio
from adafruit_servokit import ServoKit
import adafruit_motor.servo

i2c_bus = busio.I2C(board.SCL_1, board.SDA_1);
kit = ServoKit(channels=16, i2c=i2c_bus)
kit.servo[0].angle = 0