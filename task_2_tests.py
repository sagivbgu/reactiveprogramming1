from task_2 import *


def test_encrypt_caesar_cipher():
    assert encrypt_caesar_cipher("") == ""
    assert encrypt_caesar_cipher("PYTHON") == "SBWKRQ"
    assert encrypt_caesar_cipher("F1RST P0ST") == "I1UVW S0VW"


def test_decrypt_caesar_cipher():
    assert decrypt_caesar_cipher("") == ""
    assert decrypt_caesar_cipher("SBWKRQ") == "PYTHON"
    assert decrypt_caesar_cipher("I1UVW S0VW") == "F1RST P0ST"
