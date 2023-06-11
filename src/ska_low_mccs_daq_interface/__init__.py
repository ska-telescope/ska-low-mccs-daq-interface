# -*- coding: utf-8 -*-
#
# This file is part of the SKA Low MCCS project
#
#
# Distributed under the terms of the BSD 3-clause new license.
# See LICENSE for more info.
"""
This subpackage implements the monitoring and control interface to DAQ.

That is, the interface by which the DAQ Tango device communicates
with the DAQ itself.
"""


__author__ = """MCCS Team"""
__email__ = "drew.devereux@skao.int"
__version__ = "0.0.1"


__all__ = [
    "DaqClient",
    "DaqServer",
    "DaqServerBackendProtocol",
    "run_server_forever",
    "server_context",
]

from .client import DaqClient
from .server import (
    DaqServer,
    DaqServerBackendProtocol,
    run_server_forever,
    server_context,
)
