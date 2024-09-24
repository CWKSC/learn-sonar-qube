from pathlib import Path


def file_to_lines(file: Path) -> list[str]:
    with file.open("r") as f:
        return f.readlines()
