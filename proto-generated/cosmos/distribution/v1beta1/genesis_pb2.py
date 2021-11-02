# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/distribution/v1beta1/genesis.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from cosmos.distribution.v1beta1 import distribution_pb2 as cosmos_dot_distribution_dot_v1beta1_dot_distribution__pb2
from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cosmos/distribution/v1beta1/genesis.proto',
  package='cosmos.distribution.v1beta1',
  syntax='proto3',
  serialized_options=b'Z1github.com/cosmos/cosmos-sdk/x/distribution/types\250\342\036\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n)cosmos/distribution/v1beta1/genesis.proto\x12\x1b\x63osmos.distribution.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a.cosmos/distribution/v1beta1/distribution.proto\x1a\x19\x63osmos_proto/cosmos.proto\"\x8a\x01\n\x15\x44\x65legatorWithdrawInfo\x12\x33\n\x11\x64\x65legator_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x32\n\x10withdraw_address\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"\xd2\x01\n!ValidatorOutstandingRewardsRecord\x12\x33\n\x11validator_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12n\n\x13outstanding_rewards\x18\x02 \x03(\x0b\x32\x1c.cosmos.base.v1beta1.DecCoinB3\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\xc8\xde\x1f\x00:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"\xbd\x01\n$ValidatorAccumulatedCommissionRecord\x12\x33\n\x11validator_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12V\n\x0b\x61\x63\x63umulated\x18\x02 \x01(\x0b\x32;.cosmos.distribution.v1beta1.ValidatorAccumulatedCommissionB\x04\xc8\xde\x1f\x00:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"\xc1\x01\n ValidatorHistoricalRewardsRecord\x12\x33\n\x11validator_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x0e\n\x06period\x18\x02 \x01(\x04\x12N\n\x07rewards\x18\x03 \x01(\x0b\x32\x37.cosmos.distribution.v1beta1.ValidatorHistoricalRewardsB\x04\xc8\xde\x1f\x00:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"\xab\x01\n\x1dValidatorCurrentRewardsRecord\x12\x33\n\x11validator_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12K\n\x07rewards\x18\x02 \x01(\x0b\x32\x34.cosmos.distribution.v1beta1.ValidatorCurrentRewardsB\x04\xc8\xde\x1f\x00:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"\xe2\x01\n\x1b\x44\x65legatorStartingInfoRecord\x12\x33\n\x11\x64\x65legator_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x33\n\x11validator_address\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12O\n\rstarting_info\x18\x03 \x01(\x0b\x32\x32.cosmos.distribution.v1beta1.DelegatorStartingInfoB\x04\xc8\xde\x1f\x00:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"\xd1\x01\n\x19ValidatorSlashEventRecord\x12\x33\n\x11validator_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x0e\n\x06height\x18\x02 \x01(\x04\x12\x0e\n\x06period\x18\x03 \x01(\x04\x12U\n\x15validator_slash_event\x18\x04 \x01(\x0b\x32\x30.cosmos.distribution.v1beta1.ValidatorSlashEventB\x04\xc8\xde\x1f\x00:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"\x89\x07\n\x0cGenesisState\x12\x39\n\x06params\x18\x01 \x01(\x0b\x32#.cosmos.distribution.v1beta1.ParamsB\x04\xc8\xde\x1f\x00\x12<\n\x08\x66\x65\x65_pool\x18\x02 \x01(\x0b\x32$.cosmos.distribution.v1beta1.FeePoolB\x04\xc8\xde\x1f\x00\x12Z\n\x18\x64\x65legator_withdraw_infos\x18\x03 \x03(\x0b\x32\x32.cosmos.distribution.v1beta1.DelegatorWithdrawInfoB\x04\xc8\xde\x1f\x00\x12\x33\n\x11previous_proposer\x18\x04 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x61\n\x13outstanding_rewards\x18\x05 \x03(\x0b\x32>.cosmos.distribution.v1beta1.ValidatorOutstandingRewardsRecordB\x04\xc8\xde\x1f\x00\x12r\n!validator_accumulated_commissions\x18\x06 \x03(\x0b\x32\x41.cosmos.distribution.v1beta1.ValidatorAccumulatedCommissionRecordB\x04\xc8\xde\x1f\x00\x12i\n\x1cvalidator_historical_rewards\x18\x07 \x03(\x0b\x32=.cosmos.distribution.v1beta1.ValidatorHistoricalRewardsRecordB\x04\xc8\xde\x1f\x00\x12\x63\n\x19validator_current_rewards\x18\x08 \x03(\x0b\x32:.cosmos.distribution.v1beta1.ValidatorCurrentRewardsRecordB\x04\xc8\xde\x1f\x00\x12`\n\x18\x64\x65legator_starting_infos\x18\t \x03(\x0b\x32\x38.cosmos.distribution.v1beta1.DelegatorStartingInfoRecordB\x04\xc8\xde\x1f\x00\x12\\\n\x16validator_slash_events\x18\n \x03(\x0b\x32\x36.cosmos.distribution.v1beta1.ValidatorSlashEventRecordB\x04\xc8\xde\x1f\x00:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\x42\x37Z1github.com/cosmos/cosmos-sdk/x/distribution/types\xa8\xe2\x1e\x01\x62\x06proto3'
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,cosmos_dot_base_dot_v1beta1_dot_coin__pb2.DESCRIPTOR,cosmos_dot_distribution_dot_v1beta1_dot_distribution__pb2.DESCRIPTOR,cosmos__proto_dot_cosmos__pb2.DESCRIPTOR,])




