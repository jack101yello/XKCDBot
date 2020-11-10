import discord
from commands import *
client = discord.Client() # Establishes client
TOKEN = '' # This is the Bot's token... keep it safe!!!

@client.event
async def on_ready(): # Runs when the Bot first connects
    print('Connected as {0.user}'.format(client)) # Connection confirmation

@client.event
async def on_message(message): # Runs when a message is sent
    if message.author == client.user: # Prevents the Bot from responding to itself
        return
    if message.content.startswith('!XKCD'): # Runs if the trigger is called
        await message.channel.send(get_response(message.content[5:])) # Sends message

# Commands to run the Bot itself
client.run(TOKEN)
client.login(TOKEN)
