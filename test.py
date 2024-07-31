import random
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('stopwords')
nltk.download('punkt')

msg = "Hello this is Tigm"
stop_words = set(stopwords.words('english'))
msg = word_tokenize(msg) #this is... slow?
filtered_sentence = [word for word in msg if word.lower() not in stop_words]

print(filtered_sentence)