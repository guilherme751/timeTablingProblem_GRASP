from src.course import Course
from src.instance import Instance


def getCourse(courses, name):
  for c in courses:    
    if c.name == name:
      return c
  return None

def readInstance(path):

    f = open(path, "r")
    instName = f.readline().split(' ')[1]
    numCourses = int(f.readline().split(':')[1])
    numRooms = int(f.readline().split(':')[1])
    numDays = int(f.readline().split(':')[1])
    periodsPerDay = int(f.readline().split(':')[1])
    numCurricula = int(f.readline().split(':')[1])
    numConstraints = int(f.readline().split(':')[1])
    numPeriods = periodsPerDay * numDays

    f.readline()
    f.readline()
    courses = []
    for i in range(numCourses):
        c = f.readline().split(' ')
        course = Course(c[0], c[1], int(c[2]), int(c[3]), int(c[4]), numPeriods*numRooms)
        course.availableSlots_init = [(i, j) for i in range(numRooms) for j in range(numPeriods)]
        courses.append(course)
        

    f.readline()
    f.readline()

    rooms = []

    for _ in range(numRooms):
        r = f.readline().split(' ')
        name = r[0]
        capacity = int(r[1])
        rooms.append((name, capacity))


    f.readline()
    f.readline()

    curricula = []
    
    for _ in range(numCurricula):
        c = f.readline().split(' ')
        name = c[0]
        size = int(c[1])
        courses_in_Curriculum = []
        
        for j in range(size):     
            aux = getCourse(courses, name=c[j+2].strip()) 
            aux.curriculum.add(name)           
            courses_in_Curriculum.append(aux)

        curricula.append((name, courses_in_Curriculum))
    
    f.readline()
    f.readline()
    
    


    for _ in range(numConstraints):
        c = f.readline().split(' ')
        period_unavailable = int(c[1]) * periodsPerDay + int(c[2])
        course = getCourse(courses, c[0])
        
        course.constraints.append(period_unavailable)
        course.countConflict -= numRooms
        slotsRemove = [(i, period_unavailable) for i in range(numRooms)]
        
        for s in slotsRemove:
            course.availableSlots_init.remove(s)

    for c in courses:
       c.availableSlots = c.availableSlots_init.copy()   

    f.close()

    return Instance(instName, courses, rooms, numDays, periodsPerDay, curricula)


