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
          "9": 0,
          "10": 10,
          "11": 7,
          "12": 2,
          "13": 8,
          "14": 4
          }

dot = Digraph("binary graph")

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

graph_name = "graphs/initial"
dot.render(graph_name)


# empty graph
for node in maximiser_nodes:
    dot.node(node, shape="box", color="darkorchid4", label="")

for node in minimiser_nodes:
    dot.node(node, color="goldenrod3", label="")

for node in final_nodes:
    dot.node(node, shape="diamond", color="aquamarine4", label="")

graph_name = "graphs/empty"
dot.render(graph_name)


# label with actions
for node in maximiser_nodes:
    dot.node(node, shape="box", color="darkorchid4", label="maximiser\naction")

for node in minimiser_nodes:
    dot.node(node, color="goldenrod3", label="minimiser\naction")

for node in final_nodes:
    dot.node(node, shape="diamond", color="aquamarine4", label="final\nnode")

graph_name = "graphs/actions"
dot.render(graph_name)


# label with values
for node in final_nodes:
    dot.node(node, shape="diamond", color="aquamarine4",
             label=str(values[node]))

graph_name = "graphs/values"
dot.render(graph_name)


# only values
for node in maximiser_nodes:
    dot.node(node, shape="box", color="darkorchid4", label="")

for node in minimiser_nodes:
    dot.node(node, color="goldenrod3", label="")

graph_name = "graphs/values_2"
dot.render(graph_name)


# maximiser
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


for node in ["3", "4", "5", "6"]:
    dot.node(node, label=str(get_max_value(node)))
    graph_name = "graphs/values_with_node_"+node
    dot.render(graph_name)

# maximiser bis
dot.node("0", label="maximiser\naction")

for node in minimiser_nodes:
    dot.node(node, color="goldenrod3", label="minimiser\naction")

graph_name = "graphs/values_maximiser_bis"
dot.render(graph_name)


# values with minimiser
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


for node in minimiser_nodes:
    print(node)
    dot.node(node, label=str(get_min_value(node)))
    graph_name = "graphs/values_with_node_"+node
    dot.render(graph_name)


# last value
dot.node("0", label=str(get_max_value("0")))
graph_name = "graphs/values_last"
dot.render(graph_name)
