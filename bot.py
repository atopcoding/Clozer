import discord
import cloze

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    print(message.attachments)

    if message.content.startswith('Q: '):
        await message.channel.send(cloze.cloze(message.content[3:]))

client.run("ODEzMzc1Mzg2MDAzNTcwNzM4.YDOY2w.qYt4E4amESiwP2RovbWDUpS_lGo")

