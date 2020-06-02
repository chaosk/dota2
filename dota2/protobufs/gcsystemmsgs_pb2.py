# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gcsystemmsgs.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='gcsystemmsgs.proto',
  package='dota',
  syntax='proto2',
  serialized_options=b'H\001\220\001\000',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x12gcsystemmsgs.proto\x12\x04\x64ota*\xf0\x01\n\x06\x45SOMsg\x12\x13\n\x0fk_ESOMsg_Create\x10\x15\x12\x13\n\x0fk_ESOMsg_Update\x10\x16\x12\x14\n\x10k_ESOMsg_Destroy\x10\x17\x12\x1c\n\x18k_ESOMsg_CacheSubscribed\x10\x18\x12\x1e\n\x1ak_ESOMsg_CacheUnsubscribed\x10\x19\x12\x1b\n\x17k_ESOMsg_UpdateMultiple\x10\x1a\x12%\n!k_ESOMsg_CacheSubscriptionRefresh\x10\x1c\x12$\n k_ESOMsg_CacheSubscribedUpToDate\x10\x1d*\xc2\x03\n\x10\x45GCBaseClientMsg\x12\x18\n\x13k_EMsgGCPingRequest\x10\xb9\x17\x12\x19\n\x14k_EMsgGCPingResponse\x10\xba\x17\x12&\n!k_EMsgGCToClientPollConvarRequest\x10\xbb\x17\x12\'\n\"k_EMsgGCToClientPollConvarResponse\x10\xbc\x17\x12\"\n\x1dk_EMsgGCCompressedMsgToClient\x10\xbd\x17\x12)\n$k_EMsgGCCompressedMsgToClient_Legacy\x10\x8b\x04\x12#\n\x1ek_EMsgGCToClientRequestDropped\x10\xbe\x17\x12\x1a\n\x15k_EMsgGCClientWelcome\x10\xa4\x1f\x12\x1a\n\x15k_EMsgGCServerWelcome\x10\xa5\x1f\x12\x18\n\x13k_EMsgGCClientHello\x10\xa6\x1f\x12\x18\n\x13k_EMsgGCServerHello\x10\xa7\x1f\x12#\n\x1ek_EMsgGCClientConnectionStatus\x10\xa9\x1f\x12#\n\x1ek_EMsgGCServerConnectionStatus\x10\xaa\x1f\x42\x05H\x01\x90\x01\x00'
)

_ESOMSG = _descriptor.EnumDescriptor(
  name='ESOMsg',
  full_name='dota.ESOMsg',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='k_ESOMsg_Create', index=0, number=21,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='k_ESOMsg_Update', index=1, number=22,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='k_ESOMsg_Destroy', index=2, number=23,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='k_ESOMsg_CacheSubscribed', index=3, number=24,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='k_ESOMsg_CacheUnsubscribed', index=4, number=25,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='k_ESOMsg_UpdateMultiple', index=5, number=26,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='k_ESOMsg_CacheSubscriptionRefresh', index=6, number=28,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='k_ESOMsg_CacheSubscribedUpToDate', index=7, number=29,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=29,
  serialized_end=269,
)
_sym_db.RegisterEnumDescriptor(_ESOMSG)

ESOMsg = enum_type_wrapper.EnumTypeWrapper(_ESOMSG)
_EGCBASECLIENTMSG = _descriptor.EnumDescriptor(
  name='EGCBaseClientMsg',
  full_name='dota.EGCBaseClientMsg',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='k_EMsgGCPingRequest', index=0, number=3001,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='k_EMsgGCPingResponse', index=1, number=3002,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='k_EMsgGCToClientPollConvarRequest', index=2, number=3003,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='k_EMsgGCToClientPollConvarResponse', index=3, number=3004,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='k_EMsgGCCompressedMsgToClient', index=4, number=3005,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='k_EMsgGCCompressedMsgToClient_Legacy', index=5, number=523,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='k_EMsgGCToClientRequestDropped', index=6, number=3006,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='k_EMsgGCClientWelcome', index=7, number=4004,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='k_EMsgGCServerWelcome', index=8, number=4005,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='k_EMsgGCClientHello', index=9, number=4006,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='k_EMsgGCServerHello', index=10, number=4007,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='k_EMsgGCClientConnectionStatus', index=11, number=4009,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='k_EMsgGCServerConnectionStatus', index=12, number=4010,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=272,
  serialized_end=722,
)
_sym_db.RegisterEnumDescriptor(_EGCBASECLIENTMSG)

EGCBaseClientMsg = enum_type_wrapper.EnumTypeWrapper(_EGCBASECLIENTMSG)
k_ESOMsg_Create = 21
k_ESOMsg_Update = 22
k_ESOMsg_Destroy = 23
k_ESOMsg_CacheSubscribed = 24
k_ESOMsg_CacheUnsubscribed = 25
k_ESOMsg_UpdateMultiple = 26
k_ESOMsg_CacheSubscriptionRefresh = 28
k_ESOMsg_CacheSubscribedUpToDate = 29
k_EMsgGCPingRequest = 3001
k_EMsgGCPingResponse = 3002
k_EMsgGCToClientPollConvarRequest = 3003
k_EMsgGCToClientPollConvarResponse = 3004
k_EMsgGCCompressedMsgToClient = 3005
k_EMsgGCCompressedMsgToClient_Legacy = 523
k_EMsgGCToClientRequestDropped = 3006
k_EMsgGCClientWelcome = 4004
k_EMsgGCServerWelcome = 4005
k_EMsgGCClientHello = 4006
k_EMsgGCServerHello = 4007
k_EMsgGCClientConnectionStatus = 4009
k_EMsgGCServerConnectionStatus = 4010


DESCRIPTOR.enum_types_by_name['ESOMsg'] = _ESOMSG
DESCRIPTOR.enum_types_by_name['EGCBaseClientMsg'] = _EGCBASECLIENTMSG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
