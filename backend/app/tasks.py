from celery import shared_task


@shared_task
def compute_key(normal_cipher_text: str, faulty_cipher_text: str):
    return "0" * 32
