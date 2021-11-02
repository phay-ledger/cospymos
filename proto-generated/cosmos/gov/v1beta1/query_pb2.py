# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/gov/v1beta1/query.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from cosmos.gov.v1beta1 import gov_pb2 as cosmos_dot_gov_dot_v1beta1_dot_gov__pb2
from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cosmos/gov/v1beta1/query.proto',
  package='cosmos.gov.v1beta1',
  syntax='proto3',
  serialized_options=b'Z(github.com/cosmos/cosmos-sdk/x/gov/types',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1e\x63osmos/gov/v1beta1/query.proto\x12\x12\x63osmos.gov.v1beta1\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1c\x63osmos/gov/v1beta1/gov.proto\x1a\x19\x63osmos_proto/cosmos.proto\"+\n\x14QueryProposalRequest\x12\x13\n\x0bproposal_id\x18\x01 \x01(\x04\"M\n\x15QueryProposalResponse\x12\x34\n\x08proposal\x18\x01 \x01(\x0b\x32\x1c.cosmos.gov.v1beta1.ProposalB\x04\xc8\xde\x1f\x00\"\xf0\x01\n\x15QueryProposalsRequest\x12;\n\x0fproposal_status\x18\x01 \x01(\x0e\x32\".cosmos.gov.v1beta1.ProposalStatus\x12\'\n\x05voter\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12+\n\tdepositor\x18\x03 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12:\n\npagination\x18\x04 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"\x8c\x01\n\x16QueryProposalsResponse\x12\x35\n\tproposals\x18\x01 \x03(\x0b\x32\x1c.cosmos.gov.v1beta1.ProposalB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\"Z\n\x10QueryVoteRequest\x12\x13\n\x0bproposal_id\x18\x01 \x01(\x04\x12\'\n\x05voter\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"A\n\x11QueryVoteResponse\x12,\n\x04vote\x18\x01 \x01(\x0b\x32\x18.cosmos.gov.v1beta1.VoteB\x04\xc8\xde\x1f\x00\"d\n\x11QueryVotesRequest\x12\x13\n\x0bproposal_id\x18\x01 \x01(\x04\x12:\n\npagination\x18\x02 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\"\x80\x01\n\x12QueryVotesResponse\x12-\n\x05votes\x18\x01 \x03(\x0b\x32\x18.cosmos.gov.v1beta1.VoteB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\")\n\x12QueryParamsRequest\x12\x13\n\x0bparams_type\x18\x01 \x01(\t\"\xd2\x01\n\x13QueryParamsResponse\x12=\n\rvoting_params\x18\x01 \x01(\x0b\x32 .cosmos.gov.v1beta1.VotingParamsB\x04\xc8\xde\x1f\x00\x12?\n\x0e\x64\x65posit_params\x18\x02 \x01(\x0b\x32!.cosmos.gov.v1beta1.DepositParamsB\x04\xc8\xde\x1f\x00\x12;\n\x0ctally_params\x18\x03 \x01(\x0b\x32\x1f.cosmos.gov.v1beta1.TallyParamsB\x04\xc8\xde\x1f\x00\"a\n\x13QueryDepositRequest\x12\x13\n\x0bproposal_id\x18\x01 \x01(\x04\x12+\n\tdepositor\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\"J\n\x14QueryDepositResponse\x12\x32\n\x07\x64\x65posit\x18\x01 \x01(\x0b\x32\x1b.cosmos.gov.v1beta1.DepositB\x04\xc8\xde\x1f\x00\"g\n\x14QueryDepositsRequest\x12\x13\n\x0bproposal_id\x18\x01 \x01(\x04\x12:\n\npagination\x18\x02 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\"\x89\x01\n\x15QueryDepositsResponse\x12\x33\n\x08\x64\x65posits\x18\x01 \x03(\x0b\x32\x1b.cosmos.gov.v1beta1.DepositB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\".\n\x17QueryTallyResultRequest\x12\x13\n\x0bproposal_id\x18\x01 \x01(\x04\"P\n\x18QueryTallyResultResponse\x12\x34\n\x05tally\x18\x01 \x01(\x0b\x32\x1f.cosmos.gov.v1beta1.TallyResultB\x04\xc8\xde\x1f\x00\x32\xd4\t\n\x05Query\x12\x94\x01\n\x08Proposal\x12(.cosmos.gov.v1beta1.QueryProposalRequest\x1a).cosmos.gov.v1beta1.QueryProposalResponse\"3\x82\xd3\xe4\x93\x02-\x12+/cosmos/gov/v1beta1/proposals/{proposal_id}\x12\x89\x01\n\tProposals\x12).cosmos.gov.v1beta1.QueryProposalsRequest\x1a*.cosmos.gov.v1beta1.QueryProposalsResponse\"%\x82\xd3\xe4\x93\x02\x1f\x12\x1d/cosmos/gov/v1beta1/proposals\x12\x96\x01\n\x04Vote\x12$.cosmos.gov.v1beta1.QueryVoteRequest\x1a%.cosmos.gov.v1beta1.QueryVoteResponse\"A\x82\xd3\xe4\x93\x02;\x12\x39/cosmos/gov/v1beta1/proposals/{proposal_id}/votes/{voter}\x12\x91\x01\n\x05Votes\x12%.cosmos.gov.v1beta1.QueryVotesRequest\x1a&.cosmos.gov.v1beta1.QueryVotesResponse\"9\x82\xd3\xe4\x93\x02\x33\x12\x31/cosmos/gov/v1beta1/proposals/{proposal_id}/votes\x12\x8b\x01\n\x06Params\x12&.cosmos.gov.v1beta1.QueryParamsRequest\x1a\'.cosmos.gov.v1beta1.QueryParamsResponse\"0\x82\xd3\xe4\x93\x02*\x12(/cosmos/gov/v1beta1/params/{params_type}\x12\xa6\x01\n\x07\x44\x65posit\x12\'.cosmos.gov.v1beta1.QueryDepositRequest\x1a(.cosmos.gov.v1beta1.QueryDepositResponse\"H\x82\xd3\xe4\x93\x02\x42\x12@/cosmos/gov/v1beta1/proposals/{proposal_id}/deposits/{depositor}\x12\x9d\x01\n\x08\x44\x65posits\x12(.cosmos.gov.v1beta1.QueryDepositsRequest\x1a).cosmos.gov.v1beta1.QueryDepositsResponse\"<\x82\xd3\xe4\x93\x02\x36\x12\x34/cosmos/gov/v1beta1/proposals/{proposal_id}/deposits\x12\xa3\x01\n\x0bTallyResult\x12+.cosmos.gov.v1beta1.QueryTallyResultRequest\x1a,.cosmos.gov.v1beta1.QueryTallyResultResponse\"9\x82\xd3\xe4\x93\x02\x33\x12\x31/cosmos/gov/v1beta1/proposals/{proposal_id}/tallyB*Z(github.com/cosmos/cosmos-sdk/x/gov/typesb\x06proto3'
  ,
  dependencies=[cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2.DESCRIPTOR,gogoproto_dot_gogo__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,cosmos_dot_gov_dot_v1beta1_dot_gov__pb2.DESCRIPTOR,cosmos__proto_dot_cosmos__pb2.DESCRIPTOR,])




_QUERYPROPOSALREQUEST = _descriptor.Descriptor(
  name='QueryProposalRequest',
  full_name='cosmos.gov.v1beta1.QueryProposalRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='proposal_id', full_name='cosmos.gov.v1beta1.QueryProposalRequest.proposal_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=207,
  serialized_end=250,
)


_QUERYPROPOSALRESPONSE = _descriptor.Descriptor(
  name='QueryProposalResponse',
  full_name='cosmos.gov.v1beta1.QueryProposalResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='proposal', full_name='cosmos.gov.v1beta1.QueryProposalResponse.proposal', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=252,
  serialized_end=329,
)


_QUERYPROPOSALSREQUEST = _descriptor.Descriptor(
  name='QueryProposalsRequest',
  full_name='cosmos.gov.v1beta1.QueryProposalsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='proposal_status', full_name='cosmos.gov.v1beta1.QueryProposalsRequest.proposal_status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='voter', full_name='cosmos.gov.v1beta1.QueryProposalsRequest.voter', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\322\264-\024cosmos.AddressString', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='depositor', full_name='cosmos.gov.v1beta1.QueryProposalsRequest.depositor', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\322\264-\024cosmos.AddressString', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pagination', full_name='cosmos.gov.v1beta1.QueryProposalsRequest.pagination', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=332,
  serialized_end=572,
)


_QUERYPROPOSALSRESPONSE = _descriptor.Descriptor(
  name='QueryProposalsResponse',
  full_name='cosmos.gov.v1beta1.QueryProposalsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='proposals', full_name='cosmos.gov.v1beta1.QueryProposalsResponse.proposals', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pagination', full_name='cosmos.gov.v1beta1.QueryProposalsResponse.pagination', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=575,
  serialized_end=715,
)


_QUERYVOTEREQUEST = _descriptor.Descriptor(
  name='QueryVoteRequest',
  full_name='cosmos.gov.v1beta1.QueryVoteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='proposal_id', full_name='cosmos.gov.v1beta1.QueryVoteRequest.proposal_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='voter', full_name='cosmos.gov.v1beta1.QueryVoteRequest.voter', index=1,
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
  serialized_start=717,
  serialized_end=807,
)


_QUERYVOTERESPONSE = _descriptor.Descriptor(
  name='QueryVoteResponse',
  full_name='cosmos.gov.v1beta1.QueryVoteResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='vote', full_name='cosmos.gov.v1beta1.QueryVoteResponse.vote', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=809,
  serialized_end=874,
)


_QUERYVOTESREQUEST = _descriptor.Descriptor(
  name='QueryVotesRequest',
  full_name='cosmos.gov.v1beta1.QueryVotesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='proposal_id', full_name='cosmos.gov.v1beta1.QueryVotesRequest.proposal_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pagination', full_name='cosmos.gov.v1beta1.QueryVotesRequest.pagination', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=876,
  serialized_end=976,
)


_QUERYVOTESRESPONSE = _descriptor.Descriptor(
  name='QueryVotesResponse',
  full_name='cosmos.gov.v1beta1.QueryVotesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='votes', full_name='cosmos.gov.v1beta1.QueryVotesResponse.votes', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pagination', full_name='cosmos.gov.v1beta1.QueryVotesResponse.pagination', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=979,
  serialized_end=1107,
)


_QUERYPARAMSREQUEST = _descriptor.Descriptor(
  name='QueryParamsRequest',
  full_name='cosmos.gov.v1beta1.QueryParamsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='params_type', full_name='cosmos.gov.v1beta1.QueryParamsRequest.params_type', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=1109,
  serialized_end=1150,
)


_QUERYPARAMSRESPONSE = _descriptor.Descriptor(
  name='QueryParamsResponse',
  full_name='cosmos.gov.v1beta1.QueryParamsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='voting_params', full_name='cosmos.gov.v1beta1.QueryParamsResponse.voting_params', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='deposit_params', full_name='cosmos.gov.v1beta1.QueryParamsResponse.deposit_params', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tally_params', full_name='cosmos.gov.v1beta1.QueryParamsResponse.tally_params', index=2,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1153,
  serialized_end=1363,
)


_QUERYDEPOSITREQUEST = _descriptor.Descriptor(
  name='QueryDepositRequest',
  full_name='cosmos.gov.v1beta1.QueryDepositRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='proposal_id', full_name='cosmos.gov.v1beta1.QueryDepositRequest.proposal_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='depositor', full_name='cosmos.gov.v1beta1.QueryDepositRequest.depositor', index=1,
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
  serialized_options=b'\210\240\037\000\350\240\037\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1365,
  serialized_end=1462,
)


_QUERYDEPOSITRESPONSE = _descriptor.Descriptor(
  name='QueryDepositResponse',
  full_name='cosmos.gov.v1beta1.QueryDepositResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='deposit', full_name='cosmos.gov.v1beta1.QueryDepositResponse.deposit', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1464,
  serialized_end=1538,
)


_QUERYDEPOSITSREQUEST = _descriptor.Descriptor(
  name='QueryDepositsRequest',
  full_name='cosmos.gov.v1beta1.QueryDepositsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='proposal_id', full_name='cosmos.gov.v1beta1.QueryDepositsRequest.proposal_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pagination', full_name='cosmos.gov.v1beta1.QueryDepositsRequest.pagination', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=1540,
  serialized_end=1643,
)


_QUERYDEPOSITSRESPONSE = _descriptor.Descriptor(
  name='QueryDepositsResponse',
  full_name='cosmos.gov.v1beta1.QueryDepositsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='deposits', full_name='cosmos.gov.v1beta1.QueryDepositsResponse.deposits', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pagination', full_name='cosmos.gov.v1beta1.QueryDepositsResponse.pagination', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=1646,
  serialized_end=1783,
)


_QUERYTALLYRESULTREQUEST = _descriptor.Descriptor(
  name='QueryTallyResultRequest',
  full_name='cosmos.gov.v1beta1.QueryTallyResultRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='proposal_id', full_name='cosmos.gov.v1beta1.QueryTallyResultRequest.proposal_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=1785,
  serialized_end=1831,
)


_QUERYTALLYRESULTRESPONSE = _descriptor.Descriptor(
  name='QueryTallyResultResponse',
  full_name='cosmos.gov.v1beta1.QueryTallyResultResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tally', full_name='cosmos.gov.v1beta1.QueryTallyResultResponse.tally', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1833,
  serialized_end=1913,
)

_QUERYPROPOSALRESPONSE.fields_by_name['proposal'].message_type = cosmos_dot_gov_dot_v1beta1_dot_gov__pb2._PROPOSAL
_QUERYPROPOSALSREQUEST.fields_by_name['proposal_status'].enum_type = cosmos_dot_gov_dot_v1beta1_dot_gov__pb2._PROPOSALSTATUS
_QUERYPROPOSALSREQUEST.fields_by_name['pagination'].message_type = cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2._PAGEREQUEST
_QUERYPROPOSALSRESPONSE.fields_by_name['proposals'].message_type = cosmos_dot_gov_dot_v1beta1_dot_gov__pb2._PROPOSAL
_QUERYPROPOSALSRESPONSE.fields_by_name['pagination'].message_type = cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2._PAGERESPONSE
_QUERYVOTERESPONSE.fields_by_name['vote'].message_type = cosmos_dot_gov_dot_v1beta1_dot_gov__pb2._VOTE
_QUERYVOTESREQUEST.fields_by_name['pagination'].message_type = cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2._PAGEREQUEST
_QUERYVOTESRESPONSE.fields_by_name['votes'].message_type = cosmos_dot_gov_dot_v1beta1_dot_gov__pb2._VOTE
_QUERYVOTESRESPONSE.fields_by_name['pagination'].message_type = cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2._PAGERESPONSE
_QUERYPARAMSRESPONSE.fields_by_name['voting_params'].message_type = cosmos_dot_gov_dot_v1beta1_dot_gov__pb2._VOTINGPARAMS
_QUERYPARAMSRESPONSE.fields_by_name['deposit_params'].message_type = cosmos_dot_gov_dot_v1beta1_dot_gov__pb2._DEPOSITPARAMS
_QUERYPARAMSRESPONSE.fields_by_name['tally_params'].message_type = cosmos_dot_gov_dot_v1beta1_dot_gov__pb2._TALLYPARAMS
_QUERYDEPOSITRESPONSE.fields_by_name['deposit'].message_type = cosmos_dot_gov_dot_v1beta1_dot_gov__pb2._DEPOSIT
_QUERYDEPOSITSREQUEST.fields_by_name['pagination'].message_type = cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2._PAGEREQUEST
_QUERYDEPOSITSRESPONSE.fields_by_name['deposits'].message_type = cosmos_dot_gov_dot_v1beta1_dot_gov__pb2._DEPOSIT
_QUERYDEPOSITSRESPONSE.fields_by_name['pagination'].message_type = cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2._PAGERESPONSE
_QUERYTALLYRESULTRESPONSE.fields_by_name['tally'].message_type = cosmos_dot_gov_dot_v1beta1_dot_gov__pb2._TALLYRESULT
DESCRIPTOR.message_types_by_name['QueryProposalRequest'] = _QUERYPROPOSALREQUEST
DESCRIPTOR.message_types_by_name['QueryProposalResponse'] = _QUERYPROPOSALRESPONSE
DESCRIPTOR.message_types_by_name['QueryProposalsRequest'] = _QUERYPROPOSALSREQUEST
DESCRIPTOR.message_types_by_name['QueryProposalsResponse'] = _QUERYPROPOSALSRESPONSE
DESCRIPTOR.message_types_by_name['QueryVoteRequest'] = _QUERYVOTEREQUEST
DESCRIPTOR.message_types_by_name['QueryVoteResponse'] = _QUERYVOTERESPONSE
DESCRIPTOR.message_types_by_name['QueryVotesRequest'] = _QUERYVOTESREQUEST
DESCRIPTOR.message_types_by_name['QueryVotesResponse'] = _QUERYVOTESRESPONSE
DESCRIPTOR.message_types_by_name['QueryParamsRequest'] = _QUERYPARAMSREQUEST
DESCRIPTOR.message_types_by_name['QueryParamsResponse'] = _QUERYPARAMSRESPONSE
DESCRIPTOR.message_types_by_name['QueryDepositRequest'] = _QUERYDEPOSITREQUEST
DESCRIPTOR.message_types_by_name['QueryDepositResponse'] = _QUERYDEPOSITRESPONSE
DESCRIPTOR.message_types_by_name['QueryDepositsRequest'] = _QUERYDEPOSITSREQUEST
DESCRIPTOR.message_types_by_name['QueryDepositsResponse'] = _QUERYDEPOSITSRESPONSE
DESCRIPTOR.message_types_by_name['QueryTallyResultRequest'] = _QUERYTALLYRESULTREQUEST
DESCRIPTOR.message_types_by_name['QueryTallyResultResponse'] = _QUERYTALLYRESULTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

QueryProposalRequest = _reflection.GeneratedProtocolMessageType('QueryProposalRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYPROPOSALREQUEST,
  '__module__' : 'cosmos.gov.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.gov.v1beta1.QueryProposalRequest)
  })
