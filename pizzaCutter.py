def equivalent(angle1: float) -> bool:
    if (angle1 >= 360 or angle1 <= -360):
        return mayor360(angle1)
    if (angle1 < 0):
        return angle1 + 360
    return angle1


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


def mayor360(angle: float):
    if (angle > 360):
        return angle % 360


def cutPizza(testAmount: int, pizzaAngles: list) -> list:
    resAngles: list = []
    result: list = []
    # resAngles
    for i in range(testAmount):
        for j in range(len(pizzaAngles[i])-1):
            if (len(resAngles) == 0):
                resAngles.append(pizzaAngles[i][j+1])
            else:
                for x in range(len(resAngles)):
                    if not equivalentAngles(pizzaAngles[i][j+1], resAngles[x]):
                        if pizzaAngles[i][j+1] not in resAngles:
                            resAngles.append(pizzaAngles[i][j+1])
        if (pizzaAngles[i][0] == 0):
            result.append(1)
        else:
            result.append(len(resAngles)*2)
        resAngles = []
    return result


def mayor360(angle: float):
    if (angle > 360):
        return angle % 360


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


# binary search to find the equivalent angle


def binarySearch(arr: list, l: int, r: int, x: float) -> int:
    if r >= l:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)
        else:
            return binarySearch(arr, mid + 1, r, x)
    else:
        return -1

# insertion sort


print(cutPizza(4, [[2, 0, 90], [3, 45, 180, 630], [3, 90, -90, 270], [0]]))
