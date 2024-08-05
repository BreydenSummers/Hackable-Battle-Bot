from adafruit_motorkit import MotorKit


kit = MotorKit()


while True:
    kit.motor1.throttle = 0.5
    kit.motor2.throttle = -0.5