_sym_db.RegisterMessage(QueryProposalRequest)

QueryProposalResponse = _reflection.GeneratedProtocolMessageType('QueryProposalResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYPROPOSALRESPONSE,
  '__module__' : 'cosmos.gov.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.gov.v1beta1.QueryProposalResponse)
  })
_sym_db.RegisterMessage(QueryProposalResponse)

QueryProposalsRequest = _reflection.GeneratedProtocolMessageType('QueryProposalsRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYPROPOSALSREQUEST,
  '__module__' : 'cosmos.gov.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.gov.v1beta1.QueryProposalsRequest)
  })
_sym_db.RegisterMessage(QueryProposalsRequest)

QueryProposalsResponse = _reflection.GeneratedProtocolMessageType('QueryProposalsResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYPROPOSALSRESPONSE,
  '__module__' : 'cosmos.gov.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.gov.v1beta1.QueryProposalsResponse)
  })
_sym_db.RegisterMessage(QueryProposalsResponse)

QueryVoteRequest = _reflection.GeneratedProtocolMessageType('QueryVoteRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYVOTEREQUEST,
  '__module__' : 'cosmos.gov.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.gov.v1beta1.QueryVoteRequest)
  })
_sym_db.RegisterMessage(QueryVoteRequest)

QueryVoteResponse = _reflection.GeneratedProtocolMessageType('QueryVoteResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYVOTERESPONSE,
  '__module__' : 'cosmos.gov.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.gov.v1beta1.QueryVoteResponse)
  })
