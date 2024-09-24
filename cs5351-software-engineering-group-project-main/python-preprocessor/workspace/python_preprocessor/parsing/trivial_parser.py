from python_preprocessor.parsing.line_parser import LineParser
from python_preprocessor.define.ast_.ast_ import Ast
from python_preprocessor.define.ast_.trivial_ast import TrivialAst


class TrivialParser(LineParser):

    def parse(self, lines: list[str]) -> tuple[Ast, list[str]]:
        return (TrivialAst(lines[0]), lines[1:])
