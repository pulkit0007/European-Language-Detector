import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import confusion_matrix,classification_report


# Preprocessing Data
def file2sentences(filename):
    txt = ""
    with open(filename, "r", encoding="utf-8") as f:
        txt = f.read()

    txt = txt.replace("?", ".")
    txt = txt.replace("!", ".")
    txt = txt.replace("»", "")
    txt = txt.replace("«", "")
    txt = txt.replace(":", "")
    txt = txt.replace(";", "")
    txt = txt.replace("...", ".")
    txt = txt.replace("…", ".")
    txt = txt.replace("\n", ".")
    txt = txt.replace("  ", " ")
    txt = txt.replace("\"", "")
    txt = txt.replace("„", "")
    sentences = txt.split(".")
    for i in range(len(sentences)):
        sentences[i] = sentences[i].strip()

    sentences = [x for x in sentences if x != ""]
    return sentences

italian = file2sentences("It.txt")
english = file2sentences("En.txt")
german = file2sentences("Ge.txt")
french = file2sentences("Fr.txt")
spanish = file2sentences("Es.txt")

X = np.array(italian + english + german + french + spanish)
y = np.array(['Italian']*len(italian) + ['English']*len(english) + ['German']*len(german) + ['French']*len(french) + ['Spanish']*len(spanish))

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

cnt = CountVectorizer(analyzer = 'char',ngram_range=(2,2))

pipeline = Pipeline([
   ('vectorizer',cnt),
   ('model',MultinomialNB())
])
pipeline.fit(X_train,y_train)

def predictor(text):
    lan = pipeline.predict(text).astype(str)
    return lan
    
    