_sym_db.RegisterMessage(QueryVoteResponse)

QueryVotesRequest = _reflection.GeneratedProtocolMessageType('QueryVotesRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYVOTESREQUEST,
  '__module__' : 'cosmos.gov.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.gov.v1beta1.QueryVotesRequest)
  })
_sym_db.RegisterMessage(QueryVotesRequest)

QueryVotesResponse = _reflection.GeneratedProtocolMessageType('QueryVotesResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYVOTESRESPONSE,
  '__module__' : 'cosmos.gov.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.gov.v1beta1.QueryVotesResponse)
  })
_sym_db.RegisterMessage(QueryVotesResponse)

QueryParamsRequest = _reflection.GeneratedProtocolMessageType('QueryParamsRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYPARAMSREQUEST,
  '__module__' : 'cosmos.gov.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.gov.v1beta1.QueryParamsRequest)
  })
_sym_db.RegisterMessage(QueryParamsRequest)

QueryParamsResponse = _reflection.GeneratedProtocolMessageType('QueryParamsResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYPARAMSRESPONSE,
  '__module__' : 'cosmos.gov.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.gov.v1beta1.QueryParamsResponse)
  })
_sym_db.RegisterMessage(QueryParamsResponse)

QueryDepositRequest = _reflection.GeneratedProtocolMessageType('QueryDepositRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYDEPOSITREQUEST,
  '__module__' : 'cosmos.gov.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.gov.v1beta1.QueryDepositRequest)
  })
