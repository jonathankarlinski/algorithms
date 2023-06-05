from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():

    assert encrypt_message("jonathan", 4) == "naht_anoj"
    assert encrypt_message("jonathan", 5) == "tanoj_nah"
    assert encrypt_message("jonathan", 9) == "nahtanoj"

    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message(18, "jonathan")
