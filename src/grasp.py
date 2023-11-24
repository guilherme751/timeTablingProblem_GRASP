from src.instance import *
from src.course import *
import copy
import random

def sameCurriculum(curricula, c1, c2):    
    for curric in curricula:
        cont = 0
        for c in curric[1]:
            if c == c1:
                cont += 1
            if c == c2:
                cont+=1
        if cont == 2:
            return True
    return False
    
        

# 5|RFc1|v + 2|RFc2|v + |RFc3|v + |RFc4|v 
def cost(table, course, r, p, d, rooms):
    days_cpy = copy.copy(course.daysAlocated)
    days_cpy.add(d)
    diff = course.minOfDays - len(days_cpy)
    if diff > 0:
        rf1 = diff
    else:
        rf1 = 0
        
    #rf2 calcular os cursos no mesmo curriculo para cada curso
    rf2 = 0
    diff = course.numStudents - rooms[r][1]
    
    if diff > 0:
        rf3 = diff
    else:
        rf3 = 0  
    
    rooms_cpy = copy.copy(course.roomsAlocated)
    rooms_cpy.add(r)
    if (len(rooms_cpy) == 1):
        rf4 = 0
    else:
        rf4 = len(rooms_cpy) - 1   
        
    return 5*rf1 + 2*rf2 + rf3 + rf4
   

def generateNotAlocatedList(courses):
    a = copy.copy(courses)
    for c in courses:
        for i in range(1, c.weekFrequency):
            a.append(c)
    return a

def updateUnavailable(table, c):
    for i, r in enumerate(table):
        for j, p in enumerate(r):
            if (i,j) in c.availableSlots:
                if isinstance(p, Course):                   
                    c.availableSlots.remove((i,j))
                #else:
                 #   teacher = c.teacher
                  #  for room in range(table.shape()[0]):
                   #     if isinstance(table[room][j], Course) and table[room][j].teacher == teacher and room != r:
                  #        c.availableSlots.remove((room,j))
    return c.availableSlots              
                    
def biuldInicialSolution(instance, alpha):
    listnotAlocated = generateNotAlocatedList(instance.courses)
    listnotAlocated.sort(key = lambda x: x.countConflict)
    while len(listnotAlocated) > 0:
        a = listnotAlocated[0]       
        h = updateUnavailable(instance.timeTable, a)
        allCosts = []
        for (r, p) in h:
            x = cost(instance.timeTable, a, r, p, p/instance.periods_per_day, instance.rooms)
        
            allCosts.append((r, p, x))
            
        if len(h) == 0:
            print("size of h is zero")
            return
            
        cmin = min(allCosts, key=lambda x: x[2])[2]
        cmax = max(allCosts, key=lambda x: x[2])[2]
        
        rcl = []
        for (r, p, x) in allCosts:
            print(x)
            if x >= cmin and x <= cmin + alpha*(cmax - cmin):               
                rcl.append((r, p , x))
                 
        (r, p, x) = random.choice(rcl)
        
        instance.timeTable[r][p] = a
        listnotAlocated.remove(a)
        
        #listnotAlocated.sort(key = lambda x: x.countConflict)
            
        
        
    
    

    