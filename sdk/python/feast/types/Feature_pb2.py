# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: feast/types/Feature.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from feast.types import Value_pb2 as feast_dot_types_dot_Value__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='feast/types/Feature.proto',
  package='feast.types',
  syntax='proto3',
  serialized_options=_b('\n\013feast.typesB\014FeatureProtoZ6github.com/gojek/feast/protos/generated/go/feast/types'),
  serialized_pb=_b('\n\x19\x66\x65\x61st/types/Feature.proto\x12\x0b\x66\x65\x61st.types\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17\x66\x65\x61st/types/Value.proto\"8\n\x07\x46\x65\x61ture\x12\n\n\x02id\x18\x01 \x01(\t\x12!\n\x05value\x18\x02 \x01(\x0b\x32\x12.feast.types.ValueBS\n\x0b\x66\x65\x61st.typesB\x0c\x46\x65\x61tureProtoZ6github.com/gojek/feast/protos/generated/go/feast/typesb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,feast_dot_types_dot_Value__pb2.DESCRIPTOR,])




_FEATURE = _descriptor.Descriptor(
  name='Feature',
  full_name='feast.types.Feature',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='feast.types.Feature.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='feast.types.Feature.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=100,
  serialized_end=156,
)

_FEATURE.fields_by_name['value'].message_type = feast_dot_types_dot_Value__pb2._VALUE
DESCRIPTOR.message_types_by_name['Feature'] = _FEATURE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Feature = _reflection.GeneratedProtocolMessageType('Feature', (_message.Message,), dict(
  DESCRIPTOR = _FEATURE,
  __module__ = 'feast.types.Feature_pb2'
  # @@protoc_insertion_point(class_scope:feast.types.Feature)
  ))
_sym_db.RegisterMessage(Feature)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
