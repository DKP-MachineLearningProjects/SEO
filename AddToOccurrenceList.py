
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

    fout=open("NewOccuranceList.txt", "w")
    fin=open("temp.txt","r")
    for line in fin:
        fout.write(line)
    fin.close()
    fout.close()

#inputs are word to add, the url where the word is in, words frequency and file for occurrence list
AddNewWordInOccurrenceList("he", "www.helloworld.com", 5, "NewOccurrenceList.txt")