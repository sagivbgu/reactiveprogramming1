from string import ascii_uppercase
from itertools import cycle

CAESAR_CIPHER_SHIFT = 3


def encrypt_caesar_cipher(plaintext):
    return _caesar_cipher(plaintext, CAESAR_CIPHER_SHIFT)


def decrypt_caesar_cipher(ciphertext):
    return _caesar_cipher(ciphertext, -CAESAR_CIPHER_SHIFT)


def encrypt_vigenere_cipher(plaintext, keyword):
    return _vigenere_cipher(plaintext, keyword, ascii_uppercase.find)


def decrypt_vigenere_cipher(ciphertext, keyword):
    return _vigenere_cipher(ciphertext, keyword, lambda letter: - ascii_uppercase.find(letter))


def _caesar_cipher(text, shift):
    return "".join((_shift_letter(letter, shift) for letter in text))


def _vigenere_cipher(text, keyword, shift_func):
    if not keyword:
        keyword = "A"
    return "".join((_shift_letter(letter, shift_func(shift_letter))
                    for letter, shift_letter in zip(text, cycle(keyword))
                    ))


def _shift_letter(letter, shift):
    if not letter.isalpha():
        return letter
    return ascii_uppercase[(ascii_uppercase.find(letter) + shift) % len(ascii_uppercase)]


def _morse_code_translation(text, encrypt):
    translation_table = {"A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.",
                         "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.",
                         "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-", "U": "..-",
                         "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..",
                         "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....",
                         "7": "--...", "8": "---..", "9": "----.", "0": "-----"}
    if not encrypt:
        translation_table = {v: k for k, v in translation_table.items()}

    # TODO: Not sure how to join
    return "".join((translation_table[x] if x in translation_table else x for x in text))


def encrypt_morse_code(plaintext):
    return _morse_code_translation(plaintext, True)


def decrypt_morse_code(ciphertext):
    return _morse_code_translation(ciphertext, False)
