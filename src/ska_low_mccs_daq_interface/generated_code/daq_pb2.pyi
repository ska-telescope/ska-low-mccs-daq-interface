"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _ResultCode:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _ResultCodeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_ResultCode.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    OK: _ResultCode.ValueType  # 0
    STARTED: _ResultCode.ValueType  # 1
    QUEUED: _ResultCode.ValueType  # 2
    FAILED: _ResultCode.ValueType  # 3
    UNKNOWN: _ResultCode.ValueType  # 4
    REJECTED: _ResultCode.ValueType  # 5
    NOT_ALLOWED: _ResultCode.ValueType  # 6
    ABORTED: _ResultCode.ValueType  # 7

class ResultCode(_ResultCode, metaclass=_ResultCodeEnumTypeWrapper): ...

OK: ResultCode.ValueType  # 0
STARTED: ResultCode.ValueType  # 1
QUEUED: ResultCode.ValueType  # 2
FAILED: ResultCode.ValueType  # 3
UNKNOWN: ResultCode.ValueType  # 4
REJECTED: ResultCode.ValueType  # 5
NOT_ALLOWED: ResultCode.ValueType  # 6
ABORTED: ResultCode.ValueType  # 7
global___ResultCode = ResultCode

@typing_extensions.final
class CallState(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _State:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _StateEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[CallState._State.ValueType], builtins.type):  # noqa: F821
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        STOPPED: CallState._State.ValueType  # 0
        RECEIVING: CallState._State.ValueType  # 1
        LISTENING: CallState._State.ValueType  # 2

    class State(_State, metaclass=_StateEnumTypeWrapper): ...
    STOPPED: CallState.State.ValueType  # 0
    RECEIVING: CallState.State.ValueType  # 1
    LISTENING: CallState.State.ValueType  # 2

    STATE_FIELD_NUMBER: builtins.int
    state: global___CallState.State.ValueType
    def __init__(
        self,
        *,
        state: global___CallState.State.ValueType = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["state", b"state"]) -> None: ...

global___CallState = CallState

@typing_extensions.final
class CallInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DATA_TYPES_RECEIVED_FIELD_NUMBER: builtins.int
    FILES_WRITTEN_FIELD_NUMBER: builtins.int
    EXTRA_INFO_FIELD_NUMBER: builtins.int
    data_types_received: builtins.str
    files_written: builtins.str
    extra_info: builtins.str
    def __init__(
        self,
        *,
        data_types_received: builtins.str = ...,
        files_written: builtins.str = ...,
        extra_info: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["data_types_received", b"data_types_received", "extra_info", b"extra_info", "files_written", b"files_written"]) -> None: ...

global___CallInfo = CallInfo

@typing_extensions.final
class startDaqRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MODES_TO_START_FIELD_NUMBER: builtins.int
    modes_to_start: builtins.str
    def __init__(
        self,
        *,
        modes_to_start: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["modes_to_start", b"modes_to_start"]) -> None: ...

global___startDaqRequest = startDaqRequest

