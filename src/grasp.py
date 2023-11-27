from src.instance import *
from src.course import *
import copy
import random
from src.util import print_table

def sameCurriculum(c1, c2):   
  
    x = True if len(set.intersection(c1.curriculum, c2.curriculum)) > 0 else False
    return x
    
        

# 5|RFc1|v + 2|RFc2|v + |RFc3|v + |RFc4|v 
def cost(instance, course, r, p, d, rooms):
    days_cpy = copy.copy(course.daysAlocated)
    days_cpy.add(d)
    diff = course.minOfDays - len(days_cpy)
    if diff > 0:
        rf1 = diff
    else:
        rf1 = 0

    rf2 = 0  
    for  curr in course.curriculum:
        flag = 0
        if int((p+1)/instance.periods_per_day) == d:
            for i in range(len(rooms)):
                h = instance.timeTable[i][p+1]
                if h != None:
                    if curr in h.curriculum:
                        flag = 1
                        break
            if flag == 1:
                continue
            if int((p-1)/instance.periods_per_day) == d:
                for i in range(len(rooms)):
                    h = instance.timeTable[i][p-1]
                    if h != None:
                        if curr in h.curriculum:
                            flag = 1
                            break
            if flag == 0:
                rf2 += 1    
              

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
                
                

def updateUnavailable(a, r, p, table, listNotAlocated):
    
        
    for c in listNotAlocated:         
        if (r, p) in c.availableSlots:               
            c.availableSlots.remove((r, p))
            c.countConflict -= 1
        for room in range(len(table)):
            if (room, p) in c.availableSlots:
                if c.teacher == a.teacher or sameCurriculum(a, c):                    
                    c.availableSlots.remove((room, p))
                    c.countConflict -= 1  

def explodeSolution(a, instance, listnotAlocated):
    
    #primeiro passo: escolher um horário viável para colocar a
    slots = []
   
    
    for p in range(instance.periods):
        if p in a.constraints:
            continue
        
        for r in range(instance.numRooms):
            if instance.timeTable[r][p] == None:
                continue
            flag = 0
            for room in range(instance.numRooms):
                if room != r:
                    c = instance.timeTable[room][p]            
                    if c != None:                               
                        if c.teacher == a.teacher or sameCurriculum(a, c):                            
                            flag = 1
                            break
                if instance.timeTable[room][p] == a:
                    flag = 1
            if flag == 0:
                slots.append((r, p))

    if len(slots) == 0:
        print("a")
        return []


    slotChose = random.choice(slots)
    
    
    
    aux = instance.timeTable[slotChose[0]][slotChose[1]]
    
    aux.classesAlocated -= 1
    instance.timeTable[slotChose[0]][slotChose[1]] = None

    flag = 0
    for p in range(slotChose[1] - slotChose[1]%instance.periods_per_day, slotChose[1] - slotChose[1]%instance.periods_per_day + instance.periods_per_day):
        for room in range(instance.numRooms):
            if instance.timeTable[room][p] == aux:
                flag = 1
                break
    if flag == 0:
        aux.daysAlocated.remove(int(slotChose[1]/instance.periods_per_day))
    # for p in range()
    flag = 0
    for p in range(instance.periods):
        if instance.timeTable[slotChose[0]][p] == aux:
            flag = 1
            break
    if flag == 0:
        aux.roomsAlocated.remove(slotChose[0])

    listnotAlocated.append(aux)
    

    for c in listnotAlocated:
        if c == aux:
            continue
        if slotChose[1] in c.constraints:
            continue
        flag = 0
        for room in range(instance.numRooms):
            h = instance.timeTable[room][slotChose[1]]
            if h != None:
                if h.teacher == c.teacher or sameCurriculum(c, h):
                    flag = 1
                    break

        if flag == 0:
            for room in range(instance.numRooms):
                h = instance.timeTable[room][slotChose[1]]
                if h == None:
                    if (room, slotChose[1]) not in c.availableSlots:
                        c.availableSlots.append((room, slotChose[1]))
            
    return a.availableSlots


 




                    
def biuldInicialSolution(instance, alpha, seed):
   
    #random.seed(seed)
    
    listnotAlocated = generateNotAlocatedList(instance.courses)
    listnotAlocated.sort(key = lambda x: x.countConflict)


   
    while len(listnotAlocated) > 0:
        a = listnotAlocated[0] 

        
        
        #print(a.name)     
        h = a.availableSlots
       
        
        if len(h) == 0:
            #print_table(instance.timeTable)
            h = explodeSolution(a, instance, listnotAlocated) 
            if len(h) == 0:
                return None
                

       
            
        allCosts = []
        for (r, p) in h:
            x = cost(instance, a, r, p, p/instance.periods_per_day, instance.rooms)

            allCosts.append((r, p, x))
           
            
        cmin = min(allCosts, key=lambda x: x[2])[2]
        cmax = max(allCosts, key=lambda x: x[2])[2]
       
        rcl = []
        for (r, p, x) in allCosts:            
            if x >= cmin and x <= cmin + alpha*(cmax - cmin):               
                rcl.append((r, p , x))
        (r, p, x) = random.choice(rcl)
        #print((r,p,x)) 
             
        instance.timeTable[r][p] = a
        a.daysAlocated.add(int(p/instance.periods_per_day))
        a.roomsAlocated.add(r)
        a.classesAlocated += 1
        listnotAlocated.remove(a)
        

        updateUnavailable(a, r, p, instance.timeTable, instance.courses)

       
    return instance.timeTable
            
        
        
    
    

    