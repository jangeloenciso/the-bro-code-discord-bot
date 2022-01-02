import os
import discord
import random
from dotenv import load_dotenv
from broticles import articles

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome mf testing lang!'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    content = message.content
    j = ""
    for i in content:
        if i.isdigit():
            j += i
    ref = int(j)    
    print(j)

    if content == 'BroCode!':
        response = random.choice(articles)
        await message.channel.send(response)
    elif j != -1:
        if 'BroCode!' in content:
            if ref in articles:
                response = articles[ref]
                await message.channel.send(response)
            else:
                response = ".... that's not in The Bro Code, bro."
                await message.channel.send(response)
    elif message.content == 'raise-exception':
        raise discord.DiscordException
        
client.run(TOKEN)