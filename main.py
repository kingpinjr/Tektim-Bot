# main script for bot
import os
import discord
import model
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TEKTIM_TOKEN')
GUILD = os.getenv('DISCORD_SERVER')

#print(TOKEN)
intents=discord.Intents.default()
intents.members = True
intents.message_content = True
client = discord.Client(intents=intents)

# event handling
@client.event
async def on_ready():
    # locate the server that is in your env variable
    guild = discord.utils.get(client.guilds, name=GUILD)

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

    #this lists who is in the server
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Server Members:\n - {members}')

# bot response for user joining server
@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send('nyuck')

# bot response for messages
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # respond with emoji at this cringe behavior
    if(message.content.lower() == 'owo' or message.content.lower()=='uwu'):
        await message.channel.send('<:erm:1267111273275854908>')

    # admin: exception handling example
    elif (message.content.strip() == 'raise-exception' and message.author.strip() == 'tigm'):
        raise discord.DiscordException
    
    # finally if some random message is seen log it here for now
    else:
        print('\nAuthor: ', message.author)
        print('Message: ', message.content)
        response = model.generate_response()
        await message.channel.send(response)


# error-handling. Gets sent to err.log
@client.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise

client.run(TOKEN)
