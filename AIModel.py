from dotenv import load_dotenv, find_dotenv
from google import genai
import random
class AIModel():
    def __init__(self):
        load_dotenv(find_dotenv())
        self.client = genai.Client()
        self.examplePrompts = [
            "Explain black holes",
            "How do airplanes fly?",
            "Why is the sky blue?",
            "What makes thunder?",
            "Why do we have to sleep?",
            "Where does the sun go at night?",
            "How do plants grow?",
            "Why do leaves change color in autumn?",
            "What are clouds made of?",
            "How does the internet work?",
            "Why do we have teeth?",
            "How do bees make honey?",
            "Why does it rain?",
            "What is electricity?",
            "Why is the ocean salty?",
            "How do volcanoes erupt?",
            "Why do we have seasons?",
            "What are dreams?",
            "How does a rainbow form?",
            "Why do we blink?",
            "What is gravity?",
            "Why do birds sing?",
            "How do computers think?",
            "Why do shadows change size?",
            "Where do babies come from?",
            "Why do we get sick?",
            "What are stars?",
            "How do magnets work?",
            "Why do we have fingerprints?",
            "What is a fossil?",
            "How do mirrors work?",
            "Why do we have fingernails?",
            "What is DNA?",
            "How do we taste food?",
            "Why is the moon sometimes a crescent?",
            "What are earthquakes?",
            "How do bridges stay up?",
            "Why do we get goosebumps?",
            "What is an atom?",
            "How does a car engine work?",
            "Why do we have hiccups?",
            "What are germs?",
            "How do we hear sound?",
            "Why is fire hot?",
            "What is the North Pole?",
            "How do clocks work?",
            "Why do spiders build webs?",
            "What is a robot?",
            "How do we smell things?",
            "Why is ice slippery?"
        ]
    def getResponse(self,prompt):
        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents="Explain the following inquiry like I'm 5 years old. " + prompt,
        )
        print("Explain the following inquiry like I'm 5 years old. " + prompt)
        return response.text
    def randomPrompt(self):
        return self.examplePrompts[random.randint(0,len(self.examplePrompts)-1)]