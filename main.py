
from utils import DataHandler, CharacterTokenizer, WordTokenizer
from graph import Graph

import os

dev = True

# setup (data, tokenizer)
data_path = os.path.join(os.getcwd(), 'data')
data_handler = DataHandler(data_path)
data_handler.load_data()
data = data_handler.data
if dev:
    data = data[:50000]

#tokenizer = CharacterTokenizer(data)
tokenizer = WordTokenizer(data)
vocab = tokenizer.vocab
vocab_size = tokenizer.vocab_size

# setup (graph)
graph = Graph()
data = tokenizer.encode(data)

# populate graph
graph.populate(data)

# get transition probabilities
transition_probabilities = graph.get_transition_probabilities()

# generate text
start_token = tokenizer.encode('I')[0]
text = [start_token]
current_token = start_token
for i in range(100):
    next_token = max(transition_probabilities[current_token], key=transition_probabilities[current_token].get)
    text.append(next_token)
    current_token = next_token

text = tokenizer.decode(text)
print(text)