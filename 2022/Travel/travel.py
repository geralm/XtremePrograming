#totalStations = 3
#initial = [35, 230]
#stations = [[15, 240], [18, 225], [24, 240]]


def travel(totalStations: int, initial: list, stations: list):
    # llenar el tanque estacion inicial
    totalTank: int = initial[0]
    cost: int = totalTank * initial[1]
    actualTank: int = totalTank

    for i in range(totalStations-1):
        actualTank: int = actualTank - stations[i][0]
        if (actualTank - stations[i+1][0]) <= 0:
            cost += (totalTank-actualTank) * stations[i][1] + 500
            actualTank = totalTank
    return cost

#! parser


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


# ? RUN CODE
input_parser: list = parser()
T: int = get_number()
for t in range(T):
    input_parser = parser()
    totalStations: int = get_number()
    initial: list = [get_number(), get_number()]
    stations: list = []
    for i in range(totalStations):
        input_station: list = parser()
        stations.append([get_number(), get_number()])
    print(travel(totalStations, initial, stations))
