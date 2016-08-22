# coding: utf-8

"""Tests for keysmith.py"""

import keysmith


def test_main():
    """Test a full run."""
    assert keysmith.main() == 0


def test_main_stats():
    """Test a full run with statistics."""
    assert keysmith.main(['--stats']) == 0


def test_main_population():
    """Test a population file that does not exist."""
    assert keysmith.main(['--population', 'nonexistent']) == 1
