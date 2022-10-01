from sentences import get_determiner, get_noun, get_verb, get_prepositional_phrase, get_adjective
import random
import pytest


def test_get_determiner():

    single_determiners = ["a", "one", "the"]

    for _ in range(4):

        word = get_determiner(1)
        assert word in single_determiners

    plural_determiners = ["some", "many", "the"]

    for _ in range(4):

        word = get_determiner(2)
        assert word in plural_determiners

def test_get_adjective():
    
    words = ["pretty", "annoying", "still", "funny", "noisy"]
    word = get_adjective()
    assert word in words


def test_get_noun():

    single_noun = ["bird", "boy", "car", "cat", "children"]

    for _ in range(4):

        word = get_noun(1)
        assert word in single_noun

    plural_noun = ["dogs", "girls", "men", "rabbits", "women"]
    
    for _ in range(4):

        word = get_noun(2)
        assert word in plural_noun


def test_get_verb():

    verb_past = ["drank", "ate", "grew", "laughed",
                 "thought", "ran", "slept", "talked", "walked", "wrote"]

    for _ in range(4):

        word = get_verb(1, tense="past")
        assert word in verb_past

    verb_present = ["drinks", "eats", "grows", "laughs", "thinks",
                    "runs", "sleeps", "talks", "walks", "writes"]

    for _ in range(4):

        word = get_verb(1, "present")
        assert word in verb_present

    plural_verb_present = ["drink", "eat", "grow", "laugh", "think",
                           "run", "sleep", "talk", "walk", "write"]

    for _ in range(4):

        word = get_verb(2, "present")
        assert word in plural_verb_present

    future = ["will drink", "will eat", "will grow", "will laugh",
              "will think", "will run", "will sleep", "will talk",
              "will walk", "will write"]
    for _ in range(4):
        word = get_verb(1, "future")
        assert word in future



def test_get_prepositional_phrase():
    prepositions = ["about", "above", "across", "after", "along",
    "around", "at", "before", "behind", "below",
    "beyond", "by", "despite", "except", "for",
    "from", "in", "into", "near", "of",
    "off", "on", "onto", "out", "over",
    "past", "to", "under", "with", "without"]

    for _ in range(4):
        word = get_prepositional_phrase(1)
        new_word = word.split()
        assert new_word[0] in prepositions
    
    for _ in range(4):
        word = get_prepositional_phrase(2)
        new_word = word.split()
        assert new_word[0] in prepositions



pytest.main(["-v", "--tb=line", "-rN", __file__])


