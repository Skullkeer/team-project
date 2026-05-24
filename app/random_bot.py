from chatbot import ChatBot
import random
class Random_bot(ChatBot):
  def __init__(self):
    self.personality = {
      "hello": "I am currently calculating the exact gravitational pull of your average cup of coffee and testing if a rubber duck could pilot a hovercraft on Mars.",
      "good": "Sir, this is an emu sanctuary.",
      "math": "It's fish, obviously—but if you’re asking the government, they’ll try to tell you it’s a window or maybe 22 if you just slide the numbers together.",
      "weather": "The rain is just water falling at 30 km/h, but that’s the perfect excuse to wear my vintage neon poncho. It’s supposed to be sunny, but the universe is probably just projecting a 500% chance of a completely unpredictable cosmic tea party instead",
      "2+2": "A sentient cloud of glitter named Gary",
      "movie": "My name is Inigo Montoya. You killed my father. Prepare to die"

       }
    
    self.name = "Random Bot"

  def respond(self, input):
    random_bool = random.choice([True, False])
    if random_bool == True:
      if input.lower() in self.personality:
        return self.personality[input.lower()]
      else: 
        return f" I wanna sleep."
    else: 
        return " "


c = Random_bot()
c.respond("math")
c.respond("Hello")
