from base_command import Command


class Ping(Command):
    desc = "Pong!"
    full_desc = "This command could be used to check if the bot is up. Or entertainment when you're bored."

    def eval(self):
        return "Pong!"


class Pong(Command):
    desc = "Ping!"
    full_desc = "This command could be used to check if the bot is up. Or entertainment when you're bored."

    def eval(self):
        return "Ping!"


class Tags(Command):
    desc = "Player tag storage for the UNSW PCSoc discord server."
    full_desc = "This command stores user/player tags for any platform. Can be used to search up your own tags and other users/players on the server."


class Add(Tags):
    desc = "Adds/changes a player tag with associated platform/game to the list"
    pprint = dict(platform="platform/game")

    def eval(self, platform, tag):
        return "Adding %s to %s" % (tag, platform)

if __name__ == '__main__':
    print(Add.help)