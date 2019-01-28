# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hal.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='hal.proto',
  package='cps.hal',
  syntax='proto3',
  serialized_pb=_b('\n\thal.proto\x12\x07\x63ps.hal\"\x84\x01\n\x0bTemperature\x12\r\n\x05value\x18\x01 \x01(\x02\x12\'\n\x04unit\x18\x02 \x01(\x0e\x32\x19.cps.hal.Temperature.Unit\"=\n\x04Unit\x12\r\n\tUNDEFINED\x10\x00\x12\x0b\n\x07\x43\x45LSIUS\x10\x01\x12\r\n\tFARENHEIT\x10\x02\x12\n\n\x06KELVIN\x10\x03\"\x9b\x01\n\x08Humidity\x12\r\n\x05value\x18\x01 \x01(\x02\x12$\n\x04unit\x18\x02 \x01(\x0e\x32\x16.cps.hal.Humidity.Unit\"Z\n\x04Unit\x12\r\n\tUNDEFINED\x10\x00\x12\x15\n\x11RELATIVE_HUMIDITY\x10\x01\x12\x15\n\x11\x41\x42SOLUTE_HUMIDITY\x10\x02\x12\x15\n\x11SPECIFIC_HUMIDITY\x10\x03\"\xaa\x01\n\x08Pressure\x12\r\n\x05value\x18\x01 \x01(\x02\x12$\n\x04unit\x18\x02 \x01(\x0e\x32\x16.cps.hal.Pressure.Unit\"i\n\x04Unit\x12\r\n\tUNDEFINED\x10\x00\x12\n\n\x06PASCAL\x10\x01\x12\x0f\n\x0bHECTOPASCAL\x10\x02\x12\x0e\n\nKILOPASCAL\x10\x03\x12\x0e\n\nATMOSPHERE\x10\x04\x12\x07\n\x03\x42\x41R\x10\x05\x12\x0c\n\x08MILLIBAR\x10\x06\"m\n\x07Voltage\x12\r\n\x05value\x18\x01 \x01(\x02\x12#\n\x04unit\x18\x02 \x01(\x0e\x32\x15.cps.hal.Voltage.Unit\".\n\x04Unit\x12\r\n\tUNDEFINED\x10\x00\x12\r\n\tMILLIVOLT\x10\x01\x12\x08\n\x04VOLT\x10\x02\"o\n\x07\x43urrent\x12\r\n\x05value\x18\x01 \x01(\x02\x12#\n\x04unit\x18\x02 \x01(\x0e\x32\x15.cps.hal.Current.Unit\"0\n\x04Unit\x12\r\n\tUNDEFINED\x10\x00\x12\x0e\n\nMILLIAMPER\x10\x01\x12\t\n\x05\x41MPER\x10\x02\"e\n\x0bIlluminance\x12\r\n\x05value\x18\x01 \x01(\x02\x12\'\n\x04unit\x18\x02 \x01(\x0e\x32\x19.cps.hal.Illuminance.Unit\"\x1e\n\x04Unit\x12\r\n\tUNDEFINED\x10\x00\x12\x07\n\x03LUX\x10\x01\"u\n\x05\x41ngle\x12\r\n\x05value\x18\x01 \x01(\x02\x12!\n\x04unit\x18\x02 \x01(\x0e\x32\x13.cps.hal.Angle.Unit\":\n\x04Unit\x12\r\n\tUNDEFINED\x10\x00\x12\n\n\x06RADIAN\x10\x01\x12\x0b\n\x07GRADIAN\x10\x02\x12\n\n\x06\x44\x45GREE\x10\x03\"\x8d\x06\n\x07Request\x12#\n\x04\x64\x61ta\x18\x01 \x01(\x0e\x32\x15.cps.hal.Request.Data\x12)\n\x07\x63ontrol\x18\x02 \x01(\x0e\x32\x18.cps.hal.Request.Control\x12$\n\x06source\x18\x03 \x01(\x0e\x32\x14.cps.hal.PowerSource\x12\"\n\ntilt_angle\x18\x04 \x01(\x0b\x32\x0e.cps.hal.Angle\x12&\n\x0erotation_angle\x18\x05 \x01(\x0b\x32\x0e.cps.hal.Angle\x12\x0f\n\x07message\x18\x06 \x01(\t\"\xae\x03\n\x04\x44\x61ta\x12\r\n\tNO_THANKS\x10\x00\x12\x18\n\x14INTERNAL_TEMPERATURE\x10\x01\x12\x15\n\x11INTERNAL_HUMIDITY\x10\x02\x12\x15\n\x11INTERNAL_PRESSURE\x10\x04\x12\x18\n\x14INTERNAL_ILLUMINANCE\x10\x08\x12\x18\n\x14\x45XTERNAL_TEMPERATURE\x10\x10\x12\x12\n\x0e\x43OLLECTOR_TILT\x10 \x12\x16\n\x12\x43OLLECTOR_ROTATION\x10@\x12\x11\n\x0cPOWER_SOURCE\x10\x80\x01\x12\x14\n\x0f\x42\x41TTERY_VOLTAGE\x10\x80\x02\x12\x14\n\x0f\x42\x41TTERY_CURRENT\x10\x80\x04\x12\x12\n\rBATTERY_STATE\x10\x80\x08\x12\x18\n\x13\x45XTERNAL_PS_VOLTAGE\x10\x80\x10\x12\x18\n\x13\x45XTERNAL_PS_CURRENT\x10\x80 \x12\x16\n\x11\x45XTERNAL_PS_STATE\x10\x80@\x12\x1a\n\x14\x43OLLECTOR_PS_VOLTAGE\x10\x80\x80\x01\x12\x1a\n\x14\x43OLLECTOR_PS_CURRENT\x10\x80\x80\x02\x12\x18\n\x12\x43OLLECTOR_PS_STATE\x10\x80\x80\x04\"~\n\x07\x43ontrol\x12\x0b\n\x07NOTHING\x10\x00\x12\x14\n\x10SET_POWER_SOURCE\x10\x01\x12\x1c\n\x18SET_COLLECTOR_TILT_ANGLE\x10\x02\x12 \n\x1cSET_COLLECTOR_ROTATION_ANGLE\x10\x04\x12\x10\n\x0cSHOW_MESSAGE\x10\x08\"i\n\x12PowerSourceDetails\x12!\n\x07voltage\x18\x01 \x01(\x0b\x32\x10.cps.hal.Voltage\x12!\n\x07\x63urrent\x18\x02 \x01(\x0b\x32\x10.cps.hal.Current\x12\r\n\x05state\x18\x03 \x01(\t\"\xcc\x06\n\x08Response\x12(\n\x06status\x18\x01 \x01(\x0e\x32\x18.cps.hal.Response.Status\x12)\n\x0btemperature\x18\x02 \x01(\x0b\x32\x14.cps.hal.Temperature\x12#\n\x08humidity\x18\x03 \x01(\x0b\x32\x11.cps.hal.Humidity\x12#\n\x08pressure\x18\x04 \x01(\x0b\x32\x11.cps.hal.Pressure\x12)\n\x0billuminance\x18\x05 \x01(\x0b\x32\x14.cps.hal.Illuminance\x12\x31\n\x13\x65xternalTemperature\x18\x06 \x01(\x0b\x32\x14.cps.hal.Temperature\x12%\n\rcollectorTilt\x18\x07 \x01(\x0b\x32\x0e.cps.hal.Angle\x12)\n\x0bpowerSource\x18\x08 \x01(\x0e\x32\x14.cps.hal.PowerSource\x12\x33\n\x0e\x62\x61tteryDetails\x18\n \x01(\x0b\x32\x1b.cps.hal.PowerSourceDetails\x12\x36\n\x11\x65xternalPSDetails\x18\x0b \x01(\x0b\x32\x1b.cps.hal.PowerSourceDetails\x12\x37\n\x12\x63ollectorPSDetails\x18\x0c \x01(\x0b\x32\x1b.cps.hal.PowerSourceDetails\"\xca\x02\n\x06Status\x12\x06\n\x02OK\x10\x00\x12\x18\n\x14UNRECOGNISED_REQUEST\x10\x01\x12\x19\n\x15INT_TEMPERATURE_ERROR\x10\x02\x12\x13\n\x0fHUMIDITIY_ERROR\x10\x04\x12\x12\n\x0ePRESSURE_ERROR\x10\x08\x12\x15\n\x11ILLUMINANCE_ERROR\x10\x10\x12\x19\n\x15\x45XT_TEMPERATURE_ERROR\x10 \x12\x18\n\x14\x43OLLECTOR_TILT_ERROR\x10@\x12\x1d\n\x18\x43OLLECTOR_ROTATION_ERROR\x10\x80\x01\x12\x12\n\rBATTERY_ERROR\x10\x80\x02\x12\x13\n\x0e\x45XTERNAL_ERROR\x10\x80\x04\x12\x14\n\x0f\x43OLLECTOR_ERROR\x10\x80\x08\x12\x17\n\x12POWER_SOURCE_ERROR\x10\x80\x10\x12\x17\n\x12SHOW_MESSAGE_ERROR\x10\x80 *F\n\x0bPowerSource\x12\r\n\tUNDEFINED\x10\x00\x12\x0b\n\x07\x42\x41TTERY\x10\x01\x12\x0c\n\x08\x45XTERNAL\x10\x02\x12\r\n\tCOLLECTOR\x10\x03\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_POWERSOURCE = _descriptor.EnumDescriptor(
  name='PowerSource',
  full_name='cps.hal.PowerSource',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNDEFINED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BATTERY', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXTERNAL', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COLLECTOR', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=2672,
  serialized_end=2742,
)
_sym_db.RegisterEnumDescriptor(_POWERSOURCE)

