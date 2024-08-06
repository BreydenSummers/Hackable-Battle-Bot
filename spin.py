from adafruit_motorkit import MotorKit
import atexit
import signal


kit = MotorKit()


@atexit.register
def stop():
    kit.motor1.throttle = 0
    kit.motor2.throttle = 0

while True:
    kit.motor1.throttle = 1.00
    kit.motor2.throttle = 0.25
    signal.signal(signal.SIGTERM, stop)
