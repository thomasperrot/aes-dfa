from typing import Annotated, Literal

from pydantic import BaseModel, Field, ConfigDict


class CipherTexts(BaseModel):
    _cipher_text_pattern = r"[0-9a-f]{32}"
    model_config = ConfigDict(extra="forbid")

    normal_cipher_text: Annotated[
        str, Field(alias="normalCipherText", pattern=_cipher_text_pattern)
    ]
    faulty_cipher_text: Annotated[
        str, Field(alias="faultyCipherText", pattern=_cipher_text_pattern)
    ]


class TaskStatus(BaseModel):
    task_id: Annotated[str, Field(alias="taskId")]
    task_status: Annotated[
        Literal["PENDING", "STARTED", "RETRY", "FAILURE", "SUCCESS"],
        Field(alias="taskStatus"),
    ]
    task_result: Annotated[list[str] | None, Field(alias="taskResult")]

    model_config = ConfigDict(populate_by_name=True)