PowerSource = enum_type_wrapper.EnumTypeWrapper(_POWERSOURCE)
UNDEFINED = 0
BATTERY = 1
EXTERNAL = 2
COLLECTOR = 3


_TEMPERATURE_UNIT = _descriptor.EnumDescriptor(
  name='Unit',
  full_name='cps.hal.Temperature.Unit',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNDEFINED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CELSIUS', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FARENHEIT', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KELVIN', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=94,
  serialized_end=155,
)
_sym_db.RegisterEnumDescriptor(_TEMPERATURE_UNIT)

_HUMIDITY_UNIT = _descriptor.EnumDescriptor(
  name='Unit',
  full_name='cps.hal.Humidity.Unit',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNDEFINED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RELATIVE_HUMIDITY', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ABSOLUTE_HUMIDITY', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SPECIFIC_HUMIDITY', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=223,
  serialized_end=313,
)
_sym_db.RegisterEnumDescriptor(_HUMIDITY_UNIT)

_PRESSURE_UNIT = _descriptor.EnumDescriptor(
  name='Unit',
  full_name='cps.hal.Pressure.Unit',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNDEFINED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PASCAL', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HECTOPASCAL', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KILOPASCAL', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ATMOSPHERE', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BAR', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MILLIBAR', index=6, number=6,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=381,
  serialized_end=486,
)
_sym_db.RegisterEnumDescriptor(_PRESSURE_UNIT)

