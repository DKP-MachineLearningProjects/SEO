from bs4 import BeautifulSoup
import requests
import urllib
from bs4.element import Comment
from collections import Counter
from string import punctuation
import urllib.request
from nltk.corpus import stopwords 
from nltk.corpus import wordnet

stop_words = set(stopwords.words('english')) 
 
#URL = "https://www.crummy.com/software/BeautifulSoup/bs4/doc/"
URL = "https://www.webmd.com/living-healthy"
r = requests.get(URL) 
  
soup = BeautifulSoup(r.content,'html.parser') 
text = (''.join(s.findAll(text=True))for s in soup.findAll())
c = Counter((x.rstrip(punctuation).lower() for y in text for x in y.split()))
list=c.most_common()

f = open("ExtractWords.txt", "w")
for i in range(len(list)):
    if(list[i][0].isalpha()):
        if list[i][0] not in stop_words:
            if wordnet.synsets(list[i][0]):
                line=str(list[i][0]) + "\t\t\t\t\t\t\t" + str(list[i][1]) +"\n"
                f.write(line)
f.close()
#print (l[0][1]) # prints most common words staring at most common.