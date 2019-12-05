from WebScrapping import WebCrawler
from AddToOccurrenceList import AddNewWordInOccurrenceList
from AddToOccurrenceList import CreateOccurrenceList
from CompressedTrie import SearchInGivenTrie, CreateCompressedTrie
from collections import OrderedDict, Counter

def CreateURLlist(URLlist):
    #health related data
    URLlist.append("https://www.webmd.com/living-healthy")
    #technology related data
    URLlist.append("https://www.cnet.com/news/")
    #history related data
    URLlist.append("https://www.ducksters.com/history/ancient_rome.php/")
    #electric car related data
    URLlist.append("https://electrek.co/guides/tesla/")
    #NJ restaurants related data
    URLlist.append("https://www.opentable.com/g/new-york-area/new-jersey-central-restaurants/")
    #movie related data
    URLlist.append("https://screenrant.com/movie-news/")
    #astronomy related data
    URLlist.append("http://www.astronomy.com/")

def SearchEngineOptimization(HeadOfTrie):
    sentence=input("Enter a collection of words to search:")
    words=sentence.split(' ')
    #empty dictionary
    TotalCounter={}
    TotalDict={}
    TotalList=[]
    #this for loop search each word given (two or more words) and take their union based on frequencies of words
    #if a word has same frequency on two different URLs then thier frequencies are added together
    for w in words:
        #print(w)
        list=SearchInGivenTrie(w, HeadOfTrie)
        i=0
        dict={}
        while i <= len(list)-1:
            w1=list[i]
            w2=list[i+1]
            dict[w2]=w1
            i=i+2
        #this will add all frequencies of a word if they are present on different URLs
        #to switch the key value role in a given dictionary
        inv_dict = {v: k for k, v in dict.items()}
        for keys in inv_dict: 
            inv_dict[keys] = int(inv_dict[keys]) 
        TotalCounter = Counter(TotalCounter)+Counter(inv_dict)
    #these line of code are used to print the URLs for the given words in descending order from high frequency to low frequency
    for key, value in TotalCounter.items():
        TotalDict[value]=key
    for i in TotalDict:
        TotalList.append(TotalDict[i])
    TotalList.reverse()
    print("URLs for the given keywords are given below:", sentence)
    for w in TotalList:
        print(w)
    #print(TotalList)
    #print(TotalCounter)



def __main__():
    URLlist=[]
    #Head of a trie with empty structure at initial condition
    HeadOfTrie={}

    # Inside this function, we add different URLs
    # I have used 7 different URLs from seven different areas as listed inside function in same file
    CreateURLlist(URLlist)
    
    #This function create a OccurrenceList in file OccurrenceList.txt
    #This should be call only once and no need to call for every search.
    # we need this function to create Occurrence list as explained in README.md
    #I already run the function and my OccurrenceList.txt file contains data.
    #It might take more time than expected, so please be patient.
    ###########CreateOccurrenceList(URLlist)################

    #This function is defined inside CompressedTrie.py
    CreateCompressedTrie("OccurrenceList.txt", HeadOfTrie)

    # this functions takes HeadOfTrie as input and asked for the collection of words to be searched
    # and find the URLs for individual words and print URLs based on word frequencies from high to low
    SearchEngineOptimization(HeadOfTrie)
    
#This is the call of main function which is used to create OccurrenceList and Compressed Trie
#Program starts from here. Please read README.md for detail.
__main__()