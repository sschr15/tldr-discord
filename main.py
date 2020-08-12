import discord
import os
import sys
import datetime
import glob
import tldr


# noinspection SpellCheckingInspection
token: str = "revoked, accidentally made public"

# If you want a custom language, input the language as shown in the tldr pages here.
language = ""


# noinspection PyMethodMayBeStatic
class Client(discord.Client):
    async def on_ready(self):
        tldr.refresh_cache()
        print("tldr-bot is started!")

    async def on_message(self, message: discord.Message):
        content: str = message.content
        channel: discord.TextChannel = message.channel

        if content == "!tldrrefresh":
            tldr.refresh_cache()
            await channel.send("Cache refreshed!")
        elif content.startswith("!tldr"):
            if content.startswith("!tldros"):
                split_at = 2
            else:
                split_at = 1
            command = "-".join(content.split(" ")[split_at:])
            embed = tldr.parse(command, language, command[1] if bool(split_at - 1) else "common")
            await channel.send(embed=embed)


if __name__ == '__main__':
    client = Client()
    client.run(token)
