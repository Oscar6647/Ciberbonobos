#!/usr/bin/env pybricks-micropython

"""
Example LEGO® MINDSTORMS® EV3 Robot Arm Program
-----------------------------------------------

This program requires LEGO® EV3 MicroPython v2.0.
Download: https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3

Building instructions can be found at:
https://education.lego.com/en-us/support/mindstorms-ev3/building-instructions#building-core
"""

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import TouchSensor, ColorSensor
from pybricks.parameters import Port, Stop, Direction
from pybricks.pupdevices import Motor
from pybricks.tools import wait

# Initialize the EV3 Brick
ev3 = EV3Brick()

claw_motor = Motor(Port.A)
x_motor = Motor(Port.B)
y_motor = Motor(Port.C)
z_motor = Motor(Port.D)

claw_motor.control.limits(speed=60, acceleration=120)
x_motor.control.limits(speed=60, acceleration=120)
y_motor.control.limits(speed=60, acceleration=120)
z_motor.control.limits(speed=60, acceleration=120)
claw_switch = TouchSensor(Port.S1)

def go_to(x,y):
    if x==0 and y==0:
        x_motor.run_time(-30,1000)

def go_down():
    while not claw_switch.pressed():
        z_motor.run_time(-50,1000)


elbow_motor.run_time(-30, 1000)
elbow_motor.run(15)
while elbow_sensor.reflection() < 32:
    wait(10)
elbow_motor.reset_angle(0)
elbow_motor.hold()

# Initialize the base. First rotate it until the Touch Sensor
# in the base is pressed. Reset the motor angle to make this
# the zero point. Then hold the motor in place so it does not move.
base_motor.run(-60)
while not base_switch.pressed():
    wait(10)
base_motor.reset_angle(0)
base_motor.hold()

# Initialize the gripper. First rotate the motor until it stalls.
# Stalling means that it cannot move any further. This position
# corresponds to the closed position. Then rotate the motor
# by 90 degrees such that the gripper is open.
gripper_motor.run_until_stalled(200, then=Stop.COAST, duty_limit=50)
gripper_motor.reset_angle(0)
gripper_motor.run_target(200, -90)


def robot_pick(position):
    # This function makes the robot base rotate to the indicated
    # position. There it lowers the elbow, closes the gripper, and
    # raises the elbow to pick up the object.

    # Rotate to the pick-up position.
    base_motor.run_target(60, position)
    # Lower the arm.
    elbow_motor.run_target(60, -40)
    # Close the gripper to grab the wheel stack.
    gripper_motor.run_until_stalled(200, then=Stop.HOLD, duty_limit=50)
    # Raise the arm to lift the wheel stack.
    elbow_motor.run_target(60, 0)


def robot_release(position):
    # This function makes the robot base rotate to the indicated
    # position. There it lowers the elbow, opens the gripper to
    # release the object. Then it raises its arm again.

    # Rotate to the drop-off position.
    base_motor.run_target(60, position)
    # Lower the arm to put the wheel stack on the ground.
    elbow_motor.run_target(60, -40)
    # Open the gripper to release the wheel stack.
    gripper_motor.run_target(200, -90)
    # Raise the arm.
    elbow_motor.run_target(60, 0)


# Play three beeps to indicate that the initialization is complete.
for i in range(3):
    ev3.speaker.beep()
    wait(100)

# Define the three destinations for picking up and moving the wheel stacks.
LEFT = 160
MIDDLE = 100
RIGHT = 40

# This is the main part of the program. It is a loop that repeats endlessly.
#
# First, the robot moves the object on the left towards the middle.
# Second, the robot moves the object on the right towards the left.
# Finally, the robot moves the object that is now in the middle, to the right.
#
# Now we have a wheel stack on the left and on the right as before, but they
# have switched places. Then the loop repeats to do this over and over.
while True:
    # Move a wheel stack from the left to the middle.
    robot_pick(LEFT)
    robot_release(MIDDLE)

    # Move a wheel stack from the right to the left.
    robot_pick(RIGHT)
    robot_release(LEFT)

    # Move a wheel stack from the middle to the right.
    robot_pick(MIDDLE)
    robot_release(RIGHT)
