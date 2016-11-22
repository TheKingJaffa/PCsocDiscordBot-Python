class Tree(type):
    def __init__(cls, name, bases, clsdict):
        assert len(bases) < 2  # no multiple inheritance for commands
        if bases:
            name = getattr(cls, 'name', cls.__name__.lower())
            bases[0].subcommands[name] = cls
        super().__init__(name, bases, clsdict)


class Command(metaclass=Tree):
    subcommands = {}

    def __init__(self, message, *args):
        self.message = message
        self.output = self.eval(*args)

if __name__ == '__main__':
    pass