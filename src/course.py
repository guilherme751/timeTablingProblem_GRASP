class Course:
  def __init__(self, name, teacher, weekFrequency, minOfDays, numStudents, slots):
    self.name = name
    self.teacher = teacher
    self.weekFrequency = weekFrequency
    self.minOfDays = minOfDays
    self.numStudents = numStudents
    self.constraints = []
    self.countConflict = slots
    self.availableSlots = []


  def __str__(self):
    return f"{self.name} - {self.teacher} - {self.weekFrequency} - {self.minOfDays} - {self.numStudents}\n{self.constraints}\nCONFLITO:{self.countConflict}"