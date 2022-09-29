from sentences import get_determiner, get_noun, get_verb
import random
import pytest


def test_get_determiner():
    # 1. Test the single determiners.

    single_determiners = ["a", "one", "the"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_determiner(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["some", "many", "the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners
    print(f"Aqui está a palavra {word}")


def test_get_noun():
    # 1. Test the single determiners.

    single_noun = ["birds", "boys", "cars", "cats", "children"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_noun(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_noun

    # 2. Test the plural determiners.

    plural_noun = ["dogs", "girls", "men", "rabbits", "women"]
    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_noun(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
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


pytest.main(["-v", "--tb=line", "-rN", __file__])