_DELEGATORWITHDRAWINFO = _descriptor.Descriptor(
  name='DelegatorWithdrawInfo',
  full_name='cosmos.distribution.v1beta1.DelegatorWithdrawInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='delegator_address', full_name='cosmos.distribution.v1beta1.DelegatorWithdrawInfo.delegator_address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\322\264-\024cosmos.AddressString', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='withdraw_address', full_name='cosmos.distribution.v1beta1.DelegatorWithdrawInfo.withdraw_address', index=1,
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
  serialized_options=b'\350\240\037\000\210\240\037\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=204,
  serialized_end=342,
)


_VALIDATOROUTSTANDINGREWARDSRECORD = _descriptor.Descriptor(
  name='ValidatorOutstandingRewardsRecord',
  full_name='cosmos.distribution.v1beta1.ValidatorOutstandingRewardsRecord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='validator_address', full_name='cosmos.distribution.v1beta1.ValidatorOutstandingRewardsRecord.validator_address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\322\264-\024cosmos.AddressString', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='outstanding_rewards', full_name='cosmos.distribution.v1beta1.ValidatorOutstandingRewardsRecord.outstanding_rewards', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\252\337\037+github.com/cosmos/cosmos-sdk/types.DecCoins\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\350\240\037\000\210\240\037\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=345,
  serialized_end=555,
)


_VALIDATORACCUMULATEDCOMMISSIONRECORD = _descriptor.Descriptor(
  name='ValidatorAccumulatedCommissionRecord',
  full_name='cosmos.distribution.v1beta1.ValidatorAccumulatedCommissionRecord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='validator_address', full_name='cosmos.distribution.v1beta1.ValidatorAccumulatedCommissionRecord.validator_address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\322\264-\024cosmos.AddressString', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='accumulated', full_name='cosmos.distribution.v1beta1.ValidatorAccumulatedCommissionRecord.accumulated', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\350\240\037\000\210\240\037\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=558,
  serialized_end=747,
)


_VALIDATORHISTORICALREWARDSRECORD = _descriptor.Descriptor(
  name='ValidatorHistoricalRewardsRecord',
  full_name='cosmos.distribution.v1beta1.ValidatorHistoricalRewardsRecord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='validator_address', full_name='cosmos.distribution.v1beta1.ValidatorHistoricalRewardsRecord.validator_address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\322\264-\024cosmos.AddressString', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='period', full_name='cosmos.distribution.v1beta1.ValidatorHistoricalRewardsRecord.period', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rewards', full_name='cosmos.distribution.v1beta1.ValidatorHistoricalRewardsRecord.rewards', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\350\240\037\000\210\240\037\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=750,
  serialized_end=943,
)


_VALIDATORCURRENTREWARDSRECORD = _descriptor.Descriptor(
  name='ValidatorCurrentRewardsRecord',
  full_name='cosmos.distribution.v1beta1.ValidatorCurrentRewardsRecord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='validator_address', full_name='cosmos.distribution.v1beta1.ValidatorCurrentRewardsRecord.validator_address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\322\264-\024cosmos.AddressString', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rewards', full_name='cosmos.distribution.v1beta1.ValidatorCurrentRewardsRecord.rewards', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\350\240\037\000\210\240\037\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=946,
  serialized_end=1117,
)


