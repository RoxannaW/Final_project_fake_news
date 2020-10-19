import os, sys

os.path.abspath('')
root_path = os.path.dirname(os.path.abspath(''))
sys.path.append(root_path)

import pandas as pd 
import numpy as np
import os, sys
import json
import nltk

import re

import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding, LSTM, Conv1D, MaxPool1D


#nltk.download('stopwords')
#nltk.download('punkt')



def prepare_data(text):
    maxlen = 750 
    X = []
    stop_words = set(nltk.corpus.stopwords.words("english"))
    tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+')
    pattern = r'[^a-zA-z0-9\s]'

    text = list([text])
    text = np.array(text)
    
    for par in text:
        tmp = []
        sentences = nltk.sent_tokenize(par)
        for sent in sentences:
            sent = sent.lower()
            sent = re.sub(pattern, '', sent)
            tokens = tokenizer.tokenize(sent)
            filtered_words = [w.strip() for w in tokens if w not in stop_words and len(w) > 1]
            tmp.extend(filtered_words)
        X.append(tmp)

    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(X)

    X = tokenizer.texts_to_sequences(X)
    X = pad_sequences(X, maxlen=maxlen)
    return X

def test():
    print("holi")




def predict_news(text):

    x = prepare_data(text=text)
    model = tf.keras.models.load_model('C:\\Users\\Roxan\\OneDrive\\Documentos\\Final_project_fake_news\\Final_project_fake_news\\Models\\model_epoch_4_with_callback_batch_10.h5')

    result = (model.predict(x) > 0.5).astype("int32")[0][0]
    if result == 0:
        print("Fake news!")
        return ("Fake news!" + "\U0001F928")
    elif result == 1:
        print("Don't worry, the news is real \U0001F604") 	
        return "Don't worry, the news is real \U0001F604" 
    



