import os
from time import sleep
from enum import Enum


class Type(Enum):
    POWER = 0
    DRAW = 1
    POSITION = 2
    PURPLE_POWER = 3
    GRAY_POWER = 4
    BLUE_POWER = 5
    BLUE_POWER_EXIT = 6


class Question:
    def __init__(self, file):
        self.file = file
        self.type = None
        self.args = None
        self.isEmpty = False

    def parse_question(self, data: str):
        qdata = data.split()
        if qdata[0] == 'Voulez-vous':
            print('0')
            self.type = Type.POWER
            self.args = ['0', '1']
        elif qdata[0] == 'positions':
            self.type = Type.POSITION
            self.args = data[data.find('{')+1:data.find('}')].split(', ')
        elif qdata[0] == 'Tuiles':
            self.type = Type.DRAW
            self.args = data[data.find('[')+1:data.find(']')].split(', ')
        elif qdata[0] == 'Quelle' and qdata[1] == 'salle' and (
             qdata[2] == 'bloquer'):
            self.type = Type.BLUE_POWER
            self.args = data[data.find('{')+1:data.find('}')].split(', ')
        elif qdata[0] == 'Quelle' and qdata[1] == 'sortie':
            self.type = Type.BLUE_POWER_EXIT
        elif qdata[0] == 'Quelle' and qdata[1] == 'salle' and (
             qdata[2] == 'obscurcir'):
            self.type = Type.GRAY_POWER
            self.args = [str(i) for i in range(0, 8)]
        else:
            self.type = Type.PURPLE_POWER

    def read(self, wait=True, timeout=1):
        sleep_interval = 0.05
        elapsed = 0
        while os.stat(self.file).st_size == 0:
            if sleep_interval * elapsed >= timeout or not wait:
                return
            sleep(sleep_interval)
            elapsed += 1
        with open(self.file, 'r') as filehandler:
            data = filehandler.read()
        self.parse_question(data)
        with open(self.file, 'w') as filehandler:
            filehandler.seek(0)
            filehandler.truncate()


if __name__ == "__main__":
    question = Question('../0/questions.txt')
    question.read()
    print(question.type)
    print(question.args)
    print(question.isEmpty)
