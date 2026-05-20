class EventManager():
    def __init__(self):
        self.observers = []

    def attatch(self, bot):
        self.observers.append(bot)
        print(self.observers)

    def detatch(self, bot):
        self.observers.remove(bot)

    def notify(self, msg):
        responses = {}
        for bot in self.observers:
            responses[bot.name] = bot.respond(msg)
        return responses