_VOLTAGE_UNIT = _descriptor.EnumDescriptor(
  name='Unit',
  full_name='cps.hal.Voltage.Unit',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNDEFINED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MILLIVOLT', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VOLT', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=551,
  serialized_end=597,
)
_sym_db.RegisterEnumDescriptor(_VOLTAGE_UNIT)

_CURRENT_UNIT = _descriptor.EnumDescriptor(
  name='Unit',
  full_name='cps.hal.Current.Unit',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNDEFINED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MILLIAMPER', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AMPER', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=662,
  serialized_end=710,
)
_sym_db.RegisterEnumDescriptor(_CURRENT_UNIT)

_ILLUMINANCE_UNIT = _descriptor.EnumDescriptor(
  name='Unit',
  full_name='cps.hal.Illuminance.Unit',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNDEFINED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LUX', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=783,
  serialized_end=813,
)
_sym_db.RegisterEnumDescriptor(_ILLUMINANCE_UNIT)

_ANGLE_UNIT = _descriptor.EnumDescriptor(
  name='Unit',
  full_name='cps.hal.Angle.Unit',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNDEFINED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RADIAN', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GRADIAN', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEGREE', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=874,
  serialized_end=932,
)
_sym_db.RegisterEnumDescriptor(_ANGLE_UNIT)

