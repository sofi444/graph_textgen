import pprint as pp



class Node:
    def __init__(self, token):
        self.token = token
        self.neighbours = {}
        self.neighbours_count = 0

    def add_neighbour(self, neighbour):
        self.neighbours_count += 1
        if neighbour in self.neighbours:
            self.neighbours[neighbour] += 1
        else:
            self.neighbours[neighbour] = 1

    def get_transition_probabilities(self):
        # transition probabilities for one node to each neighbour
        transition_probabilities = {}
        for neighbour, count in self.neighbours.items():
            transition_probabilities[neighbour] = count / self.neighbours_count
        return transition_probabilities
    


class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, token):
        if token not in self.nodes:
            self.nodes[token] = Node(token)

    def add_edge(self, token, next_token):
        # add nodes for the current token and the next token (if they don't already exist)
        # add edge between them (directed: token -> next_token)
        self.add_node(token)
        self.add_node(next_token)
        self.nodes[token].add_neighbour(next_token)

    def get_transition_probabilities(self):
        transition_probabilities = {}
        for node in self.nodes.values():
            transition_probabilities[node.token] = node.get_transition_probabilities()
        return transition_probabilities
    
    def populate(self, data):
        # add tokens to graph (nodes and edges)
        for i in range(len(data) - 1):
            token = data[i]
            next_token = data[i + 1]
            self.add_edge(token, next_token)
    
