from adafruit_motorkit import MotorKit
import atexit

kit = MotorKit()


@atexit.register
def stop():
    kit.motor1.throttle = 0
    kit.motor2.throttle = 0

while True:
    kit.motor1.throttle = 0.5
    kit.motor2.throttle = -0.5
