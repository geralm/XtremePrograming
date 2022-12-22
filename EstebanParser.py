# a simple parser for python. use get_number() and get_word() to read
import scipy
import numpy
#!
#! Read perform the input data
#!


def read():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield (number)
# ?---------------------------------
# ? Get the next word from the input
# ?---------------------------------


def getWord(inputData):
    return next(inputData)
# ?---------------------------------
# ? get the next number from the input
# ?---------------------------------


def getNum(inputData):
    data = getWord(inputData)
    try:
        return int(data)
    except ValueError:
        return float(data)
# ?---------------------------------------------------------------------
# ? Get the list of the data in the input and will have the len of amount
# ?---------------------------------


def getList(inputData, amount) -> list:
    return [getWord(inputData) for i in range(amount)]


"""
Copy this without comments


import scipy
import numpy
#input
def read():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield (number)
#get str
def getWord(inputData):
    return next(inputData)
#get num
def getNum(inputData):
    data = getWord(inputData)
    try:
        return int(data)
    except ValueError:
        return float(data)
#getList 
def getList(inputData, amount) -> list:
    return [getWord(inputData) for i in range(amount)]


"""
