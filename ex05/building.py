import sys

def main():
    '''displays the sums of its upper-case chars, lower-case
    chars, punctuation chars, digits and spaces.'''

    args = sys.argv
    try:
        tot,u,l,p,d,s = 0,0,0,0,0,0
        if len(args) < 2: return(print("Plz put an argument(one)!"), 0)
        assert (len(args) == 2), "Only one argument is required"

        for c in args[1]:
            tot+=1
            if (ord(c) >= 65 and ord(c) <= 90): u+=1
            elif (ord(c) == 46 or ord(c) == 63 or ord(c) == 33): p+=1
            elif (ord(c) >= 97 and ord(c) <= 122): l+=1
            elif (ord(c) >= 48 and ord(c) <= 57): d+=1
            elif (ord(c) == 32): s+=1
            else: assert False, f"I do not understand -> {c}."

        print(f'The text contains {tot} characters:\n {u} upper letters\
        \n {l} lower letters\n {p} punctuation marks\n {s} spaces\n {d} digits')

    except AssertionError as msg:
        print(msg)

if __name__ == "__main__":
    main()
