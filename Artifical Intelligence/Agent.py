# The basic idea of an AI in an agent that takes an percept and reacts to it
# Note this code below shouldn't work. Its just to understand the concept
from sensor import advance_camera

running = True
storage = []
positive = 0
negative = 0

main_cam = advance_camera(0, None)


def move_robot(direction):
    moves = {"left": -1, "right": +1, "up": ++1, "down": --1}
    return moves[direction]


def get_distance(start, end):
    return end - start


def critic(old, new):
    if old > new:
        positive += 1
    else:
        negative += 1


def at_goal(coordinate):
    return coordinate == "goal" or negative == 0

# Main Running loop