_DELEGATORSTARTINGINFORECORD = _descriptor.Descriptor(
  name='DelegatorStartingInfoRecord',
  full_name='cosmos.distribution.v1beta1.DelegatorStartingInfoRecord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='delegator_address', full_name='cosmos.distribution.v1beta1.DelegatorStartingInfoRecord.delegator_address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\322\264-\024cosmos.AddressString', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='validator_address', full_name='cosmos.distribution.v1beta1.DelegatorStartingInfoRecord.validator_address', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\322\264-\024cosmos.AddressString', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='starting_info', full_name='cosmos.distribution.v1beta1.DelegatorStartingInfoRecord.starting_info', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\350\240\037\000\210\240\037\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1120,
  serialized_end=1346,
)


_VALIDATORSLASHEVENTRECORD = _descriptor.Descriptor(
  name='ValidatorSlashEventRecord',
  full_name='cosmos.distribution.v1beta1.ValidatorSlashEventRecord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='validator_address', full_name='cosmos.distribution.v1beta1.ValidatorSlashEventRecord.validator_address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\322\264-\024cosmos.AddressString', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='height', full_name='cosmos.distribution.v1beta1.ValidatorSlashEventRecord.height', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='period', full_name='cosmos.distribution.v1beta1.ValidatorSlashEventRecord.period', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='validator_slash_event', full_name='cosmos.distribution.v1beta1.ValidatorSlashEventRecord.validator_slash_event', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\350\240\037\000\210\240\037\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1349,
  serialized_end=1558,
)


_GENESISSTATE = _descriptor.Descriptor(
  name='GenesisState',
  full_name='cosmos.distribution.v1beta1.GenesisState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='params', full_name='cosmos.distribution.v1beta1.GenesisState.params', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fee_pool', full_name='cosmos.distribution.v1beta1.GenesisState.fee_pool', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='delegator_withdraw_infos', full_name='cosmos.distribution.v1beta1.GenesisState.delegator_withdraw_infos', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='previous_proposer', full_name='cosmos.distribution.v1beta1.GenesisState.previous_proposer', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\322\264-\024cosmos.AddressString', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='outstanding_rewards', full_name='cosmos.distribution.v1beta1.GenesisState.outstanding_rewards', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='validator_accumulated_commissions', full_name='cosmos.distribution.v1beta1.GenesisState.validator_accumulated_commissions', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='validator_historical_rewards', full_name='cosmos.distribution.v1beta1.GenesisState.validator_historical_rewards', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='validator_current_rewards', full_name='cosmos.distribution.v1beta1.GenesisState.validator_current_rewards', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='delegator_starting_infos', full_name='cosmos.distribution.v1beta1.GenesisState.delegator_starting_infos', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='validator_slash_events', full_name='cosmos.distribution.v1beta1.GenesisState.validator_slash_events', index=9,
      number=10, type=11, cpp_type=10, label=3,
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
  serialized_options=b'\350\240\037\000\210\240\037\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1561,
  serialized_end=2466,
)

