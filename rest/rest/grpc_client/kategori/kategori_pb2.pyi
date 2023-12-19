from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Kategori(_message.Message):
    __slots__ = ("id", "nama")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAMA_FIELD_NUMBER: _ClassVar[int]
    id: int
    nama: str
    def __init__(self, id: _Optional[int] = ..., nama: _Optional[str] = ...) -> None: ...

class KategoriRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class KategoriResponse(_message.Message):
    __slots__ = ("kategori",)
    KATEGORI_FIELD_NUMBER: _ClassVar[int]
    kategori: Kategori
    def __init__(self, kategori: _Optional[_Union[Kategori, _Mapping]] = ...) -> None: ...

class KategoriListRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class KategoriListResponse(_message.Message):
    __slots__ = ("kategori",)
    KATEGORI_FIELD_NUMBER: _ClassVar[int]
    kategori: _containers.RepeatedCompositeFieldContainer[Kategori]
    def __init__(self, kategori: _Optional[_Iterable[_Union[Kategori, _Mapping]]] = ...) -> None: ...

class KategoriCreateRequest(_message.Message):
    __slots__ = ("nama",)
    NAMA_FIELD_NUMBER: _ClassVar[int]
    nama: str
    def __init__(self, nama: _Optional[str] = ...) -> None: ...

class KategoriCreateResponse(_message.Message):
    __slots__ = ("id", "nama")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAMA_FIELD_NUMBER: _ClassVar[int]
    id: int
    nama: str
    def __init__(self, id: _Optional[int] = ..., nama: _Optional[str] = ...) -> None: ...

class KategoriUpdateRequest(_message.Message):
    __slots__ = ("id", "nama")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAMA_FIELD_NUMBER: _ClassVar[int]
    id: int
    nama: str
    def __init__(self, id: _Optional[int] = ..., nama: _Optional[str] = ...) -> None: ...

class KategoriUpdateResponse(_message.Message):
    __slots__ = ("id", "nama")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAMA_FIELD_NUMBER: _ClassVar[int]
    id: int
    nama: str
    def __init__(self, id: _Optional[int] = ..., nama: _Optional[str] = ...) -> None: ...

class KategoriDeleteRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class KategoriDeleteResponse(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...
