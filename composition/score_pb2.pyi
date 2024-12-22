from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ScoreRequest(_message.Message):
    __slots__ = ("login",)
    LOGIN_FIELD_NUMBER: _ClassVar[int]
    login: str
    def __init__(self, login: _Optional[str] = ...) -> None: ...

class ScoreResponse(_message.Message):
    __slots__ = ("score",)
    SCORE_FIELD_NUMBER: _ClassVar[int]
    score: float
    def __init__(self, score: _Optional[float] = ...) -> None: ...
