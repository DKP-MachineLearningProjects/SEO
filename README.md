# SEO (Search Engine Optimization)

############################################################################################################################
Basic Introduction

Dictionary is the core information stored by a search engine, where inverted index(or inverted file) are key-value pair. To implement inverted index, trie data structure is used and to store word (and its corresponding web URLs and frequency), occurrence list is maintained in secondary storage as shown in sample below:

First 10 samples taken from OccurrenceList.txt file

health https://www.webmd.com/living-healthy 200
healthy https://www.webmd.com/living-healthy 131
food https://www.webmd.com/living-healthy 90 https://www.opentable.com/g/new-york-area/new-jersey-central-restaurants/ 154
fitness https://www.webmd.com/living-healthy 79
find https://www.webmd.com/living-healthy 68 http://www.astronomy.com/ 97
beauty https://www.webmd.com/living-healthy 67
diet https://www.webmd.com/living-healthy 67
void https://www.webmd.com/living-healthy 66
living https://www.webmd.com/living-healthy 64
cancer https://www.webmd.com/living-healthy 64

Corresponding file pointer are stored in the leaf node of the trie for a particular word.

The URLs used to create a OccurrenceList from different area are:
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

##########################################
There are four different files that stores related functions and they are:
main.py
WebScrapping.py
CompressedTrie.py
AddToOccurrenceList.py

There are two different text files created during the execution of program
OccurrenceList.txt      #used by Search Engine
ExtractWords.txt        #temporarily used to create OccurrenceList for different URLs

############################################
About main.py

1. This function first calls CreateURLList() function to create a URLlist, URLlist contains all URLs from where we extract words
2. In second step, it calls CreateOccurrenceList(URLlist) which creates OccurrenceList.txt. This function should be call only once.
3. In third step, CreateCompressedTrie() function is called and corresponding trie is stored in HeadOfTrie. Each leaf node of trie contains a file pointer in secondary storage and fetch only needed data from OccurrenceList.txt file.
4. In fourth and final step, SearchEngineOptimization() function is called with HeadOfTrie as input. This function asks for different words to search from OccurrenceList. It first search a word in Trie and if present in trie, it fetch the entry of the word from Occurrence list.

##########################################
WebScrapping.py 

This python file contains functions that extracts words from given URLs and their corresponding frequencies.

##########################################
CompressedTrie.py

This python file contains functions related to creating tries used for our search engine.

###########################################
AddToOccurrenceList.py

This python file contains functions related to create OccurrenceList required to store huge information on secondary storage. Each entry in Occurrence List linked to HeadOfTrie created.



############################################################################################################################
