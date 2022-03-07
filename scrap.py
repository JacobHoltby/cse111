from sentences import get_determiner, get_noun, get_preposition, get_prepositional_phrase
import random
import pytest

def test_get_prepositional_phrase():
    list_of_prepositions = ['about', 'above', 'across', 'after', 'along',
        'around', 'at', 'before', 'behind', 'below',
        'beyond', 'by', 'despite', 'except', 'for',
        'from', 'in', 'into', 'near', 'of',
        'off', 'on', 'onto', 'out', 'over',
        'past', 'to', 'under', 'with', 'without']

    for _ in range(30):
        preposition = get_preposition()

    single_determiners = ["a", "one", "the"]
    for _ in range(4):
        word = get_determiner(1)
        
    plural_determiners = ["two", "some", "many", "the"]
    for _ in range(4):
        quantity = random.randint(2, 11)
        word = get_determiner(quantity)

    single_nouns = ['bird', 'boy', 'car', 'cat', 'child', \
            'dog', 'girl', 'man', 'rabbit', 'woman']

    for _ in range(11):
        noun = get_noun(1)

    plural_nouns = ['birds', 'boys', 'cars', 'cats', 'children', \
            'dogs', 'girls', 'men', 'rabbits', 'women']

    for _ in range(11):
        quantity = random.randint(2, 11)
        noun = get_noun(quantity)

    prepositional_phrase = f'{preposition} {word} {noun}'
    check_it = prepositional_phrase.split()
    assert check_it


pytest.main(["-v", "--tb=line", "-rN", __file__])