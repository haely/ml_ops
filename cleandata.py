import readdata
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

filepath=""
df_raw = readdata(filepath)

def make_lowercase(df_raw):
    # df_lowercase = df_raw.applymap(lambda s: s.lower() if type(s) == str else s)
    df_lowercase = df_raw.apply(lambda x: x.str.lower() if x.dtype == "object" else x) 
    return df_lowercase

def drop_punctuation(df_lowercase):
    df_nopunctuation = df_lowercase.str.replace('[^\w\s]','')
    return df_nopunctuation

def drop_stopwords(df_nopunctuation):
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(df_nopunctuation)
    df_nostopwords = df_nopunctuation.apply(lambda x: ' '.join([word for word in x.split() if word not in (stop_words)]))
    return df_nostopwords

def tokenise(df_nostopwords):
    df_tokenised = df_nostopwords
    return df_tokenised

# to do:
"""
Lowecasing the data
Removing Puncuatations
Removing Numbers
Removing extra space
Replacing the repetitions of punctations
Removing Emojis
Removing emoticons
Removing Contractions
"""