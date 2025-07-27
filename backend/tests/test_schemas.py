import pytest
from pydantic import ValidationError

from app.schemas import CipherTexts


def test_invalid_ciphertext():
    with pytest.raises(ValidationError):
        CipherTexts(normalCipherText="test", faultyCipherText="1" * 32)


def test_missing_ciphertext():
    with pytest.raises(ValidationError):
        CipherTexts(normalCipherText="test")


def test_extra_field():
    with pytest.raises(ValidationError):
        CipherTexts(normalCipherText="0" * 32, faultyCipherText="1" * 32, extra="test")


def test_valid_ciphertext():
    cipher_texts = CipherTexts(normalCipherText="0" * 32, faultyCipherText="1" * 32)
    assert cipher_texts.normal_cipher_text == "0" * 32
    assert cipher_texts.faulty_cipher_text == "1" * 32
