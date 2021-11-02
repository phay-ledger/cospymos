# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/feegrant/v1beta1/tx.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cosmos/feegrant/v1beta1/tx.proto',
  package='cosmos.feegrant.v1beta1',
  syntax='proto3',
  serialized_options=b'Z\'github.com/cosmos/cosmos-sdk/x/feegrant',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n cosmos/feegrant/v1beta1/tx.proto\x12\x17\x63osmos.feegrant.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x19google/protobuf/any.proto\x1a\x19\x63osmos_proto/cosmos.proto\"\xa5\x01\n\x11MsgGrantAllowance\x12)\n\x07granter\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12)\n\x07grantee\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12:\n\tallowance\x18\x03 \x01(\x0b\x32\x14.google.protobuf.AnyB\x11\xca\xb4-\rFeeAllowanceI\"\x1b\n\x19MsgGrantAllowanceResponse\"j\n\x12MsgRevokeAllowance\x12)\n\x07granter\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12)\n\x07grantee\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\"\x1c\n\x1aMsgRevokeAllowanceResponse2\xec\x01\n\x03Msg\x12p\n\x0eGrantAllowance\x12*.cosmos.feegrant.v1beta1.MsgGrantAllowance\x1a\x32.cosmos.feegrant.v1beta1.MsgGrantAllowanceResponse\x12s\n\x0fRevokeAllowance\x12+.cosmos.feegrant.v1beta1.MsgRevokeAllowance\x1a\x33.cosmos.feegrant.v1beta1.MsgRevokeAllowanceResponseB)Z\'github.com/cosmos/cosmos-sdk/x/feegrantb\x06proto3'
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,google_dot_protobuf_dot_any__pb2.DESCRIPTOR,cosmos__proto_dot_cosmos__pb2.DESCRIPTOR,])




_MSGGRANTALLOWANCE = _descriptor.Descriptor(
  name='MsgGrantAllowance',
  full_name='cosmos.feegrant.v1beta1.MsgGrantAllowance',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='granter', full_name='cosmos.feegrant.v1beta1.MsgGrantAllowance.granter', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\322\264-\024cosmos.AddressString', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='grantee', full_name='cosmos.feegrant.v1beta1.MsgGrantAllowance.grantee', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\322\264-\024cosmos.AddressString', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='allowance', full_name='cosmos.feegrant.v1beta1.MsgGrantAllowance.allowance', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\312\264-\rFeeAllowanceI', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=138,
  serialized_end=303,
)


_MSGGRANTALLOWANCERESPONSE = _descriptor.Descriptor(
  name='MsgGrantAllowanceResponse',
  full_name='cosmos.feegrant.v1beta1.MsgGrantAllowanceResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=305,
  serialized_end=332,
)


_MSGREVOKEALLOWANCE = _descriptor.Descriptor(
  name='MsgRevokeAllowance',
  full_name='cosmos.feegrant.v1beta1.MsgRevokeAllowance',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='granter', full_name='cosmos.feegrant.v1beta1.MsgRevokeAllowance.granter', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\322\264-\024cosmos.AddressString', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='grantee', full_name='cosmos.feegrant.v1beta1.MsgRevokeAllowance.grantee', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\322\264-\024cosmos.AddressString', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=334,
  serialized_end=440,
)


_MSGREVOKEALLOWANCERESPONSE = _descriptor.Descriptor(
  name='MsgRevokeAllowanceResponse',
  full_name='cosmos.feegrant.v1beta1.MsgRevokeAllowanceResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=442,
  serialized_end=470,
)

_MSGGRANTALLOWANCE.fields_by_name['allowance'].message_type = google_dot_protobuf_dot_any__pb2._ANY
DESCRIPTOR.message_types_by_name['MsgGrantAllowance'] = _MSGGRANTALLOWANCE
DESCRIPTOR.message_types_by_name['MsgGrantAllowanceResponse'] = _MSGGRANTALLOWANCERESPONSE
DESCRIPTOR.message_types_by_name['MsgRevokeAllowance'] = _MSGREVOKEALLOWANCE
DESCRIPTOR.message_types_by_name['MsgRevokeAllowanceResponse'] = _MSGREVOKEALLOWANCERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MsgGrantAllowance = _reflection.GeneratedProtocolMessageType('MsgGrantAllowance', (_message.Message,), {
  'DESCRIPTOR' : _MSGGRANTALLOWANCE,
  '__module__' : 'cosmos.feegrant.v1beta1.tx_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.feegrant.v1beta1.MsgGrantAllowance)
  })
_sym_db.RegisterMessage(MsgGrantAllowance)

MsgGrantAllowanceResponse = _reflection.GeneratedProtocolMessageType('MsgGrantAllowanceResponse', (_message.Message,), {
  'DESCRIPTOR' : _MSGGRANTALLOWANCERESPONSE,
  '__module__' : 'cosmos.feegrant.v1beta1.tx_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.feegrant.v1beta1.MsgGrantAllowanceResponse)
  })
_sym_db.RegisterMessage(MsgGrantAllowanceResponse)

MsgRevokeAllowance = _reflection.GeneratedProtocolMessageType('MsgRevokeAllowance', (_message.Message,), {
  'DESCRIPTOR' : _MSGREVOKEALLOWANCE,
  '__module__' : 'cosmos.feegrant.v1beta1.tx_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.feegrant.v1beta1.MsgRevokeAllowance)
  })
_sym_db.RegisterMessage(MsgRevokeAllowance)

MsgRevokeAllowanceResponse = _reflection.GeneratedProtocolMessageType('MsgRevokeAllowanceResponse', (_message.Message,), {
  'DESCRIPTOR' : _MSGREVOKEALLOWANCERESPONSE,
  '__module__' : 'cosmos.feegrant.v1beta1.tx_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.feegrant.v1beta1.MsgRevokeAllowanceResponse)
  })
_sym_db.RegisterMessage(MsgRevokeAllowanceResponse)


DESCRIPTOR._options = None
_MSGGRANTALLOWANCE.fields_by_name['granter']._options = None
_MSGGRANTALLOWANCE.fields_by_name['grantee']._options = None
_MSGGRANTALLOWANCE.fields_by_name['allowance']._options = None
_MSGREVOKEALLOWANCE.fields_by_name['granter']._options = None
_MSGREVOKEALLOWANCE.fields_by_name['grantee']._options = None

_MSG = _descriptor.ServiceDescriptor(
  name='Msg',
  full_name='cosmos.feegrant.v1beta1.Msg',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=473,
  serialized_end=709,
  methods=[
  _descriptor.MethodDescriptor(
    name='GrantAllowance',
    full_name='cosmos.feegrant.v1beta1.Msg.GrantAllowance',
    index=0,
    containing_service=None,
    input_type=_MSGGRANTALLOWANCE,
    output_type=_MSGGRANTALLOWANCERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='RevokeAllowance',
    full_name='cosmos.feegrant.v1beta1.Msg.RevokeAllowance',
    index=1,
    containing_service=None,
    input_type=_MSGREVOKEALLOWANCE,
    output_type=_MSGREVOKEALLOWANCERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MSG)

DESCRIPTOR.services_by_name['Msg'] = _MSG

# @@protoc_insertion_point(module_scope)