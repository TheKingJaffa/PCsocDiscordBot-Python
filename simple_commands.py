from base_command import Command


class Ping(Command):
    def eval(self):
        return 'pong'

class Pong(Command):
    def eval(self):
        return 'ping'
