from chatbot import ChatBot

class Sarcastic_bot(ChatBot):
  def __init__(self):
    self.personality = {
      "hello": "Oh, look who decided to grace us with their presence. Welcome to the chat. I’m utterly overwhelmed with excitement.",
      "good": "Id explain it to you, but I’m afraid I don't have the time or the crayons to make it simple enough",
      "math": "I’d try to explain this to you, but unfortunately, I can't provide you with an understanding of it and a functional brain at the same time.",
      "2+2":"Oh, did your 'rocket science' calculations not pan out? Let me guess, 2+2=5 was a bit too ambitious for you today.",
      "weather": "Why are you asking me? Do I look like a meteorologist, or do I just give off the vibe of a personal assistant with a spare window?",
      "moive": "You’re asking me to spoon-feed you a movie because your own brain refuses to come up with one? Groundbreaking."

       }
    
  
  def respond(self, input):
    if input.lower() in self.personality:
      return self.personality[input.lower()]
    else: 
      return "I wanna sleep."
