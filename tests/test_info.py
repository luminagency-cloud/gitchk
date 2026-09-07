import subprocess
from unittest.mock import patch, MagicMock

import pytest

from gitchk import info


@patch("subprocess.run")
def test_run_quiet_diff(mock_run):
    mock_return = MagicMock()
    mock_run.return_value = mock_return
    got = info.run_quiet_diff(["--flags"], ["my", "args"], "/a/b/c")
    mock_run.assert_called_once_with(
        ["git", "--flags", "diff", "--quiet", "my", "args"],
        stderr=subprocess.DEVNULL,
        cwd="/a/b/c",
    )
    assert got == mock_return.returncode


@pytest.mark.parametrize(
    "now, commit_stamp, expected",
    [
        (1_700_000_000, 1_700_000_000 - 22 * 3600, "-022hrs"),
        (1_700_000_000, 1_700_000_000 - 2 * 86400, "-002day"),
        (1_700_000_000, 1_700_000_000, "-000hrs"),
        (1_700_000_000, 1_700_000_000 - 23 * 3600 - 3599, "-023hrs"),
    ],
)
def test_get_commit_time(now, commit_stamp, expected, monkeypatch):
    mock_result = MagicMock(stdout=f"{commit_stamp}\n")
    monkeypatch.setattr(subprocess, "run", lambda *a, **k: mock_result)
    monkeypatch.setattr(info.time, "time", lambda: now)
    got = info.get_commit_time({"path": "/a/b", "flags": []}, info.Truncate())
    assert got == expected
