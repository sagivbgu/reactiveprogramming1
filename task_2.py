from string import ascii_uppercase


def _caesar_cipher(text, encrypt):
    shift = 3
    if not encrypt:
        shift = -shift

    def shift_letter(letter):
        return ascii_uppercase[(ascii_uppercase.find(letter) + shift) % len(ascii_uppercase)]

    return "".join((shift_letter(letter) if letter.isalpha() else letter for letter in text))


def encrypt_caesar_cipher(plaintext):
    return _caesar_cipher(plaintext, True)


def decrypt_caesar_cipher(ciphertext):
    return _caesar_cipher(ciphertext, False)


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
