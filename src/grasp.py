from src.instance import *
from src.course import *

def isValid(table, c, r, p):
    if isinstance(table[r][p], Course):
        return False
    for constraint in c.constraints:
        if constraint == p:
            return False
        
    return True
    
    
def biuldInicialSolution(instance):
    instance.courses.sort(key = lambda x: x.countConflict)
    for c in instance.courses:
        for p in instance.timeTable:
            for r in p:
                if isValid(instance.timeTable, c, r, p):
                    instance.timeTable[r][p] = c