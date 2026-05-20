from chatbot import ChatBot

class Helpful_bot(ChatBot):
  def __init__(self):
    self.personality = {
      "hello": "Hello, how are you doing today?",
      "good": "Thats great, how can I help?",
      "math": "Math is a great subeject you have any questions",
      "weather": "It is going to be sunny today, with some clouds.",
      "2+2": "Ther answer is 4.",
      "movie": "A good movie suggestion, Kiki's delivery service."

       }

    self.name = "Helpful Bot"
    
  
  def respond(self, input):
    if input.lower() in self.personality:
      return self.personality[input.lower()]
    else: 
      return f" I wanna sleep."



c = Helpful_bot()
c.respond("math")
c.respond("hello")
