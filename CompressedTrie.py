
def SearchInGivenTrie(word, HeadOfTrie):
    cur=HeadOfTrie
    for ch in word:
        if ch not in cur:
            #print("Not Found")
            #return
            return []
        cur=cur[ch]
    if '*' in cur:
        list=cur['*']
        #this gives the file posision in OccurrenceList for the given word 
        file_pos=list[1]
        #print(file_pos)
        with open("OccurrenceList.txt", "r") as f:
            f.seek(file_pos)
            line=f.readline()
            list=line.split()
            list.pop(0)
            #print("Websites containing the word: "+ word)
            #print(list)
            return list
    else:
        #print( "Not found")
        return []

#add a given word in compressed trie
def add(word, file_pos, HeadOfTrie):
    #print(file_pos)
    cur=HeadOfTrie
    for ch in word:
        if ch not in cur:
            cur[ch]={}
        cur=cur[ch]
    cur['*']=[True, file_pos]

#create a compressed trie from all words of file OccuranceList.txt 
def CreateCompressedTrie(filename, HeadOfTrie):
    with open(filename, "r") as f:
        file_pos=0
        for line in f:
            # print(file_pos)
            list=line.split()
            #print(list[0])
            add(list[0], file_pos, HeadOfTrie)
            file_pos+=len(line)


#print(head)
