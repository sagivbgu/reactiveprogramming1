from task_2 import *


def test_encrypt_caesar_cipher():
    assert encrypt_caesar_cipher("") == ""
    assert encrypt_caesar_cipher("PYTHON") == "SBWKRQ"
    assert encrypt_caesar_cipher("F1RST P0ST") == "I1UVW S0VW"


def test_decrypt_caesar_cipher():
    assert decrypt_caesar_cipher("") == ""
    assert decrypt_caesar_cipher("SBWKRQ") == "PYTHON"
    assert decrypt_caesar_cipher("I1UVW S0VW") == "F1RST P0ST"


def test_encrypt_vigenere_cipher():
    assert encrypt_vigenere_cipher("", "") == ""
    assert encrypt_vigenere_cipher("", "A") == ""
    assert encrypt_vigenere_cipher("A", "") == "A"
    assert encrypt_vigenere_cipher("ATTACKATDAWN", "LEMON") == "LXFOPVEFRNHR"
    assert encrypt_vigenere_cipher("AT", "LEMON") == "LX"
    assert encrypt_vigenere_cipher("ATT4CKATD9WN.", "LEMON") == "LXF4PVEFR9HR."


def test_decrypt_vigenere_cipher():
    assert decrypt_vigenere_cipher("", "") == ""
    assert decrypt_vigenere_cipher("", "A") == ""
    assert decrypt_vigenere_cipher("A", "") == "A"
    assert decrypt_vigenere_cipher("LXFOPVEFRNHR", "LEMON") == "ATTACKATDAWN"
    assert decrypt_vigenere_cipher("LX", "LEMON") == "AT"
    assert decrypt_vigenere_cipher("LXF4PVEFR9HR", "LEMON") == "ATT4CKATD9WN"
