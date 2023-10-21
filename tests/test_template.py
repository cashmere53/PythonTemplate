from __future__ import annotations

from pathlib import Path
from re import Match, fullmatch

from template import __version__


def test_version() -> None:
    pyproject_file: Path = Path("./pyproject.toml")
    with pyproject_file.open("r") as fp:
        buffer: str = next(filter(lambda x: x.startswith("version"), fp))
    m_res: Match[str] | None = fullmatch(r'version = "(.*)"\n', buffer)
    if m_res is None:
        msg = "version string is not found in pyproject.toml"
        raise ValueError(msg)
    version: str = m_res[1]

    assert __version__ == version
