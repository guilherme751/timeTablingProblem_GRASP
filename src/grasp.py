from src.instance import *
from src.course import *
import copy

# 5|RFc1|v + 2|RFc2|v + |RFc3|v + |RFc4|v 
def custo(table, course, r, p, d, rooms):
    days_cpy = copy.copy(course.daysAlocated)
    days_cpy.add(d)
    diff = course.minOfDays - len(course.days_cpy)
    if diff > 0:
        rf1 = diff
    else:
        rf1 = 0
        
    #rf2 calcular os cursos no mesmo curriculo para cada curso
    
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
                    
def biuldInicialSolution(instance):
    listnotAlocated = generateNotAlocatedList(instance.courses)
    listnotAlocated.sort(key = lambda x: x.countConflict)
    while len(listnotAlocated) > 0:
        a = listnotAlocated[0]       
        h = updateUnavailable(instance.timeTable, a)
        print(a.name, h)
        if len(h) == 0:
            print("size of h is zero")
            return
        
        listnotAlocated.remove(a)
    
    

    