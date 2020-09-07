# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fl_comm_libs/proto/co_proxy.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='fl_comm_libs/proto/co_proxy.proto',
  package='jdfl',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n!fl_comm_libs/proto/co_proxy.proto\x12\x04jdfl\")\n\x06Status\x12\x0e\n\x06status\x18\x01 \x01(\r\x12\x0f\n\x07\x65rr_msg\x18\x02 \x01(\t\"(\n\x07Request\x12\x0c\n\x04uuid\x18\x01 \x03(\t\x12\x0f\n\x07ip_port\x18\x02 \x01(\t\"6\n\x0bServicePair\x12\x12\n\nlocal_uuid\x18\x01 \x01(\t\x12\x13\n\x0bremote_uuid\x18\x02 \x01(\t\"X\n\x10PairInfoResponse\x12\x1c\n\x06status\x18\x01 \x01(\x0b\x32\x0c.jdfl.Status\x12&\n\x0bservice_map\x18\x02 \x03(\x0b\x32\x11.jdfl.ServicePair2p\n\x0bPairService\x12+\n\x0cRegisterUUID\x12\r.jdfl.Request\x1a\x0c.jdfl.Status\x12\x34\n\x0bGetPairInfo\x12\r.jdfl.Request\x1a\x16.jdfl.PairInfoResponseb\x06proto3')
)




_STATUS = _descriptor.Descriptor(
  name='Status',
  full_name='jdfl.Status',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='jdfl.Status.status', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='err_msg', full_name='jdfl.Status.err_msg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=43,
  serialized_end=84,
)


_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='jdfl.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='jdfl.Request.uuid', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ip_port', full_name='jdfl.Request.ip_port', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=86,
  serialized_end=126,
)


_SERVICEPAIR = _descriptor.Descriptor(
  name='ServicePair',
  full_name='jdfl.ServicePair',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='local_uuid', full_name='jdfl.ServicePair.local_uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='remote_uuid', full_name='jdfl.ServicePair.remote_uuid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=128,
  serialized_end=182,
)


_PAIRINFORESPONSE = _descriptor.Descriptor(
  name='PairInfoResponse',
  full_name='jdfl.PairInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='jdfl.PairInfoResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='service_map', full_name='jdfl.PairInfoResponse.service_map', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=184,
  serialized_end=272,
)

_PAIRINFORESPONSE.fields_by_name['status'].message_type = _STATUS
_PAIRINFORESPONSE.fields_by_name['service_map'].message_type = _SERVICEPAIR
DESCRIPTOR.message_types_by_name['Status'] = _STATUS
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['ServicePair'] = _SERVICEPAIR
DESCRIPTOR.message_types_by_name['PairInfoResponse'] = _PAIRINFORESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Status = _reflection.GeneratedProtocolMessageType('Status', (_message.Message,), {
  'DESCRIPTOR' : _STATUS,
  '__module__' : 'fl_comm_libs.proto.co_proxy_pb2'
  # @@protoc_insertion_point(class_scope:jdfl.Status)
  })
_sym_db.RegisterMessage(Status)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), {
  'DESCRIPTOR' : _REQUEST,
  '__module__' : 'fl_comm_libs.proto.co_proxy_pb2'
  # @@protoc_insertion_point(class_scope:jdfl.Request)
  })
_sym_db.RegisterMessage(Request)

ServicePair = _reflection.GeneratedProtocolMessageType('ServicePair', (_message.Message,), {
  'DESCRIPTOR' : _SERVICEPAIR,
  '__module__' : 'fl_comm_libs.proto.co_proxy_pb2'
  # @@protoc_insertion_point(class_scope:jdfl.ServicePair)
  })
_sym_db.RegisterMessage(ServicePair)

PairInfoResponse = _reflection.GeneratedProtocolMessageType('PairInfoResponse', (_message.Message,), {
  'DESCRIPTOR' : _PAIRINFORESPONSE,
  '__module__' : 'fl_comm_libs.proto.co_proxy_pb2'
  # @@protoc_insertion_point(class_scope:jdfl.PairInfoResponse)
  })
_sym_db.RegisterMessage(PairInfoResponse)



_PAIRSERVICE = _descriptor.ServiceDescriptor(
  name='PairService',
  full_name='jdfl.PairService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=274,
  serialized_end=386,
  methods=[
  _descriptor.MethodDescriptor(
    name='RegisterUUID',
    full_name='jdfl.PairService.RegisterUUID',
    index=0,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_STATUS,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetPairInfo',
    full_name='jdfl.PairService.GetPairInfo',
    index=1,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_PAIRINFORESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_PAIRSERVICE)

DESCRIPTOR.services_by_name['PairService'] = _PAIRSERVICE

# @@protoc_insertion_point(module_scope)
