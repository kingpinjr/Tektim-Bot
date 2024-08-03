import discord
import datetime

def retrieve(channel, server):
    one_week_ago = datetime.datetime.now() - datetime.timedelta(days=7)
    messages = []
    
    for message in channel.history(after=one_week_ago):
        messages.append(message)
    print('hi')