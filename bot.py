import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('2qbx'):
        await message.channel.send('oilllll')

client.run("ODEzMzc1Mzg2MDAzNTcwNzM4.YDOY2w.8eQDCy9yWtM191Si_G5nbvcAjrM")
