from graphviz import Digraph

depth = 3

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

successors = {"0": ["1", "2"],
              "1": ["3", "4"],
              "2": ["5", "6"],
              "3": ["7", "8"],
              "4": ["9", "10"],
              "5": ["11", "12", "13"],
              "6": ["14"],
              }

values = {"7": 1,
          "8": 3,
          "9": 11,
          "10": 10,
          "11": 1,
          "12": 2,
          "13": 0,
          "14": 4
          }

dot = Digraph("binary graph", strict=True)

# initial graph
for node in maximiser_nodes:
    dot.node(node, shape="box", color="darkorchid4")

for node in minimiser_nodes:
    dot.node(node, color="goldenrod3")

for node in final_nodes:
    dot.node(node, shape="diamond", color="aquamarine4")

for node in successors:
    for successor in successors[node]:
        dot.edge(node, successor)

graph_name = "graphs_2/initial"
dot.render(graph_name)


# empty graph
for node in maximiser_nodes:
    dot.node(node, shape="box", color="darkorchid4", label="")

for node in minimiser_nodes:
    dot.node(node, color="goldenrod3", label="")

for node in final_nodes:
    dot.node(node, shape="diamond", color="aquamarine4", label="")

graph_name = "graphs_2/empty"
dot.render(graph_name)


# label with actions
for node in maximiser_nodes:
    dot.node(node, shape="box", color="darkorchid4", label="maximiser\naction")

for node in minimiser_nodes:
    dot.node(node, color="goldenrod3", label="minimiser\naction")

for node in final_nodes:
    dot.node(node, shape="diamond", color="aquamarine4", label="final\nnode")

graph_name = "graphs_2/actions"
dot.render(graph_name)


# only values
for node in final_nodes:
    dot.node(node, shape="diamond", color="aquamarine4",
             label=str(values[node]))

for node in maximiser_nodes:
    dot.node(node, shape="box", color="darkorchid4", label="")

for node in minimiser_nodes:
    dot.node(node, color="goldenrod3", label="")

graph_name = "graphs_2/values_final_nodes"
dot.render(graph_name)

# empty graph
for node in maximiser_nodes:
    dot.node(node, shape="box", color="darkorchid4", label="")

for node in minimiser_nodes:
    dot.node(node, color="goldenrod3", label="")

for node in final_nodes:
    dot.node(node, shape="diamond", color="aquamarine4", label="")

graph_name = "graphs_2/empty"
dot.render(graph_name)


# maximise
def get_max_value(node):
    next_values = []
    for next_node in successors[node]:
        next_values.append(values[next_node])
    # find the maximum
    value = max(next_values)
    # update the dictionary of values
    values[node] = value
    # return the result
    return value


# minimise
def get_min_value(node):
    next_values = []
    for next_node in successors[node]:
        next_values.append(values[next_node])
    # find the minimum
    value = min(next_values)
    # update the dictionary of values
    values[node] = value
    # return the result
    return value


# node 7
dot.node("7", label=str(values["7"]))
graph_name = "graphs_2/alpha_1_n7"
dot.render(graph_name)

# node 8
dot.node("8", label=str(values["8"]))
graph_name = "graphs_2/alpha_2_n8"
dot.render(graph_name)

# node 3
dot.node("3", label=str(get_max_value("3")))
graph_name = "graphs_2/alpha_3_n3"
dot.render(graph_name)

# node 9
dot.node("9", label=str(values["9"]))
graph_name = "graphs_2/alpha_4_n9"
dot.render(graph_name)

# node 4
dot.node("4", label=str(">= 11"))
dot.node("10", label="x", color="grey", fontcolor="grey")
dot.edge("4", "10", color="grey")
graph_name = "graphs_2/alpha_5_n4"
dot.render(graph_name)

# node 1
dot.node("1", label="3")
graph_name = "graphs_2/alpha_6_n1"
dot.render(graph_name)

# node 11
dot.node("11", label=str(values["11"]))
graph_name = "graphs_2/alpha_7_n11"
dot.render(graph_name)

# node 12
dot.node("12", label=str(values["12"]))
graph_name = "graphs_2/alpha_8_n12"
dot.render(graph_name)

# node 13
dot.node("13", label=str(values["13"]))
graph_name = "graphs_2/alpha_9_n13"
dot.render(graph_name)

# node 5
dot.node("5", label="2")
graph_name = "graphs_2/alpha_10_n5"
dot.render(graph_name)

# node 2
dot.node("2", label="=<2")
dot.node("6", label="x", color="grey", fontcolor="grey")
dot.node("14", label="x", color="grey", fontcolor="grey")
graph_name = "graphs_2/alpha_91_n2"
dot.render(graph_name)

# node 0
dot.node("0", label="3")
graph_name = "graphs_2/alpha_92_n0"
dot.render(graph_name)

