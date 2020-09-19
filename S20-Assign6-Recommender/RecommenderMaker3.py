'''
@author: Julia Rosner jhr44
'''

import RecommenderEngine

def makerecs(name, items, ratings, numUsers, top):
    '''
    This function calculates the top recommendations and returns a two-tuple consisting of two lists.
    The second list is the top items not seen/rated by name (string)
    '''

    newList = RecommenderEngine.recommendations(name, items, ratings, numUsers)
    topThree=[]
    person= []
    for i in ratings:
        if i== name:
            person= ratings[i]
            break
    counter=0
    for i in range(0, len(items)):
        if counter== top:
            break
        if person[i]==0:
            tuple= (items[i], newList[i][1])
            topThree.append(tuple)
            counter+=1
    if len(topThree):
        for i in range(0,top):
            topThree.append(newList[i])
    return topThree


if __name__ == '__main__':
    name = 'Jeanice'
    items = ['lions', 'tigers', 'bears']
    ratings = dict([('Nohemi', [1, -2, 1]), ('Ines', [-2, 2, 0]), ('Evelynn', [-1, -2, -1]), ('Jeanice', [1, -2, 1])])
    size = 2
    sim = RecommenderEngine.similarities(name, ratings)
    print('sim =', sim) # Printing for your convenience

    ret = RecommenderEngine.recommendations(name, items, ratings, size)
    print(ret[0][0])
    print(ret[0][1])
             



