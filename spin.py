from adafruit_motorkit import MotorKit
import atexit
import signal
import time

kit = MotorKit()


@atexit.register
def stop():
    kit.motor1.throttle = 0
    kit.motor2.throttle = 0

while True:
    kit.motor1.throttle = 0.40
    kit.motor2.throttle = 0.40
    time.sleep(1) 
    kit.motor1.throttle = -0.40
    kit.motor2.throttle = -0.40
    time.sleep(1) 
    signal.signal(signal.SIGTERM, stop)
