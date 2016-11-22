from collections import OrderedDict
import inspect

from helpers import classproperty


class Tree(type):
    def __init__(cls, name, bases, clsdict):
        assert len(bases) < 2  # no multiple inheritance for commands
        if bases:
            bases[0].subcommands[cls.name] = cls
        super().__init__(name, bases, clsdict)
        cls.subcommands = OrderedDict()


class Command(metaclass=Tree):
    desc = 'PCSoc discord bot'
    subcommands = OrderedDict()

    @classproperty
    def name(cls):
        return cls.__name__.lower()

    def __init__(self, message, *args):
        self.message = message
        if hasattr(self, 'eval'):
            self.output = self.eval(*args)
        else:
            self.output = self.help

    @classproperty
    def tag_prefix_list(cls):
        if cls.__base__ == object:
            return []
        return cls.__base__.tag_prefix_list + [cls.name]

    @classproperty
    def tag_markup(cls):
        prefix = cls.tag_prefix_list
        return '**`!' + prefix[0] + '`** ' + \
               ' '.join('`' + item + '`' for item in prefix[1:])

    @classproperty
    def help(cls, full=False):
        if cls.subcommands:
            lines = [cls.desc, '', '**Subcommands**']
            if cls.__base__ != object:
                lines = [cls.tag_markup] + lines
            for command in cls.subcommands.values():
                lines.append(command.tag_markup)
                lines.append(command.desc)
        else:
            lines = [cls.tag_markup , cls.desc]
        return '\n'.join(lines)
