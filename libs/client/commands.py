import json
from libs.shared.playerConfigs import UP, DOWN, LEFT, RIGHT


def move(pDirection):
    message = {
        "move": 0
    }
    
    direction = pDirection.split(" ")[1].lower()

    # Example for an alternative way to do this
    # choices = {
    #     "up": UP,
    #     "down": DOWN,
    #     "left": LEFT,
    #     "right": RIGHT
    # }

    # if choices.get(direction) is not None:
    #     message["move"] = choices[direction]

    if direction == "up":
        message["move"] = UP
    elif direction == "down":
        message["move"] = DOWN
    elif direction == "left":
        message["move"] = LEFT
    elif direction == "right":
        message["move"] = RIGHT
    else:
        print("Invalid direction")
        return None

    return json.dumps(message)