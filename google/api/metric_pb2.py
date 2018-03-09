# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/api/metric.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import label_pb2 as google_dot_api_dot_label__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/api/metric.proto',
  package='google.api',
  syntax='proto3',
  serialized_pb=_b('\n\x17google/api/metric.proto\x12\ngoogle.api\x1a\x16google/api/label.proto\"\xd2\x03\n\x10MetricDescriptor\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x08 \x01(\t\x12+\n\x06labels\x18\x02 \x03(\x0b\x32\x1b.google.api.LabelDescriptor\x12<\n\x0bmetric_kind\x18\x03 \x01(\x0e\x32\'.google.api.MetricDescriptor.MetricKind\x12:\n\nvalue_type\x18\x04 \x01(\x0e\x32&.google.api.MetricDescriptor.ValueType\x12\x0c\n\x04unit\x18\x05 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x06 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x07 \x01(\t\"O\n\nMetricKind\x12\x1b\n\x17METRIC_KIND_UNSPECIFIED\x10\x00\x12\t\n\x05GAUGE\x10\x01\x12\t\n\x05\x44\x45LTA\x10\x02\x12\x0e\n\nCUMULATIVE\x10\x03\"q\n\tValueType\x12\x1a\n\x16VALUE_TYPE_UNSPECIFIED\x10\x00\x12\x08\n\x04\x42OOL\x10\x01\x12\t\n\x05INT64\x10\x02\x12\n\n\x06\x44OUBLE\x10\x03\x12\n\n\x06STRING\x10\x04\x12\x10\n\x0c\x44ISTRIBUTION\x10\x05\x12\t\n\x05MONEY\x10\x06\"u\n\x06Metric\x12\x0c\n\x04type\x18\x03 \x01(\t\x12.\n\x06labels\x18\x02 \x03(\x0b\x32\x1e.google.api.Metric.LabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42&\n\x0e\x63om.google.apiB\x0bMetricProtoP\x01\xa2\x02\x04GAPIb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_label__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_METRICDESCRIPTOR_METRICKIND = _descriptor.EnumDescriptor(
  name='MetricKind',
  full_name='google.api.MetricDescriptor.MetricKind',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='METRIC_KIND_UNSPECIFIED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GAUGE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DELTA', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CUMULATIVE', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=336,
  serialized_end=415,
)
_sym_db.RegisterEnumDescriptor(_METRICDESCRIPTOR_METRICKIND)

_METRICDESCRIPTOR_VALUETYPE = _descriptor.EnumDescriptor(
  name='ValueType',
  full_name='google.api.MetricDescriptor.ValueType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='VALUE_TYPE_UNSPECIFIED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOOL', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INT64', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DOUBLE', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STRING', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DISTRIBUTION', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MONEY', index=6, number=6,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=417,
  serialized_end=530,
)
_sym_db.RegisterEnumDescriptor(_METRICDESCRIPTOR_VALUETYPE)


_METRICDESCRIPTOR = _descriptor.Descriptor(
  name='MetricDescriptor',
  full_name='google.api.MetricDescriptor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.api.MetricDescriptor.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='google.api.MetricDescriptor.type', index=1,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='labels', full_name='google.api.MetricDescriptor.labels', index=2,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='metric_kind', full_name='google.api.MetricDescriptor.metric_kind', index=3,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value_type', full_name='google.api.MetricDescriptor.value_type', index=4,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unit', full_name='google.api.MetricDescriptor.unit', index=5,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description', full_name='google.api.MetricDescriptor.description', index=6,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='display_name', full_name='google.api.MetricDescriptor.display_name', index=7,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _METRICDESCRIPTOR_METRICKIND,
    _METRICDESCRIPTOR_VALUETYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=64,
  serialized_end=530,
)


_METRIC_LABELSENTRY = _descriptor.Descriptor(
  name='LabelsEntry',
  full_name='google.api.Metric.LabelsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='google.api.Metric.LabelsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='google.api.Metric.LabelsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=604,
  serialized_end=649,
)

_METRIC = _descriptor.Descriptor(
  name='Metric',
  full_name='google.api.Metric',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='google.api.Metric.type', index=0,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='labels', full_name='google.api.Metric.labels', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_METRIC_LABELSENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=532,
  serialized_end=649,
)

_METRICDESCRIPTOR.fields_by_name['labels'].message_type = google_dot_api_dot_label__pb2._LABELDESCRIPTOR
_METRICDESCRIPTOR.fields_by_name['metric_kind'].enum_type = _METRICDESCRIPTOR_METRICKIND
_METRICDESCRIPTOR.fields_by_name['value_type'].enum_type = _METRICDESCRIPTOR_VALUETYPE
_METRICDESCRIPTOR_METRICKIND.containing_type = _METRICDESCRIPTOR
_METRICDESCRIPTOR_VALUETYPE.containing_type = _METRICDESCRIPTOR
_METRIC_LABELSENTRY.containing_type = _METRIC
_METRIC.fields_by_name['labels'].message_type = _METRIC_LABELSENTRY
DESCRIPTOR.message_types_by_name['MetricDescriptor'] = _METRICDESCRIPTOR
DESCRIPTOR.message_types_by_name['Metric'] = _METRIC

MetricDescriptor = _reflection.GeneratedProtocolMessageType('MetricDescriptor', (_message.Message,), dict(
  DESCRIPTOR = _METRICDESCRIPTOR,
  __module__ = 'google.api.metric_pb2'
  # @@protoc_insertion_point(class_scope:google.api.MetricDescriptor)
  ))
_sym_db.RegisterMessage(MetricDescriptor)

Metric = _reflection.GeneratedProtocolMessageType('Metric', (_message.Message,), dict(

  LabelsEntry = _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), dict(
    DESCRIPTOR = _METRIC_LABELSENTRY,
    __module__ = 'google.api.metric_pb2'
    # @@protoc_insertion_point(class_scope:google.api.Metric.LabelsEntry)
    ))
  ,
  DESCRIPTOR = _METRIC,
  __module__ = 'google.api.metric_pb2'
  # @@protoc_insertion_point(class_scope:google.api.Metric)
  ))
_sym_db.RegisterMessage(Metric)
_sym_db.RegisterMessage(Metric.LabelsEntry)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\016com.google.apiB\013MetricProtoP\001\242\002\004GAPI'))
_METRIC_LABELSENTRY.has_options = True
_METRIC_LABELSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
# @@protoc_insertion_point(module_scope)
