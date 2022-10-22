from itertools import product


# a simple parser for python. use get_number() and get_word() to read
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


n = get_number()
m = get_number()


def solve(nums):
    n = len(nums)
    is_palindrome = 0
    i = 0
    while i <= n // 2 and n != 0:
        if nums[i] != nums[n - i - 1]:
            is_palindrome = 1
            break
        i += 1
    if is_palindrome == 1:
        return False
    else:
        return True


def palindromeCutting(large, amax):
    amax = amax % 9982443539982443534
    amin = 1
    combinations = list(map(list, product(range(amin, amax+1), repeat=large)))
    count = 0

    for combination in combinations:

        for i in range(2, large+2, 2):
            flag = 1
            index = 0
            while index <= large-i:
                auxList = []
                for puntero in range(index, index+i):
                    auxList.append(combination[puntero])
                index += i
                if not solve(auxList):
                    flag = 0
                    break
            if flag:
                count += 1
                break
    return count


print(palindromeCutting(n, m))
