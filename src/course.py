class Course:
  def __init__(self, name = "vazio", teacher= "vazio", weekFrequency = 0, minOfDays = 0, numStudents = 0, slots = 0):
    self.name = name
    self.teacher = teacher
    self.weekFrequency = weekFrequency
    self.minOfDays = minOfDays
    self.numStudents = numStudents
    self.constraints = []
    self.countConflict = slots
    self.availableSlots = []
    self.daysAlocated = set()  
    self.roomsAlocated = set() 
    


  def __str__(self):
    return f"{self.name} - {self.teacher} - {self.weekFrequency} - {self.minOfDays} - {self.numStudents}\n{self.constraints}\nCONFLITO:{self.countConflict}"