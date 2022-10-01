import random

from pyparsing import Word

def main():
    print(get_determiner(1), get_adjective(), get_noun(1), get_verb(1, "past"), get_prepositional_phrase(1), get_prepositional_phrase(1))
    print(get_determiner(1), get_adjective(), get_noun(1), get_verb(1, "present"), get_prepositional_phrase(1), get_prepositional_phrase(1))
    print(get_determiner(1), get_adjective(), get_noun(1), get_verb(1, "future"), get_prepositional_phrase(1), get_prepositional_phrase(1))
    print(get_determiner(2), get_adjective(), get_noun(2), get_verb(2, "past"), get_prepositional_phrase(2), get_prepositional_phrase(2))
    print(get_determiner(2), get_adjective(), get_noun(2), get_verb(2, "present"), get_prepositional_phrase(2), get_prepositional_phrase(2))
    print(get_determiner(2), get_adjective(), get_noun(2), get_verb(2, "future"), get_prepositional_phrase(2), get_prepositional_phrase(2))
    
    

def get_determiner(quantity):

    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word


def get_adjective():
    words = ["pretty", "annoying", "still", "funny", "noisy"]
    word = random.choice(words)
    return word


def get_noun(quantity):
 
    if quantity == 1:
        words = ["bird", "boy", "car", "cat", "children"]
    else:
        words = ["dogs", "girls", "men", "rabbits", "women"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word


def get_verb(quantity, tense):

    if tense == "past":
        words = ["drank", "ate", "grew", "laughed", "thought",
                 "ran", "slept", "talked", "walked", "wrote"]
    elif quantity == 1 and tense == "present":
        words = ["drinks", "eats", "grows", "laughs", "thinks",
                 "runs", "sleeps", "talks", "walks", "writes"]
    elif quantity > 1 and tense == "present":
        words = ["drink", "eat", "grow", "laugh", "think",
                 "run", "sleep", "talk", "walk", "write"]

    elif tense == "future":
        words = ["will drink", "will eat", "will grow", "will laugh",
                 "will think", "will run", "will sleep", "will talk",
                 "will walk", "will write"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word


def get_preposition():
    prepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]

    word = random.choice(prepositions)
    return word

def get_prepositional_phrase(quantity):
    if quantity == 1:
        preposition = get_preposition() 
        determiner = get_determiner(1)
        noun =  get_noun(1)
    elif quantity > 1:
        preposition = get_preposition() 
        determiner = get_determiner(2)
        noun =  get_noun(2)

    
    phrase = (f"{preposition} {determiner} {noun}")
  
    return phrase

if __name__ == ("__main__"):
    main()



