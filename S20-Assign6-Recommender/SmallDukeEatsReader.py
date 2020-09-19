import json

def getdata():

    st = open("data/food.json").read()
    ratings = json.loads(st)
    st = open("data/eateries.txt").read()
    places = json.loads(st)

    return (places,ratings)


if __name__ == '__main__':
    items, ratings = getdata()
    print(items)
    print(ratings)