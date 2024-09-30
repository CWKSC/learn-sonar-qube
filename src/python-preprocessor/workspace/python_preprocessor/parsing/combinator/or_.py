from typing import Optional

from python_preprocessor.define.ast_.ast_ import Ast
from python_preprocessor.parsing.line_parser import LineParser


class Or:
    def __init__(self, *parsers: LineParser):
        self.parsers = parsers

    def parse(self, lines: list[str]) -> Optional[tuple[Ast, list[str]]]:
        for parser in self.parsers:
            result = parser.parse(lines)
            if result is None:
                continue
            ast, lines = result
            return (ast, lines)
        return None
