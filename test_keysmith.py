"""Test Keysmith."""

import subprocess
import sys

import keysmith


def test_script():
    """Test a full run when directly invoking."""
    subprocess.check_call([sys.executable, keysmith.__file__])


def test_python_m():
    """Test python -m."""
    command = [sys.executable, '-m', 'keysmith']
    assert subprocess.run(command).returncode == 0


def test_main_stats():
    """Test a full run with statistics."""
    assert keysmith.main(['--stats']) == 0


def test_main_population():
    """Test a population file that does not exist."""
    assert keysmith.main(['--population', 'nonexistent']) == 1
