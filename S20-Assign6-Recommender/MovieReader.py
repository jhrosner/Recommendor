'''
@author: julia rosner jhr44
'''


def getdata():
    '''
    This function reads data from a file and returns the data in the form of a two-tuple.
    The first element of the two-tuple is a list of strings, the second element is a
    dictionary.
    '''

    file= open("movies.txt", "r")
    words=[]
    for line in file:
        line=line.strip()
        line=line.split(",")
        number=line[2]
        line = line[1] + "," + line[0] + "," + number
        words.append(line)
    file.close()
    words.sort()
    newSort=[]
    for i in words:
        i=i.split(",")
        newSort.append(i)
    movieList=[]
    for i in newSort:
        if i[0] not in movieList:
            movieList.append(i[0])
    dict={}
    for k in newSort:
        dict[k[1]]=[0 for x in range(0,len(movieList))]

    for i in movieList:
        for k in newSort:
            if k[0]==i:
                index= movieList.index(i)
                dict[k[1]][index]= int(k[2])
    movieList=sorted(movieList)
    tuple = (movieList , dict)
    #print(len(movieList))
    return tuple

if __name__ == '__main__':
    print(getdata())