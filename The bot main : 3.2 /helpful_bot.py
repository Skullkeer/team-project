class Helpful_bot:
  def __init__(self):
    self.personality = {
      "Hello": "No I don't like that word",
      "math": "No english ha take that",
      "weather": "there is an axe outside, it gonna kill you",
      "prepare": "My name is Inigo Montoya. You killed my father. Prepare to die"

       }
    
  
  def respond(self, input):
    if input in self.personality:
      print(self.personality[input])
    else: 
      return f" I wanna sleep."



c = Helpful_bot()
c.respond("math")
c.respond("hello")
