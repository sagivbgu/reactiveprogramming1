from string import ascii_uppercase
from itertools import cycle


def encrypt_caesar_cipher(plaintext):
    return _caesar_cipher(plaintext, 3)


def decrypt_caesar_cipher(ciphertext):
    return _caesar_cipher(ciphertext, -3)


def encrypt_vigenere_cipher(plaintext, keyword):
    return _vigenere_cipher(plaintext, keyword, ascii_uppercase.find)


def decrypt_vigenere_cipher(ciphertext, keyword):
    return _vigenere_cipher(ciphertext, keyword, lambda letter: - ascii_uppercase.find(letter))


def _caesar_cipher(text, shift):
    return "".join((_shift_letter(letter, shift) if letter.isalpha() else letter for letter in text))


def _vigenere_cipher(text, keyword, shift_func):
    if not keyword:
        keyword = "A"
    return "".join((_shift_letter(letter, shift_func(shift_letter)) if letter.isalpha() else letter
                    for letter, shift_letter in zip(text, cycle(keyword))
                    ))


def _shift_letter(letter, shift):
    return ascii_uppercase[(ascii_uppercase.find(letter) + shift) % len(ascii_uppercase)]
