import os, sys
import pandas as pd
from IPython.display import Image
import seaborn as sns
import matplotlib.pyplot  as plt
import xlrd
import plotly.offline as py
from plotly.offline import init_notebook_mode, iplot
import plotly.express as px
import plotly.graph_objs as go
from plotly.offline import plot
import plotly.io as pio
from bubbly.bubbly import bubbleplot
import random
import plotly

import plotly.offline as pyoff
import plotly.graph_objs as go

from wordcloud import WordCloud
import nltk

#nltk.download('stopwords')
#nltk.download('punkt')


os.path.abspath('')
root_path = os.path.dirname(os.path.abspath(''))
sys.path.append(root_path)

def subject_distribution(df):
    plt.figure(figsize=(8,5))
    sns.countplot("subject", data=df)
    plt.show()

def show_wordcloud(df):
    text = ''
    for news in df.text.values:
        text += f" {news}"


    wordcloud = WordCloud(
        width = 3000,
        height = 2000,
        background_color = 'black',
        stopwords = set(nltk.corpus.stopwords.words("english"))).generate(text)
    fig = plt.figure(
        figsize = (40, 30),
        facecolor = 'k',
        edgecolor = 'k')
    plt.imshow(wordcloud, interpolation = 'bilinear')
    plt.axis('off')
    plt.tight_layout(pad=0)
    plt.show()
    del text

def plot_by_time(df_true, df_false):
    plot_data = [
        go.Scatter(
            x=df_false.index,
            y=df_false['category'],
            name='Fake',
            #x_axis="OTI",
            #y_axis="time",
        ),
        go.Scatter(
            x=df_true.index,
            y=df_true['category'],
            name='Real'
        )
        
    ]
    plot_layout = go.Layout(
            title='Fake and Real news plotted by time',
            yaxis_title='Count',
            xaxis_title='Time',
            plot_bgcolor='rgba(0,0,0,0)'
        )
    fig = go.Figure(data=plot_data, layout=plot_layout)
    pyoff.iplot(fig)

def amount_characters(df):
    fig,(ax1,ax2)=plt.subplots(1,2,figsize=(12,8))
    text_len=df[df['category']==1]['text'].str.len()
    ax1.hist(text_len,color='red')
    ax1.set_title('Real text')
    text_len=df[df['category']==0]['text'].str.len()
    ax2.hist(text_len,color='green')
    ax2.set_title('Fake text')
    fig.suptitle('Characters in texts')
    plt.show()


def amount_words(df):
    fig,(ax1,ax2)=plt.subplots(1,2,figsize=(12,8))
    text_len=df[df['category']==1]['text'].str.split().map(lambda x: len(x))
    ax1.hist(text_len,color='red')
    ax1.set_title('Real text')
    text_len=df[df['category']==0]['text'].str.split().map(lambda x: len(x))
    ax2.hist(text_len,color='green')
    ax2.set_title('Fake text')
    fig.suptitle('Words in texts')
    plt.show()

def compare_word_length(df):
    fig,(ax1,ax2)=plt.subplots(1,2,figsize=(10,5))
    word=df[df['category']==1]['text'].str.split().apply(lambda x : [len(i) for i in x])
    sns.distplot(word.map(lambda x: np.mean(x)),ax=ax1,color='red')
    ax1.set_title('Real text')
    word=df[df['category']==0]['text'].str.split().apply(lambda x : [len(i) for i in x])
    sns.distplot(word.map(lambda x: np.mean(x)),ax=ax2,color='green')
    ax2.set_title('Fake text')
    fig.suptitle('Average word length in each text')
    plt.show()
