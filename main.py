from input.readInstance import * 
from src.course import *
from src.instance import *
from src.grasp import * 


instance = readInstance('data/toy.ctt')

#biuldInicialSolution(instance=instance)

for c in instance.curricula:
    for name in c[1]:
        print(name.name)

