import discord
import random

TOKEN = 'NDM5MTAzNjQyMTI2MTIzMDE4.DcOf9g.dNGLrcju5jGe5bMpcTLF3zxpwhA'

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('!rolldice'):
        x = random.randint(1,6)
        msg = 'You rolled a ' + str(x)
        await client.send_message(message.channel, msg)
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)