# -*- coding: utf-8 -*-
#
# This file is part of the SKA Low MCCS project
#
#
# Distributed under the terms of the BSD 3-clause new license.
# See LICENSE for more info.
"""An implementation of a client interface for a DAQ receiver."""
from __future__ import annotations

import functools
from typing import Any, Iterator, cast

import grpc
from google.protobuf.json_format import MessageToDict
from ska_control_model import ResultCode, TaskStatus

from .generated_code import daq_pb2, daq_pb2_grpc

# pylint: disable = redefined-builtin
print = functools.partial(print, flush=True)  # noqa: A001
__all__ = ["DaqClient"]


class DaqClient:
    """A client for a DAQ gRPC server."""

    def __init__(
        self: DaqClient,
        address: str,
    ) -> None:
        """
        Initialise a new instance.

        :param address: address of the DAQ server.
            In this implementation this is a gRPC channel.
            However we deliberately leave this interface
            as taking an abstract string "address",
            in case we ever want to change the underlying implementation.
        """
        self._grpc_channel = address

    def initialise(
        self: DaqClient,
        configuration: str,
    ) -> dict[str, Any]:
        """
        Tell the DAQ server to initialise the DAQ by applying a configuration.

        :param configuration: the configuration to apply, as a JSON string.

        :return: the result of the call
        """
        with grpc.insecure_channel(self._grpc_channel) as channel:
            stub = daq_pb2_grpc.DaqStub(channel)  # type: ignore[no-untyped-call]
            response = stub.InitDaq(daq_pb2.configDaqRequest(config=configuration))
            return MessageToDict(response)

    def get_configuration(self: DaqClient) -> dict[str, Any]:
        """
        Tell the DAQ server to return the current DAQ configuration.

        :return: the current DAQ configuration
        """
        with grpc.insecure_channel(self._grpc_channel) as channel:
            stub = daq_pb2_grpc.DaqStub(channel)  # type: ignore[no-untyped-call]
            response = stub.GetConfiguration(daq_pb2.getConfigRequest())
        return MessageToDict(message=response, preserving_proto_field_name=True)

    def configure_daq(
        self: DaqClient,
        daq_config: str,
    ) -> tuple[ResultCode, str]:
        """
        Tell the DAQ server to apply the given DAQ configuration.

        :param daq_config: the configuration to be applied,
            in the form of a JSON string.

        :return: a (result code, message) tuple
        """
        with grpc.insecure_channel(self._grpc_channel) as channel:
            stub = daq_pb2_grpc.DaqStub(channel)  # type: ignore[no-untyped-call]
            response = stub.ConfigureDaq(daq_pb2.configDaqRequest(config=daq_config))
        return (response.result_code, response.message)

    def get_status(self: DaqClient) -> str:
        """
        Request the status of the DAQ from the DAQ server.

        :return: the DAQ status as a JSON-encoded string
        """
        with grpc.insecure_channel(self._grpc_channel) as channel:
            stub = daq_pb2_grpc.DaqStub(channel)  # type: ignore[no-untyped-call]
            response = stub.DaqStatus(daq_pb2.daqStatusRequest())
        return cast(str, response.status)

    def start_daq(self: DaqClient, modes_to_start: str) -> Iterator[dict[str, Any]]:
        """
        Tell the DAQ server to start the DAQ.

        :param modes_to_start: the DAQ modes to be started.

        :yields: updates on DAQ status.
        """
        with grpc.insecure_channel(self._grpc_channel) as channel:
            stub = daq_pb2_grpc.DaqStub(channel)  # type: ignore[no-untyped-call]
            responses = stub.StartDaq(
                daq_pb2.startDaqRequest(
                    modes_to_start=modes_to_start,
                )
            )
            yield {
                "status": TaskStatus.IN_PROGRESS,
                "message": "Start Command issued to gRPC stub",
            }

            for response in responses:
                response_dict: dict[str, Any] = {}  # XXX Make this a TypedDict
                if response.HasField("call_state"):
                    daq_state = response.call_state.state
                    # When we start the daq it will respond with a streaming update
                    # When it streams listening we notify the task_callback.
                    if daq_state == daq_pb2.CallState.State.LISTENING:
                        response_dict["status"] = TaskStatus.COMPLETED
                        response_dict[
                            "message"
                        ] = "Daq has been started and is listening"
                    # When stopped we need to ensure we clean up the thread.
                    # This is done with responses.cancel()
                    elif daq_state == daq_pb2.CallState.State.STOPPED:
                        # First the gRPC server hangs up the call.
                        # then the Client hangs up the call.
                        responses.cancel()
                        return

                if response.HasField("call_info"):
                    response_dict["types"] = response.call_info.data_types_received
                    response_dict["files"] = response.call_info.files_written

                yield response_dict

    def stop_daq(self: DaqClient) -> tuple[ResultCode, str]:
        """
        Tell the DAQ server to stop the DAQ.

        :return: a (result_code, message) tuple
        """
        with grpc.insecure_channel(self._grpc_channel) as channel:
            stub = daq_pb2_grpc.DaqStub(channel)  # type: ignore[no-untyped-call]
            response = stub.StopDaq(daq_pb2.stopDaqRequest())
        return (response.result_code, response.message)

    def start_bandpass_monitor(
        self: DaqClient,
        argin: str,
    ) -> Iterator[dict[str, Any]]:
        """
        Begin monitoring antenna bandpasses.

        :param argin: A json string with keywords
            - station_config_path
            Path to a station configuration file.
            - plot_directory
            Directory in which to store bandpass plots.
            - monitor_rms
            Whether or not to additionally produce RMS plots.
            Default: False.
            - auto_handle_daq
            Whether DAQ should be automatically reconfigured,
            started and stopped without user action if necessary.
            This set to False means we expect DAQ to already
            be properly configured and listening for traffic
            and DAQ will not be stopped when `StopBandpassMonitor`
            is called.
            Default: False.
        """
        print(f"IN DAQ CLIENT START BANDPASS WITH: {locals()}")
        with grpc.insecure_channel(self._grpc_channel) as channel:
            stub = daq_pb2_grpc.DaqStub(channel)  # type: ignore[no-untyped-call]
            responses = stub.BandpassMonitorStart(
                daq_pb2.bandpassMonitorStartRequest(config=argin)
            )
            print(f"BEFORE FIRST YIELD WITH: {responses}")
            yield {
                "result_code": TaskStatus.IN_PROGRESS,
                "message": "StartBandpassMonitor command issued to gRPC stub",
            }
            print("AFTER FIRST YIELD")
            try:
                for response in responses:
                    print(f"IN RESPONSES WITH {response}")
                    response_dict: dict[str, Any] = {}

                    response_dict["result_code"] = response.result_code
                    response_dict["message"] = response.message
                    response_dict["x_bandpass_plot"] = [
                        response.x_bandpass_plot
                        if response.HasField("x_bandpass_plot")
                        else None
                    ]
                    response_dict["y_bandpass_plot"] = [
                        response.y_bandpass_plot
                        if response.HasField("y_bandpass_plot")
                        else None
                    ]
                    response_dict["rms_plot"] = [
                        response.rms_plot if response.HasField("rms_plot") else None
                    ]
                    print(f"response_dict: {response_dict}", flush=True)
                    if (
                        response.result_code == ResultCode.OK
                        and response.message == "Bandpass monitoring complete."
                    ):
                        responses.cancel()
                    yield response_dict
            # pylint: disable = broad-exception-caught
            except Exception as exp:
                print(f"..CAUGHT EXCEPTION: {exp}")

    def stop_bandpass_monitor(self: DaqClient) -> tuple[ResultCode, str]:
        """Cease monitoring antenna bandpasses."""
        print("IN DAQ CLIENT STOP BANDPASS")
        with grpc.insecure_channel(self._grpc_channel) as channel:
            stub = daq_pb2_grpc.DaqStub(channel)  # type: ignore[no-untyped-call]
            response = stub.BandpassMonitorStop(daq_pb2.bandpassMonitorStopRequest())
        print(
            f"AFTER DAQCLIENT STOP BANDPASS: {(response.result_code,response.message)}"
        )
        return (response.result_code, response.message)
