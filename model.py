import json
import random
import pickle
import nltk
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

with open("intents.json") as file:
    data = json.load(file)

with open("chatbot_model.pkl", "rb") as f:
    model = pickle.load(f)

def get_bot_response(user_input):
    tag = model.predict([user_input.lower()])[0]

    for intent in data["intents"]:
        if intent["tag"] == tag:
            return random.choice(intent["responses"])

    return "I'm not sure how to help with that."
