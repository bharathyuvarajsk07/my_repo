import string
import string

def print_rangoli(size):
    # Create a list of the first 'size' lowercase letters
    alpha = list(string.ascii_lowercase[:size])
    # The 'beta' list :reverse (starting from the 'size'-th letter)
    beta = alpha[::-1]
    # Formula: (size * 4) - 3
    width = (size * 2 - 1) + (size * 2 - 2)
    for i in range(size):
        pattern = '-'.join(beta[:i+1] + alpha[size-i:])
        print(pattern.center(width, '-'))
    for i in range(size-2, -1, -1):
        pattern = '-'.join(beta[:i+1] + alpha[size-i:])
        print(pattern.center(width, '-'))

