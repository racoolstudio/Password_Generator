import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def GeneratePassword(L=6, S=6, N=4):
    """ This functoin Generates Password"""
    nr_letters = int(L)
    nr_symbols = int(S)
    nr_numbers = int(N)
    l = [random.choice(letters) for i in range(nr_letters)]
    s = [random.choice(numbers) for j in range(nr_numbers)]
    n = [random.choice(symbols) for k in range(nr_symbols)]
    p = l + s + n
    gP = [random.choice(p) for i in range(len(p))]
    str_gP = ''.join(gP)
    return str_gP
