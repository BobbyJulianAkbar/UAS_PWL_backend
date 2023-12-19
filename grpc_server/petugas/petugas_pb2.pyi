from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Petugas(_message.Message):
    __slots__ = ("id", "fnama", "email", "password", "username", "status")
    ID_FIELD_NUMBER: _ClassVar[int]
    FNAMA_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    id: int
    fnama: str
    email: str
    password: str
    username: str
    status: str
    def __init__(self, id: _Optional[int] = ..., fnama: _Optional[str] = ..., email: _Optional[str] = ..., password: _Optional[str] = ..., username: _Optional[str] = ..., status: _Optional[str] = ...) -> None: ...

class PetugasListRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PetugasListResponse(_message.Message):
    __slots__ = ("petugas",)
    PETUGAS_FIELD_NUMBER: _ClassVar[int]
    petugas: _containers.RepeatedCompositeFieldContainer[Petugas]
    def __init__(self, petugas: _Optional[_Iterable[_Union[Petugas, _Mapping]]] = ...) -> None: ...

class PetugasDetailRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class PetugasDetailResponse(_message.Message):
    __slots__ = ("petugas",)
    PETUGAS_FIELD_NUMBER: _ClassVar[int]
    petugas: Petugas
    def __init__(self, petugas: _Optional[_Union[Petugas, _Mapping]] = ...) -> None: ...

class PetugasCreateRequest(_message.Message):
    __slots__ = ("fnama", "email", "password", "username", "status")
    FNAMA_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    fnama: str
    email: str
    password: str
    username: str
    status: str
    def __init__(self, fnama: _Optional[str] = ..., email: _Optional[str] = ..., password: _Optional[str] = ..., username: _Optional[str] = ..., status: _Optional[str] = ...) -> None: ...

class PetugasCreateResponse(_message.Message):
    __slots__ = ("petugas",)
    PETUGAS_FIELD_NUMBER: _ClassVar[int]
    petugas: Petugas
    def __init__(self, petugas: _Optional[_Union[Petugas, _Mapping]] = ...) -> None: ...

class PetugasUpdateRequest(_message.Message):
    __slots__ = ("id", "fnama", "email", "password", "username", "status")
    ID_FIELD_NUMBER: _ClassVar[int]
    FNAMA_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    id: int
    fnama: str
    email: str
    password: str
    username: str
    status: str
    def __init__(self, id: _Optional[int] = ..., fnama: _Optional[str] = ..., email: _Optional[str] = ..., password: _Optional[str] = ..., username: _Optional[str] = ..., status: _Optional[str] = ...) -> None: ...

class PetugasUpdateResponse(_message.Message):
    __slots__ = ("petugas",)
    PETUGAS_FIELD_NUMBER: _ClassVar[int]
    petugas: Petugas
    def __init__(self, petugas: _Optional[_Union[Petugas, _Mapping]] = ...) -> None: ...

class PetugasDeleteRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class PetugasDeleteResponse(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class PetugasLoginRequest(_message.Message):
    __slots__ = ("email", "password")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    email: str
    password: str
    def __init__(self, email: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class PetugasLoginResponse(_message.Message):
    __slots__ = ("token", "email", "fnama")
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    FNAMA_FIELD_NUMBER: _ClassVar[int]
    token: str
    email: str
    fnama: str
    def __init__(self, token: _Optional[str] = ..., email: _Optional[str] = ..., fnama: _Optional[str] = ...) -> None: ...

class PetugasLogoutRequest(_message.Message):
    __slots__ = ("token",)
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: str
    def __init__(self, token: _Optional[str] = ...) -> None: ...

class PetugasLogoutResponse(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...
