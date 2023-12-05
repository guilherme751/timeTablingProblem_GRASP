def f(S, instance):
    rf1 = 0; rf2 = 0; rf3 = 0; rf4 = 0
    
    for c in instance.courses:
        diff = c.minOfDays - len(c.daysAlocated)        
        if diff > 0:
            rf1 += diff   
       
        rf4 += len(c.roomsAlocated) - 1     
 
    for r in range(len(S)):
        for p in range(len(S[r])):
            c = S[r][p]
            if c != None:
                diff = c.numStudents - instance.rooms[r][1]
                if diff > 0:
                    rf3 += diff                
                d = int(p/instance.periods_per_day)
                
                for curr in c.curriculum:
                    flag = 0
                    if int((p+1)/instance.periods_per_day) == d:
                        for i in range(len(S)):
                            h = S[i][p+1]
                            if h != None:
                                if curr in h.curriculum:
                                    flag = 1
                                    break
                        if flag == 1:
                            continue
                    if int((p-1)/instance.periods_per_day) == d:
                        for i in range(len(S)):
                            h = S[i][p-1]
                            if h != None:
                                if curr in h.curriculum:
                                    flag = 1
                                    break
                    if flag == 0:                        
                        rf2 += 1    
    #print(f"\nrf1 = {rf1}, rf2 = {rf2}, rf3 = {rf3}, rf4 = {rf4}")
    return 5*rf1 + 2*rf2 + rf3 + rf4

def print_table(S):
    
    for p in S:
        print()
        for r in p:
            if r != None:
                print(r.name, end=" ")
            else:
                print(None, end= " ")

def feasibleSolution(instance, S):
   
    for c in instance.courses:
        if (c.classesAlocated == c.weekFrequency) == False:  
            print("aqui")                               
            return False

    for p in range(instance.periods):
        teachers = set()
        curriculos = []
        cont = 0
        for r in range(instance.numRooms):
            if S[r][p] != None:
                if p in S[r][p].constraints:
                    return False
                cont += 1
                teachers.add(S[r][p].teacher)
                for cur in S[r][p].curriculum:
                    if cur in curriculos:                                                 
                        return False
                    curriculos.append(cur)
            if cont != len(teachers):                
                return False
    return True


def resetCourses(courses):
    for c in courses:
        c.resetCourse()


def outputBestSolution(instance, path, best_S):
    
    f = open("validate/" + path.split("/")[1].split(".")[0] + ".txt", "w")
    for p in range(instance.periods):
        for r in range(instance.numRooms):
            
            c = best_S[r][p]
            if c != None:
                f.write(c.name + " " + instance.rooms[r][0] + " " + str(int(p/instance.periods_per_day)) + " " + str(p%instance.periods_per_day) + "\n")
