from input.readInstance import * 
from src.course import *
from src.instance import *
from src.grasp import * 
from src.util import *


maxItr = 10


instance = readInstance('data/comp02.ctt')

for i in range(maxItr):
    S = biuldInicialSolution(instance=instance, alpha=0.2, seed= 17)
    if (S == None):
        maxItr += 1
        instance.resetTable()
        resetCourses(instance.courses)
        continue
    if i == 0:
        best_S = S
        best_f = f(S, instance)
    else:
        f_now = f(S, instance)
        if f_now < best_f:
            best_S = S
            best_f = f_now
    instance.resetTable()
        
        
    print("SOLUCAO VALIDA: ", feasibleSolution(instance, S))
        
    resetCourses(instance.courses)


print("MELHOR CUSTO: ", best_f)







