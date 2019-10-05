import numpy as np
import random
import matplotlib.pyplot as plt

world = np.load("world.npy")
reward = np.load("reward.npy")
gamma = 0.8

# load environment data
value_function = np.zeros(world.shape)
known_reward = np.zeros(world.shape)
available_positions = np.where(world)


def pick_random_position(available_positions):
    """
    we can pick a ranom initial position
    """
    number_of_available_positions = available_positions[0].shape[0]
    random_index = random.randint(0, number_of_available_positions-1)
    i_coordinate = available_positions[0][random_index]
    j_coordinate = available_positions[1][random_index]
    return i_coordinate, j_coordinate


def generate_random_policy(world):
    """
    We generate a policy.
    So we must define one action per state
    """
    policy = {}
    for state_index in range(len(available_positions[0])):
        state = available_positions[0][state_index], available_positions[1][state_index]
        action = find_new_position(state, world)
        policy[state] = action
    return policy


def plot_position(agent_position, world, step):
    title = f"position of agent at step {step}"
    # we need to make a copy otherwise it will not work
    world_copy = np.copy(world)
    world_copy[agent_position[0], agent_position[1]] = 3
    plt.imshow(world_copy)
    plt.title(title)
    plt.savefig(f"images/value_iteration/agent_position_step_{step}.pdf")
    plt.close()


def plot_value_function(value_function, loop):
    title = f"value function at loop {loop}"
    plt.imshow(value_function)
    plt.colorbar()
    plt.title(title)
    plt.savefig(f"images/policy_iteration/value_function_loop_{loop}.pdf")
    plt.close()


def new_position_available(new_position, world):
    return world[new_position[0], new_position[1]]


def find_new_position(agent_position, world):
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
        if new_position_available(new_position, world):
            # go out of the loop
            moved_agent = True
    return new_position


def get_reward(agent_position):
    return reward[agent_position[0], agent_position[1]]


def update_value_function(value_function, known_reward):
    for i in range(1, world.shape[0]-1):
        for j in range(1, world.shape[0]-1):
            # check that the position is available
            if world[i, j]:
                next_state = tuple(policy[i, j])
                value_function[i, j] = known_reward[i, j] +\
                    gamma*value_function[next_state]
    return value_function


def move_agent(state):
    return policy(state)


def improve_policy(policy, value_function):
    for state in policy:
        # for readability
        i, j = state
        left = (i, j-1)
        top = (i-1, j)
        right = (i, j+1)
        bottom = (i+1, j)
        neighbor_values = {left: value_function[left],
                          top: value_function[top],
                          right: value_function[right],
                          bottom: value_function[bottom]}
        sorted_values = \
            sorted(neighbor_values,
                   key=lambda action: neighbor_values[action], reverse=True)

        if value_function[sorted_values[0]] > value_function[state]:
            print(f"update policy for state {state}")
            policy[state] = sorted_values[0]

    # return the new policy
    return policy


nb_policy_evaluation_steps = 15
nb_loops = 50

# initialize position
agent_position = pick_random_position(available_positions)

# initialize random policy
policy = generate_random_policy(world)


for loop in range(nb_loops):
    print(f"Loop {loop}")
    print("policy evaluation")
    for k in range(nb_policy_evaluation_steps):

        # move agent
        agent_position = policy[agent_position]
        # convert list to tuple
        agent_position = tuple(agent_position)

        # update reward
        obtained_reward = get_reward(agent_position)
        if obtained_reward > 0:
            print(f"found reward in position {agent_position}")
            known_reward[agent_position[0],
                         agent_position[1]] = obtained_reward

        # update value function
        value_function = update_value_function(value_function, known_reward)

    print("policy improvement")
    if loop % 10 == 0:
        policy = generate_random_policy(world)
    policy = improve_policy(policy, value_function)
    plot_value_function(value_function, loop)