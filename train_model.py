import json
import random
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import nltk
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()

with open("intents.json") as file:
    data = json.load(file)

corpus = []
labels = []

for intent in data["intents"]:
    for pattern in intent["patterns"]:
        corpus.append(pattern.lower())
        labels.append(intent["tag"])

pipeline = Pipeline([
    ("vectorizer", CountVectorizer()),
    ("classifier", MultinomialNB())
])

pipeline.fit(corpus, labels)

with open("chatbot_model.pkl", "wb") as f:
    pickle.dump(pipeline, f)

with open("chatbot_vectorizer.pkl", "wb") as f:
    pickle.dump(pipeline.named_steps["vectorizer"], f)

print("Model trained and saved.")
