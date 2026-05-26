from adafruit_servokit import ServoKit
import time

kit = ServoKit(channels=16)


servos = {
    "front_left_hip": 0,
    "front_left_knee": 1,

    "front_right_hip": 2,
    "front_right_knee": 3,

    "back_left_hip": 4,
    "back_left_knee": 5,

    "back_right_hip": 6,
    "back_right_knee": 7,
}

STAND_ANGLE = 90
UP_ANGLE = 60
DOWN_ANGLE = 120

MOVE_DELAY = 0.02


def set_all_servos(angle):
    for servo_channel in servos.values():
        kit.servo[servo_channel].angle = angle


def smooth_move(start_angle, end_angle, delay=MOVE_DELAY):

    step = 1 if end_angle > start_angle else -1


    for angle in range(start_angle, end_angle, step):
        set_all_servos(angle)
        time.sleep(delay)

    set_all_servos(end_angle)


def robot_up():
    smooth_move(DOWN_ANGLE, UP_ANGLE)


def robot_down():
    smooth_move(UP_ANGLE, DOWN_ANGLE)



set_all_servos(STAND_ANGLE)
time.sleep(1)

try:
    while True:
        print("up")
        smooth_move(STAND_ANGLE, UP_ANGLE)
        time.sleep(0.5)

        print(" down")
        smooth_move(UP_ANGLE, DOWN_ANGLE)
        time.sleep(0.5)

        print("stand")

        smooth_move(DOWN_ANGLE, STAND_ANGLE)
        time.sleep(0.5)

except KeyboardInterrupt:
    print("Stopping robot")
    set_all_servos(STAND_ANGLE)