import sys
import string
from collections import Counter

def main():
    """displays the sums of its upper-case chars, lower-case
    chars, punctuation chars, digits and spaces."""

    args = sys.argv
    try:
        u = set(string.ascii_uppercase)
        l = set(string.ascii_lowercase)
        p = set(string.punctuation)
        d = set(string.digits)
        s = " "
        count = Counter({
            'tot': 0,
            'u': 0,
            'l': 0,
            'p': 0,
            'd': 0,
            's': 0
        })

        if len(args) < 2: return(print("Plz put an argument(one)!"), 0)
        assert (len(args) == 2), "Only one argument is required"

        for c in args[1]:
            count['tot']+=1
            if c in u: count['u'] += 1
            elif c in p: count['p'] += 1
            elif c in l: count['l'] += 1
            elif c in d: count['d'] += 1
            elif c == s: count['s'] += 1
            else: assert False, f"I do not understand -> {c}."

        print(f'The text contains {count['tot']} characters:\n {count['u']} upper letters\
        \n {count['l']} lower letters\n {count['p']} punctuation marks\n {count['s']} spaces\n {count['d']} digits')

    except AssertionError as msg:
        print(msg)

if __name__ == "__main__":
    print(f'{__doc__} \n')
    main()
