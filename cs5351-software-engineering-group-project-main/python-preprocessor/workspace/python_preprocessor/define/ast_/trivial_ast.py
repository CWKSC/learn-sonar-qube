from dataclasses import dataclass

from python_preprocessor.define.ast_.ast_ import Ast


@dataclass
class TrivialAst(Ast):
    value: str