_sym_db.RegisterMessage(QueryDepositRequest)

QueryDepositResponse = _reflection.GeneratedProtocolMessageType('QueryDepositResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYDEPOSITRESPONSE,
  '__module__' : 'cosmos.gov.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.gov.v1beta1.QueryDepositResponse)
  })
_sym_db.RegisterMessage(QueryDepositResponse)

QueryDepositsRequest = _reflection.GeneratedProtocolMessageType('QueryDepositsRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYDEPOSITSREQUEST,
  '__module__' : 'cosmos.gov.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.gov.v1beta1.QueryDepositsRequest)
  })
_sym_db.RegisterMessage(QueryDepositsRequest)

QueryDepositsResponse = _reflection.GeneratedProtocolMessageType('QueryDepositsResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYDEPOSITSRESPONSE,
  '__module__' : 'cosmos.gov.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.gov.v1beta1.QueryDepositsResponse)
  })
_sym_db.RegisterMessage(QueryDepositsResponse)

QueryTallyResultRequest = _reflection.GeneratedProtocolMessageType('QueryTallyResultRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYTALLYRESULTREQUEST,
  '__module__' : 'cosmos.gov.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.gov.v1beta1.QueryTallyResultRequest)
  })
_sym_db.RegisterMessage(QueryTallyResultRequest)

