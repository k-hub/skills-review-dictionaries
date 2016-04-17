"""Skills-dictionaries.

**IMPORTANT:** these problems are meant to be solved using
dictionaries and sets.
"""


def without_duplicates(words):
    """Given a list of words, return list with duplicates removed.

    For example::

        >>> sorted(without_duplicates(
        ...     ["rose", "is", "a", "rose", "is", "a", "rose"]))
        ['a', 'is', 'rose']

    You should treat differently-capitalized words as different::

        >>> sorted(without_duplicates(
        ...     ["Rose", "is", "a", "rose", "is", "a", "rose"]))
        ['Rose', 'a', 'is', 'rose']

        An empty list should return an empty list::

        >>> sorted(without_duplicates(
        ...     []))
        []

    The function should work for a list containing integers::

        >>> sorted(without_duplicates([111111, 2, 33333, 2]))
        [2, 33333, 111111]
    """

    unique_words = set(words)

    list_unique_words = list(unique_words)

    return list_unique_words


def find_unique_common_items(items1, items2):
    """Produce the set of *unique* common items in two lists.

    Given two lists, return a list of the *unique* common items
    shared between the lists.

    **IMPORTANT**: you may not use `'if ___ in ___``
    or the method `list.index()`.

    This should find [1, 2]::

        >>> sorted(find_unique_common_items([1, 2, 3, 4], [2, 1]))
        [1, 2]

    However, now we only want unique items, so for these lists,
    don't show more than 1 or 2 once::

        >>> sorted(find_unique_common_items([3, 2, 1], [1, 1, 2, 2]))
        [1, 2]

    The elements should not be treated as duplicates if they are
    different data types::

        >>> sorted(find_unique_common_items(["2", "1", 2], [2, 1]))
        [2]
    """
    unique_items1 = set(items1)
    unique_items2 = set(items2)

    common_items = unique_items1 & unique_items2

    return common_items


