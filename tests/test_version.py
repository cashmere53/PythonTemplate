from pathlib import Path

import tomllib as tl


def test_version() -> None:
    import template

    pyproject_file = Path("./pyproject.toml")
    with pyproject_file.open("rb") as fp:
        parsed_content = tl.load(fp)

    correct_version = parsed_content["tool"]["poetry"]["version"]
    assert template.__version__ == correct_version
