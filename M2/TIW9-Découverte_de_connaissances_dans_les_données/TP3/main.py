# %% Étape 0 : imports
import pandas as pd
import nltk
from nltk.tokenize import word_tokenize

# %% Étape 1 : chargement des données
filenames = {
    "Youtube01-Psy.csv",
    "Youtube03-LMFAO.csv",
    "Youtube05-Shakira.csv",
    "Youtube02-KatyPerry.csv",
    "Youtube04-Eminem.csv"
}
frames = []
for filename in filenames:
    # file = open("./data/" + filename, "r")
    # reader = csv.reader(file, delimiter=",")
    # for row in reader:
    #    dataset.append(row)
    frames.append(pd.read_csv("./data/" + filename))

# %% Étape 1 : traitement
dataframe = pd.concat(frames)
dataframe = dataframe.drop(columns=["COMMENT_ID", "AUTHOR", "DATE"])
print(dataframe)

# %% Étape 2 : f(x -> normalisation, tokénisation, suppression stopwords et lemmatization)
def preprossessing(text):
    normalizedText = text.lower()
    tokens = word_tokenize(normalizedText)
    return tokens

commentaire = "iS IN TOP 10 , IN YOUTUBE TOP VIEWS ,\
 ON 9 IS MILEY CYRUS: http://www.google.ro/url?sa=t&\
 amp;rct=j&amp;q=&amp;esrc=s&amp;source=web&amp;cd=1\
 &amp;ved=0CB8QFjAA&amp;url=http%3A%2F%2Fen.wikipedi\
 a.org%2Fwiki%2FList_of_most_viewed_YouTube_videos&a\
 mp;ei=OQ3yU9DWC8L4yQOYo4GoAw&amp;usg=AFQjCNGKM-Idpl\
 al6kuVKoEkVgdTT2jVLQ&amp;sig2=OnqZzad3q3CmNBe9nml4g\
 A&amp;bvm=bv.73231344,d.bGQ&amp;cad=rja ﻿"

test = preprossessing(commentaire)
print(test)
