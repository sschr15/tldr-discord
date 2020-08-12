# TLDR Discord Bot

This is a simple Discord bot that accesses the [TLDR man pages](https://tldr.sh).

## Running

If you don't want to go through the hassle of setting it up yourself, I host an english version on my own computer that you can
[easily add to your server!](https://discord.com/api/oauth2/authorize?client_id=742800507210301520&permissions=18432&scope=bot)

If you don't want to use that, see the instructions below.

## Building

[Python 3](https://python.org) is required.

1. Clone this repository
2. Install the requirements
    - *nix: `python3 -m pip install -r requirements.txt`
    - Windows: `pip install -r requirements.txt`
3. [Create a Discord bot](https://discord.com/developers/applications)
4. In `main.py`, replace the contents of `token` with the bot token
5. Optional: Change the language by 
  [changing the `language` variable](https://github.com/sschr15/tldr-discord/blob/master/main.py#L13)
6. Run the program
    - *nix: `python3 main.py`
    - Windows: `python main.py`
