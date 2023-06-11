# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: daq.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\tdaq.proto\x12\x03\x64\x61q"d\n\tCallState\x12#\n\x05state\x18\x02 \x01(\x0e\x32\x14.daq.CallState.State"2\n\x05State\x12\x0b\n\x07STOPPED\x10\x00\x12\r\n\tRECEIVING\x10\x01\x12\r\n\tLISTENING\x10\x02"R\n\x08\x43\x61llInfo\x12\x1b\n\x13\x64\x61ta_types_received\x18\x01 \x01(\t\x12\x15\n\rfiles_written\x18\x02 \x01(\t\x12\x12\n\nextra_info\x18\x03 \x01(\t")\n\x0fstartDaqRequest\x12\x16\n\x0emodes_to_start\x18\x01 \x01(\t"r\n\x10startDaqResponse\x12$\n\ncall_state\x18\x01 \x01(\x0b\x32\x0e.daq.CallStateH\x00\x12"\n\tcall_info\x18\x02 \x01(\x0b\x32\r.daq.CallInfoH\x00\x42\x14\n\x12start_daq_response"\x10\n\x0estopDaqRequest"\x12\n\x10getConfigRequest"#\n\x11getConfigResponse\x12\x0e\n\x06\x63onfig\x18\x01 \x01(\t"\x12\n\x10\x64\x61qStatusRequest"#\n\x11\x64\x61qStatusResponse\x12\x0e\n\x06status\x18\x01 \x01(\t"H\n\x0f\x63ommandResponse\x12$\n\x0bresult_code\x18\x01 \x01(\x0e\x32\x0f.daq.ResultCode\x12\x0f\n\x07message\x18\x02 \x01(\t""\n\x10\x63onfigDaqRequest\x12\x0e\n\x06\x63onfig\x18\x01 \x01(\t"\x9f\x07\n\x15\x43onfigurationResponse\x12\x14\n\x0cnof_antennas\x18\x01 \x01(\x05\x12\x14\n\x0cnof_channels\x18\x02 \x01(\x05\x12\x11\n\tnof_beams\x18\x03 \x01(\x05\x12\x19\n\x11nof_polarisations\x18\x04 \x01(\x05\x12\x11\n\tnof_tiles\x18\x05 \x01(\x05\x12\x17\n\x0fnof_raw_samples\x18\x06 \x01(\x05\x12\x19\n\x11raw_rms_threshold\x18\x07 \x01(\x05\x12\x1b\n\x13nof_channel_samples\x18\x08 \x01(\x05\x12\x1e\n\x16nof_correlator_samples\x18\t \x01(\x05\x12\x1f\n\x17nof_correlator_channels\x18\n \x01(\x05\x12\x19\n\x11\x63ontinuous_period\x18\x0b \x01(\x05\x12\x18\n\x10nof_beam_samples\x18\x0c \x01(\x05\x12\x19\n\x11nof_beam_channels\x18\r \x01(\x05\x12\x1b\n\x13nof_station_samples\x18\x0e \x01(\x05\x12!\n\x19receiver_frames_per_block\x18\x0f \x01(\x05\x12\x1b\n\x13receiver_nof_blocks\x18\x10 \x01(\x05\x12\x1c\n\x14receiver_nof_threads\x18\x11 \x01(\x05\x12\x1b\n\x13receiver_frame_size\x18\x12 \x01(\x05\x12\x1c\n\x14\x61\x63quisition_duration\x18\x13 \x01(\x05\x12\x1e\n\x16\x61\x63quisition_start_time\x18\x14 \x01(\x05\x12\x19\n\x11\x61ppend_integrated\x18\x15 \x01(\x08\x12\x0f\n\x07logging\x18\x16 \x01(\x08\x12\x15\n\rwrite_to_disk\x18\x17 \x01(\x08\x12\x15\n\rsampling_time\x18\x18 \x01(\x01\x12\x15\n\rsampling_rate\x18\x19 \x01(\x01\x12\x1b\n\x13oversampling_factor\x18\x1a \x01(\x01\x12\x16\n\x0ereceiver_ports\x18\x1b \x01(\t\x12\x1c\n\x14observation_metadata\x18\x1c \x01(\t\x12\x1a\n\x12receiver_interface\x18\x1d \x01(\t\x12\x13\n\x0breceiver_ip\x18\x1e \x01(\t\x12\x11\n\tdirectory\x18\x1f \x01(\t\x12\x13\n\x0b\x64\x65scription\x18  \x01(\t\x12"\n\x0estation_config\x18! \x01(\x0b\x32\n.daq.empty\x12 \n\x0cmax_filesize\x18" \x01(\x0b\x32\n.daq.empty"\x07\n\x05\x65mpty*r\n\nResultCode\x12\x06\n\x02OK\x10\x00\x12\x0b\n\x07STARTED\x10\x01\x12\n\n\x06QUEUED\x10\x02\x12\n\n\x06\x46\x41ILED\x10\x03\x12\x0b\n\x07UNKNOWN\x10\x04\x12\x0c\n\x08REJECTED\x10\x05\x12\x0f\n\x0bNOT_ALLOWED\x10\x06\x12\x0b\n\x07\x41\x42ORTED\x10\x07\x32\xfa\x02\n\x03\x44\x61q\x12;\n\x08StartDaq\x12\x14.daq.startDaqRequest\x1a\x15.daq.startDaqResponse"\x00\x30\x01\x12\x36\n\x07StopDaq\x12\x13.daq.stopDaqRequest\x1a\x14.daq.commandResponse"\x00\x12\x38\n\x07InitDaq\x12\x15.daq.configDaqRequest\x1a\x14.daq.commandResponse"\x00\x12=\n\x0c\x43onfigureDaq\x12\x15.daq.configDaqRequest\x1a\x14.daq.commandResponse"\x00\x12G\n\x10GetConfiguration\x12\x15.daq.getConfigRequest\x1a\x1a.daq.ConfigurationResponse"\x00\x12<\n\tDaqStatus\x12\x15.daq.daqStatusRequest\x1a\x16.daq.daqStatusResponse"\x00\x62\x06proto3'
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "daq_pb2", globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _RESULTCODE._serialized_start = 1544
    _RESULTCODE._serialized_end = 1658
    _CALLSTATE._serialized_start = 18
    _CALLSTATE._serialized_end = 118
    _CALLSTATE_STATE._serialized_start = 68
    _CALLSTATE_STATE._serialized_end = 118
    _CALLINFO._serialized_start = 120
    _CALLINFO._serialized_end = 202
    _STARTDAQREQUEST._serialized_start = 204
    _STARTDAQREQUEST._serialized_end = 245
    _STARTDAQRESPONSE._serialized_start = 247
    _STARTDAQRESPONSE._serialized_end = 361
    _STOPDAQREQUEST._serialized_start = 363
    _STOPDAQREQUEST._serialized_end = 379
    _GETCONFIGREQUEST._serialized_start = 381
    _GETCONFIGREQUEST._serialized_end = 399
    _GETCONFIGRESPONSE._serialized_start = 401
    _GETCONFIGRESPONSE._serialized_end = 436
    _DAQSTATUSREQUEST._serialized_start = 438
    _DAQSTATUSREQUEST._serialized_end = 456
    _DAQSTATUSRESPONSE._serialized_start = 458
    _DAQSTATUSRESPONSE._serialized_end = 493
    _COMMANDRESPONSE._serialized_start = 495
    _COMMANDRESPONSE._serialized_end = 567
    _CONFIGDAQREQUEST._serialized_start = 569
    _CONFIGDAQREQUEST._serialized_end = 603
    _CONFIGURATIONRESPONSE._serialized_start = 606
    _CONFIGURATIONRESPONSE._serialized_end = 1533
    _EMPTY._serialized_start = 1535
    _EMPTY._serialized_end = 1542
    _DAQ._serialized_start = 1661
    _DAQ._serialized_end = 2039
# @@protoc_insertion_point(module_scope)
