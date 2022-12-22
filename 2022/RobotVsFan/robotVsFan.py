

def nextMove(posRobot: list, move: str) -> list:
    if (move == ">"):

        return [posRobot[0], posRobot[1] + 1]
    elif (move == "<"):
        return [posRobot[0], posRobot[1] - 1]
    elif (move == "^"):
        return [posRobot[0]-1, posRobot[1]]
    elif (move == "v"):
        return [posRobot[0]+1, posRobot[1]]


def moveDust(posDust: int, dustMoves: int) -> int:
    if (posDust == len(dustMoves)-1):
        return 0
    else:
        return posDust + 1


def isNeverFind(time: int, tamm: int) -> bool:
    if (time >= tamm):
        return True
    else:
        return False


def catchDust(postRobot: list, posDust: list) -> bool:
    if (postRobot[0] == posDust[0] and postRobot[1] == posDust[1]):
        return True
    else:
        return False


def robotVsFan(square: list, dustMoves: list) -> int:
    posRobot: list = [0, 0]
    posDust: int = 0
    time = 0
    while not catchDust(posRobot, dustMoves[posDust]):
        elval: str = square[posRobot[0]][posRobot[1]]
        posRobot = nextMove(posRobot, elval)
        posDust = moveDust(posDust, dustMoves)
        time += 1

    return time


def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield (number)


def get_word():
    global input_parser
    return next(input_parser)


def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)


# numpy and scipy are available for use
input_parser = parser()
# Read the number of testcases
T = get_number()

# Process each test case
for t in range(T):
    input_parser = parser()
    mlen = get_number()
    square = []
    for n in range(mlen):
        input_parser = parser()
        square.append(get_word())
    input_parser = parser()
    dustMoves = []
    for n in range(get_number()):
        input_parser = parser()
        dustMoves.append([get_number(), get_number()])
    time = robotVsFan(square, dustMoves)
    if (time == -1):
        print("never")
    else:
        print(time)
