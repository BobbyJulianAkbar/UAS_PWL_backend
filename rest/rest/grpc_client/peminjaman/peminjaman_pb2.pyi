from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Peminjaman(_message.Message):
    __slots__ = ("id", "id_buku", "id_anggota", "tanggal_peminjaman", "tanggal_pengembalian", "status")
    ID_FIELD_NUMBER: _ClassVar[int]
    ID_BUKU_FIELD_NUMBER: _ClassVar[int]
    ID_ANGGOTA_FIELD_NUMBER: _ClassVar[int]
    TANGGAL_PEMINJAMAN_FIELD_NUMBER: _ClassVar[int]
    TANGGAL_PENGEMBALIAN_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    id: int
    id_buku: int
    id_anggota: int
    tanggal_peminjaman: str
    tanggal_pengembalian: str
    status: str
    def __init__(self, id: _Optional[int] = ..., id_buku: _Optional[int] = ..., id_anggota: _Optional[int] = ..., tanggal_peminjaman: _Optional[str] = ..., tanggal_pengembalian: _Optional[str] = ..., status: _Optional[str] = ...) -> None: ...

class PeminjamanListRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PeminjamanListResponse(_message.Message):
    __slots__ = ("peminjaman",)
    PEMINJAMAN_FIELD_NUMBER: _ClassVar[int]
    peminjaman: _containers.RepeatedCompositeFieldContainer[Peminjaman]
    def __init__(self, peminjaman: _Optional[_Iterable[_Union[Peminjaman, _Mapping]]] = ...) -> None: ...

class PeminjamanRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class PeminjamanResponse(_message.Message):
    __slots__ = ("peminjaman",)
    PEMINJAMAN_FIELD_NUMBER: _ClassVar[int]
    peminjaman: Peminjaman
    def __init__(self, peminjaman: _Optional[_Union[Peminjaman, _Mapping]] = ...) -> None: ...

class PeminjamanCreateRequest(_message.Message):
    __slots__ = ("id_buku", "id_anggota", "tanggal_peminjaman", "tanggal_pengembalian", "status")
    ID_BUKU_FIELD_NUMBER: _ClassVar[int]
    ID_ANGGOTA_FIELD_NUMBER: _ClassVar[int]
    TANGGAL_PEMINJAMAN_FIELD_NUMBER: _ClassVar[int]
    TANGGAL_PENGEMBALIAN_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    id_buku: int
    id_anggota: int
    tanggal_peminjaman: str
    tanggal_pengembalian: str
    status: str
    def __init__(self, id_buku: _Optional[int] = ..., id_anggota: _Optional[int] = ..., tanggal_peminjaman: _Optional[str] = ..., tanggal_pengembalian: _Optional[str] = ..., status: _Optional[str] = ...) -> None: ...

class PeminjamanCreateResponse(_message.Message):
    __slots__ = ("peminjaman",)
    PEMINJAMAN_FIELD_NUMBER: _ClassVar[int]
    peminjaman: Peminjaman
    def __init__(self, peminjaman: _Optional[_Union[Peminjaman, _Mapping]] = ...) -> None: ...

class PeminjamanUpdateRequest(_message.Message):
    __slots__ = ("id", "id_buku", "id_anggota", "tanggal_peminjaman", "tanggal_pengembalian", "status")
    ID_FIELD_NUMBER: _ClassVar[int]
    ID_BUKU_FIELD_NUMBER: _ClassVar[int]
    ID_ANGGOTA_FIELD_NUMBER: _ClassVar[int]
    TANGGAL_PEMINJAMAN_FIELD_NUMBER: _ClassVar[int]
    TANGGAL_PENGEMBALIAN_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    id: int
    id_buku: int
    id_anggota: int
    tanggal_peminjaman: str
    tanggal_pengembalian: str
    status: str
    def __init__(self, id: _Optional[int] = ..., id_buku: _Optional[int] = ..., id_anggota: _Optional[int] = ..., tanggal_peminjaman: _Optional[str] = ..., tanggal_pengembalian: _Optional[str] = ..., status: _Optional[str] = ...) -> None: ...

class PeminjamanUpdateResponse(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class PeminjamanDeleteRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class PeminjamanDeleteResponse(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...
