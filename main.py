from input.readInstance import * 
from src.course import *
from src.instance import *
from src.grasp import * 
from src.util import *
import time

def timeTablingInstance(maxItr, alpha, path, benchMark):
   


    #f_out = open("output/" + "out_" + path.split("/")[1], "w")



    instance = readInstance(path)
    #f_out.write(instance.name + "alpha = " + str(alpha) + "\n")




    startTime = time.time()
    best_f = np.inf 
    best_S = None
    for i in range(maxItr):
        
        startItr = time.time()  
        S = biuldInicialSolution(instance=instance, alpha=alpha, seed= 17, startItr= startItr, startTime=startTime)
        if (S == None):        
            maxItr += 1
            if time.time() - startTime > benchMark:            
                break
            instance.resetTable()
            resetCourses(instance.courses)        
            continue
        
    

        S, f_now = localSearch(S, f(S, instance), instance, startTime)
        if S == None:        
            break
        if i == 0:
            best_S = S
            best_f = f_now
        else:        
            if f_now < best_f:
                best_S = S
                best_f = f_now

        instance.resetTable()
        
        #f_out.write(str(best_f) + "\n") 
    
        if time.time() - startTime > benchMark:        
            break  
        if i != maxItr - 1:    
            resetCourses(instance.courses)

        
        
        


    return best_f
    # if best_S != None:
    #     print("\nviavel: ", feasibleSolution(instance, best_S))

    #print(time.time() - startTime)




    # outputBestSolution()