_VALIDATOROUTSTANDINGREWARDSRECORD.fields_by_name['outstanding_rewards'].message_type = cosmos_dot_base_dot_v1beta1_dot_coin__pb2._DECCOIN
_VALIDATORACCUMULATEDCOMMISSIONRECORD.fields_by_name['accumulated'].message_type = cosmos_dot_distribution_dot_v1beta1_dot_distribution__pb2._VALIDATORACCUMULATEDCOMMISSION
_VALIDATORHISTORICALREWARDSRECORD.fields_by_name['rewards'].message_type = cosmos_dot_distribution_dot_v1beta1_dot_distribution__pb2._VALIDATORHISTORICALREWARDS
_VALIDATORCURRENTREWARDSRECORD.fields_by_name['rewards'].message_type = cosmos_dot_distribution_dot_v1beta1_dot_distribution__pb2._VALIDATORCURRENTREWARDS
_DELEGATORSTARTINGINFORECORD.fields_by_name['starting_info'].message_type = cosmos_dot_distribution_dot_v1beta1_dot_distribution__pb2._DELEGATORSTARTINGINFO
_VALIDATORSLASHEVENTRECORD.fields_by_name['validator_slash_event'].message_type = cosmos_dot_distribution_dot_v1beta1_dot_distribution__pb2._VALIDATORSLASHEVENT
_GENESISSTATE.fields_by_name['params'].message_type = cosmos_dot_distribution_dot_v1beta1_dot_distribution__pb2._PARAMS
_GENESISSTATE.fields_by_name['fee_pool'].message_type = cosmos_dot_distribution_dot_v1beta1_dot_distribution__pb2._FEEPOOL
_GENESISSTATE.fields_by_name['delegator_withdraw_infos'].message_type = _DELEGATORWITHDRAWINFO
_GENESISSTATE.fields_by_name['outstanding_rewards'].message_type = _VALIDATOROUTSTANDINGREWARDSRECORD
_GENESISSTATE.fields_by_name['validator_accumulated_commissions'].message_type = _VALIDATORACCUMULATEDCOMMISSIONRECORD
_GENESISSTATE.fields_by_name['validator_historical_rewards'].message_type = _VALIDATORHISTORICALREWARDSRECORD
_GENESISSTATE.fields_by_name['validator_current_rewards'].message_type = _VALIDATORCURRENTREWARDSRECORD
_GENESISSTATE.fields_by_name['delegator_starting_infos'].message_type = _DELEGATORSTARTINGINFORECORD
_GENESISSTATE.fields_by_name['validator_slash_events'].message_type = _VALIDATORSLASHEVENTRECORD
DESCRIPTOR.message_types_by_name['DelegatorWithdrawInfo'] = _DELEGATORWITHDRAWINFO
DESCRIPTOR.message_types_by_name['ValidatorOutstandingRewardsRecord'] = _VALIDATOROUTSTANDINGREWARDSRECORD
DESCRIPTOR.message_types_by_name['ValidatorAccumulatedCommissionRecord'] = _VALIDATORACCUMULATEDCOMMISSIONRECORD
DESCRIPTOR.message_types_by_name['ValidatorHistoricalRewardsRecord'] = _VALIDATORHISTORICALREWARDSRECORD
DESCRIPTOR.message_types_by_name['ValidatorCurrentRewardsRecord'] = _VALIDATORCURRENTREWARDSRECORD
DESCRIPTOR.message_types_by_name['DelegatorStartingInfoRecord'] = _DELEGATORSTARTINGINFORECORD
DESCRIPTOR.message_types_by_name['ValidatorSlashEventRecord'] = _VALIDATORSLASHEVENTRECORD
DESCRIPTOR.message_types_by_name['GenesisState'] = _GENESISSTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DelegatorWithdrawInfo = _reflection.GeneratedProtocolMessageType('DelegatorWithdrawInfo', (_message.Message,), {
  'DESCRIPTOR' : _DELEGATORWITHDRAWINFO,
  '__module__' : 'cosmos.distribution.v1beta1.genesis_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.distribution.v1beta1.DelegatorWithdrawInfo)
  })
_sym_db.RegisterMessage(DelegatorWithdrawInfo)

ValidatorOutstandingRewardsRecord = _reflection.GeneratedProtocolMessageType('ValidatorOutstandingRewardsRecord', (_message.Message,), {
  'DESCRIPTOR' : _VALIDATOROUTSTANDINGREWARDSRECORD,
  '__module__' : 'cosmos.distribution.v1beta1.genesis_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.distribution.v1beta1.ValidatorOutstandingRewardsRecord)
  })
_sym_db.RegisterMessage(ValidatorOutstandingRewardsRecord)

ValidatorAccumulatedCommissionRecord = _reflection.GeneratedProtocolMessageType('ValidatorAccumulatedCommissionRecord', (_message.Message,), {
  'DESCRIPTOR' : _VALIDATORACCUMULATEDCOMMISSIONRECORD,
  '__module__' : 'cosmos.distribution.v1beta1.genesis_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.distribution.v1beta1.ValidatorAccumulatedCommissionRecord)
  })
_sym_db.RegisterMessage(ValidatorAccumulatedCommissionRecord)

ValidatorHistoricalRewardsRecord = _reflection.GeneratedProtocolMessageType('ValidatorHistoricalRewardsRecord', (_message.Message,), {
  'DESCRIPTOR' : _VALIDATORHISTORICALREWARDSRECORD,
  '__module__' : 'cosmos.distribution.v1beta1.genesis_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.distribution.v1beta1.ValidatorHistoricalRewardsRecord)
  })
_sym_db.RegisterMessage(ValidatorHistoricalRewardsRecord)

