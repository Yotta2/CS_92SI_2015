"""
Assignment 1: Cryptography
Course: CS 92SI
Name: <YOUR NAME>
Date: <DATE>

Replace this with a description of the program.
"""

plain_to_cipher = {}

for old_char_val in range(ord('a'), ord('z') + 1):
    new_char_val = old_char_val + 3
    if (new_char_val > ord('z')):
        new_char_val -= 26
    plain_to_cipher[chr(old_char_val)] = chr(new_char_val)

for old_char_val in range(ord('A'), ord('Z') + 1):
    new_char_val = old_char_val + 3
    if (new_char_val > ord('Z')):
        new_char_val -= 26
    plain_to_cipher[chr(old_char_val)] = chr(new_char_val)

cipher_to_plain = {}
for old_char_val in range(ord('a'), ord('z') + 1):
    new_char_val = old_char_val - 3
    if (new_char_val < ord('a')):
        new_char_val += 26
    cipher_to_plain[chr(old_char_val)] = chr(new_char_val)

for old_char_val in range(ord('A'), ord('Z') + 1):
    new_char_val = old_char_val - 3
    if (new_char_val < ord('A')):
        new_char_val += 26
    cipher_to_plain[chr(old_char_val)] = chr(new_char_val)


def encrypt_caesar(plaintext):
    """
    Encrypts plaintext using a Caesar cipher.
    Add more implementation details here.
    """
    return ''.join([plain_to_cipher[old] for old in plaintext.upper()])


def decrypt_caesar(ciphertext):
    """
    Decrypts a ciphertext using a Caesar cipher.
    Add more implementation details here.
    """
    return ''.join([cipher_to_plain[old] for old in ciphertext.upper()])

def caesar_transform(operation, str):
    """
    Transform a string using caesar cypher. operation is either 'E'(encrypt) or 'D'(decrypt).
    return transformed str
    """
    if operation == 'E':
        return encrypt_caesar(str)
    else:
        return decrypt_caesar(str)

def encrypt_vigenere(plaintext, keyword):
    """
    Encrypts plaintext using a Vigenere cipher with a keyword.
    Return encrypted str
    """
    list = []
    index = 0
    for char in plaintext:
        new_char_val = ord(char) + ord(keyword[index]) - ord('A')
        if new_char_val > ord('Z'):
            new_char_val -= 26
        list.append(chr(new_char_val))
        index += 1
        index %= len(keyword)
    return ''.join(list)


def decrypt_vigenere(ciphertext, keyword):
    """
    Decrypts ciphertext using a Vigenere cipher with a keyword.
    Return decrypted str
    """
    list = []
    index = 0
    for char in ciphertext:
        new_char_val = ord(char) - (ord(keyword[index]) - ord('A'))
        if new_char_val < ord('A'):
            new_char_val += 26
        list.append(chr(new_char_val))
        index += 1
        index %= len(keyword)
    return ''.join(list)

def vigenere_transform(operation, str):
    """
    Transform a string using vigenere cypher. operation is either 'E'(encrypt) or 'D'(decrypt).
    return transformed str
    """
    key = input("Passkey? ").upper()

    if operation == 'E':
        print("Encrypting {0} using Vigenere cipher with key {1}".format(str, key))
        print("...")
        return encrypt_vigenere(str, key)
    else:
        print("Decrypting {0} using Vigenere cipher with key {1}".format(str, key))
        print("...")
        return decrypt_vigenere(str, key)

def encrypt_railfence(plaintext, num_rails):
    """
    Encrypts plaintext using a railfence cipher.
    Return encrypted str
    """
    if num_rails == 1:
        return plaintext

    lists = []
    for i in range(0, num_rails):
        lists.append([])
    row = -1
    dir = 1
    for char in plaintext:
        row += dir
        lists[row].append(char)
        if row == 0:
            dir = 1
        elif row == num_rails - 1:
            dir = -1
    encrypted = ""
    for list in lists:
        #print(list)
        encrypted += ''.join(list)
    return encrypted

def slice_ciphertext(ciphertext, num_rails):
    """
    slice ciphertext into num_rails lists
    """
    cycle = num_rails + num_rails - 2
    lists = [[] for i in range(num_rails)]

    cipher_len = len(ciphertext)
    start = 0
    for row in range(num_rails):
        if row == 0 or row == num_rails - 1:
            row_len = cipher_len // cycle
            if cipher_len % cycle > row:
                row_len += 1
            lists[row] = ciphertext[start:start+row_len]
            start += row_len
        else:
            row_len = cipher_len // cycle * 2
            if cipher_len % cycle > row:
                row_len += 1
            lists[row] = ciphertext[start:start+row_len]
            start += row_len
    return lists

