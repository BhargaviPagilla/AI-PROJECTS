import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from preprocessing import clean_text
df=pd.read_csv("../database/spam.csv")
df['clean']=df["message"].apply(clean_text)
vectorizer=TfidfVectorizer()
X=vectorizer.fit_transform(df["clean"])
y=df["label"]
model=MultinomialNB()
model.fit(X,y)
joblib.dump(model, "../model.pkl")
joblib.dump(vectorizer, "../vectorizer.pkl")