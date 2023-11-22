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
        courses.append(Course(c[0], c[1], int(c[2]), int(c[3]), int(c[4]), numPeriods*numRooms))
        

    f.readline()
    f.readline()

    rooms = []

    for i in range(numRooms):
        r = f.readline().split(' ')
        name = r[0]
        capacity = int(r[1])
        rooms.append((name, capacity))


    f.readline()
    f.readline()

    curricula = []

    for i in range(numCurricula):
        c = f.readline().split(' ')
        name = c[0]
        size = int(c[1])
        courses_in_Curriculum = []
        for j in range(size):           
            courses_in_Curriculum.append(getCourse(courses, name=c[j+2]))

        curricula.append((name, courses_in_Curriculum))

    f.readline()
    f.readline()
    
    
    

    for i in range(numConstraints):
        c = f.readline().split(' ')
        period_unavailable = int(c[1]) * periodsPerDay + int(c[2])
        course = getCourse(courses, c[0])
        course.availableSlots = [(i, j) for i in range(numRooms) for j in range(numPeriods)]
        
        course.constraints.append(period_unavailable)
        course.countConflict -= numRooms
        slotsRemove = [(i, period_unavailable) for i in range(numRooms)]
        
        for s in slotsRemove:
            course.availableSlots.remove(s)
        

    f.close()

    return Instance(instName, courses, rooms, numDays, periodsPerDay, curricula)


