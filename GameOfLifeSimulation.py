# Game Of Life container

import consts as Consts
import Field
import array
import random
import math

DEBUG = True


class GameOfLifeSimulation(object):

    def __init__(self):
        self.field = Field.Field("RANDOM")
        self.nextField = Field.Field("EMPTY")
        self.generation = 0

    def __del__(self):
        pass

    def update(self):
        if self.generation >= Consts.BOA_MAX_GENERATION:
            return False
        self.generation += 1
        if DEBUG:
            print("generation N°", self.generation)
        for y in range(self.field.height):
            for x in range(self.field.width):
                self.nextField.setFrame(x, y, self.field.getFrame(x, y))
                if self.getNeighboursCount(x, y) == 3:
                    self.nextField.setFrame(x, y, Consts.BOA_ALIVE_REPR)
                elif self.field.getFrame(x, y) == Consts.BOA_ALIVE_REPR and self.getNeighboursCount(x, y) == 2:
                    pass
                else:
                    self.nextField.setFrame(x, y, Consts.BOA_DEAD_REPR)
        self.field.copy(self.nextField)
        self.nextField.resetField("EMPTY")
        return True

    def getNeighboursCount(self, x, y):
        degree = 0
        neighboursCount = 0
        while degree < 360:
            adjustX = round(math.cos(math.radians(degree)))
            adjustY = round(math.sin(math.radians(degree)))
            if (x + adjustX >= 0 and x + adjustX < self.field.width
                and y + adjustY >= 0 and y + adjustY < self.field.height):
                if self.field.getFrame(x + adjustX, y + adjustY) == Consts.BOA_ALIVE_REPR:
                    neighboursCount += 1
            degree += 45
        return neighboursCount