ValidatorCurrentRewardsRecord = _reflection.GeneratedProtocolMessageType('ValidatorCurrentRewardsRecord', (_message.Message,), {
  'DESCRIPTOR' : _VALIDATORCURRENTREWARDSRECORD,
  '__module__' : 'cosmos.distribution.v1beta1.genesis_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.distribution.v1beta1.ValidatorCurrentRewardsRecord)
  })
_sym_db.RegisterMessage(ValidatorCurrentRewardsRecord)

DelegatorStartingInfoRecord = _reflection.GeneratedProtocolMessageType('DelegatorStartingInfoRecord', (_message.Message,), {
  'DESCRIPTOR' : _DELEGATORSTARTINGINFORECORD,
  '__module__' : 'cosmos.distribution.v1beta1.genesis_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.distribution.v1beta1.DelegatorStartingInfoRecord)
  })
_sym_db.RegisterMessage(DelegatorStartingInfoRecord)

ValidatorSlashEventRecord = _reflection.GeneratedProtocolMessageType('ValidatorSlashEventRecord', (_message.Message,), {
  'DESCRIPTOR' : _VALIDATORSLASHEVENTRECORD,
  '__module__' : 'cosmos.distribution.v1beta1.genesis_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.distribution.v1beta1.ValidatorSlashEventRecord)
  })
_sym_db.RegisterMessage(ValidatorSlashEventRecord)

GenesisState = _reflection.GeneratedProtocolMessageType('GenesisState', (_message.Message,), {
  'DESCRIPTOR' : _GENESISSTATE,
  '__module__' : 'cosmos.distribution.v1beta1.genesis_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.distribution.v1beta1.GenesisState)
  })
_sym_db.RegisterMessage(GenesisState)


DESCRIPTOR._options = None
_DELEGATORWITHDRAWINFO.fields_by_name['delegator_address']._options = None
_DELEGATORWITHDRAWINFO.fields_by_name['withdraw_address']._options = None
_DELEGATORWITHDRAWINFO._options = None
_VALIDATOROUTSTANDINGREWARDSRECORD.fields_by_name['validator_address']._options = None
_VALIDATOROUTSTANDINGREWARDSRECORD.fields_by_name['outstanding_rewards']._options = None
_VALIDATOROUTSTANDINGREWARDSRECORD._options = None
_VALIDATORACCUMULATEDCOMMISSIONRECORD.fields_by_name['validator_address']._options = None
_VALIDATORACCUMULATEDCOMMISSIONRECORD.fields_by_name['accumulated']._options = None
_VALIDATORACCUMULATEDCOMMISSIONRECORD._options = None
_VALIDATORHISTORICALREWARDSRECORD.fields_by_name['validator_address']._options = None
_VALIDATORHISTORICALREWARDSRECORD.fields_by_name['rewards']._options = None
_VALIDATORHISTORICALREWARDSRECORD._options = None
_VALIDATORCURRENTREWARDSRECORD.fields_by_name['validator_address']._options = None
_VALIDATORCURRENTREWARDSRECORD.fields_by_name['rewards']._options = None
_VALIDATORCURRENTREWARDSRECORD._options = None
_DELEGATORSTARTINGINFORECORD.fields_by_name['delegator_address']._options = None
_DELEGATORSTARTINGINFORECORD.fields_by_name['validator_address']._options = None
_DELEGATORSTARTINGINFORECORD.fields_by_name['starting_info']._options = None
_DELEGATORSTARTINGINFORECORD._options = None
_VALIDATORSLASHEVENTRECORD.fields_by_name['validator_address']._options = None
_VALIDATORSLASHEVENTRECORD.fields_by_name['validator_slash_event']._options = None
_VALIDATORSLASHEVENTRECORD._options = None
_GENESISSTATE.fields_by_name['params']._options = None
_GENESISSTATE.fields_by_name['fee_pool']._options = None
_GENESISSTATE.fields_by_name['delegator_withdraw_infos']._options = None
_GENESISSTATE.fields_by_name['previous_proposer']._options = None
_GENESISSTATE.fields_by_name['outstanding_rewards']._options = None
_GENESISSTATE.fields_by_name['validator_accumulated_commissions']._options = None
_GENESISSTATE.fields_by_name['validator_historical_rewards']._options = None
_GENESISSTATE.fields_by_name['validator_current_rewards']._options = None
_GENESISSTATE.fields_by_name['delegator_starting_infos']._options = None
_GENESISSTATE.fields_by_name['validator_slash_events']._options = None
_GENESISSTATE._options = None
# @@protoc_insertion_point(module_scope)