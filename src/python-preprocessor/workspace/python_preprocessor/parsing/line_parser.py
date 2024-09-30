from abc import ABC, abstractmethod

from python_preprocessor.define.ast_.ast_ import Ast


class LineParser(ABC):

    @abstractmethod
    def parse(self, lines: list[str]) -> tuple[Ast, list[str]]:
        pass
