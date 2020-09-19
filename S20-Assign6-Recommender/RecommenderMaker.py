'''
@author: Julia Rosner jhr44
'''

import RecommenderEngine

def makerecs(name, items, ratings, numUsers, top):
    '''
    This function calculates the top recommendations and returns a two-tuple consisting of two lists.
    The second list is the top items not seen/rated by name (string)
    '''
    newAverages = RecommenderEngine.recommendations(name, items, ratings, numUsers)
    eaten = []
    notEaten = []
    i = 0
    for item in newAverages:
        if ratings[name][items.index(item[0])] != 0:
            eaten.append(newAverages[i])
            i += 1
        if ratings[name][items.index(item[0])] == 0:
            notEaten.append(newAverages[i])
            i += 1
    eaten = sorted(eaten, key=lambda x: x[0])
    eaten = sorted(eaten, key = lambda x:x[1], reverse=True)
    eaten = eaten[0:top]
    notEaten = sorted(notEaten, key=lambda x:x[0])
    notEaten = sorted(notEaten, key=lambda x:x[1], reverse=True)
    notEaten = notEaten[0:top]

    return (eaten,notEaten)

if __name__ == '__main__':
    items = ["DivinityCafe", "Farmstead", "IlForno", "LoopPizzaGrill", "McDonalds", "PandaExpress", "Tandoor", "TheCommons", "TheSkillet"]


