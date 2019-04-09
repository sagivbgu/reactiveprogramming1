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
