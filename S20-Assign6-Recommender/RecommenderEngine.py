'''
@author: Julia Rosner jhr44
'''


def averages(items, ratings):
    '''
    This function calculates the average ratings for items.
    A two-tuple is returned, where the first element is a string and the second element is a float.
    '''

    guy = {}
    count = []
    for item in items:
        guy[item] = 0
        count.append(0)

    for v in ratings.values():
        i = 0
        for thing in v:
            guy[items[i]] += thing
            if thing != 0:
                count[i] += 1
            i += 1
    finalAve = []
    i = 0
    for item in items:
        if count[i] != 0:
            finalAve.append((item, float((guy[item] / count[i]))))
            i += 1
        else:
            finalAve.append((item, float(0)))
            i += 1
    finalAve.sort(key=lambda x: x[0])
    finalAve.sort(key=lambda x: x[1], reverse=True)
    return finalAve


def similarities(name, ratings):
    '''
    This function calculates how similar the rater called name is to all other raters.
    A two-tuple is returned, where the first element is a string and the second element is an integer.
    '''
    interSim = {}
    finalSim = []
    for k,v in ratings.items():
        i = 0
        if k != name:
            interSim[k] = 0
            for rating in v:
                interSim[k] += (rating * ratings[name][i])
                i +=1
    for k,v in interSim.items():
        finalSim.append((k,v))
    finalSim.sort(key=lambda x: x[0])
    finalSim.sort(key=lambda x: x[1], reverse=True)
    return finalSim


def recommendations(name, items, ratings, numUsers):
    '''
    This function calculates the weighted average ratings and makes recommendations
    based on the parameters and weighted average. A two-tuple is returned, where
    the first element is a string and the second element is a float.
    '''
    sim = similarities(name, ratings)
    newRatings = ratings.copy()
    del newRatings[name]

    for person in sim:
        i = 0
        for v in newRatings[person[0]]:
            x = v * person[1]
            newRatings[person[0]][i] = x
            i += 1
    finalRatings = {}
    for k,v in newRatings.items():
        for guy in sim[:numUsers]:
            if k == guy[0]:
                finalRatings[k] = v
    ave = averages(items, finalRatings)
    return ave


if __name__ == '__main__':
    ratings = {"Sarah Lee":
                   [3, 3, 3, 3, 0, -3, 5, 0, -3],
               "Melanie":
                   [5, 0, 3, 0, 1, 3, 3, 3, 1],
               "J J":
                   [0, 1, 0, -1, 1, 1, 3, 0, 1],
               "Sly one":
                   [5, 0, 1, 3, 0, 0, 3, 3, 3],
               "Sung-Hoon":
                   [0, -1, -1, 5, 1, 3, -3, 1, -3],
               "Nana Grace":
                   [5, 0, 3, -5, -1, 0, 1, 3, 0],
               "Harry":
                   [5, 3, 0, -1, -3, -5, 0, 5, 1],
               "Wei":
                   [1, 1, 0, 3, -1, 0, 5, 3, 0]}

    items = ["DivinityCafe", "FarmStead", "IlForno",
             "LoopPizzaGrill", "McDonalds", "PandaExpress",
             "Tandoor", "TheCommons", "TheSkillet"]

    recommendations("Sarah Lee", items, ratings, 2)