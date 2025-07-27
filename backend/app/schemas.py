from typing import Annotated

from pydantic import BaseModel, Field, ConfigDict


class CipherTexts(BaseModel):
    _cipher_text_pattern = r"[0-9a-f]{32}"
    model_config = ConfigDict(extra="forbid")

    normal_cipher_text: Annotated[str, Field(alias="normalCipherText", pattern=_cipher_text_pattern)]
    faulty_cipher_text: Annotated[str, Field(alias="faultyCipherText", pattern=_cipher_text_pattern)]


