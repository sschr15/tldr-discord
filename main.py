import discord
import os
import sys
import datetime
import glob
import tldr


# noinspection SpellCheckingInspection
token: str = "NzQyODAwNTA3MjEwMzAxNTIw.XzLY4Q.ujWraK6YPI775Sheb3Ym_KSBqT8"


# noinspection PyMethodMayBeStatic
class Client(discord.Client):
    async def on_ready(self):
        tldr.refresh_cache()
        print("tldr-bot is started!")

    async def on_message(self, message: discord.Message):
        content: str = message.content
        channel: discord.TextChannel = message.channel

        if content.startswith("!tldr "):
            command = "-".join(content.split(" ")[1:])
            embed = tldr.parse(command)
            await channel.send(embed=embed)
        elif content == "!tldrrefresh":
            tldr.refresh_cache()
            await channel.send("Cache refreshed!")


if __name__ == '__main__':
    client = Client()
    client.run(token)
