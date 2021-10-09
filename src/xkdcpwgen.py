import sys
from random import randint

# turn text file into list of words
words_list = open("words_alpha.txt").read().splitlines()

# list of symbols
sym_list = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '.', ':', ';']

# generates passwords with certain parameters
def gen_password(words, caps, nums, syms):
    generated_password = []

    # checking for errors, returns closest possible password
    # if command does not exist, the command is ignored and
    # the custom password is returned
    if caps > words:
        return gen_password(4, 4, nums, syms)

    # generates the words that would be in the password
    for i in range(0, words):
        generated_password.append(words_list[randint(0, len(words_list) - 1)])

    # creates a list of indicies and a random number to choose which index to use
    indicies = list(range(0, len(generated_password)))
    
    # randomly capitalizes a number of letters in a list of words
    while caps > 0:
        rand = randint(0, len(indicies) - 1)

        generated_password[indicies[rand]] = generated_password[indicies[rand]].title()
        caps = caps - 1
        indicies.pop(rand)
    
    # randomly inserts a given number of numbers (can repeat numbers) into
    # a list of items
    while nums > 0:
        rand = randint(0, len(generated_password) - 1)
        generated_password.insert(rand, str(randint(0, 9)))
        nums = nums - 1
    
    # randomly inserts a given number of symbols into a list of items
    while syms > 0:
        rand = randint(0, len(generated_password) - 1)
        generated_password.insert(rand, sym_list[randint(0, len(sym_list) - 1)])
        syms = syms - 1

    # return final password
    return ''.join(generated_password)

# variables to determine the number of words, capitals, numbers, and symbols
# in a password
words = 4
caps = 0
nums = 0
syms = 0

# determines number of generated words if words command called
if '-w' in sys.argv:
    words = int(sys.argv[sys.argv.index('-w') + 1])
elif '--words' in sys.argv:
    words = int(sys.argv[sys.argv.index('--words') + 1])

# determines number of capitalized words if caps command called
if '-c' in sys.argv:
    caps = int(sys.argv[sys.argv.index('-c') + 1])
elif '--caps' in sys.argv:
    caps = int(sys.argv[sys.argv.index('-caps') + 1])

# determines number of numbers if numbers command is called
if '-n' in sys.argv:
    nums = int(sys.argv[sys.argv.index('-n') + 1])
elif '--numbers' in sys.argv:
    nums = int(sys.argv[sys.argv.index('--numbers') + 1])

# determines number of symbols if symbols command is called
if '-s' in sys.argv:
    syms = int(sys.argv[sys.argv.index('-s') + 1])
elif '--symbols' in sys.argv:
    syms = int(sys.argv[sys.argv.index('--symbols') + 1])

# generates a help message
if '-h' in sys.argv or '--help' in sys.argv:
    print('usage: xkcdpwgen [-h] [-w WORDS] [-c CAPS] [-n NUMBERS] [-s SYMBOLS] \n\n'
        'Generate a secure, memorable password using the XKCD method\n\n'
        'optional arguments:\n'
        '     -h, --help           show this help message and exit\n'
        '     -w WORDS, --words WORDS\n'
        '                          include WORDS words in the password (default=4)\n'
        '     -c CAPS, --caps CAPS capitalize the first letter of CAPS random words (default=0)\n'
        '     -n NUMBERS, --numbers NUMBERS\n'
        '                          insert NUMBERS random numbers in the password (default=0)\n'
        '     -s SYMBOLS, --symbols SYMBOLS\n'
          '                          insert SYMBOLS random symbols in the password (default=0)')
else:
    # print randomly generated password
    print(gen_password(words, caps, nums, syms))
