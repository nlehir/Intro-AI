import os
import json
import time

LOG_DIR = './log'


class Logger():
    """
    Get data from the text files and output a JSON file
    at the end of game containing all the informations
    easy to read
    """
    def __init__(self, player_id: int):
        self._log = list()  # type: list
        self.id = player_id

    def log_turn(self, turn_data: dict):
        self._log.append(turn_data)

    def save(self):
        if not os.path.isdir(LOG_DIR):
            os.mkdir(LOG_DIR)
        filename = f'{LOG_DIR}/gamelog-{self.id}-{int(time.time())}.json'
        with open(filename, 'w') as fhandler:
            ret = json.dump(dict(turns=self._log), fhandler)
