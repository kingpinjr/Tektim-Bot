import random

def generate_response():
    # temporary solution for interactions for now
    print('generating response')
    msg_options = ['nyuck',
                   '?',
                   'shut up']
    return random.choice(msg_options)