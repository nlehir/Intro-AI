"""
    Perform the value iteration algorithm
    in a simple 2D world.
"""

import numpy as np
import random
import matplotlib.pyplot as plt

# load the environment
world = np.load("world.npy")
reward = np.load("reward.npy")
# discount factor
gamma = 0.8

value_function = np.zeros(world.shape)
# the reward from the point of view of the agent
known_reward = np.zeros(world.shape)
available_positions = np.where(world)


def pick_random_position(available_positions):
    """
        Initialize randomly the position of the agent.
    """
    number_of_available_positions = available_positions[0].shape[0]
    random_index = random.randint(0, number_of_available_positions-1)
    i_coordinate = available_positions[0][random_index]
    j_coordinate = available_positions[1][random_index]
    return i_coordinate, j_coordinate


def plot_position(agent_position, world, step):
    title = f"position of agent at step {step}"
    # we need to make a copy otherwise it will not work
    world_copy = np.copy(world)
    world_copy[agent_position[0], agent_position[1]] = 3
    plt.imshow(world_copy)
    plt.title(title)
    plt.savefig(f"images/value_iteration/agent_position_step_{step}.pdf")
    plt.close()


def plot_value_function(value_function, step):
    title = "value function at step {}".format(step)
    plt.imshow(value_function)
    plt.colorbar()
    plt.title(title)
    plt.savefig(f"images/value_iteration/value_function_step_{step}.pdf")
    plt.close()


def new_position_is_available(new_position, world):
    return world[new_position[0], new_position[1]]


def move_agent(agent_position, world):
    """
        When exploring the world
        in order to maybe find rewards,
        the agent moves randomly.
    """
    # boolean representing if we moved the agent
    moved_agent = False
    # try to move the agent until it moves
    while not moved_agent:
        direction = random.randint(0, 3)
        if direction == 0:
            # try to go left
            new_position = [agent_position[0], agent_position[1]-1]
        elif direction == 1:
            # try to go top
            new_position = [agent_position[0]-1, agent_position[1]]
        elif direction == 2:
            # try to go right
            new_position = [agent_position[0], agent_position[1]+1]
        elif direction == 3:
            # try to go bottom
            new_position = [agent_position[0]+1, agent_position[1]]
        # check if position is available
        if new_position_is_available(new_position, world):
            # go out of the loop
            moved_agent = True
    return new_position


def get_reward(agent_position):
    return reward[agent_position[0], agent_position[1]]


def update_value_function(value_function, known_reward):
    """
        When the agent learns about rewards
        in the world, it updates the value function
        of each known state.
    """
    for i in range(1, world.shape[0]-1):
        for j in range(1, world.shape[0]-1):
            # check that the position is available
            if world[i, j]:
                value_function[i, j] = known_reward[i, j] +\
                    max(gamma*value_function[i-1, j],
                        gamma*value_function[i, j-1],
                        gamma*value_function[i, j+1],
                        gamma*value_function[i+1, j])
    return value_function


"""
    Value Iteration algorithm.
"""
agent_position = pick_random_position(available_positions)
for step in range(300):
    print(f"step {step} : agent position {agent_position}")
    if step % 20 == 0:
        plot_position(agent_position, world, step)
    # move the agent randomly
    agent_position = move_agent(agent_position, world)
    obtained_reward = get_reward(agent_position)
    if obtained_reward > 0:
        print(f"found reward in position {agent_position}")
        known_reward[agent_position[0], agent_position[1]] = obtained_reward
    value_function = update_value_function(value_function, known_reward)
    if step % 5 == 0:
        plot_value_function(value_function, step)
    if step % 15 == 0:
        print("re initialize agent position")
        agent_position = pick_random_position(available_positions)


# save the value function to a file
np.save("value_function.npy", value_function)
