# -*- coding: utf-8 -*-
"""Basic tests for the dork cli
"""
import unittest
from types import FunctionType
from unittest.mock import Mock
import dork.cli


def test_cli_exists(run):
    """Dork.cli.main should always exist and run
    """
    assert "main" in vars(dork.cli), "Dork.cli should define a main method"
    assert isinstance(dork.cli.main, FunctionType)
    try:
        run(dork.cli.main)
    except:  # noqa: E722
        raise AssertionError("cannot run 'dork' command")


def test_cli_help(run):
    """CLI's help command should return helpful information
    """
    out, err = run(dork.cli.main, "-h")
    out, err = run(dork.cli.main(mock_cli), "-h")
    assert "usage: " in out, \
        "Failed to run the cli.main method: {err}".format(err=err)
