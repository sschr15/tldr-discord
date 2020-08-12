from typing import List, Optional, Tuple
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


def get_or_none(name: str, language: str = "", preferred_os: str = "common") -> Tuple[Optional[str], str]:
    """
    Get the markdown file, or None if it doesn't exist
    """
    if name.startswith("pages"):
        if name in cache:
            with zipfile.ZipFile("tldr.zip") as zf:
                file_loc = zf.extract(name)
            with open(file_loc) as file:
                return file.read(), ""
        else:
            return None, ""
    else:
        for i in [preferred_os, "common", "linux", "windows", "osx", "sunos"]:
            results = get_or_none(f'pages{"." + language if language else ""}/{i}/{name}.md')
            if results == (None, "") and language:
                results = get_or_none(name)
            elif results != (None, ""):
                break
        return results[0], i


def parse(name: str, language: str = "", preferred_os="common") -> discord.Embed:
    """
    Take a command and return a Discord Embed of the tldr command

    :param name: the command (using dashes in place of spaces)
    :param language: the language to use for the pages, or an empty string for English
    :param preferred_os: the OS to check first
    :return: an embed of the tldr file
    """
    file = get_or_none(name, language, preferred_os)
    if file[0]:
        lines = file[0].replace("\n\n", "\n").splitlines()
        title = lines[0][2:]
        embed = discord.Embed(
            title=title + ("" if preferred_os == file[1] else f' ({file[1]})'),
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
