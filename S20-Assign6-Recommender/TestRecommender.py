'''
@author: Julia Rosner
'''

import RecommenderEngine


def driver():
    
    (items,ratings) = SmallDukeEatsReader.getdata()
    print("items = ",items)
    print("ratings = ", ratings)

    
    avg = RecommenderEngine.averages(items,ratings)
    if avg == [('DivinityCafe', 4.0), ('TheCommons', 3.0),
                  ('Tandoor', 2.4285714285714284), ('IlForno', 1.8),
                  ('FarmStead', 1.4), ('LoopPizzaGrill', 1.0),
                  ('TheSkillet', 0.0), ('PandaExpress', -0.2),
                  ('McDonalds', -0.3333333333333333)]:
        print("AVERAGES WORKS")
    else:
        print("AVERAGES FAILS")

    print("average",avg)
     
    for key in ratings:
        slist = RecommenderEngine.similarities(key,ratings)
        print(key,slist)
        r3 = RecommenderEngine.recommendations(key,items,ratings,3)
        print("top",r3)
        
        
        
if __name__ == '__main__':
    driver()