from pony.orm import db_session

from commands.base import Command
from models import Tag


class Tags(Command):
    db_required = True
    pprint = dict(platform="platform/game")
    desc = "Player tag storage for the UNSW PCSoc discord server."


class Add(Tags):
    desc = "Adds/changes a player tag with associated platform/game to the list"
    def eval(self, platform, tag):
        Tag.create_or_update(user=self.user, platform=platform, tag=tag)
        return "%s added as %s tag for %s" % (tag, platform, self.name)


class Remove(Tags):
    desc = "Removes a user/player tag to the bot."
    def eval(self, platform):
        return "Removed tag for " + platform


class Get(Tags):
    desc = "Returns your own tag for a platform / game"
    def eval(self, platform):
        tag = Tag.get_or_err("Platform/game not found",
                             user=self.user, platform=platform)
        return "The %s tag of %s is %s" % (platform, self.name, tag.tag)


class List(Tags):
    desc = "Returns a list of user tags for a specified platform"
    def eval(self, platform):
        return "Got a list of tags for " + platform