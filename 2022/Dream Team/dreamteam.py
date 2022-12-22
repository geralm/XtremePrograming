def getTeamScore(team: list) -> int:
    scores = 0
    for score in team:
        scores += score[1]
    return scores


def backtracking(pos1: list, pos2: list, pos3: list, pos4: list, pos5: list, budget: int) -> list:
    best_team = []
    best_score = 0
    for player1 in pos1:
        for player2 in pos2:
            for player3 in pos3:
                for player4 in pos4:
                    for player5 in pos5:
                        team = [player1, player2, player3, player4, player5]
                        score = getTeamScore(team)
                        if score > best_score and score < budget:
                            best_score = score
                            best_team = team
    for i in range(5):
        print(best_team[i][0])
    return best_team


def dynamicSED(a, b, lenA, lenB):
    tabla = [[0 for x in range(lenB + 1)] for x in range(lenA + 1)]

# caso 1.a, si el string a esta vacio, la respuesta es j
    for j in range(lenB+1):
        tabla[0][j] = j
# caso 1.b, si el string b esta vacio, la respuesta es i
    for i in range(lenA+1):
        tabla[i][0] = i

    for i in range(1, lenA + 1):
        for j in range(1, lenB + 1):
            # caso 2, si las letras son iguales, no se hace nada,
            # #el numero de operaciones es igual al anterior
            if a[i-1] == b[j-1]:
                tabla[i][j] = tabla[i-1][j-1]

            else:
                # caso 3, se comparan las 3 operaciones
             # y se mantiene la mejor
                tabla[i][j] = 1 + min(tabla[i][j-1],  # ins
                                      tabla[i-1][j], tabla[i-1][j-1])  # sust
    return tabla[lenA][lenB]  # el resultado esta en la ultima celd


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


def callBT() -> None:
    budget = get_number()
    pos1: list = []
    pos2: list = []
    pos3: list = []
    pos4: list = []
    pos5: list = []
    for i in range(5):
        posAct = get_number()
        for j in range(posAct):
            player: str = get_word()
            salary: int = get_number()
            if i == 0:
                pos1.append([player, salary])
            elif i == 1:
                pos2.append([player, salary])
            elif i == 2:
                pos3.append([player, salary])
            elif i == 3:
                pos4.append([player, salary])
            elif i == 4:
                pos5.append([player, salary])
    return backtracking(pos1, pos2, pos3, pos4, pos5, budget)


callBT()
