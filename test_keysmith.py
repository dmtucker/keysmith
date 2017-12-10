# coding: utf-8

"""Tests for keysmith.py"""

import subprocess

import keysmith


def test_script():
    """Test a full run when directly invoking."""
    subprocess.check_call([keysmith.__file__])


def test_main_stats():
    """Test a full run with statistics."""
    assert keysmith.main(['--stats']) == 0


def test_main_population():
    """Test a population file that does not exist."""
    assert keysmith.main(['--population', 'nonexistent']) == 1
