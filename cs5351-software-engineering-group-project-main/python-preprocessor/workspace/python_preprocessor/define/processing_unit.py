from pathlib import Path
from dataclasses import dataclass

from python_preprocessor.util.file import file_to_lines


@dataclass
class ProcessingUnit:
    file: Path

    def preprocess(self):
        lines = file_to_lines(self.file)
        from python_preprocessor.parsing.parser import parser

        return parser.parse(lines)
