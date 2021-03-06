# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/vesting/v1beta1/tx.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from cosmos.vesting.v1beta1 import vesting_pb2 as cosmos_dot_vesting_dot_v1beta1_dot_vesting__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cosmos/vesting/v1beta1/tx.proto',
  package='cosmos.vesting.v1beta1',
  syntax='proto3',
  serialized_options=b'Z1github.com/cosmos/cosmos-sdk/x/auth/vesting/types',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1f\x63osmos/vesting/v1beta1/tx.proto\x12\x16\x63osmos.vesting.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a$cosmos/vesting/v1beta1/vesting.proto\"\xfd\x01\n\x17MsgCreateVestingAccount\x12.\n\x0c\x66rom_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12,\n\nto_address\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12[\n\x06\x61mount\x18\x03 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x12\x10\n\x08\x65nd_time\x18\x04 \x01(\x03\x12\x0f\n\x07\x64\x65layed\x18\x05 \x01(\x08:\x04\xe8\xa0\x1f\x01\"!\n\x1fMsgCreateVestingAccountResponse\"\xa4\x01\n\x1fMsgCreatePeriodicVestingAccount\x12\x14\n\x0c\x66rom_address\x18\x01 \x01(\t\x12\x12\n\nto_address\x18\x02 \x01(\t\x12\x12\n\nstart_time\x18\x03 \x01(\x03\x12=\n\x0fvesting_periods\x18\x04 \x03(\x0b\x32\x1e.cosmos.vesting.v1beta1.PeriodB\x04\xc8\xde\x1f\x00:\x04\xe8\xa0\x1f\x00\")\n\'MsgCreatePeriodicVestingAccountResponse2\xa3\x02\n\x03Msg\x12\x80\x01\n\x14\x43reateVestingAccount\x12/.cosmos.vesting.v1beta1.MsgCreateVestingAccount\x1a\x37.cosmos.vesting.v1beta1.MsgCreateVestingAccountResponse\x12\x98\x01\n\x1c\x43reatePeriodicVestingAccount\x12\x37.cosmos.vesting.v1beta1.MsgCreatePeriodicVestingAccount\x1a?.cosmos.vesting.v1beta1.MsgCreatePeriodicVestingAccountResponseB3Z1github.com/cosmos/cosmos-sdk/x/auth/vesting/typesb\x06proto3'
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,cosmos_dot_base_dot_v1beta1_dot_coin__pb2.DESCRIPTOR,cosmos__proto_dot_cosmos__pb2.DESCRIPTOR,cosmos_dot_vesting_dot_v1beta1_dot_vesting__pb2.DESCRIPTOR,])




_MSGCREATEVESTINGACCOUNT = _descriptor.Descriptor(
  name='MsgCreateVestingAccount',
  full_name='cosmos.vesting.v1beta1.MsgCreateVestingAccount',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='from_address', full_name='cosmos.vesting.v1beta1.MsgCreateVestingAccount.from_address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\322\264-\024cosmos.AddressString', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='to_address', full_name='cosmos.vesting.v1beta1.MsgCreateVestingAccount.to_address', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\322\264-\024cosmos.AddressString', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='amount', full_name='cosmos.vesting.v1beta1.MsgCreateVestingAccount.amount', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='end_time', full_name='cosmos.vesting.v1beta1.MsgCreateVestingAccount.end_time', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='delayed', full_name='cosmos.vesting.v1beta1.MsgCreateVestingAccount.delayed', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\350\240\037\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=179,
  serialized_end=432,
)


_MSGCREATEVESTINGACCOUNTRESPONSE = _descriptor.Descriptor(
  name='MsgCreateVestingAccountResponse',
  full_name='cosmos.vesting.v1beta1.MsgCreateVestingAccountResponse',
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
  serialized_start=434,
  serialized_end=467,
)


_MSGCREATEPERIODICVESTINGACCOUNT = _descriptor.Descriptor(
  name='MsgCreatePeriodicVestingAccount',
  full_name='cosmos.vesting.v1beta1.MsgCreatePeriodicVestingAccount',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='from_address', full_name='cosmos.vesting.v1beta1.MsgCreatePeriodicVestingAccount.from_address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='to_address', full_name='cosmos.vesting.v1beta1.MsgCreatePeriodicVestingAccount.to_address', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='start_time', full_name='cosmos.vesting.v1beta1.MsgCreatePeriodicVestingAccount.start_time', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='vesting_periods', full_name='cosmos.vesting.v1beta1.MsgCreatePeriodicVestingAccount.vesting_periods', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\350\240\037\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=470,
  serialized_end=634,
)


