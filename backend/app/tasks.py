from celery import shared_task
import time

@shared_task
def compute_keys(normal_cipher_text: str, faulty_cipher_text: str):
    time.sleep(10)
    return "0" * 32
