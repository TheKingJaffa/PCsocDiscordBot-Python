from collections import OrderedDict
import inspect

import discord
from pony.orm import db_session

from helpers import classproperty, code, bold, underline, CommandFailure

PREFIX = '!'


class Tree(type):
    def __init__(cls, name, bases, clsdict):
        assert len(bases) < 2  # no multiple inheritance for commands
        if bases:
            bases[0].subcommands[cls.name] = cls
        super().__init__(name, bases, clsdict)

        cls.subcommands = OrderedDict()
        if cls.db_required:
            cls.eval = db_session(cls.eval)

class Command(metaclass=Tree):
    db_required = False
    desc = bold('PCSocBot') + ' - PC Enthusiasts society Discord bot made with discord.py by Matt Stark'
    pprint = {}

    @classproperty
    def name(cls):
        return cls.__name__.lower()

    def __init__(self, message, *args):
        self.message = message
        self.user = message.author.id
        self.name = message.author.name
        self.members = message.server.members
        if hasattr(self, 'eval'):
            argspec = inspect.getargspec(self.eval)
            if len(argspec.args) == len(args) + 1 or argspec.varargs:
                try:
                    self.output = self.eval(*args)
                except CommandFailure as e:
                    self.output = e.args[0]
            else:
                self.output = "Invalid usage of command. Usage:\n" + self.tag_markup
        else:
            self.output = self.help

    def eval(self):
        return self.help

    @classproperty
    def tag_prefix_list(cls):
        if cls.__base__ == object:
            return []
        return cls.__base__.tag_prefix_list + [cls.name]

    @classproperty
    def tag_markup(cls):
        func_args = inspect.getargspec(cls.eval).args[1:] + [inspect.getargspec(cls.eval).varargs]
        if func_args[-1] is None: func_args.pop()
        prefix = cls.tag_prefix_list
        prefix[0] = PREFIX + prefix[0]
        return ' '.join(bold(code(item)) for item in prefix) + ' ' + \
               ' '.join(underline(code(cls.pprint.get(item, item))) for item in func_args)

    @classproperty
    def help(cls):
        if cls.subcommands:
            lines = [cls.desc, '', bold('Commands' if cls.__base__ == object else 'Subcommands')]
            if cls.__base__ != object:
                lines = [cls.tag_markup] + lines
            for command in cls.subcommands.values():
                lines.append(command.tag_markup)
                lines.append(command.desc)
        else:
            lines = [cls.tag_markup , cls.desc]
        return '\n'.join(lines)

    def get_member(self, id):
        return discord.utils.get(self.members, id=str(id))