def decrypt_railfence(ciphertext, num_rails):
    """
    Decrypts ciphertext using a railfence cipher.
    Return decrypted str
    """
    if num_rails == 1:
        return ciphertext

    lists = slice_ciphertext(ciphertext, num_rails) # could use queue to simply the implementation once we got to OOP

    #print(lists)
    rows_indices = [0] * num_rails    

    decrypted = ''
    row = -1
    dir = 1
    cipher_len = len(ciphertext)
    for i in range(cipher_len):
        row += dir
        decrypted += lists[row][rows_indices[row]]
        rows_indices[row] += 1
        if row == 0:
            dir = 1
        elif row == num_rails - 1:
            dir = -1
    return decrypted


def railfence_transform(operation, str):
    """
    Transform a string using railfence cypher. operation is either 'E'(encrypt) or 'D'(decrypt).
    return transformed str
    """
    num_rails = int(input("Rails: "))
    if operation == 'E':
        print("Encrypting {0} using Railfence cipher with num_rails {1}".format(str, num_rails))
        print("...")
        return encrypt_railfence(str, num_rails)
    else:
        print("Decrypting {0} using Railfence cipher with num_rails {1}".format(str, num_rails))
        print("...")
        return decrypt_railfence(str, num_rails)

def read_from_file(filename):
    """
    Reads and returns content from a file.
    Read file line by line and concatenate them
    """
    with open(filename, 'r') as f:
        lines = [line for line in f]

    return "".join(lines)



def write_to_file(filename, content):
    """
    Writes content to a file.
    Add more implementation details here.
    """
    with open(filename, 'w') as f:
        f.write(content)

def get_input():
    """
    get input string from console input or file.
    return string is capitalized
    """
    choice = input("(F)ile or (S)tring? ").upper()
    while not choice or choice[0] not in ['F', 'S']:
        choice = input("Please enter either 'F' or 'S'. Again (F/S)? ").upper()
    if choice[0] == 'S':
        input_str = input("Enter the string to encrypt/decrypt: ")
    else:
        filename = input("Filename: ")
        input_str = read_from_file(filename)
    return input_str.upper()

def strip(str):
    """
    Strip a given string by removing all non-alphabetic chars
    """
    return ''.join([char for char in str if char.isalpha()])

def transform(str):
    """
    transform(encrypt/decrypt) a given string based on user input
    """
    operation = input("(E)ncrypt or (D)ecrypt? ").upper()
    while not operation or operation not in ['E', 'D']:
        operation = input("Please enter either 'E' or 'D'. Again (E/D)? ").upper()

    cipher = input("(C)aesar, (V)igenere, or (R)ailfence? ").upper()
    while not cipher or cipher not in ['C', 'V', 'R']:
        cipher = input("Please enter either 'C', 'V' or 'R'. Again (C/V/R)? ").upper()
    if cipher == 'C':
        return operation, caesar_transform(operation, str)
    elif cipher == 'V':
        return operation, vigenere_transform(operation, str)
    elif cipher == 'R':
        return operation, railfence_transform(operation, str)

def output(operation, transformed):
    output_option = input("(F)ile or (S)tring ").upper()
    while not output_option or output_option not in ['F', 'S']:
        output_option = input("Please enter either 'F' or 'S'. Again (F/S)? ").upper()
    if (output_option == 'S'):
        if (operation == 'E'):
            print("The ciphertext is: {0}".format(transformed))
        else:
            print("The plaintext is: {0}".format(transformed))
    else:
        output_file = input("Filename? ")
        if (operation == 'E'):
            print("Writing ciphertext to {0}...".format(output_file))
        else:
            print("Writing plaintext to {0}...".format(output_file))
        write_to_file(output_file, transformed)

def run_suite():
    """
    Runs a single iteration of the cryptography suite.

    Asks the user for input text from a string or file, whether to encrypt
    or decrypt, what tool to use, and where to show the output.
    """
    print("*Input*")
    input_str = get_input()
    stripped = strip(input_str)

    print("*Transform*")
    operation, transformed = transform(stripped)

    print("*Output*")
    output(operation, transformed)


# Do not modify code beneath this point.
def should_continue():
    """
    Asks the user whether they would like to continue.
    Responses that begin with a `Y` return True. (case-insensitively)
    Responses that begin with a `N` return False. (case-insensitively)
    All other responses (including '') cause a reprompt.
    """
    choice = input("Again (Y/N)? ").upper()
    while not choice or choice[0] not in ['Y', 'N']:
        choice = input("Please enter either 'Y' or 'N'. Again (Y/N)? ").upper()
    return choice[0] == 'Y'


def main():
    """Harness for the Cryptography Suite"""
    print("Welcome to the Cryptography Suite!")
    run_suite()
    while should_continue():
        run_suite()
    print("Goodbye!")


if __name__ == '__main__':
    """This block is run if and only if the Python script is invoked from the
    command line."""
    main()