_REQUEST_DATA = _descriptor.EnumDescriptor(
  name='Data',
  full_name='cps.hal.Request.Data',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NO_THANKS', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INTERNAL_TEMPERATURE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INTERNAL_HUMIDITY', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INTERNAL_PRESSURE', index=3, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INTERNAL_ILLUMINANCE', index=4, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXTERNAL_TEMPERATURE', index=5, number=16,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COLLECTOR_TILT', index=6, number=32,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COLLECTOR_ROTATION', index=7, number=64,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POWER_SOURCE', index=8, number=128,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BATTERY_VOLTAGE', index=9, number=256,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BATTERY_CURRENT', index=10, number=512,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BATTERY_STATE', index=11, number=1024,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXTERNAL_PS_VOLTAGE', index=12, number=2048,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXTERNAL_PS_CURRENT', index=13, number=4096,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXTERNAL_PS_STATE', index=14, number=8192,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COLLECTOR_PS_VOLTAGE', index=15, number=16384,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COLLECTOR_PS_CURRENT', index=16, number=32768,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COLLECTOR_PS_STATE', index=17, number=65536,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1158,
  serialized_end=1588,
)
_sym_db.RegisterEnumDescriptor(_REQUEST_DATA)

_REQUEST_CONTROL = _descriptor.EnumDescriptor(
  name='Control',
  full_name='cps.hal.Request.Control',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NOTHING', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SET_POWER_SOURCE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SET_COLLECTOR_TILT_ANGLE', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SET_COLLECTOR_ROTATION_ANGLE', index=3, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SHOW_MESSAGE', index=4, number=8,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1590,
  serialized_end=1716,
)
_sym_db.RegisterEnumDescriptor(_REQUEST_CONTROL)

_RESPONSE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='cps.hal.Response.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OK', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNRECOGNISED_REQUEST', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INT_TEMPERATURE_ERROR', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HUMIDITIY_ERROR', index=3, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRESSURE_ERROR', index=4, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ILLUMINANCE_ERROR', index=5, number=16,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXT_TEMPERATURE_ERROR', index=6, number=32,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COLLECTOR_TILT_ERROR', index=7, number=64,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COLLECTOR_ROTATION_ERROR', index=8, number=128,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BATTERY_ERROR', index=9, number=256,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXTERNAL_ERROR', index=10, number=512,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COLLECTOR_ERROR', index=11, number=1024,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POWER_SOURCE_ERROR', index=12, number=2048,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SHOW_MESSAGE_ERROR', index=13, number=4096,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=2340,
  serialized_end=2670,
)
_sym_db.RegisterEnumDescriptor(_RESPONSE_STATUS)


_TEMPERATURE = _descriptor.Descriptor(
  name='Temperature',
  full_name='cps.hal.Temperature',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='cps.hal.Temperature.value', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unit', full_name='cps.hal.Temperature.unit', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TEMPERATURE_UNIT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=23,
  serialized_end=155,
)


_HUMIDITY = _descriptor.Descriptor(
  name='Humidity',
  full_name='cps.hal.Humidity',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='cps.hal.Humidity.value', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unit', full_name='cps.hal.Humidity.unit', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _HUMIDITY_UNIT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=158,
  serialized_end=313,
)


_PRESSURE = _descriptor.Descriptor(
  name='Pressure',
  full_name='cps.hal.Pressure',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='cps.hal.Pressure.value', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unit', full_name='cps.hal.Pressure.unit', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PRESSURE_UNIT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=316,
  serialized_end=486,
)


_VOLTAGE = _descriptor.Descriptor(
  name='Voltage',
  full_name='cps.hal.Voltage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='cps.hal.Voltage.value', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unit', full_name='cps.hal.Voltage.unit', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _VOLTAGE_UNIT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=488,
  serialized_end=597,
)


_CURRENT = _descriptor.Descriptor(
  name='Current',
  full_name='cps.hal.Current',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='cps.hal.Current.value', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unit', full_name='cps.hal.Current.unit', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CURRENT_UNIT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=599,
  serialized_end=710,
)


_ILLUMINANCE = _descriptor.Descriptor(
  name='Illuminance',
  full_name='cps.hal.Illuminance',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='cps.hal.Illuminance.value', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unit', full_name='cps.hal.Illuminance.unit', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ILLUMINANCE_UNIT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=712,
  serialized_end=813,
)


_ANGLE = _descriptor.Descriptor(
  name='Angle',
  full_name='cps.hal.Angle',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='cps.hal.Angle.value', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unit', full_name='cps.hal.Angle.unit', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ANGLE_UNIT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=815,
  serialized_end=932,
)


