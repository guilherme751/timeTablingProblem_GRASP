from input.readInstance import * 
from src.course import *
from src.instance import *
from src.grasp import * 
from src.util import *

#ENTRADAS:
maxItr = 1
alpha = 0.1
path = "data/comp03.ctt"


f_out = open("output/" + "out_" + path.split("/")[1], "w")



instance = readInstance(path)
f_out.write(instance.name)






for i in range(maxItr):
    S = biuldInicialSolution(instance=instance, alpha=alpha, seed= 17)
    if (S == None):
        maxItr += 1
        instance.resetTable()
        resetCourses(instance.courses)
        continue
    

    S, f_now = localSearch(S, f(S, instance), instance)

    if i == 0:
        best_S = S
        best_f = f_now
    else:        
        if f_now < best_f:
            best_S = S
            best_f = f_now

    instance.resetTable()
        
    f_out.write(str(best_f) + "\n") 
   
    if i != maxItr - 1:    
        resetCourses(instance.courses)


print("MELHOR CUSTO: ", best_f)
print("\nviavel: ", feasibleSolution(instance, best_S))







