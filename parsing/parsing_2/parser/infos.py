import re
import typing
from time import sleep
from parser.read_question import Question, Type

from game.turn import Turn
import game.characters as characters


def read_file(file, wait=True, readline=False) -> str:
    while wait:
        with open(file, 'r') as fhandler:
            if readline:
                data = fhandler.readline()
            else:
                data = fhandler.read()
        if data:
            wait = False
        sleep(0.1)
    return data


def ghost_color() -> str:
    data = read_file('1/infos.txt', readline=True)
    color = data.split()[-1]
    return color


def parse_events(events) -> tuple:
    tour = int(re.findall("Tour:([0-9]+),", events)[0])
    score = int(re.findall("Score:([0-9]+)/", events)[0])
    ombre = int(re.findall("Ombre:([0-9]),", events)[0])
    bloque = tuple(int(pos) for pos in re.findall(
        "Bloque:{([0-9]), ([0-9])}", events)[0])
    return tour, score, ombre, bloque


def current_turn_infos(role):
    data = read_file(f'{role}/infos.txt')
    turns = data.split('**************************\n')
    if role == 0:
        turns.pop(0)
    current_turn = turns[-1].split('\n')
    events = parse_events(current_turn[0])
    status = current_turn[1].split()
    subs_current = turns[-1].split('****\n')
    subs_current.pop(0)
    for i, sub in enumerate(subs_current):
        for line in sub.split('\n'):
            if line.startswith("NOUVEAU PLACEMENT : "):
                new_pos = line[20:]
                for i, suspect in enumerate(status):
                    if suspect.startswith(new_pos[:new_pos.find('-')]):
                        status[i] = new_pos
            # Add new features here for parsing each turn
    return events, status


def all_turns(role: int) -> list:
    all_turns_info = list()  # type: list
    subturn_counter = 0
    question = Question(None)
    data = read_file(f'{role}/infos.txt')
    turns = data.split('**************************\n')
    turns.pop(0)
    for big_turn in turns:
        turn_meta = big_turn.split('\n', 2)
        turn_data = Turn(*parse_events(turn_meta[0]))
        suspects = turn_meta[1].split()
        sub_turns = big_turn.split('****\n')
        sub_turns.pop(0)
        for sub_turn in sub_turns:
            turn_info = dict()  # type: typing.Dict[str, typing.Any]
            turn_info['tour'] = turn_data.tour
            turn_info['score'] = turn_data.score
            turn_info['ombre'] = turn_data.ombre
            turn_info['bloqué'] = turn_data.bloque
            turn_info['suspects'] = suspects.copy()
            turn_info['cri'] = 0  # Using int not bool for later learning
            turn_info['pouvoir action'] = None
            if subturn_counter > 3:
                all_turns_info[
                    subturn_counter - 4]['score fin'] = turn_data.score
            for line in sub_turn.split('\n'):
                if line.startswith("  Tour de l'"):
                    turn_info['joueur'] = 0
                if line.startswith("  Tour de le"):
                    turn_info['joueur'] = 1
                if line.startswith('QUESTION : '):
                    question.parse_question(line[11:])
                if line.startswith('REPONSE INTERPRETEE : '):
                    if question.type == Type.POSITION:
                        turn_info['déplacement'] = int(line[22:])
                    elif question.type == Type.DRAW:
                        turn_info['tuiles'] = question.args
                        turn_info['perso joué'] = line[22:]
                    elif question.type == Type.POWER:
                        turn_info['pouvoir utilisé'] = 0 if (
                            line[22:] == "False") else 1
                    else:
                        turn_info['pouvoir action'] = line[22:]
                if line.startswith('NOUVEAU PLACEMENT : '):
                    nouveau_placement = line[20:]
                    for i, suspect in enumerate(suspects):
                        if suspect.startswith(nouveau_placement[
                                :nouveau_placement.find('-')]):
                            suspects[i] = nouveau_placement
                if line.startswith('le fantome frappe'):
                    turn_info['cri'] = 1
                if line.startswith('Score final :'):
                    turn_info['score fin'] = int(line[14:])
                    for i in range(subturn_counter - 3, subturn_counter):
                        all_turns_info[i]['score fin'] = turn_info['score fin']
            all_turns_info.append(turn_info)
            if turn_info['cri']:
                for i in range(subturn_counter - 3, subturn_counter):
                    all_turns_info[i]['cri'] = 1
            subturn_counter += 1
            # fin parsing tour joueur
        # fin parsing tour global
    return all_turns_info


def game_over(role: int) -> bool:
    with open(f"./{role}/infos.txt", 'r') as fhandler:
        data = fhandler.read()
    if not data:
        return False
    last_line = data.split('\n')[-2]
    return True if last_line.startswith('Score final') else False
