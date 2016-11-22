import discord
import asyncio

from base_command import run_command

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    import commands

@client.event
async def on_message(message):
    if message.content.startswith('!'):
        output = run_command(message, *message.content[1:].split())
        if output is not None:
            await client.send_message(message.channel, output)

client.run('MjUwNTU1MTI2ODY1OTg1NTM3.CxWjNw.LEUX8aV33pxAZ6tWKh7jaXtQhKk')

server = client.accept_invite('yMS5Kya')