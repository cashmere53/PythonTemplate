import tomllib as tl
from pathlib import Path


def test_version() -> None:
    import template  # noqa: PLC0415

    pyproject_file = Path("./pyproject.toml")
    with pyproject_file.open("rb") as fp:
        parsed_content = tl.load(fp)

    correct_version = parsed_content["project"]["version"]
    assert template.__version__ == correct_version
