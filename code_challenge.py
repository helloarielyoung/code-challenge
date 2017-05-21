
""" sample input
    mm nn oo pppp

    sample output
    p
    o
    m
    n

    """

#string_input = raw_input()


def order_letters(letters):
    letter_dict = {}

    letters = ''.join(letters.split())
    for letter in letters:
            letter_dict[letter] = letter_dict.setdefault(letter, 0) + 1
    #{'p': 4, 'm': 2, 'o': 3, 'n': 2}

# close, but not quite
    # for key, value in sorted(letter_dict.iteritems(), reverse=True, key=lambda x: (x[0], -x[1])):
    #     print value, key

    list_letters = [v[0] for v in sorted(letter_dict.iteritems(), key=lambda(k, v): (-v, k))]

    for l in list_letters:
        print l
