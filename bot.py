import discord
import json
import ocr
import cloze

#Loads config.json
with open("./config.json") as f:
    data = json.load(f)

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    # Never respond to own message
    if message.author == client.user:
        return

    # Scan image then respond with the ans
    if message.attachments and message.content == 'Ques':
        for attachment in message.attachments:
            await attachment.save(f'imgs/{attachment.filename}')
            await message.channel.send(ocr.ocr(f'imgs/{attachment.filename}'))
    
    if message.content.startswith('Q: '):
        await message.channel.send(cloze.clozer(message.content[3:]))

client.run(data["discordKey"])
