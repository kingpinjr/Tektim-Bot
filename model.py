import random
import pandas as pd

'''
raw data needed for preprocessing:
    1. Input: what prompted my message
    2. Response: my message
    3. Other features: other things that could influence my response
        - time of day
        - user
        - which server its in
    
        Note: Due to dataset size it may be not in my best interest to make it too complex

'''

df = pd.read_csv('data/test_sheet.csv')
df = df[['userName', 'content','date']]
print(df.head(5))

def train_data():
    print('admin function train_data')

def generate_response():
    print('generating response')
    msg_options = ['nyuck',
                   '?',
                   'shut up']
    return random.choice(msg_options)