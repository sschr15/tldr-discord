from typing import List, Optional
import zipfile
import discord

cache: List[str] = []


def refresh_cache():
    """
    Update the zip file and refresh the file list cache
    :return: the list of files in the zip file
    """
    global cache
    import requests

    file = requests.get("https://tldr-pages.github.io/assets/tldr.zip").content
    with open("tldr.zip", "wb") as zf:
        zf.write(file)
    with zipfile.ZipFile("tldr.zip") as zf:
        cache = zf.namelist()


def get_or_none(name: str) -> Optional[str]:
    """
    Get the markdown file, or None if it doesn't exist
    :param name: the name of the command (dashes replacing spaces)
    """
    if name.startswith("pages/"):
        if name in cache:
            with zipfile.ZipFile("tldr.zip") as zf:
                file_loc = zf.extract(name)
            with open(file_loc) as file:
                return file.read()
        else:
            return None
    else:
        for i in ["common", "linux", "windows", "macos", "sunos"]:
            results = get_or_none(f'pages/{i}/{name}.md')
            if results is not None:
                break
        return results


def parse(name: str) -> discord.Embed:
    """
    Take a command and return a Discord Embed of the tldr command

    :param name: the command (using dashes in place of spaces)
    :return: an embed of the tldr file
    """
    file = get_or_none(name)
    if file:
        lines = file.splitlines()
        title = lines[0][2:]
        embed = discord.Embed(
            title=title,
            colour=0x00F0FF,
            description="\n".join(lines[1:]).strip()
        )
        return embed
    else:
        return discord.Embed(
            title="No item found!",
            colour=0xF23C3C,
            description="The database does not include this item! Send `!tldrrefresh` to refresh the cache."
        )