_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='cps.hal.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='cps.hal.Request.data', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='control', full_name='cps.hal.Request.control', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='source', full_name='cps.hal.Request.source', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tilt_angle', full_name='cps.hal.Request.tilt_angle', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rotation_angle', full_name='cps.hal.Request.rotation_angle', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='cps.hal.Request.message', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _REQUEST_DATA,
    _REQUEST_CONTROL,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=935,
  serialized_end=1716,
)


_POWERSOURCEDETAILS = _descriptor.Descriptor(
  name='PowerSourceDetails',
  full_name='cps.hal.PowerSourceDetails',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='voltage', full_name='cps.hal.PowerSourceDetails.voltage', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='current', full_name='cps.hal.PowerSourceDetails.current', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='state', full_name='cps.hal.PowerSourceDetails.state', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1718,
  serialized_end=1823,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='cps.hal.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='cps.hal.Response.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='temperature', full_name='cps.hal.Response.temperature', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='humidity', full_name='cps.hal.Response.humidity', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pressure', full_name='cps.hal.Response.pressure', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='illuminance', full_name='cps.hal.Response.illuminance', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='externalTemperature', full_name='cps.hal.Response.externalTemperature', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='collectorTilt', full_name='cps.hal.Response.collectorTilt', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='powerSource', full_name='cps.hal.Response.powerSource', index=7,
      number=8, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='batteryDetails', full_name='cps.hal.Response.batteryDetails', index=8,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='externalPSDetails', full_name='cps.hal.Response.externalPSDetails', index=9,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='collectorPSDetails', full_name='cps.hal.Response.collectorPSDetails', index=10,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _RESPONSE_STATUS,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1826,
  serialized_end=2670,
)

_TEMPERATURE.fields_by_name['unit'].enum_type = _TEMPERATURE_UNIT
_TEMPERATURE_UNIT.containing_type = _TEMPERATURE
_HUMIDITY.fields_by_name['unit'].enum_type = _HUMIDITY_UNIT
_HUMIDITY_UNIT.containing_type = _HUMIDITY
_PRESSURE.fields_by_name['unit'].enum_type = _PRESSURE_UNIT
_PRESSURE_UNIT.containing_type = _PRESSURE
_VOLTAGE.fields_by_name['unit'].enum_type = _VOLTAGE_UNIT
_VOLTAGE_UNIT.containing_type = _VOLTAGE
_CURRENT.fields_by_name['unit'].enum_type = _CURRENT_UNIT
_CURRENT_UNIT.containing_type = _CURRENT
_ILLUMINANCE.fields_by_name['unit'].enum_type = _ILLUMINANCE_UNIT
_ILLUMINANCE_UNIT.containing_type = _ILLUMINANCE
_ANGLE.fields_by_name['unit'].enum_type = _ANGLE_UNIT
_ANGLE_UNIT.containing_type = _ANGLE
_REQUEST.fields_by_name['data'].enum_type = _REQUEST_DATA
_REQUEST.fields_by_name['control'].enum_type = _REQUEST_CONTROL
_REQUEST.fields_by_name['source'].enum_type = _POWERSOURCE
_REQUEST.fields_by_name['tilt_angle'].message_type = _ANGLE
_REQUEST.fields_by_name['rotation_angle'].message_type = _ANGLE
_REQUEST_DATA.containing_type = _REQUEST
_REQUEST_CONTROL.containing_type = _REQUEST
_POWERSOURCEDETAILS.fields_by_name['voltage'].message_type = _VOLTAGE
_POWERSOURCEDETAILS.fields_by_name['current'].message_type = _CURRENT
_RESPONSE.fields_by_name['status'].enum_type = _RESPONSE_STATUS
_RESPONSE.fields_by_name['temperature'].message_type = _TEMPERATURE
_RESPONSE.fields_by_name['humidity'].message_type = _HUMIDITY
_RESPONSE.fields_by_name['pressure'].message_type = _PRESSURE
_RESPONSE.fields_by_name['illuminance'].message_type = _ILLUMINANCE
_RESPONSE.fields_by_name['externalTemperature'].message_type = _TEMPERATURE
_RESPONSE.fields_by_name['collectorTilt'].message_type = _ANGLE
_RESPONSE.fields_by_name['powerSource'].enum_type = _POWERSOURCE
_RESPONSE.fields_by_name['batteryDetails'].message_type = _POWERSOURCEDETAILS
_RESPONSE.fields_by_name['externalPSDetails'].message_type = _POWERSOURCEDETAILS
_RESPONSE.fields_by_name['collectorPSDetails'].message_type = _POWERSOURCEDETAILS
_RESPONSE_STATUS.containing_type = _RESPONSE
DESCRIPTOR.message_types_by_name['Temperature'] = _TEMPERATURE
DESCRIPTOR.message_types_by_name['Humidity'] = _HUMIDITY
DESCRIPTOR.message_types_by_name['Pressure'] = _PRESSURE
DESCRIPTOR.message_types_by_name['Voltage'] = _VOLTAGE
DESCRIPTOR.message_types_by_name['Current'] = _CURRENT
DESCRIPTOR.message_types_by_name['Illuminance'] = _ILLUMINANCE
DESCRIPTOR.message_types_by_name['Angle'] = _ANGLE
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['PowerSourceDetails'] = _POWERSOURCEDETAILS
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
DESCRIPTOR.enum_types_by_name['PowerSource'] = _POWERSOURCE

