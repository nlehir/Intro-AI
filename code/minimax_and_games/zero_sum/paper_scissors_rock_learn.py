import numpy as np
import matplotlib.pyplot as plt

player_A_strategy = [1/3, 1/3, 1/3]
player_A_actions = ["paper", "scissors", "rock"]
player_B_strategy = [5/10, 5/10, 0/10]
# player_B_strategy = [9/10, 1/10, 0/10]
player_B_actions = ["paper", "scissors", "rock"]

player_A_victory = [("paper", "rock"),
                    ("scissors", "paper"),
                    ("rock", "scissors")]


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
    return result, action_a, action_b


beaters = {"paper": "scissors",
           "scissors": "rock",
           "rock": "paper"}

number_of_games = 7000
average = 0
played_games = 0
player_A_sum = 0
player_A_victories = 0
# learn the strategy of player B
player_B_counter = [0, 0, 0]
percentages = []
for game in range(number_of_games):
    # play a game
    result, action_a, action_b = play(player_A_strategy, player_B_strategy)
    # count the actions played by B
    player_B_counter[player_B_actions.index(action_b)] += 1
    # compute the probabilities played by B
    player_B_learned = [x/sum(player_B_counter) for x in player_B_counter]

    # update our strategy
    most_probable_action_B_index = player_B_learned.index(
        max(player_B_learned))
    least_probable_action_B_index = player_B_learned.index(
        min(player_B_learned))
    most_probable_action_B = player_B_actions[most_probable_action_B_index]
    least_probable_action_B = player_B_actions[least_probable_action_B_index]

    # update
    remaining_actions = [0, 1, 2]

    # most relevant action for A
    A_best_action_index = player_A_actions.index(
        beaters[most_probable_action_B])
    remaining_actions.remove(A_best_action_index)

    # least relevant action for A
    A_worst_action_index = player_A_actions.index(
        beaters[least_probable_action_B])
    remaining_actions.remove(A_worst_action_index)

    # there is still one action
    A_intermediate_action_index = remaining_actions.pop()

    # define our strategy
    player_A_strategy[A_best_action_index] = max(player_B_learned)
    player_A_strategy[A_worst_action_index] = min(player_B_learned)
    player_A_strategy[A_intermediate_action_index] = 1 - \
        max(player_B_learned)-min(player_B_learned)

    # print strategies
    print(player_B_learned)
    print(player_A_strategy)

    # evaluate performance
    result, _, _ = play(player_A_strategy, player_B_strategy)
    played_games += 1
    player_A_sum += result
    if result == 1:
        player_A_victories += 1
    average = player_A_sum/played_games
    percentage = 100*player_A_victories/played_games
    print(f"expectation after {played_games} games : {average}")
    print(f"percentage of victory {percentage}")
    percentages.append(percentage)

plt.plot(range(number_of_games), percentages)
plt.title(f"strategy of B {player_B_strategy}")
plt.savefig(f"percentage of victory_{player_B_strategy}.pdf")
plt.close()
