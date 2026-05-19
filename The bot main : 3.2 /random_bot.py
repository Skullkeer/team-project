class Random_bot:
  def __init__(self, input):
    self.input = input

  personality = {
        "hello": "No I don't like that word",
        "math": "no english ha take that"
         }
  
  def respond(input):

    if input == personality:
      print("hello")