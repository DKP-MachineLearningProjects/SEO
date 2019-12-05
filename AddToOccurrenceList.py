from WebScrapping import WebCrawler

#Create OccurrenceList.txt for all the URLs provided
def CreateOccurrenceList(URLlist):
    open('OccurrenceList.txt', 'r+').truncate(0)
    for newURL in URLlist:
        #this function puts all words and frequency into a file named ExtractWords.txt
        WebCrawler(newURL)
        #now the file ExtractWords.txt contains all words and their frequencies
        f=open("ExtractWords.txt", "r")
        #i=0
        for line in f:
            words=line.split()
            AddNewWordInOccurrenceList(words[0],newURL,words[1],"OccurrenceList.txt")
            # i=i+1
            # if(i==20):
            #     break
        f.close()

#this function add a word and its frequency in OccurrenceList.txt file with URL as well.
def AddNewWordInOccurrenceList(wordtoadd, url, freq, filename):
    fin=open(filename, "r")
    fout=open("temp.txt","w")
    wordFound=False

    for line in fin:
        words=line.split()
        if(words[0]==wordtoadd):
            wordFound=True
            #fout.write(line.replace('tello','hello'))
            fout.write(line.rstrip('\n')+" "+url+" "+str(freq)+'\n')
        else:
            fout.write(line)
    #if word is already not in occurrence list, then add a fresh copy with corresponding url.
    if(wordFound == False):
        fout.write(wordtoadd+" "+url+" "+str(freq)+'\n')
    fin.close()
    fout.close()

    fout=open(filename, "w")
    fin=open("temp.txt","r")
    for line in fin:
        fout.write(line)
    fin.close()
    fout.close()


#inputs are word to add, the url where the word is in, words frequency and file for occurrence list
#this function for local checking of the working. Not important
#AddNewWordInOccurrenceList("he", "www.helloworld.com", 5, "NewOccurrenceList.txt")