"""
Note: Pour utiliser le super parser correctement, lancer le script après
chaque partie.
"""

from parser.logger import Logger
from parser.infos import all_turns


def main():
    # for player_id, filepath in ((0, '0/infos.txt'), (1, ('1/infos.txt'))):
    for player_id, filepath in ((0, '0/infos.txt'), ):
        logger = Logger(player_id)
        turns_data = all_turns(player_id)
        for data in turns_data:
            logger.log_turn(data)
        logger.save()


if __name__ == "__main__":
    main()
