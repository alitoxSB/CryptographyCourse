import random
from random import randint

seed = randint(0,2)
abc = ["a","b","c"]

def pseudo_random(seed, random_word):
    """esta funcion genera dos sistemas alfanumericos aleatorios"""
    random_word = abc[seed]
    expand_seed = seed + (seed * 3)
    pseudo = [expand_seed,random_word]
    return pseudo

if __name__ == '__main__':
    print(pseudo_random(seed,abc))





