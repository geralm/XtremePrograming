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
