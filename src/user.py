import random
import numpy as np
import pandas as pd

class UserProfile:
    def __init__(self,name):
        self.name = name
        self.age = 0
        
        self.attributes = {
            "health": random.randint(1, 10),
            "wealth": random.randint(1, 10),
            "happiness": random.randint(1, 10),
            "intelligence": random.randint(1, 10)
        }
        
        self.decision_history = []
    
    def save_to_excel(self,filename):
        data = {
            "Name": [self.name],
            "Age": [self.age],
            "Health": [self.attributes["health"]],
            "Wealth": [self.attributes["wealth"]],
            "Happiness": [self.attributes["happiness"]],
            "Intelligence": [self.attributes["intelligence"]],
            "Decisions": [", ".join([f"{d['age']} - {d['decision']}" for d in self.decision_history])]
        }
        data_df = pd.DataFrame(data)
        data_df.to_excel(filename,index=False)
    
    def update_attributes(self, health=None, wealth=None, happiness=None, intelligence=None):
        if health is not None:
            self.attributes["health"] += health
        if wealth is not None:
            self.attributes["wealth"] += wealth
        if happiness is not None:
            self.attributes["happiness"] += happiness
        if intelligence is not None:
            self.attributes["intelligence"] += intelligence
    
    def add_decision(self,age,decision):
        self.decision_history.append({"age":age,"decision":decision})
        