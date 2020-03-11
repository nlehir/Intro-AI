import numpy as np

player_A_strategy = [2/4, 0/4, 0/4, 2/4]
player_A_actions = ["paper", "scissors", "rock", "well"]
player_B_strategy = [1/4, 1/4, 1/4, 1/4]
player_B_actions = ["paper", "scissors", "rock", "well"]

player_A_victory = [("paper", "rock"),
                    ("paper", "well"),
                    ("scissors", "paper"),
                    ("rock", "scissors"),
                    ("well", "rock"),
                    ("well", "scissors")]


def play(player_A_strategy, player_B_strategy):
    # draw action a
    action_a = np.random.choice(player_A_actions, p=player_A_strategy)
    action_b = np.random.choice(player_B_actions, p=player_B_strategy)
    print("\nA : "+action_a+", B : "+action_b)

    if action_a == action_b:
        result = 0
        print("draw")
    else:
        if (action_a, action_b) in player_A_victory:
            print("player A wins")
            result = 1
        else:
            result = -1
            print("player B wins")
    return result


number_of_games = 10000
played_games = 0
player_A_victories = 0
player_A_sum = 0
for game in range(number_of_games):
    result = play(player_A_strategy, player_B_strategy)
    played_games += 1
    player_A_sum += result
    if result == 1:
        player_A_victories += 1
    average = player_A_sum/played_games
    print(f"expectation after {played_games} games : {average}")
    print(f"percentage of victory {100*player_A_victories/played_games}")
