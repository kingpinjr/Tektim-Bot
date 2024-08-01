import random
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re

def generate_response(msg):
    '''
    Two types of messages should be send:
        1. When a message with <3 words is sent, send a predetermined message
        2. When a message with >=3 words is sent, send x on my y till she z
    '''
    msg_options = ['nyuck',
                   '?',
                   'shut up']
    
    stop_words = set(stopwords.words('english'))
    msg = re.sub(r'[^\w\s?!]', '', msg)
    msg = word_tokenize(msg) #this is... slow?
    filtered_sentence = [word for word in msg if word.lower() not in stop_words]

    if len(filtered_sentence) >= 3:
        random_words = random.sample(filtered_sentence, 3)
        response = "she " + random_words[0] + " on my " + random_words[1] + " till i " + random_words[2]
    else:
        response = random.choice(msg_options)
    return response

def generate_react_on_media():
    #If an image is sent, for now respond with an emote. 10 10 80 split
    rng = random.randrange(1, 10)
    reaction = ''
    match rng:
        case 1:
            reaction = "<:catchest:1267111295145087057>"
        case 2:
            reaction = "<:erm:1267111273275854908>"
        case 3:
            rng2 = random.rangrange(1, 100)
            if rng2 == 1:
                reaction = "<:golden_catchest:1268418504990654546>"

    return reaction

nltk.download('stopwords')
nltk.download('punkt')