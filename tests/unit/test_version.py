#!/usr/bin/env python

"""Tests for `ska_low_mccs_daq_interface` package."""

import ska_low_mccs_daq_interface


def test_content() -> None:
    """Check that the package version is as expected.

    :param version: the version fixture
    """
    assert ska_low_mccs_daq_interface.__version__ == "0.2.0"
