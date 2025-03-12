import sys

def encrypt(sms):
    cipher = ''
    MORSE_CODE_DICT = { ' ':'/', 'A':'.-', 'B':'-...',
                        'C':'-.-.', 'D':'-..', 'E':'.',
                        'F':'..-.', 'G':'--.', 'H':'....',
                        'I':'..', 'J':'.---', 'K':'-.-',
                        'L':'.-..', 'M':'--', 'N':'-.',
                        'O':'---', 'P':'.--.', 'Q':'--.-',
                        'R':'.-.', 'S':'...', 'T':'-',
                        'U':'..-', 'V':'...-', 'W':'.--',
                        'X':'-..-', 'Y':'-.--', 'Z':'--..',
                        '1':'.----', '2':'..---', '3':'...--',
                        '4':'....-', '5':'.....', '6':'-....',
                        '7':'--...', '8':'---..', '9':'----.',
                        '0':'-----', ', ':'--..--', '.':'.-.-.-',
                        '?':'..--..', '/':'-..-.', '-':'-....-',
                        '(':'-.--.', ')':'-.--.-'}
    for c in sms:
        if (ord(c) >= 97 and ord(c) <= 122):
            c = chr(ord(c) - 32)
        if (c not in MORSE_CODE_DICT):
            raise AssertionError(f"AssertionError: The arguments are bad {c}")
        cipher += MORSE_CODE_DICT[c] + ' '
    return cipher

def main():
    """ Morse code is a method of transmitting text information as \
    a series of on-off tones, lights, or clicks that can be directly \
    understood by a skilled listener or observer without special \
    equipment. It is named for Samuel F. B. Morse, an inventor \
    of the telegraph."""

    try:
        if (len(sys.argv) > 2 or len(sys.argv) < 2):
            raise AssertionError("Wrong number of arguments")
        print(encrypt(sys.argv[1]))
    except AssertionError as e:
        print(f"AssertionError: {e}")

if __name__ == "__main__":
    main()
