# this program extracts all words in a given URL and store them in ExtracWords.txt file

from bs4 import BeautifulSoup
import requests
import urllib
from bs4.element import Comment
from collections import Counter
from string import punctuation
import urllib.request
from nltk.corpus import stopwords #/home/suraja/nltk_data/corpora/stopwords
from nltk.corpus import wordnet #/home/suraja/nltk_data/corpora/wordnet


#this function extracts all words and their frequencies form an URL and stores them in ExtractWords.txt file. 
def WebCrawler(URL):
    #URL = "https://www.crummy.com/software/BeautifulSoup/bs4/doc/"
    r = requests.get(URL) 
  
    soup = BeautifulSoup(r.content,'html.parser') 
    text = (''.join(s.findAll(text=True))for s in soup.findAll())
    c = Counter((x.rstrip(punctuation).lower() for y in text for x in y.split()))
    list=c.most_common()

    stop_words = set(stopwords.words('english')) 
    f = open("ExtractWords.txt", "w")
    for i in range(len(list)):
        if(list[i][0].isalpha()):
            if list[i][0] not in stop_words:
                if wordnet.synsets(list[i][0]):
                    line=str(list[i][0]) + " " + str(list[i][1]) +'\n'
                    f.write(line)
    f.close()