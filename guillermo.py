import random

color_list = [0,1,2,3]
GameOrder = []

'''
Pone en una lista el orden del nivel
'''
def Return_GameOrder (level):
    #Returns a list of the level
    global GameOrder
    Increase = int((level/5)+1)

    for i in range (Increase):
        GameOrder+=[random.choice(color_list)]

    return (GameOrder)

def reset_GameOrder ():
    #reserts the list of notes
    global GameOrder
    GameOrder = []