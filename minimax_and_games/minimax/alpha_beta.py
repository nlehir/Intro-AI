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

# for each state, there are some possible successor states
successors = {"0": ["1", "2"],
              "1": ["3", "4"],
              "2": ["5", "6"],
              "3": ["7", "8"],
              "4": ["9", "10"],
              "5": ["11", "12", "13"],
              "6": ["14"],
              }

# values of the final nodes
values = {"7": 1,
          "8": 3,
          "9": 11,
          "10": 10,
          "11": 1,
          "12": 2,
          "13": 0,
          "14": 4
          }


def alpha_beta(node, values, alpha, beta, padding):

    # base case  : first check if the node is a final node
    pad = "---"*padding
    print(pad+f" computing value of node {node}")
    if node in final_nodes:
        print(pad + " the node is final")
        return(values[node])

    # recursive case 1
    if node in maximiser_nodes:
        for next_node in successors[node]:
            # print(pad+f" alpha={alpha}")
            # print(pad+f" beta={beta}")
            if alpha < beta:
                alpha = max(alpha, alpha_beta(next_node,
                                              values,
                                              alpha,
                                              beta,
                                              padding+1))
            else:
                # exit the loop
                print(pad + " node "+node+" : discard the branch")
                break
        values[node] = alpha
        # return the result
        return alpha

    # recursive case 2
    elif node in minimiser_nodes:
        for next_node in successors[node]:
            # print(pad+f" alpha={alpha}")
            # print(pad+f" beta={beta}")
            if alpha < beta:
                beta = min(beta, alpha_beta(next_node,
                                            values,
                                            alpha,
                                            beta,
                                            padding+1))
            else:
                print(pad + " node "+node+": discard the branch")
                break
        values[node] = beta
        # return the result
        return beta

    # there is a mistake somewhere
    else:
        raise ValueError("the node is neither final, nor maximiser, nor\
                         minimiser !")


node = "0"
print("\n====")
print(f"value of node {node} : {alpha_beta(node, values, 0, 1000, 0)}")

node = "8"
print("\n====")
print(f"value of node {node} : {alpha_beta(node, values, 0, 1000, 0)}")

node = "2"
print("\n====")
print(f"value of node {node} : {alpha_beta(node, values, 0, 1000, 0)}")

node = "3"
print("\n====")
print(f"value of node {node} : {alpha_beta(node, values, 0, 1000, 0)}")
