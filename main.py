import discord
from commands import *
client = discord.Client() # Establishes client
TOKEN = 'NzUxNTc3MjY3MDc5MjE3MjIz.X1LG4A.XfX2M2obWOioP6xKrANFoT6InC4' # This is the Bot's token... keep it safe!!!

@client.event
async def on_ready(): # Runs when the Bot first connects
    print('Diagnostics:')
    print('Connected as {0.user}'.format(client))  # Username
    print('Joining the following guilds:', end=""), print(await client.fetch_guilds(limit=150).flatten())
    print('Connection obtained via:', end=""), print(client.ws)
    print('Application information:', end=""), print(await client.application_info())
    print('Log:')

@client.event
async def on_message(message): # Runs when a message is sent
    if message.author == client.user: # Prevents the Bot from responding to itself
        return
    if message.content.startswith('!XKCD'): # Runs if the trigger is called
        response = get_response(message.content[5:])
        print('/// New command')
        print('Command: ', end=""), print(message.content)
        print('User: ', end=""), print(message.author)
        print('Response: ', end=""), print(response)
        await message.channel.send(response) # Sends message

# Commands to run the Bot itself
client.run(TOKEN)
client.login(TOKEN)
