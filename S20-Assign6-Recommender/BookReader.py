'''
@author: Julia Rosner jhr44
'''


def getdata():

    '''
    This function reads data from a file and returns the data in the form of a two-tuple.
    The first element of the two-tuple is a list of strings, the second element is a
    dictionary.
    '''

    file= open("books.txt", "r")
    words=[]
    for line in file:
        line=line.strip()
        line=line.split(",")
        words.append(line)
    file.close()

    bookList=[]
    k=1
    while k< len(words[0]):
        k+=2
    dict ={}
    listRate=[]

    for k in words:
        student=k[0]
        i=2
        while i < len(k):
            listRate.append(int(k[i]))
            i+=2
        dict[student]= listRate
        listRate=[]
    tuple=(bookList, dict)
    return tuple


if __name__ == '__main__':
    print(getdata())
