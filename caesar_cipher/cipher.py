import string


def encrypt(plaintext, key):
    """
    takes in a plaintext phrase and a numeric shift key. the phrase is shifted that many letters to encrypt it
    :param plaintext: string, representing the phrase to be encrypted
    :param key: int, representing the number places to shift the alphabet for encryption
    :return ciphertext: string, representing the encypted phrase

    solution adapted from https://stackoverflow.com/a/8895517
    """
    # initialize return value string
    ciphertext = str()
    # create translation table for lower case alphabetic characters
    alpha_lower = string.ascii_lowercase
    shifted_lower = alpha_lower[key:] + alpha_lower[:key]
    table_lower = str.maketrans(alpha_lower, shifted_lower)
    # create translation table for upper case alphabetic characters
    alpha_upper = string.ascii_uppercase
    shifted_upper = alpha_upper[key:] + alpha_upper[:key]
    table_upper = str.maketrans(alpha_upper, shifted_upper)
    # for each character in the plaintext phrase to be encrypted
    for char in plaintext:
        # test if character is alphabetic
        if char.isalpha():
            # use str.translate() to shift character and join shifted character to return value
            ciphertext += char.translate(table_lower) if char.islower() else char.translate(table_upper)
        # join un-modified non-alphabetic character to return value
        else:
            ciphertext += char
    # return encrypted phrase
    return ciphertext


def decrypt(ciphertext, key):
    return encrypt(ciphertext, key * -1)


def crack(ciphertext):
    pass


if __name__ == "__main__":
    encrypt("doodah", 3)
