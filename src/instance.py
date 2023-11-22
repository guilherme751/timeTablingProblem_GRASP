import numpy as np
class Instance:
  def __init__(self, name, courses, rooms, days, periods_per_day, curricula):
    self.name = name
    self.courses = courses
    self.days = days
    self.rooms = rooms
    self.periods_per_day = periods_per_day
    self.periods = days * periods_per_day
    self.curricula = curricula
    self.timeTable = np.empty((len(rooms), self.periods))

    def __str__(self):
      return f"{self.name}\n - {self.courses}\n - {self.periods}\n - {self.curricula}\n - {self.rooms}"