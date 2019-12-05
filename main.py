from WebScrapping import WebCrawler
from AddToOccurrenceList import AddNewWordInOccurrenceList

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


def main():
    URLlist=[]
    CreateURLlist(URLlist)
    for newURL in URLlist:
        if newURL=="https://electrek.co/guides/tesla/":
            WebCrawler(newURL)
        f=open("ExtractWords.txt", "r")
        i=1
        for line in f:
            words=line.split()
            AddNewWordInOccurrenceList(words[0],newURL,words[1],"OccurrenceList.txt")
            i=i+1
            if(i==5):
                break
        f.close()

main()