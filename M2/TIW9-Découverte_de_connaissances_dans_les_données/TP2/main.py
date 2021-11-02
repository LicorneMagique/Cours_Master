# %% Imports
import pandas as pd
import csv

# %% Chargement des données
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

# %% Tests
dataframe = pd.concat(frames)
dataframe = dataframe.drop(columns=["COMMENT_ID", "AUTHOR", "DATE"])
dataframe
print(dataframe)
