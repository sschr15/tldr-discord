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
            if content == "!tldros":
                embed = discord.Embed(
                    title="OS Command",
                    color=0x00FE4D,
                    description="Request a tldr, prioritizing an OS.\nOptions are `linux`, `windows`, `osx`, and `sunos`."
                )
            elif content == "!tldrlang":
                embed = discord.Embed(
                    title="Language Command",
                    color=0x00FE4D,
                    description="Request a tldr, in a certain language if possible.\nAvailable options are:\n`" + "`, `".join(tldr.languages()) + "`"
                )
            elif content == "!tldr":
                embed = discord.Embed(
                    title="tldr",
                    color=0xA930D9,
                    description="man pages made simple"
                )
                embed.set_footer(text="Discord bot created by sschr15")
            else:
                custom_os = False
                custom_lang = False
                if content.startswith("!tldros"):
                    split_at = 2
                    custom_os = True
                elif content.startswith("!tldrlang"):
                    split_at = 2
                    custom_lang = True
                else:
                    split_at = 1
                command = "-".join(content.split(" ")[split_at:])
                first = content.split(" ")[1]
                embed = tldr.parse(command, first if custom_lang else language, first if custom_os else "common")
            await channel.send(embed=embed)


if __name__ == '__main__':
    client = Client()
    client.run(token)
