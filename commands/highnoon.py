import asyncio
from datetime import date, time, timedelta, datetime

from commands import Command

HIGH_NOON_CHANNEL = 'gaming'


class HighNoon(Command):
    pass


async def high_noon(client, channel):
    next_noon = datetime.combine(date.today(), time(hour=12))
    if next_noon < datetime.now():
        next_noon += timedelta(days=1)
    while True:
        duration = (next_noon - datetime.now()).total_seconds()
        await asyncio.sleep(duration)
        await client.send_message(channel, "It's high noon")
        await client.send_file(channel, 'files/mccree.png')
        next_noon += timedelta(days=1)