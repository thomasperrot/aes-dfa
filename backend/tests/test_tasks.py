import pytest

from app.tasks import compute_keys


@pytest.mark.skip(reason="This test takes 50s to complete")
def test_compute_keys():
    keys = compute_keys(
        normal_cipher_text="81d6cdc3bd16fb8d72b9bb88818b5be9",
        faulty_cipher_text="eff93508630187b8d3494e8b70e6887e",
    )
    assert "41414141414141414141414141414141" in keys


def test_compute_keys_mock(mocker):
    """To reach 100% coverage"""

    mocker.patch("app.tasks.crack_key", return_value=[b'AAAAAAAAAAAAAAAA', b'BBBBBBBBBBBBBBBB'])

    keys = compute_keys(
        normal_cipher_text="81d6cdc3bd16fb8d72b9bb88818b5be9",
        faulty_cipher_text="eff93508630187b8d3494e8b70e6887e",
    )
    assert "41414141414141414141414141414141" in keys
