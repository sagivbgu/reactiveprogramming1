from string import ascii_uppercase
from itertools import cycle

CAESAR_CIPHER_SHIFT = 3
TEXT_TO_MORSE = {"A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.",
                 "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.",
                 "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-", "U": "..-",
                 "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..",
                 "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....",
                 "7": "--...", "8": "---..", "9": "----.", "0": "-----"}
MORSE_LETTER_DELIMITER = " "
MORSE_WORD_DELIMITER = "  "

def encrypt_caesar_cipher(plaintext):
    return _caesar_cipher(plaintext, CAESAR_CIPHER_SHIFT)


def decrypt_caesar_cipher(ciphertext):
    return _caesar_cipher(ciphertext, -CAESAR_CIPHER_SHIFT)


def encrypt_vigenere_cipher(plaintext, keyword):
    return _vigenere_cipher(plaintext, keyword, ascii_uppercase.find)


def decrypt_vigenere_cipher(ciphertext, keyword):
    return _vigenere_cipher(ciphertext, keyword, lambda letter: - ascii_uppercase.find(letter))


def encrypt_morse_code(plaintext):
    def word_to_morse(word):
        return MORSE_LETTER_DELIMITER.join(TEXT_TO_MORSE[letter] for letter in word)

    return MORSE_WORD_DELIMITER.join(word_to_morse(word) for word in plaintext.split(MORSE_LETTER_DELIMITER))


def decrypt_morse_code(ciphertext):
    morse_to_text = {v: k for k, v in TEXT_TO_MORSE.items()}

    def word_from_morse(word):
        return "".join(morse_to_text[letter] for letter in word.split(MORSE_LETTER_DELIMITER))

    return MORSE_LETTER_DELIMITER.join(word_from_morse(word) for word in ciphertext.split(MORSE_WORD_DELIMITER))


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
