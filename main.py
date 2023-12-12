from input.readInstance import * 
from src.course import *
from src.instance import *
from src.grasp import * 
from src.util import *
import time
# f_out = open("output/" + "out_"  + str(j) +  path.split("/")[1], "w")
# f_out.write(instance.name + "alpha = " + str(alpha) + "\n")
# f_out.write(str(best_f) + "\n") 
# f_out.write(str(best_f) + "\n") 





def timeTablingInstance(maxItr, alpha, path, benchMark, j):
    instance = readInstance(path)
    startTime = time.time()
    best_f = np.inf 
    best_S = None
    flag = 0
    for i in range(maxItr):    
        # salva o tempo de início da iteração, a fase construtiva irá ser interrompida caso
        # extrapole esse tempo, retornando None 
        startItr = time.time() 
         
        S = biuldInicialSolution(instance=instance, alpha=alpha, startItr= startItr, 
                                 startTime=startTime, benchMark = benchMark)
        
        if (S == None):      #reinicia a instância e começa uma nova iteração
            maxItr += 1
            if time.time() - startTime > benchMark:            
                break
            instance.resetTable()
            resetCourses(instance.courses)  
            continue   
        if j == 0:
            if flag == 0:
                outputBestSolution(instance, path, S)           
                
                flag = 1
        
        # busca local. Retorna a melhor solução encontrada pela busca e seu custo
        S, f_now = localSearch(S, f(S, instance), instance, startTime, benchMark)
        if S == None:                 
            break        
        
        # atualiza a melhor solução e o melhor custo    
        if f_now < best_f:
            best_S = S
            best_f = f_now

        instance.resetTable()   # reinicia a instância     
    
        if time.time() - startTime > benchMark:        
            break         

    outputBestSolution(instance, path, best_S)
    return best_f, i + 1





    #print(time.time() - startTime)

    # if best_S != None:
    #     print("\nviavel: ", feasibleSolution(instance, best_S))