QueryTallyResultResponse = _reflection.GeneratedProtocolMessageType('QueryTallyResultResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYTALLYRESULTRESPONSE,
  '__module__' : 'cosmos.gov.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.gov.v1beta1.QueryTallyResultResponse)
  })
_sym_db.RegisterMessage(QueryTallyResultResponse)


DESCRIPTOR._options = None
_QUERYPROPOSALRESPONSE.fields_by_name['proposal']._options = None
_QUERYPROPOSALSREQUEST.fields_by_name['voter']._options = None
_QUERYPROPOSALSREQUEST.fields_by_name['depositor']._options = None
_QUERYPROPOSALSREQUEST._options = None
_QUERYPROPOSALSRESPONSE.fields_by_name['proposals']._options = None
_QUERYVOTEREQUEST.fields_by_name['voter']._options = None
_QUERYVOTEREQUEST._options = None
_QUERYVOTERESPONSE.fields_by_name['vote']._options = None
_QUERYVOTESRESPONSE.fields_by_name['votes']._options = None
_QUERYPARAMSRESPONSE.fields_by_name['voting_params']._options = None
_QUERYPARAMSRESPONSE.fields_by_name['deposit_params']._options = None
_QUERYPARAMSRESPONSE.fields_by_name['tally_params']._options = None
_QUERYDEPOSITREQUEST.fields_by_name['depositor']._options = None
_QUERYDEPOSITREQUEST._options = None
_QUERYDEPOSITRESPONSE.fields_by_name['deposit']._options = None
_QUERYDEPOSITSRESPONSE.fields_by_name['deposits']._options = None
_QUERYTALLYRESULTRESPONSE.fields_by_name['tally']._options = None

