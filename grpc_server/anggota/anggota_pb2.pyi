from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Anggota(_message.Message):
    __slots__ = ("id", "nama", "email", "nis", "password", "token")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAMA_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    NIS_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    id: int
    nama: str
    email: str
    nis: str
    password: str
    token: str
    def __init__(self, id: _Optional[int] = ..., nama: _Optional[str] = ..., email: _Optional[str] = ..., nis: _Optional[str] = ..., password: _Optional[str] = ..., token: _Optional[str] = ...) -> None: ...

class AnggotaListRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AnggotaListResponse(_message.Message):
    __slots__ = ("anggota",)
    ANGGOTA_FIELD_NUMBER: _ClassVar[int]
    anggota: _containers.RepeatedCompositeFieldContainer[Anggota]
    def __init__(self, anggota: _Optional[_Iterable[_Union[Anggota, _Mapping]]] = ...) -> None: ...

class AnggotaRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class AnggotaResponse(_message.Message):
    __slots__ = ("anggota",)
    ANGGOTA_FIELD_NUMBER: _ClassVar[int]
    anggota: Anggota
    def __init__(self, anggota: _Optional[_Union[Anggota, _Mapping]] = ...) -> None: ...

class AnggotaCreateRequest(_message.Message):
    __slots__ = ("nama", "email", "nis", "password")
    NAMA_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    NIS_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    nama: str
    email: str
    nis: str
    password: str
    def __init__(self, nama: _Optional[str] = ..., email: _Optional[str] = ..., nis: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class AnggotaCreateResponse(_message.Message):
    __slots__ = ("anggota",)
    ANGGOTA_FIELD_NUMBER: _ClassVar[int]
    anggota: Anggota
    def __init__(self, anggota: _Optional[_Union[Anggota, _Mapping]] = ...) -> None: ...

class AnggotaUpdateRequest(_message.Message):
    __slots__ = ("id", "nama", "email", "nis", "password")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAMA_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    NIS_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    id: int
    nama: str
    email: str
    nis: str
    password: str
    def __init__(self, id: _Optional[int] = ..., nama: _Optional[str] = ..., email: _Optional[str] = ..., nis: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class AnggotaUpdateResponse(_message.Message):
    __slots__ = ("anggota",)
    ANGGOTA_FIELD_NUMBER: _ClassVar[int]
    anggota: Anggota
    def __init__(self, anggota: _Optional[_Union[Anggota, _Mapping]] = ...) -> None: ...

class AnggotaDeleteRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class AnggotaDeleteResponse(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class AnggotaLoginRequest(_message.Message):
    __slots__ = ("email", "password")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    email: str
    password: str
    def __init__(self, email: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class AnggotaLoginResponse(_message.Message):
    __slots__ = ("token", "email", "nama", "id")
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    NAMA_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    token: str
    email: str
    nama: str
    id: int
    def __init__(self, token: _Optional[str] = ..., email: _Optional[str] = ..., nama: _Optional[str] = ..., id: _Optional[int] = ...) -> None: ...

class AnggotaLogoutRequest(_message.Message):
    __slots__ = ("token",)
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: str
    def __init__(self, token: _Optional[str] = ...) -> None: ...

class AnggotaLogoutResponse(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...
