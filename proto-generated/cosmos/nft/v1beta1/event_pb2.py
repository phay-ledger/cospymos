# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/nft/v1beta1/event.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cosmos/nft/v1beta1/event.proto',
  package='cosmos.nft.v1beta1',
  syntax='proto3',
  serialized_options=b'Z\"github.com/cosmos/cosmos-sdk/x/nft',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1e\x63osmos/nft/v1beta1/event.proto\x12\x12\x63osmos.nft.v1beta1\x1a\x14gogoproto/gogo.proto\"K\n\tEventSend\x12\x10\n\x08\x63lass_id\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x0e\n\x06sender\x18\x03 \x01(\t\x12\x10\n\x08receiver\x18\x04 \x01(\t\"8\n\tEventMint\x12\x10\n\x08\x63lass_id\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\r\n\x05owner\x18\x03 \x01(\t\"8\n\tEventBurn\x12\x10\n\x08\x63lass_id\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\r\n\x05owner\x18\x03 \x01(\tB$Z\"github.com/cosmos/cosmos-sdk/x/nftb\x06proto3'
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,])




_EVENTSEND = _descriptor.Descriptor(
  name='EventSend',
  full_name='cosmos.nft.v1beta1.EventSend',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='class_id', full_name='cosmos.nft.v1beta1.EventSend.class_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='cosmos.nft.v1beta1.EventSend.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sender', full_name='cosmos.nft.v1beta1.EventSend.sender', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='receiver', full_name='cosmos.nft.v1beta1.EventSend.receiver', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=76,
  serialized_end=151,
)


_EVENTMINT = _descriptor.Descriptor(
  name='EventMint',
  full_name='cosmos.nft.v1beta1.EventMint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='class_id', full_name='cosmos.nft.v1beta1.EventMint.class_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='cosmos.nft.v1beta1.EventMint.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='owner', full_name='cosmos.nft.v1beta1.EventMint.owner', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=153,
  serialized_end=209,
)


_EVENTBURN = _descriptor.Descriptor(
  name='EventBurn',
  full_name='cosmos.nft.v1beta1.EventBurn',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='class_id', full_name='cosmos.nft.v1beta1.EventBurn.class_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='cosmos.nft.v1beta1.EventBurn.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='owner', full_name='cosmos.nft.v1beta1.EventBurn.owner', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=211,
  serialized_end=267,
)

DESCRIPTOR.message_types_by_name['EventSend'] = _EVENTSEND
DESCRIPTOR.message_types_by_name['EventMint'] = _EVENTMINT
DESCRIPTOR.message_types_by_name['EventBurn'] = _EVENTBURN
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EventSend = _reflection.GeneratedProtocolMessageType('EventSend', (_message.Message,), {
  'DESCRIPTOR' : _EVENTSEND,
  '__module__' : 'cosmos.nft.v1beta1.event_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.nft.v1beta1.EventSend)
  })
_sym_db.RegisterMessage(EventSend)

EventMint = _reflection.GeneratedProtocolMessageType('EventMint', (_message.Message,), {
  'DESCRIPTOR' : _EVENTMINT,
  '__module__' : 'cosmos.nft.v1beta1.event_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.nft.v1beta1.EventMint)
  })
_sym_db.RegisterMessage(EventMint)

EventBurn = _reflection.GeneratedProtocolMessageType('EventBurn', (_message.Message,), {
  'DESCRIPTOR' : _EVENTBURN,
  '__module__' : 'cosmos.nft.v1beta1.event_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.nft.v1beta1.EventBurn)
  })
_sym_db.RegisterMessage(EventBurn)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)