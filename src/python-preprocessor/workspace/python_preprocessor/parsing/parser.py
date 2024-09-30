from typing import Optional

from python_preprocessor.parsing.if_derivative_parser import IfDerivativeParser
from python_preprocessor.parsing.trivial_parser import TrivialParser
from python_preprocessor.parsing.combinator.or_ import Or
from python_preprocessor.define.ast_.ast_ import Ast

parsers = Or(IfDerivativeParser(), TrivialParser())


class Parser:

    def parse(self, lines: list[str]) -> Optional[tuple[Ast, list[str]]]:
        return parsers.parse(lines)


parser = Parser()