Temperature = _reflection.GeneratedProtocolMessageType('Temperature', (_message.Message,), dict(
  DESCRIPTOR = _TEMPERATURE,
  __module__ = 'hal_pb2'
  # @@protoc_insertion_point(class_scope:cps.hal.Temperature)
  ))
_sym_db.RegisterMessage(Temperature)

Humidity = _reflection.GeneratedProtocolMessageType('Humidity', (_message.Message,), dict(
  DESCRIPTOR = _HUMIDITY,
  __module__ = 'hal_pb2'
  # @@protoc_insertion_point(class_scope:cps.hal.Humidity)
  ))
_sym_db.RegisterMessage(Humidity)

Pressure = _reflection.GeneratedProtocolMessageType('Pressure', (_message.Message,), dict(
  DESCRIPTOR = _PRESSURE,
  __module__ = 'hal_pb2'
  # @@protoc_insertion_point(class_scope:cps.hal.Pressure)
  ))
_sym_db.RegisterMessage(Pressure)

Voltage = _reflection.GeneratedProtocolMessageType('Voltage', (_message.Message,), dict(
  DESCRIPTOR = _VOLTAGE,
  __module__ = 'hal_pb2'
  # @@protoc_insertion_point(class_scope:cps.hal.Voltage)
  ))
_sym_db.RegisterMessage(Voltage)

Current = _reflection.GeneratedProtocolMessageType('Current', (_message.Message,), dict(
  DESCRIPTOR = _CURRENT,
  __module__ = 'hal_pb2'
  # @@protoc_insertion_point(class_scope:cps.hal.Current)
  ))
_sym_db.RegisterMessage(Current)

Illuminance = _reflection.GeneratedProtocolMessageType('Illuminance', (_message.Message,), dict(
  DESCRIPTOR = _ILLUMINANCE,
  __module__ = 'hal_pb2'
  # @@protoc_insertion_point(class_scope:cps.hal.Illuminance)
  ))
_sym_db.RegisterMessage(Illuminance)

Angle = _reflection.GeneratedProtocolMessageType('Angle', (_message.Message,), dict(
  DESCRIPTOR = _ANGLE,
  __module__ = 'hal_pb2'
  # @@protoc_insertion_point(class_scope:cps.hal.Angle)
  ))
_sym_db.RegisterMessage(Angle)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
  DESCRIPTOR = _REQUEST,
  __module__ = 'hal_pb2'
  # @@protoc_insertion_point(class_scope:cps.hal.Request)
  ))
_sym_db.RegisterMessage(Request)

PowerSourceDetails = _reflection.GeneratedProtocolMessageType('PowerSourceDetails', (_message.Message,), dict(
  DESCRIPTOR = _POWERSOURCEDETAILS,
  __module__ = 'hal_pb2'
  # @@protoc_insertion_point(class_scope:cps.hal.PowerSourceDetails)
  ))
_sym_db.RegisterMessage(PowerSourceDetails)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSE,
  __module__ = 'hal_pb2'
  # @@protoc_insertion_point(class_scope:cps.hal.Response)
  ))
_sym_db.RegisterMessage(Response)


# @@protoc_insertion_point(module_scope)
