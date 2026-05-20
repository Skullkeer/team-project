from abc import ABC, abstractmethod

class ChatBot(ABC): 
    @abstractmethod
    def __init__(self, name):
        self.name = name

    def name(self):
        return self.name
