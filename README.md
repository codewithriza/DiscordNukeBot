# Discord Nuke Bot 💀

This Discord bot is designed for a specific purpose: to quickly and dramatically alter a Discord server by deleting all existing channels and roles, then creating a large number of new channels and roles. This can be useful for testing server resilience, creating chaos for fun, or any other scenario where you need to drastically change the server's structure.



> [!note]  
> This bot should be used with caution and only in servers where you have permission to make such drastic changes. It is recommended to use this bot in a controlled environment or on a server dedicated for testing purposes.

## Features

- Nuke command to delete all channels, create new channels, and modify roles.
- Customizable settings for channel names, role names, and batch sizes.
- Integration with the Discord API to perform actions efficiently.


> [!IMPORTANT]  
> **Use for educational purposes only! Do not use this bot against anyone.**


## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/discord-nuke-bot.git
   ```

2. Install the required dependencies:
   ```bash
   pip install discord asyncio python-dotenv
   ```

3. Go to the [Discord Developers Portal](https://discord.com/developers/applications) and create a new application.

4. Grab the bot token and guild ID and put them in the `.env` file:

   ```makefile
   BOT_TOKEN=paste_the_token
   GUILD_ID=paste_the_guild_id
   ```

5.Customize the message and other parameters in the `main.py` file.

6.Run the bot: 
   ```bash
   python3 main.py
   ```

## Support

If you need help, please create an [issue](https://github.com/codewithriza/DiscordNukeBot/issues) in the repo and we will check it as soon as possible.




