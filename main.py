from WebScrapping import WebCrawler
from AddToOccurrenceList import AddNewWordInOccurrenceList
from AddToOccurrenceList import CreateOccurrenceList
from CompressedTrie import SearchInGivenTrie, CreateCompressedTrie

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



def __main__():
    URLlist=[]
    #Head of a trie with empty structure at initial condition
    HeadOfTrie={}
    CreateURLlist(URLlist)
    
    #This function create a OccurrenceList in file OccurrenceList.txt
    #This should be call only once and no need to call for every search
    CreateCompressedTrie("OccurrenceList.txt", HeadOfTrie)
    
    
    SearchInGivenTrie("black", HeadOfTrie)

#This is the call of main function which is used to create OccurrenceList and Compressed Trie
#        
__main__()