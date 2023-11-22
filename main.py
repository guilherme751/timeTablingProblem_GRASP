from input.readInstance import * 
from src.course import *
from src.instance import *
from src.grasp import * 


instance = readInstance('data/toy.ctt')

#biuldInicialSolution(instance=instance)

for i, r in enumerate(instance.timeTable):
    print(i)

