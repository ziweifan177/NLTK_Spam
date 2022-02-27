import nltk
from nltk.corpus import webtext
from nltk.probability import FreqDist
import wordcloud
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import string
import collections
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import pandas as pd
import codecs
import path_config

# nltk.download('punkt')
# nltk.download('stopwords')
csv_path = path_config.csv_path

words_path = r'D:\Other_Projects\NLTK\env_nltk\data\corpora\webtext'
# txt_path = r'D:\Other_Projects\NLTK\env_nltk\data\email_dataset.txt'
stopwords_file = r'D:\Other_Projects\NLTK\env_nltk\data\custom_stops.txt'

#==================Read email data================
df = pd.read_csv(csv_path)
#shape of the dataframe
print('The shape of the dataframe is :',df.shape)
#first few records
df.head()


spam1 = df[df.spam==1]
print(spam1.head())

#====================Data Cleaning and Preparation==================
#Before building the word cloud, it is important to clean the data
# 1. Converting the Text to Lower Case
spam1['Subject'] = spam1['Subject'].str.lower()
print(spam1['Subject'].head())


# 2. Splitting and Removing Punctuation from the Text
all_spam = spam1['Subject'].str.split(' ')
print(all_spam.head(4))

# 3. Stop words
default_stopwords = STOPWORDS
print('default_stopwords: ', default_stopwords)
custom_stopwords = set(codecs.open(stopwords_file, 'r', 'utf-8').read().splitlines())
print('custom_stopwords:', custom_stopwords)

all_stopwords = default_stopwords | custom_stopwords
print('all_stopwords:', all_stopwords)

# 4. Join all cleaned words
all_cleaned_word = []
for text in all_spam:
    print('****', text)
    text = [word.strip(string.punctuation) for word in text] # Remove punctuation
    text  = [word for word in text if not word.isnumeric()]  # Remove number
    text = [word for word in text if word not in all_stopwords and word!=''] #Remove stopwords

    print('===>', text)
    
    for cleaned_word in text:
        all_cleaned_word.append(cleaned_word)

print('All words after cleaning:', all_cleaned_word)


#=====================2. Get Frequency============================
fdist = nltk.FreqDist(all_cleaned_word)# Calculate frequency distribution
print(fdist)

for word, frequency in fdist.most_common(50): # Output top 50 words
    print(u'{};{}'.format(word, frequency))


#================3. Word Cloud for 'spam' Emails==============
# wordcloud_spam = WordCloud(background_color="white").generate_from_frequencies(fdist)
wordcloud_spam = WordCloud(stopwords=set(all_stopwords), background_color="white").generate_from_frequencies(fdist)
plt.imshow(wordcloud_spam, interpolation='bilinear')


plt.axis("off")
(-0.5, 399.5, 199.5, -0.5)
plt.show()

