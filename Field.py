# Field container

import consts as Consts
import array
import random

DEBUG = True


class Field(object):

    def __init__(self, option):
        self.field = array.array(Consts.BOA_FIELD_TYPECODE)
        self.height = Consts.BOA_HEIGHT
        self.width = Consts.BOA_HEIGHT
        self.FUNCTIONS_BY_OPTION = {"RANDOM": [lambda: self.__AddRandomCell(), lambda x, y: self.__SetRandomCell(x, y)],
                                    "EMPTY": [lambda: self.__AddDeadCell(), lambda x, y: self.__SetDeadCell(x, y)]}
        self.__InitField(option)

    def __del__(self):
        del self.field

    def __AddRandomCell(self):
        if random.random() < Consts.DISTRIBUTION:
            self.__AddDeadCell()
        else:
            self.__AddAliveCell()

    def __AddDeadCell(self):
        self.field.append(Consts.BOA_DEAD_REPR)

    def __AddAliveCell(self):
        self.field.append(Consts.BOA_ALIVE_REPR)

    def __InitField(self, option):
        for y in range(self.height):
            for x in range(self.width):
                self.FUNCTIONS_BY_OPTION[option][0]()

    def __SetRandomCell(self, x, y):
        if random.random() < Consts.DISTRIBUTION:
            self.__SetDeadCell(x, y)
        else:
            self.__SetAliveCell(x, y)

    def __SetDeadCell(self, x, y):
        self.setFrame(x, y, Consts.BOA_DEAD_REPR)

    def __SetAliveCell(self, x, y):
        self.setFrame(x, y, Consts.BOA_ALIVE_REPR)

    def resetField(self, option):
        for y in range(self.height):
            for x in range(self.width):
                self.FUNCTIONS_BY_OPTION[option][1](x, y)

    def getFrame(self, x, y):
        return self.field[self.__TransformCoords(x, y)]

    def setFrame(self, x, y, value):
        self.field[self.__TransformCoords(x, y)] = value

    def __TransformCoords(self, x, y):
        return (y * self.width) + x

    def copy(self, other):
        for y in range(self.height):
            for x in range(self.width):
                self.setFrame(x, y, other.getFrame(x, y))

    def dump(self):
        for y in range(self.height):
            print(self.field[(y * self.width):(y * self.width) + self.width])
