class Course:
  def __init__(self, name = "vazio", teacher= "vazio", weekFrequency = 0, minOfDays = 0, numStudents = 0, slots = 0):
    self.name = name
    self.teacher = teacher
    self.weekFrequency = weekFrequency
    self.minOfDays = minOfDays
    self.numStudents = numStudents
    self.constraints = []
    self.slots = slots
    self.curriculum = set()
    self.countConflict = slots
    self.availableSlots_init = []
    self.availableSlots = []
    self.daysAlocated = set()  
    self.roomsAlocated = set() 
    self.classesAlocated = 0
    
  def resetCourse(self):
    self.countConflict = len(self.availableSlots_init)
    self.availableSlots = self.availableSlots_init.copy()
    self.daysAlocated = set()  
    self.roomsAlocated = set() 
    self.classesAlocated = 0
   

  def __str__(self):
    return f"{self.name} - {self.teacher} - {self.weekFrequency} - {self.minOfDays} - {self.numStudents}\n{self.constraints}\nCONFLITO:{self.countConflict}"