_MSGCREATEPERIODICVESTINGACCOUNTRESPONSE = _descriptor.Descriptor(
  name='MsgCreatePeriodicVestingAccountResponse',
  full_name='cosmos.vesting.v1beta1.MsgCreatePeriodicVestingAccountResponse',
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
  serialized_start=636,
  serialized_end=677,
)

_MSGCREATEVESTINGACCOUNT.fields_by_name['amount'].message_type = cosmos_dot_base_dot_v1beta1_dot_coin__pb2._COIN
_MSGCREATEPERIODICVESTINGACCOUNT.fields_by_name['vesting_periods'].message_type = cosmos_dot_vesting_dot_v1beta1_dot_vesting__pb2._PERIOD
DESCRIPTOR.message_types_by_name['MsgCreateVestingAccount'] = _MSGCREATEVESTINGACCOUNT
DESCRIPTOR.message_types_by_name['MsgCreateVestingAccountResponse'] = _MSGCREATEVESTINGACCOUNTRESPONSE
DESCRIPTOR.message_types_by_name['MsgCreatePeriodicVestingAccount'] = _MSGCREATEPERIODICVESTINGACCOUNT
DESCRIPTOR.message_types_by_name['MsgCreatePeriodicVestingAccountResponse'] = _MSGCREATEPERIODICVESTINGACCOUNTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MsgCreateVestingAccount = _reflection.GeneratedProtocolMessageType('MsgCreateVestingAccount', (_message.Message,), {
  'DESCRIPTOR' : _MSGCREATEVESTINGACCOUNT,
  '__module__' : 'cosmos.vesting.v1beta1.tx_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.vesting.v1beta1.MsgCreateVestingAccount)
  })
_sym_db.RegisterMessage(MsgCreateVestingAccount)

MsgCreateVestingAccountResponse = _reflection.GeneratedProtocolMessageType('MsgCreateVestingAccountResponse', (_message.Message,), {
  'DESCRIPTOR' : _MSGCREATEVESTINGACCOUNTRESPONSE,
  '__module__' : 'cosmos.vesting.v1beta1.tx_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.vesting.v1beta1.MsgCreateVestingAccountResponse)
  })
_sym_db.RegisterMessage(MsgCreateVestingAccountResponse)

MsgCreatePeriodicVestingAccount = _reflection.GeneratedProtocolMessageType('MsgCreatePeriodicVestingAccount', (_message.Message,), {
  'DESCRIPTOR' : _MSGCREATEPERIODICVESTINGACCOUNT,
  '__module__' : 'cosmos.vesting.v1beta1.tx_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.vesting.v1beta1.MsgCreatePeriodicVestingAccount)
  })
_sym_db.RegisterMessage(MsgCreatePeriodicVestingAccount)

MsgCreatePeriodicVestingAccountResponse = _reflection.GeneratedProtocolMessageType('MsgCreatePeriodicVestingAccountResponse', (_message.Message,), {
  'DESCRIPTOR' : _MSGCREATEPERIODICVESTINGACCOUNTRESPONSE,
  '__module__' : 'cosmos.vesting.v1beta1.tx_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.vesting.v1beta1.MsgCreatePeriodicVestingAccountResponse)
  })
_sym_db.RegisterMessage(MsgCreatePeriodicVestingAccountResponse)


DESCRIPTOR._options = None
_MSGCREATEVESTINGACCOUNT.fields_by_name['from_address']._options = None
_MSGCREATEVESTINGACCOUNT.fields_by_name['to_address']._options = None
_MSGCREATEVESTINGACCOUNT.fields_by_name['amount']._options = None
_MSGCREATEVESTINGACCOUNT._options = None
_MSGCREATEPERIODICVESTINGACCOUNT.fields_by_name['vesting_periods']._options = None
_MSGCREATEPERIODICVESTINGACCOUNT._options = None

_MSG = _descriptor.ServiceDescriptor(
  name='Msg',
  full_name='cosmos.vesting.v1beta1.Msg',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=680,
  serialized_end=971,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateVestingAccount',
    full_name='cosmos.vesting.v1beta1.Msg.CreateVestingAccount',
    index=0,
    containing_service=None,
    input_type=_MSGCREATEVESTINGACCOUNT,
    output_type=_MSGCREATEVESTINGACCOUNTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CreatePeriodicVestingAccount',
    full_name='cosmos.vesting.v1beta1.Msg.CreatePeriodicVestingAccount',
    index=1,
    containing_service=None,
    input_type=_MSGCREATEPERIODICVESTINGACCOUNT,
    output_type=_MSGCREATEPERIODICVESTINGACCOUNTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MSG)

DESCRIPTOR.services_by_name['Msg'] = _MSG

# @@protoc_insertion_point(module_scope)
