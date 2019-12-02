head={}

def add(word, file_pos):
    global head
    print(file_pos)
    cur=head
    for ch in word:
        if ch not in cur:
            cur[ch]={}
        cur=cur[ch]
    cur['*']=[True, file_pos]


def search(word):
    global head
    cur=head
    for ch in word:
        if ch not in cur:
            print("Not Found")
            return
        cur=cur[ch]
    if '*' in cur:
        list=cur['*']
        file_pos=list[1]
        print(file_pos)
        with open("OccurrenceList.txt", "r") as f:
            f.seek(file_pos)
            line=f.readline()
            list=line.split()
            list.pop(0)
            print("Websites containing the word: "+ word)
            print(list)
    else:
        print( "Not found")


with open("OccurrenceList.txt", "r") as f:
    file_pos=0
    for line in f:
        # print(file_pos)
        list=line.split()
        print(list[0])
        add(list[0], file_pos)
        file_pos+=len(line)

search("apple")

print(head)
