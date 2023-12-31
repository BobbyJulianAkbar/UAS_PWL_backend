# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: anggota.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ranggota.proto\x12\x07\x61nggota\"`\n\x07\x41nggota\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04nama\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12\x0b\n\x03nis\x18\x04 \x01(\t\x12\x10\n\x08password\x18\x05 \x01(\t\x12\r\n\x05token\x18\x06 \x01(\t\"\x14\n\x12\x41nggotaListRequest\"8\n\x13\x41nggotaListResponse\x12!\n\x07\x61nggota\x18\x01 \x03(\x0b\x32\x10.anggota.Anggota\"\x1c\n\x0e\x41nggotaRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"4\n\x0f\x41nggotaResponse\x12!\n\x07\x61nggota\x18\x01 \x01(\x0b\x32\x10.anggota.Anggota\"R\n\x14\x41nggotaCreateRequest\x12\x0c\n\x04nama\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\x0b\n\x03nis\x18\x03 \x01(\t\x12\x10\n\x08password\x18\x04 \x01(\t\":\n\x15\x41nggotaCreateResponse\x12!\n\x07\x61nggota\x18\x01 \x01(\x0b\x32\x10.anggota.Anggota\"^\n\x14\x41nggotaUpdateRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04nama\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12\x0b\n\x03nis\x18\x04 \x01(\t\x12\x10\n\x08password\x18\x05 \x01(\t\":\n\x15\x41nggotaUpdateResponse\x12!\n\x07\x61nggota\x18\x01 \x01(\x0b\x32\x10.anggota.Anggota\"\"\n\x14\x41nggotaDeleteRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"(\n\x15\x41nggotaDeleteResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"6\n\x13\x41nggotaLoginRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"N\n\x14\x41nggotaLoginResponse\x12\r\n\x05token\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\x0c\n\x04nama\x18\x03 \x01(\t\x12\n\n\x02id\x18\x04 \x01(\x05\"%\n\x14\x41nggotaLogoutRequest\x12\r\n\x05token\x18\x01 \x01(\t\"(\n\x15\x41nggotaLogoutResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2\xf7\x03\n\x0e\x41nggotaService\x12\x41\n\x04List\x12\x1b.anggota.AnggotaListRequest\x1a\x1c.anggota.AnggotaListResponse\x12\x38\n\x03Get\x12\x17.anggota.AnggotaRequest\x1a\x18.anggota.AnggotaResponse\x12G\n\x06\x43reate\x12\x1d.anggota.AnggotaCreateRequest\x1a\x1e.anggota.AnggotaCreateResponse\x12G\n\x06Update\x12\x1d.anggota.AnggotaUpdateRequest\x1a\x1e.anggota.AnggotaUpdateResponse\x12G\n\x06\x44\x65lete\x12\x1d.anggota.AnggotaDeleteRequest\x1a\x1e.anggota.AnggotaDeleteResponse\x12\x44\n\x05Login\x12\x1c.anggota.AnggotaLoginRequest\x1a\x1d.anggota.AnggotaLoginResponse\x12G\n\x06Logout\x12\x1d.anggota.AnggotaLogoutRequest\x1a\x1e.anggota.AnggotaLogoutResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'anggota_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_ANGGOTA']._serialized_start=26
  _globals['_ANGGOTA']._serialized_end=122
  _globals['_ANGGOTALISTREQUEST']._serialized_start=124
  _globals['_ANGGOTALISTREQUEST']._serialized_end=144
  _globals['_ANGGOTALISTRESPONSE']._serialized_start=146
  _globals['_ANGGOTALISTRESPONSE']._serialized_end=202
  _globals['_ANGGOTAREQUEST']._serialized_start=204
  _globals['_ANGGOTAREQUEST']._serialized_end=232
  _globals['_ANGGOTARESPONSE']._serialized_start=234
  _globals['_ANGGOTARESPONSE']._serialized_end=286
  _globals['_ANGGOTACREATEREQUEST']._serialized_start=288
  _globals['_ANGGOTACREATEREQUEST']._serialized_end=370
  _globals['_ANGGOTACREATERESPONSE']._serialized_start=372
  _globals['_ANGGOTACREATERESPONSE']._serialized_end=430
  _globals['_ANGGOTAUPDATEREQUEST']._serialized_start=432
  _globals['_ANGGOTAUPDATEREQUEST']._serialized_end=526
  _globals['_ANGGOTAUPDATERESPONSE']._serialized_start=528
  _globals['_ANGGOTAUPDATERESPONSE']._serialized_end=586
  _globals['_ANGGOTADELETEREQUEST']._serialized_start=588
  _globals['_ANGGOTADELETEREQUEST']._serialized_end=622
  _globals['_ANGGOTADELETERESPONSE']._serialized_start=624
  _globals['_ANGGOTADELETERESPONSE']._serialized_end=664
  _globals['_ANGGOTALOGINREQUEST']._serialized_start=666
  _globals['_ANGGOTALOGINREQUEST']._serialized_end=720
  _globals['_ANGGOTALOGINRESPONSE']._serialized_start=722
  _globals['_ANGGOTALOGINRESPONSE']._serialized_end=800
  _globals['_ANGGOTALOGOUTREQUEST']._serialized_start=802
  _globals['_ANGGOTALOGOUTREQUEST']._serialized_end=839
  _globals['_ANGGOTALOGOUTRESPONSE']._serialized_start=841
  _globals['_ANGGOTALOGOUTRESPONSE']._serialized_end=881
  _globals['_ANGGOTASERVICE']._serialized_start=884
  _globals['_ANGGOTASERVICE']._serialized_end=1387
# @@protoc_insertion_point(module_scope)
