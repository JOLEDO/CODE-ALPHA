import time
import spacy
import json

class ChatBot:
    def __init__(self):
        print("Chatbot: Initializing...")
        time.sleep(4)
        self.nlp = spacy.load("en_core_web_sm") 
        self.intents = self.load_intents()["intents"]
        print("Good day, How may I help you today? Type 'bye' to exit the chatbot.")
        self.chat()

    def load_intents(self):
        with open("intents.json", "r", encoding='utf-8') as file:
            return json.load(file)

    def chat(self):
        while True:
            self.user_input = input("<---->: ").lower()
            if self.user_input == "bye" or self.user_input == "goodbye":
                print("Goodbye! Take care. 🫶")
                break
            self.response = self.get_response(self.user_input)
            print(f"[----] {self.response}")

    def get_response(self, text):
        doc = self.nlp(text) 

        for intent in self.intents:
            for pattern in intent["pattern"]:
                pattern_doc = self.nlp(pattern)
                if doc.similarity(pattern_doc) > 0.7:
                    return intent["response"] 

        return "I'm not sure how to respond to that. Can you rephrase?"

if __name__ == "__main__":
    ChatBot()
