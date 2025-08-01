import binascii

from celery import shared_task
from aes_dfa import crack_key

from .settings import settings


@shared_task
def compute_keys(normal_cipher_text: str, faulty_cipher_text: str) -> list[str]:
    keys: list[bytes] = crack_key(
        normal_cipher_text=binascii.unhexlify(normal_cipher_text),
        faulty_cipher_text=binascii.unhexlify(faulty_cipher_text),
        nb_threads=settings.nb_threads,
    )
    return [binascii.hexlify(key).decode() for key in keys]
