import discord

from base_command import COMMAND_PREFIX
from commands import Help

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith(COMMAND_PREFIX):
        args = message.content[1:].split()
        cls, args = Help.find_command(args)
        output = cls(message, *args).output
        if output is not None:
            await client.send_message(message.channel, output)

client.run('MjUwNTU1MTI2ODY1OTg1NTM3.CxWjNw.LEUX8aV33pxAZ6tWKh7jaXtQhKk')

server = client.accept_invite('yMS5Kya')