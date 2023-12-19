from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Buku(_message.Message):
    __slots__ = ("id", "judul", "pengarang", "penerbit", "tahun_terbit", "kategori_id", "isbn", "jumlah_buku", "deskripsi")
    ID_FIELD_NUMBER: _ClassVar[int]
    JUDUL_FIELD_NUMBER: _ClassVar[int]
    PENGARANG_FIELD_NUMBER: _ClassVar[int]
    PENERBIT_FIELD_NUMBER: _ClassVar[int]
    TAHUN_TERBIT_FIELD_NUMBER: _ClassVar[int]
    KATEGORI_ID_FIELD_NUMBER: _ClassVar[int]
    ISBN_FIELD_NUMBER: _ClassVar[int]
    JUMLAH_BUKU_FIELD_NUMBER: _ClassVar[int]
    DESKRIPSI_FIELD_NUMBER: _ClassVar[int]
    id: int
    judul: str
    pengarang: str
    penerbit: str
    tahun_terbit: str
    kategori_id: int
    isbn: str
    jumlah_buku: int
    deskripsi: str
    def __init__(self, id: _Optional[int] = ..., judul: _Optional[str] = ..., pengarang: _Optional[str] = ..., penerbit: _Optional[str] = ..., tahun_terbit: _Optional[str] = ..., kategori_id: _Optional[int] = ..., isbn: _Optional[str] = ..., jumlah_buku: _Optional[int] = ..., deskripsi: _Optional[str] = ...) -> None: ...

class BukuListRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BukuListResponse(_message.Message):
    __slots__ = ("buku",)
    BUKU_FIELD_NUMBER: _ClassVar[int]
    buku: _containers.RepeatedCompositeFieldContainer[Buku]
    def __init__(self, buku: _Optional[_Iterable[_Union[Buku, _Mapping]]] = ...) -> None: ...

class BukuDetailRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class BukuDetailResponse(_message.Message):
    __slots__ = ("buku",)
    BUKU_FIELD_NUMBER: _ClassVar[int]
    buku: Buku
    def __init__(self, buku: _Optional[_Union[Buku, _Mapping]] = ...) -> None: ...

class BukuCreateRequest(_message.Message):
    __slots__ = ("judul", "pengarang", "penerbit", "tahun_terbit", "kategori_id", "isbn", "jumlah_buku", "deskripsi")
    JUDUL_FIELD_NUMBER: _ClassVar[int]
    PENGARANG_FIELD_NUMBER: _ClassVar[int]
    PENERBIT_FIELD_NUMBER: _ClassVar[int]
    TAHUN_TERBIT_FIELD_NUMBER: _ClassVar[int]
    KATEGORI_ID_FIELD_NUMBER: _ClassVar[int]
    ISBN_FIELD_NUMBER: _ClassVar[int]
    JUMLAH_BUKU_FIELD_NUMBER: _ClassVar[int]
    DESKRIPSI_FIELD_NUMBER: _ClassVar[int]
    judul: str
    pengarang: str
    penerbit: str
    tahun_terbit: str
    kategori_id: int
    isbn: str
    jumlah_buku: int
    deskripsi: str
    def __init__(self, judul: _Optional[str] = ..., pengarang: _Optional[str] = ..., penerbit: _Optional[str] = ..., tahun_terbit: _Optional[str] = ..., kategori_id: _Optional[int] = ..., isbn: _Optional[str] = ..., jumlah_buku: _Optional[int] = ..., deskripsi: _Optional[str] = ...) -> None: ...

class BukuCreateResponse(_message.Message):
    __slots__ = ("buku",)
    BUKU_FIELD_NUMBER: _ClassVar[int]
    buku: Buku
    def __init__(self, buku: _Optional[_Union[Buku, _Mapping]] = ...) -> None: ...

class BukuUpdateRequest(_message.Message):
    __slots__ = ("id", "judul", "pengarang", "penerbit", "tahun_terbit", "kategori_id", "isbn", "jumlah_buku", "deskripsi")
    ID_FIELD_NUMBER: _ClassVar[int]
    JUDUL_FIELD_NUMBER: _ClassVar[int]
    PENGARANG_FIELD_NUMBER: _ClassVar[int]
    PENERBIT_FIELD_NUMBER: _ClassVar[int]
    TAHUN_TERBIT_FIELD_NUMBER: _ClassVar[int]
    KATEGORI_ID_FIELD_NUMBER: _ClassVar[int]
    ISBN_FIELD_NUMBER: _ClassVar[int]
    JUMLAH_BUKU_FIELD_NUMBER: _ClassVar[int]
    DESKRIPSI_FIELD_NUMBER: _ClassVar[int]
    id: int
    judul: str
    pengarang: str
    penerbit: str
    tahun_terbit: str
    kategori_id: int
    isbn: str
    jumlah_buku: int
    deskripsi: str
    def __init__(self, id: _Optional[int] = ..., judul: _Optional[str] = ..., pengarang: _Optional[str] = ..., penerbit: _Optional[str] = ..., tahun_terbit: _Optional[str] = ..., kategori_id: _Optional[int] = ..., isbn: _Optional[str] = ..., jumlah_buku: _Optional[int] = ..., deskripsi: _Optional[str] = ...) -> None: ...

class BukuUpdateResponse(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class BukuDeleteRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class BukuDeleteResponse(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...
