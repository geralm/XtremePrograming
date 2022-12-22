"""             Unfair Game
Alex and Ben have a set of N integers, so they decided to play  a game. The two players take turns playing, Alex being the first to move. This game
is asymmetrical, as follows:
When it's Alex's turn, he chooses any non-empty subset of numbers and remove then from the set.
When it's Ben's turn, he chooses exacly one number and removes it from the set.

The Game ends when there are no numbers left in the set. Alex's goal is to maximize the sum of the numbers he chooses, while Ben just tries to
minimize the Alex's sum. Considering that both of them play optimally, you should compute the out come of the game.

Stardad input
The first line contains a single integer N, the size of the set
The second line contains the N values in the set

Standard output
The output should contain a sigle number representing Alex's sum if they both play optimally.
-------------------------------------------------------------------------------------------------------------------------------
? Dificultad: Easy
? Note:  
? Time: 1:36 min 
? Observations:
Perdí mucho tiempo en el parser, tuve que crear uno genérico para poder usarlo en los próximos ejercicios 
Funciona bien, especialmente es útil ya que ya no necesito la variable global para el viejo parser (confundía mucho), cada vez que necesito una entrada
solo llamo a la función y listo, no necesito crear una variable global para el parser, y no necesito crear una variable global para el input

Otra cosa que me fue muy útil fue crear un parser que me permitiera leer listas de números
Utilicé funciones por defecto como max y min, lo cuál fue muy útil, ya que no necesité crear funciones para eso
Debo mejorar mucho en el tiempo y tratar de entender el ejercicio primero para obtener los resultados deseados con cualquier entrada
Perdí tiempo creyendo que Ben elegía el mínimo siempre, lo cuál era incorrecto (Ben no resta los números de Alex, solo quita las opciones de Alex) por lo que
Ben debe elegir el máximo de los restantes para eliminarle las opciones a Alex
? Rubros para la iteración número 1 del ejercio
? _________________________________________________________________
? Rubro         |   Puntaje   |     pts.Obtenidos     
? -----------------------------------------------------------------
? Eficiencia    |    25       | 
? -----------------------------------------------------------------
? Tiempo        |    25       | 
? -----------------------------------------------------------------
? Legibilidad   |    25       |
? -----------------------------------------------------------------
? Correctitud   |    25       |
? -----------------------------------------------------------------
? Total         |    100      |
? Comentarios:
-------------------------------------------------------------------------------------------------------------------------------
"""

import scipy
import numpy


def read():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield (number)


def getWord(inputData):
    return next(inputData)


def getNum(inputData):
    data = getWord(inputData)
    try:
        return int(data)
    except ValueError:
        return float(data)


def getList(inputData, amount) -> list:
    return [getNum(inputData) for i in range(amount)]
#! End parser


def alexPlay() -> int:
    global dataSet
    print("Alex choosen: ", max(dataSet), end=" ")
    previusSum: int = 0
    maxSelection: int = max(dataSet)
    tempSum: int = maxSelection
    dataSet.remove(maxSelection)
    while tempSum > previusSum:
        previusSum = tempSum
        maxSelection: int = max(dataSet)
        tempSum += maxSelection
        print(maxSelection, end=" ")
        dataSet.remove(maxSelection)
    else:
        tempSum = previusSum
    return tempSum


def benPlay() -> int:
    global dataSet
    print("\nBen chooses: ", min(dataSet))
    res = min(dataSet)
    dataSet.remove(res)
    return res


def unfair_Game() -> int:
    global dataSet
    alexTurn: bool = True  # Alex turn
    alexSum: int = 0
    while dataSet != []:
        if alexTurn:
            alexSum += alexPlay()
        else:
            benPlay()
        alexTurn = not alexTurn  # invert boolean
    return alexSum


# set  is a reserved word and it means a collection
num: int = getNum(read())
dataSet: list = getList(read(), num)
print(unfair_Game())
