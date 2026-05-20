class Helpful_bot:
  def __init__(self):
    self.personality = {
      "Hello": "Hello, how are you doing today?",
      "good": "Thats great, how can I help?",
      "math": "Math is a great subeject you have any questions",
      "weather": "It is going to be sunny today, with some clouds.",
      "2+2": "Ther answer is 4.",
      "movie": "A good movie suggestion, Kiki's delivery service."

       }
    
  
  def respond(self, input):
    if input in self.personality:
      print(self.personality[input])
    else: 
      return f" I wanna sleep."



c = Helpful_bot()
c.respond("math")
c.respond("hello")
