import bisect


def binary_search(arr, low, high, x):

    # Check base case
    if high >= low:

        mid = (high + low) // 2

        # If element is present at the middle itself
        if arr[mid] == x or equivalentAngles(arr[mid], x):
            return mid

        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)

        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)

    else:
        # Element is not present in the array
        return -1


def equivalentAngles(angle1: float, angle2: float) -> bool:
    if (angle1 > 360 or angle1 < -360):
        angle1 = mayor360(angle1)
    if (angle2 > 360 or angle2 < -360):
        angle2 = mayor360(angle2)

    if (angle1 == angle2):
        return True

    if (angle1 + 180) == angle2 or (angle2 + 180) == angle1 or (angle1 - 180) == angle2 or (angle2 - 180) == angle1:
        return True
    else:
        return False


def cutPizza(pizzaAngles: list) -> list:
    resAngles: list = []
    for j in range(len(pizzaAngles)-1):
        if (len(resAngles) == 0):
            resAngles.append(equivalent(pizzaAngles[j+1]))
        else:
            if binary_search(resAngles, 0, len(resAngles)-1, equivalent(pizzaAngles[j+1])) == -1:
                bisect.insort(resAngles, equivalent(pizzaAngles[j+1]))
    if len(resAngles) == 0:
        return 1
    return len(resAngles)*2


def mayor360(angle: float):
    return angle % 360


def equivalentAngles(angle1: float, angle2: float) -> bool:
    if (angle1 == angle2):
        return True

    if (angle1 + 180) == angle2 or (angle2 + 180) == angle1 or (angle1 - 180) == angle2 or (angle2 - 180) == angle1:
        return True
    else:
        return False


def equivalent(angle1: float) -> bool:
    if (angle1 >= 360 or angle1 <= -360):
        return mayor360(angle1)
    if (angle1 < 0):
        return angle1 + 360
    return angle1


def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield (number)


input_parser = parser()


def get_word():
    global input_parser
    return next(input_parser)


def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)


pizzaAngles: list = []
T = get_number()

# Process each test case
for t in range(T):
    N = get_number()

    answer = 0
    # Read each offset
    # TODO: You will need to figure out how to
    # process the offset and change the variable answer
    subPizzaArray: list = []
    subPizzaArray.append(N)
    for n in range(N):
        D = get_number()
        subPizzaArray.append(D)
    # Output your answer
    pizzaAngles.append(subPizzaArray)
for i in pizzaAngles:
    print(cutPizza(i))
