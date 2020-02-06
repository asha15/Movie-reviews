import tensorflow as td
from tensorflow import keras 
from keras.datasets import imdb
import numpy as np

data = keras.datasets.imdb

(train_data, train_labels), (test_data, test_labels) = data.load_data(num_words=10000)

print(train_data[1])

print()

word_index = imdb.get_word_index()



