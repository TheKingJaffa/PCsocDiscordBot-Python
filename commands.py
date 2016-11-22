import simple_commands
from base_command import Command


def run_command(message, *args):
    cls = Command
    first_arg = 0
    for arg in args:
        if arg in cls.subcommands:
            cls = cls.subcommands[arg]
            first_arg += 1
        else:
            break
    args = args[first_arg:]
    return cls(message, *args).output