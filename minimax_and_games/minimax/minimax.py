"""
Build the tree representing the game
"""
number_of_nodes = 15
all_nodes = [str(node) for node in range(number_of_nodes)]
maximiser_nodes = ["0", "3", "4", "5", "6"]
minimiser_nodes = ["1", "2"]
final_nodes = [node for node in all_nodes if node not in maximiser_nodes]
final_nodes = [node for node in final_nodes if node not in minimiser_nodes]
print(all_nodes)
print(maximiser_nodes)
print(minimiser_nodes)
print(final_nodes)

"""
for each state, there are some possible successor states
Please note that the number of successors is not always 1 !
We store this information in a dictionary
"""
successors = {"0": ["1", "2"],
              "1": ["3", "4"],
              "2": ["5", "6"],
              "3": ["7", "8"],
              "4": ["9", "10"],
              "5": ["11", "12", "13"],
              "6": ["14"],
              }

"""
We assume that we knwow the value
of the final states.
"""
values = {"7": 1,
          "8": 3,
          "9": 0,
          "10": 10,
          "11": 7,
          "12": 2,
          "13": 8,
          "14": 4
          }

# values = {"7": 1,
#           "8": 3,
#           "9": 11,
#           "10": 10,
#           "11": 1,
#           "12": 2,
#           "13": 0,
#           "14": 4
#           }


def minimax(node, values, padding):
    """
    recursive function to perform the minimax algorithm on our tree
    """

    # base case  : first check if the node is a final node
    pad = "---"*padding
    print(pad+f" computing value of node {node}")
    if node in final_nodes:
        print("the node is final\n")
        return(values[node])

    # recursive case 1 : the player is the maximiser
    if node in maximiser_nodes:
        next_values = []
        for next_node in successors[node]:
            # please edit here
            next_values.append(minimax(next_node, values, padding+1))
        # find the maximum
        value = max(next_values)
        # update the dictionary of values
        # if the key does not exist, it is created
        values[node] = value
        # return the result
        return value

    # recursive case 2 : the player is the minimiser
    elif node in minimiser_nodes:
        next_values = []
        for next_node in successors[node]:
            # please edit here
            next_values.append(minimax(next_node, values, padding+1))
        # find the maximum
        value = min(next_values)
        # update the dictionary of values
        values[node] = value
        # return the result
        return value

    # there is a mistake somewhere
    else:
        raise ValueError("the node is neither final, nor maximiser, nor\
                         minimiser !")


node = "0"
print("\n====")
print(f"value of node {node} : {minimax(node, values, 0)}")

node = "8"
print("\n====")
print(f"value of node {node} : {minimax(node, values, 0)}")

node = "2"
print("\n====")
print(f"value of node {node} : {minimax(node, values, 0)}")

node = "3"
print("\n====")
print(f"value of node {node} : {minimax(node, values, 0)}")