_QUERY = _descriptor.ServiceDescriptor(
  name='Query',
  full_name='cosmos.gov.v1beta1.Query',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1916,
  serialized_end=3152,
  methods=[
  _descriptor.MethodDescriptor(
    name='Proposal',
    full_name='cosmos.gov.v1beta1.Query.Proposal',
    index=0,
    containing_service=None,
    input_type=_QUERYPROPOSALREQUEST,
    output_type=_QUERYPROPOSALRESPONSE,
    serialized_options=b'\202\323\344\223\002-\022+/cosmos/gov/v1beta1/proposals/{proposal_id}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Proposals',
    full_name='cosmos.gov.v1beta1.Query.Proposals',
    index=1,
    containing_service=None,
    input_type=_QUERYPROPOSALSREQUEST,
    output_type=_QUERYPROPOSALSRESPONSE,
    serialized_options=b'\202\323\344\223\002\037\022\035/cosmos/gov/v1beta1/proposals',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Vote',
    full_name='cosmos.gov.v1beta1.Query.Vote',
    index=2,
    containing_service=None,
    input_type=_QUERYVOTEREQUEST,
    output_type=_QUERYVOTERESPONSE,
    serialized_options=b'\202\323\344\223\002;\0229/cosmos/gov/v1beta1/proposals/{proposal_id}/votes/{voter}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Votes',
    full_name='cosmos.gov.v1beta1.Query.Votes',
    index=3,
    containing_service=None,
    input_type=_QUERYVOTESREQUEST,
    output_type=_QUERYVOTESRESPONSE,
    serialized_options=b'\202\323\344\223\0023\0221/cosmos/gov/v1beta1/proposals/{proposal_id}/votes',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Params',
    full_name='cosmos.gov.v1beta1.Query.Params',
    index=4,
    containing_service=None,
    input_type=_QUERYPARAMSREQUEST,
    output_type=_QUERYPARAMSRESPONSE,
    serialized_options=b'\202\323\344\223\002*\022(/cosmos/gov/v1beta1/params/{params_type}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Deposit',
    full_name='cosmos.gov.v1beta1.Query.Deposit',
    index=5,
    containing_service=None,
    input_type=_QUERYDEPOSITREQUEST,
    output_type=_QUERYDEPOSITRESPONSE,
    serialized_options=b'\202\323\344\223\002B\022@/cosmos/gov/v1beta1/proposals/{proposal_id}/deposits/{depositor}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Deposits',
    full_name='cosmos.gov.v1beta1.Query.Deposits',
    index=6,
    containing_service=None,
    input_type=_QUERYDEPOSITSREQUEST,
    output_type=_QUERYDEPOSITSRESPONSE,
    serialized_options=b'\202\323\344\223\0026\0224/cosmos/gov/v1beta1/proposals/{proposal_id}/deposits',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='TallyResult',
    full_name='cosmos.gov.v1beta1.Query.TallyResult',
    index=7,
    containing_service=None,
    input_type=_QUERYTALLYRESULTREQUEST,
    output_type=_QUERYTALLYRESULTRESPONSE,
    serialized_options=b'\202\323\344\223\0023\0221/cosmos/gov/v1beta1/proposals/{proposal_id}/tally',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_QUERY)

DESCRIPTOR.services_by_name['Query'] = _QUERY

# @@protoc_insertion_point(module_scope)
