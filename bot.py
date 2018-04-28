import asyncio
import discord
from discord.ext.commands import Bot
client = discord.Client()

@client.event
async def on_ready():
    print ("Running")
    await client.change_presence(game=discord.Game(name="Try"))

@client.event

async def on_message(message):
 if message.content.startswith("im"):
     
    variable = message.content[len('im'):].strip()
    v2 = 'Hi ' + variable + ", I'm Mom!"
    await client.send_message(message.channel, v2)

 
client.run('process.env.BOT_TOKEN')
