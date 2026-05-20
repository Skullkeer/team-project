from helpful_bot import Helpful_bot
from sarcastic_bot import Sarcastic_bot
from random_bot import Random_bot

def create_bot(type):
    if type == "help":
        return Helpful_bot()

    if type == "sarc":
        return Sarcastic_bot()

    if type == "rand":
        return Random_bot()
