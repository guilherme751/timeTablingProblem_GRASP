from input.readInstance import * 
from src.course import *
from src.instance import *
from src.grasp import * 


def printTimeTable():
    for p in instance.timeTable:
        print()
        for r in p:
            if r != None:
                print(r.name, end=" ")
            else:
                print(None, end= " ")

instance = readInstance('data/toy.ctt')

biuldInicialSolution(instance=instance, alpha=0.2)



printTimeTable()
