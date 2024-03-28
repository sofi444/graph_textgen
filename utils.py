import os
import re
import nltk

from nltk.tokenize import sent_tokenize, word_tokenize
from string import punctuation



class DataHandler:
    def __init__(self, data_path):
        self.data_path = data_path # dir or file path
        self.data = ""

    def load_data(self):
        if os.path.isdir(self.data_path):
            for file in os.listdir(self.data_path):
                with open(os.path.join(self.data_path, file), 'r', encoding="utf-8-sig") as f:
                    self.data += f.read().strip('\n')
        else:
            with open(self.data_path, 'r', encoding="utf-8-sig") as f:
                self.data = f.read().strip('\n')



class CharacterTokenizer:
    def __init__(self, data):
        self.vocab = sorted(list(set(data)))
        self.vocab_size = len(self.vocab)
        self.char_to_int = {
            char:i for i,char in enumerate(self.vocab)
        }
        self.int_to_char = {
            i:char for i,char in enumerate(self.vocab)
        }

    def encode(self, text) -> list[int]:
        return [self.char_to_int[char] for char in text]

    def decode(self, encoded) -> str:
        return ''.join([self.int_to_char[i] for i in encoded])
    


class WordTokenizer:
    def __init__(self, data):
        self.data = data
        self.vocab = self.create_vocab(self.data)
        self.vocab_size = len(self.vocab)
        
        self.word_to_int = {
            word:i for i,word in enumerate(self.vocab)
        }
        self.int_to_word = {
            i:word for i,word in enumerate(self.vocab)
        }

    def create_vocab(self, data) -> list[str]:
        vocab = set()
        for word in word_tokenize(data):
            if word not in punctuation:
                word = re.sub(r'^\W+|\W+$', '', word)
            vocab.add(word)

        return sorted(list(vocab))

    def encode(self, text) -> list[int]:
        encoded = []
        for word in word_tokenize(text):
            if word not in punctuation:
                word = re.sub(r'^\W+|\W+$', '', word)
            encoded.append(self.word_to_int[word])

        return encoded

    def decode(self, encoded) -> str:
        return ' '.join([self.int_to_word[i] for i in encoded])
    
    



if __name__ == '__main__':
    data_path = os.path.join(os.getcwd(), 'data')
    data_handler = DataHandler(data_path)
    data_handler.load_data()
    data = data_handler.data
    data = data[:1000]

    tokenizer = WordTokenizer(data)
    vocab = tokenizer.vocab

    print(vocab)