@typing_extensions.final
class startDaqResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CALL_STATE_FIELD_NUMBER: builtins.int
    CALL_INFO_FIELD_NUMBER: builtins.int
    @property
    def call_state(self) -> global___CallState: ...
    @property
    def call_info(self) -> global___CallInfo: ...
    def __init__(
        self,
        *,
        call_state: global___CallState | None = ...,
        call_info: global___CallInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["call_info", b"call_info", "call_state", b"call_state", "start_daq_response", b"start_daq_response"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["call_info", b"call_info", "call_state", b"call_state", "start_daq_response", b"start_daq_response"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["start_daq_response", b"start_daq_response"]) -> typing_extensions.Literal["call_state", "call_info"] | None: ...

global___startDaqResponse = startDaqResponse

@typing_extensions.final
class stopDaqRequest(google.protobuf.message.Message):
    """Empty messages as no params expected but this is in case it changes."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___stopDaqRequest = stopDaqRequest

@typing_extensions.final
class getConfigRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___getConfigRequest = getConfigRequest

@typing_extensions.final
class getConfigResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CONFIG_FIELD_NUMBER: builtins.int
    config: builtins.str
    def __init__(
        self,
        *,
        config: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["config", b"config"]) -> None: ...

global___getConfigResponse = getConfigResponse

@typing_extensions.final
class daqStatusRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___daqStatusRequest = daqStatusRequest

@typing_extensions.final
class daqStatusResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    STATUS_FIELD_NUMBER: builtins.int
    status: builtins.str
    def __init__(
        self,
        *,
        status: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["status", b"status"]) -> None: ...

global___daqStatusResponse = daqStatusResponse

@typing_extensions.final
class commandResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESULT_CODE_FIELD_NUMBER: builtins.int
    MESSAGE_FIELD_NUMBER: builtins.int
    result_code: global___ResultCode.ValueType
    message: builtins.str
    def __init__(
        self,
        *,
        result_code: global___ResultCode.ValueType = ...,
        message: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["message", b"message", "result_code", b"result_code"]) -> None: ...

global___commandResponse = commandResponse

@typing_extensions.final
class configDaqRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CONFIG_FIELD_NUMBER: builtins.int
    config: builtins.str
    def __init__(
        self,
        *,
        config: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["config", b"config"]) -> None: ...

global___configDaqRequest = configDaqRequest

@typing_extensions.final
class ConfigurationResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NOF_ANTENNAS_FIELD_NUMBER: builtins.int
    NOF_CHANNELS_FIELD_NUMBER: builtins.int
    NOF_BEAMS_FIELD_NUMBER: builtins.int
    NOF_POLARISATIONS_FIELD_NUMBER: builtins.int
    NOF_TILES_FIELD_NUMBER: builtins.int
    NOF_RAW_SAMPLES_FIELD_NUMBER: builtins.int
    RAW_RMS_THRESHOLD_FIELD_NUMBER: builtins.int
    NOF_CHANNEL_SAMPLES_FIELD_NUMBER: builtins.int
    NOF_CORRELATOR_SAMPLES_FIELD_NUMBER: builtins.int
    NOF_CORRELATOR_CHANNELS_FIELD_NUMBER: builtins.int
    CONTINUOUS_PERIOD_FIELD_NUMBER: builtins.int
    NOF_BEAM_SAMPLES_FIELD_NUMBER: builtins.int
    NOF_BEAM_CHANNELS_FIELD_NUMBER: builtins.int
    NOF_STATION_SAMPLES_FIELD_NUMBER: builtins.int
    RECEIVER_FRAMES_PER_BLOCK_FIELD_NUMBER: builtins.int
    RECEIVER_NOF_BLOCKS_FIELD_NUMBER: builtins.int
    RECEIVER_NOF_THREADS_FIELD_NUMBER: builtins.int
    RECEIVER_FRAME_SIZE_FIELD_NUMBER: builtins.int
    ACQUISITION_DURATION_FIELD_NUMBER: builtins.int
    ACQUISITION_START_TIME_FIELD_NUMBER: builtins.int
    APPEND_INTEGRATED_FIELD_NUMBER: builtins.int
    LOGGING_FIELD_NUMBER: builtins.int
    WRITE_TO_DISK_FIELD_NUMBER: builtins.int
    SAMPLING_TIME_FIELD_NUMBER: builtins.int
    SAMPLING_RATE_FIELD_NUMBER: builtins.int
    OVERSAMPLING_FACTOR_FIELD_NUMBER: builtins.int
    RECEIVER_PORTS_FIELD_NUMBER: builtins.int
    OBSERVATION_METADATA_FIELD_NUMBER: builtins.int
    RECEIVER_INTERFACE_FIELD_NUMBER: builtins.int
    RECEIVER_IP_FIELD_NUMBER: builtins.int
    DIRECTORY_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    STATION_CONFIG_FIELD_NUMBER: builtins.int
    MAX_FILESIZE_FIELD_NUMBER: builtins.int
    nof_antennas: builtins.int
    """
    int32
    """
    nof_channels: builtins.int
    nof_beams: builtins.int
    nof_polarisations: builtins.int
    nof_tiles: builtins.int
    nof_raw_samples: builtins.int
    raw_rms_threshold: builtins.int
    nof_channel_samples: builtins.int
    nof_correlator_samples: builtins.int
    nof_correlator_channels: builtins.int
    continuous_period: builtins.int
    nof_beam_samples: builtins.int
    nof_beam_channels: builtins.int
    nof_station_samples: builtins.int
    receiver_frames_per_block: builtins.int
    receiver_nof_blocks: builtins.int
    receiver_nof_threads: builtins.int
    receiver_frame_size: builtins.int
    acquisition_duration: builtins.int
    acquisition_start_time: builtins.int
    append_integrated: builtins.bool
    """
    bool
    """
    logging: builtins.bool
    write_to_disk: builtins.bool
    sampling_time: builtins.float
    """
    double
    """
    sampling_rate: builtins.float
    oversampling_factor: builtins.float
    receiver_ports: builtins.str
    """
    string
    """
    observation_metadata: builtins.str
    receiver_interface: builtins.str
    receiver_ip: builtins.str
    directory: builtins.str
    description: builtins.str
    @property
    def station_config(self) -> global___empty:
        """
        None
        """
    @property
    def max_filesize(self) -> global___empty: ...
    def __init__(
        self,
        *,
        nof_antennas: builtins.int = ...,
        nof_channels: builtins.int = ...,
        nof_beams: builtins.int = ...,
        nof_polarisations: builtins.int = ...,
        nof_tiles: builtins.int = ...,
        nof_raw_samples: builtins.int = ...,
        raw_rms_threshold: builtins.int = ...,
        nof_channel_samples: builtins.int = ...,
        nof_correlator_samples: builtins.int = ...,
        nof_correlator_channels: builtins.int = ...,
        continuous_period: builtins.int = ...,
        nof_beam_samples: builtins.int = ...,
        nof_beam_channels: builtins.int = ...,
        nof_station_samples: builtins.int = ...,
        receiver_frames_per_block: builtins.int = ...,
        receiver_nof_blocks: builtins.int = ...,
        receiver_nof_threads: builtins.int = ...,
        receiver_frame_size: builtins.int = ...,
        acquisition_duration: builtins.int = ...,
        acquisition_start_time: builtins.int = ...,
        append_integrated: builtins.bool = ...,
        logging: builtins.bool = ...,
        write_to_disk: builtins.bool = ...,
        sampling_time: builtins.float = ...,
        sampling_rate: builtins.float = ...,
        oversampling_factor: builtins.float = ...,
        receiver_ports: builtins.str = ...,
        observation_metadata: builtins.str = ...,
        receiver_interface: builtins.str = ...,
        receiver_ip: builtins.str = ...,
        directory: builtins.str = ...,
        description: builtins.str = ...,
        station_config: global___empty | None = ...,
        max_filesize: global___empty | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["max_filesize", b"max_filesize", "station_config", b"station_config"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["acquisition_duration", b"acquisition_duration", "acquisition_start_time", b"acquisition_start_time", "append_integrated", b"append_integrated", "continuous_period", b"continuous_period", "description", b"description", "directory", b"directory", "logging", b"logging", "max_filesize", b"max_filesize", "nof_antennas", b"nof_antennas", "nof_beam_channels", b"nof_beam_channels", "nof_beam_samples", b"nof_beam_samples", "nof_beams", b"nof_beams", "nof_channel_samples", b"nof_channel_samples", "nof_channels", b"nof_channels", "nof_correlator_channels", b"nof_correlator_channels", "nof_correlator_samples", b"nof_correlator_samples", "nof_polarisations", b"nof_polarisations", "nof_raw_samples", b"nof_raw_samples", "nof_station_samples", b"nof_station_samples", "nof_tiles", b"nof_tiles", "observation_metadata", b"observation_metadata", "oversampling_factor", b"oversampling_factor", "raw_rms_threshold", b"raw_rms_threshold", "receiver_frame_size", b"receiver_frame_size", "receiver_frames_per_block", b"receiver_frames_per_block", "receiver_interface", b"receiver_interface", "receiver_ip", b"receiver_ip", "receiver_nof_blocks", b"receiver_nof_blocks", "receiver_nof_threads", b"receiver_nof_threads", "receiver_ports", b"receiver_ports", "sampling_rate", b"sampling_rate", "sampling_time", b"sampling_time", "station_config", b"station_config", "write_to_disk", b"write_to_disk"]) -> None: ...

global___ConfigurationResponse = ConfigurationResponse

@typing_extensions.final
class bandpassMonitorStartRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CONFIG_FIELD_NUMBER: builtins.int
    config: builtins.str
    """
    CURRENT MEMBERS
    string config.station_config_path
    string config.plot_directory
    bool config.monitor_rms
    bool config.auto_handle_daq
    """
    def __init__(
        self,
        *,
        config: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["config", b"config"]) -> None: ...

global___bandpassMonitorStartRequest = bandpassMonitorStartRequest

@typing_extensions.final
class bandpassMonitorStartResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESULT_CODE_FIELD_NUMBER: builtins.int
    MESSAGE_FIELD_NUMBER: builtins.int
    X_BANDPASS_PLOT_FIELD_NUMBER: builtins.int
    Y_BANDPASS_PLOT_FIELD_NUMBER: builtins.int
    RMS_PLOT_FIELD_NUMBER: builtins.int
    result_code: global___ResultCode.ValueType
    message: builtins.str
    x_bandpass_plot: builtins.bytes
    y_bandpass_plot: builtins.bytes
    rms_plot: builtins.bytes
    def __init__(
        self,
        *,
        result_code: global___ResultCode.ValueType = ...,
        message: builtins.str = ...,
        x_bandpass_plot: builtins.bytes | None = ...,
        y_bandpass_plot: builtins.bytes | None = ...,
        rms_plot: builtins.bytes | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_rms_plot", b"_rms_plot", "_x_bandpass_plot", b"_x_bandpass_plot", "_y_bandpass_plot", b"_y_bandpass_plot", "rms_plot", b"rms_plot", "x_bandpass_plot", b"x_bandpass_plot", "y_bandpass_plot", b"y_bandpass_plot"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_rms_plot", b"_rms_plot", "_x_bandpass_plot", b"_x_bandpass_plot", "_y_bandpass_plot", b"_y_bandpass_plot", "message", b"message", "result_code", b"result_code", "rms_plot", b"rms_plot", "x_bandpass_plot", b"x_bandpass_plot", "y_bandpass_plot", b"y_bandpass_plot"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_rms_plot", b"_rms_plot"]) -> typing_extensions.Literal["rms_plot"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_x_bandpass_plot", b"_x_bandpass_plot"]) -> typing_extensions.Literal["x_bandpass_plot"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_y_bandpass_plot", b"_y_bandpass_plot"]) -> typing_extensions.Literal["y_bandpass_plot"] | None: ...

global___bandpassMonitorStartResponse = bandpassMonitorStartResponse

@typing_extensions.final
class bandpassMonitorStopRequest(google.protobuf.message.Message):
    """Empty"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___bandpassMonitorStopRequest = bandpassMonitorStopRequest

@typing_extensions.final
class empty(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___empty = empty