def count_words(phrase):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys, and the number of
    times that word appears in the string as values.

    For example::

        >>> print_dict(count_words("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time::

        >>> print_dict(count_words("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different::

        >>> print_dict(count_words("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}
    """
    words_and_words_count = {}

    words = phrase.split()  # Create a list with each word in a string as an element in the list.

    for word in words:
        # Sets the key to a value 0 if they key doesn't exist in the dictionary and
        # then add 1 to the value each time it encounters the key in the words list.
        words_and_words_count[word] = words_and_words_count.get(word, 0) + 1

    return words_and_words_count


def translate_to_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak
    equivalent. Words that cannot be translated into Pirate-speak
    should pass through unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    ----------  ----------------
    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    boy         matey
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    restroom    head
    my          me
    is          be
    ----------  ----------------

    For example::

        >>> translate_to_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words::

        >>> translate_to_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'
    """
    english_pirate_translations = {
        "sir" : "matey",
        "man" : "matey",
        "hotel" : "fleabag inn",
        "student" : "swabbie",
        "boy" : "matey",
        "professor" : "foul blaggart",
        "restaurant" : "galley",
        "your" : "yer",
        "excuse" : "arr",
        "students" : "swabbies",
        "are" : "be",
        "restroom" : "head",
        "my" : "me",
        "is" : "be"
    }

    words = phrase.split()
    translation = []

    for word in words:
        if word in english_pirate_translations.keys():
            translation.append(english_pirate_translations[word])
        else:
            translation.append(word)

    return (' ').join(translation)


def sort_by_word_length(words):
    """Given list of words, return list of ascending (len, [words]).

    Given a list of words, return a list of tuples, ordered by
    word-length. Each tuple should have two items --- the length
    of the words for that word-length, and the list of words of
    that word length.

    For example::

        >>> sort_by_word_length(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['ok', 'an']), (3, ['day']), (5, ['apple'])]
    """
    unique_lengths_words = {}

    for word in words:
        unique_lengths_words.setdefault(len(word), []).append(word)

    ascending_length = unique_lengths_words.items()
    ascending_length.sort()

    return ascending_length


def get_sum_zero_pairs(numbers):
    """Given list of numbers, return list of pair summing to 0.

    Given a list of numbers, add up each individual pair of numbers.
    Return a list of each pair of numbers that adds up to 0.

    For example::

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1]) )
        [[-2, 2], [-1, 1]]

        >>> sort_pairs( get_sum_zero_pairs([3, -3, 2, 1, -2, -1]))
        [[-3, 3], [-2, 2], [-1, 1]]

    This should always be a unique list, even if there are
    duplicates in the input list::

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1]) )
        [[-2, 2], [-1, 1]]

    Of course, if there are one or more zeros to pair together,
    that's fine, too (even a single zero can pair with itself)::

        >>> sort_pairs( get_sum_zero_pairs([1, 3, -1, 1, 1, 0]))
        [[-1, 1], [0, 0]]
    """
    unique_numbers = set(numbers)
    new_numbers = list(unique_numbers)
    pairs_summing_zero = []

    index = 0

    for i in range(len(new_numbers) - 1):
        if new_numbers[i] == 0:
            zero_pair = [new_numbers[i], new_numbers[i]]
            pairs_summing_zero.append(zero_pair)

        # pair = [new_numbers[index], new_numbers[i + 1]]
        # print "New pair:", pair

        if new_numbers[i] - new_numbers[i + 1] == 0 or new_numbers[i] + new_numbers[i + 1] == 0:
            pair = [new_numbers[i], new_numbers[i + 1]]
            print "Current pair: ", pair

            pairs_summing_zero.append(pair)
            # index += 1

    return pairs_summing_zero


def kids_game(names):
    """Play a kids' word chain game.

    Given a list of names, like::

      bagon baltoy yamask starly nosepass kalob nicky

    Do the following:

    1. Always start with the first word ("bagon", in this example).

    2. Add it to the results.

    3. Use the last letter of that word to look for the next word.
       Since "bagon" ends with n, find the *first* word starting
       with "n" in our list --- in this case, "nosepass".

    4. Add "nosepass" to the results, and continue. Once a word has
       been used, it can't be used again --- so we'll never get to
       use "bagon" or "nosepass" a second time.

    5. When you can't find an unused word to use, you're done!
       Return the list of output words.

    For example::

        >>> kids_game(["bagon", "baltoy", "yamask", "starly",
        ...            "nosepass", "kalob", "nicky", "booger"])
        ['bagon', 'nosepass', 'starly', 'yamask', 'kalob', 'baltoy']

    (After "baltoy", there are no more y-words, so we end, even
    though "nicky" and "booger" weren't used.)

    This is a tricky problem. In particular, think about how using
    a dictionary (with the super-fast lookup they provide) can help;
    good solutions here will definitely require a dictionary.
    """
    # words = [names[0]]

    # first_word = names[0]

    last_letter_new_word = {}

    outcome = []

    for name in names:
        # print "This is the name: ", name
        # last_letter_new_word[name[-1]] = []  # last letter of each word added as a key with an empty list value
        # last_letter_new_word.setdefault(name[-1], []).append(name)  # Creating the dictionary based on the last letter of each word but appending word that has the same last letter as the key
        last_letter_new_word.setdefault(name[-1], [])  # dictionary keys of all last letters with empty list values
         
    for name in names:
        if name[0] in last_letter_new_word.keys():
            last_letter_new_word.get(name[0], name)

    # for name in names:
    #     if name[-1] in last_letter_new_word.keys():
    #          outcome.append(last_letter_new_word[name[-1]])


        # if name[0] in last_letter_new_word.keys():
        #     last_letter_new_word[name[-1]] = name
        # print "This is the dictionary: ", last_letter_new_word


    # for name in names:
    #     if name[0] in last_letter_new_word.keys():
    #         # take the name and add it to a value to one of the keys in the dictionary
    #         # dictionary[key] = [name]
    #         last_letter_new_word[name[0]].append(name)

    print last_letter_new_word
    # print outcome
    # return last_letter_new_word


#####################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is used to print dictionaries in key-alphabetical
    # order, and is only for our doctests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join(
            "%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is
    # used only for documentation tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
