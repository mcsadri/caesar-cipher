import string
import re
import nltk
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download('words', quiet='True')
nltk.download('names', quiet='True')

from nltk.corpus import words, names


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
    """
    takes in a ciphertext phrase and a numeric shift key. the phrase is shifted that many letters to decrypt it
    :param ciphertext: string, representing the phrase to be decrypted
    :param key: int, representing the number places to unshift the alphabet for decryption
    :return: string, representing the decypted phrase
    """
    # call the encrpyt() method and pass it the ciphertext phrase, and the shift key * 1 (to perform the unshift)
    return encrypt(ciphertext, key * -1)


def crack(ciphertext):
    """
    takes in an encrypted phrase (without a shift key) and attempts to brute force crack the original plaintext
    :param ciphertext: ciphertext: string, representing the phrase to be decrypted
    :return: string, representing the decypted phrase
    """

    # holds the % value returned by calc_percent_english()
    percent_english = float()
    # shift key counter
    key = 0
    # unshifts/decrypted guess phrase
    phrase = str()

    # repeat until percent_english is > 90% or shift key counter iterates through the entire alphabet
    while percent_english < .9 and key < 26:
        # get decryption guess phrase
        phrase = decrypt(ciphertext, key)
        # get the success % of the decryption guess phrase
        percent_english = calc_percent_english(phrase)
        # increment the shift key counter
        key += 1

    # if success is at least 90% return the guess phrase
    if percent_english > .9:
        return phrase
    # else return nothing
    else:
        return ""


def calc_percent_english(phrase):
    """
    takes in a phrase and determine the % of words that match known words or names from nltk.corpus
    :param phrase: string, the phrase of words to be validated against the word/name list
    :return: float, the % of words in the phrase that match match known words or names
    """
    word_list = words.words()
    name_list = names.words()

    phrase_words_list = phrase.split()
    word_counter = 0

    for word in phrase_words_list:
        word = re.sub(r"[^A-Za-z]+", "", word)
        if word.lower() in word_list or word in name_list:
            word_counter += 1

    return word_counter / len(phrase_words_list)


if __name__ == "__main__":
    pass
