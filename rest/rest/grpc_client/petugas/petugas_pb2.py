# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: petugas.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rpetugas.proto\x12\x07petugas\"g\n\x07Petugas\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05\x66nama\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12\x10\n\x08password\x18\x04 \x01(\t\x12\x10\n\x08username\x18\x05 \x01(\t\x12\x0e\n\x06status\x18\x06 \x01(\t\"\x14\n\x12PetugasListRequest\"8\n\x13PetugasListResponse\x12!\n\x07petugas\x18\x01 \x03(\x0b\x32\x10.petugas.Petugas\"\"\n\x14PetugasDetailRequest\x12\n\n\x02id\x18\x01 \x01(\x05\":\n\x15PetugasDetailResponse\x12!\n\x07petugas\x18\x01 \x01(\x0b\x32\x10.petugas.Petugas\"h\n\x14PetugasCreateRequest\x12\r\n\x05\x66nama\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\x10\n\x08password\x18\x03 \x01(\t\x12\x10\n\x08username\x18\x04 \x01(\t\x12\x0e\n\x06status\x18\x05 \x01(\t\":\n\x15PetugasCreateResponse\x12!\n\x07petugas\x18\x01 \x01(\x0b\x32\x10.petugas.Petugas\"t\n\x14PetugasUpdateRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05\x66nama\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12\x10\n\x08password\x18\x04 \x01(\t\x12\x10\n\x08username\x18\x05 \x01(\t\x12\x0e\n\x06status\x18\x06 \x01(\t\":\n\x15PetugasUpdateResponse\x12!\n\x07petugas\x18\x01 \x01(\x0b\x32\x10.petugas.Petugas\"\"\n\x14PetugasDeleteRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"(\n\x15PetugasDeleteResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"6\n\x13PetugasLoginRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"C\n\x14PetugasLoginResponse\x12\r\n\x05token\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\r\n\x05\x66nama\x18\x03 \x01(\t\"%\n\x14PetugasLogoutRequest\x12\r\n\x05token\x18\x01 \x01(\t\"(\n\x15PetugasLogoutResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2\x86\x04\n\x0ePetugasService\x12\x41\n\x04List\x12\x1b.petugas.PetugasListRequest\x1a\x1c.petugas.PetugasListResponse\x12G\n\x06\x44\x65tail\x12\x1d.petugas.PetugasDetailRequest\x1a\x1e.petugas.PetugasDetailResponse\x12G\n\x06\x43reate\x12\x1d.petugas.PetugasCreateRequest\x1a\x1e.petugas.PetugasCreateResponse\x12G\n\x06Update\x12\x1d.petugas.PetugasUpdateRequest\x1a\x1e.petugas.PetugasUpdateResponse\x12G\n\x06\x44\x65lete\x12\x1d.petugas.PetugasDeleteRequest\x1a\x1e.petugas.PetugasDeleteResponse\x12\x44\n\x05Login\x12\x1c.petugas.PetugasLoginRequest\x1a\x1d.petugas.PetugasLoginResponse\x12G\n\x06Logout\x12\x1d.petugas.PetugasLogoutRequest\x1a\x1e.petugas.PetugasLogoutResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'petugas_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_PETUGAS']._serialized_start=26
  _globals['_PETUGAS']._serialized_end=129
  _globals['_PETUGASLISTREQUEST']._serialized_start=131
  _globals['_PETUGASLISTREQUEST']._serialized_end=151
  _globals['_PETUGASLISTRESPONSE']._serialized_start=153
  _globals['_PETUGASLISTRESPONSE']._serialized_end=209
  _globals['_PETUGASDETAILREQUEST']._serialized_start=211
  _globals['_PETUGASDETAILREQUEST']._serialized_end=245
  _globals['_PETUGASDETAILRESPONSE']._serialized_start=247
  _globals['_PETUGASDETAILRESPONSE']._serialized_end=305
  _globals['_PETUGASCREATEREQUEST']._serialized_start=307
  _globals['_PETUGASCREATEREQUEST']._serialized_end=411
  _globals['_PETUGASCREATERESPONSE']._serialized_start=413
  _globals['_PETUGASCREATERESPONSE']._serialized_end=471
  _globals['_PETUGASUPDATEREQUEST']._serialized_start=473
  _globals['_PETUGASUPDATEREQUEST']._serialized_end=589
  _globals['_PETUGASUPDATERESPONSE']._serialized_start=591
  _globals['_PETUGASUPDATERESPONSE']._serialized_end=649
  _globals['_PETUGASDELETEREQUEST']._serialized_start=651
  _globals['_PETUGASDELETEREQUEST']._serialized_end=685
  _globals['_PETUGASDELETERESPONSE']._serialized_start=687
  _globals['_PETUGASDELETERESPONSE']._serialized_end=727
  _globals['_PETUGASLOGINREQUEST']._serialized_start=729
  _globals['_PETUGASLOGINREQUEST']._serialized_end=783
  _globals['_PETUGASLOGINRESPONSE']._serialized_start=785
  _globals['_PETUGASLOGINRESPONSE']._serialized_end=852
  _globals['_PETUGASLOGOUTREQUEST']._serialized_start=854
  _globals['_PETUGASLOGOUTREQUEST']._serialized_end=891
  _globals['_PETUGASLOGOUTRESPONSE']._serialized_start=893
  _globals['_PETUGASLOGOUTRESPONSE']._serialized_end=933
  _globals['_PETUGASSERVICE']._serialized_start=936
  _globals['_PETUGASSERVICE']._serialized_end=1454
# @@protoc_insertion_point(module_scope)