from src.instance import *
from src.course import *


def updateUnavailable(table, c):
    for i, r in enumerate(table):
        for j, p in enumerate(r):
            if c.availableSlots.belongs((i,j)):
                if isinstance(p, Course):
                    c.availableSlots.remove((i,j))
                else:
                    teacher = c.teacher
                    for room in range(table.shape()[0]):
                        if isinstance(table[room][j], Course) and table[room][j].teacher == teacher and room != r:
                            c.availableSlots.remove((room,j))