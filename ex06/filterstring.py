import sys
from ft_filter import ft_filter

def main():
    '''This script takes two arguments: a string S and an integer N. 
    It filters out words from S that have a length greater than N and prints them.'''

    try:
        assert len(sys.argv) == 3, "the arguments are bad"

        S, N = sys.argv[1], sys.argv[2]

        try:
            N = int(N)
        except ValueError:
            raise AssertionError("the arguments are bad")

        words = S.split()

        filter_condition = lambda word: len(word) > N
        filtered_words = list(ft_filter(filter_condition, words))

        print(f'{filter.__doc__} \n')
        print(filtered_words)

    except AssertionError as e:
        print(f"AssertionError: {e}")

if __name__ == "__main__":
    main()