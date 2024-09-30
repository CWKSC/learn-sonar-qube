from typing import Optional

from python_preprocessor.define.ast_.ast_ import Ast
from python_preprocessor.define.ast_.if_derivative_ast import IfDerivativeAst
from python_preprocessor.parsing.line_parser import LineParser

command_if = "# pypre if "
command_else = "# pypre else"
command_else_if = "# pypre else if "
command_end = "# pypre endif"


class IfDerivativeParser(LineParser):

    def parse(self, lines: list[str]) -> Optional[tuple[IfDerivativeAst, list[str]]]:
        if len(lines) == 0:
            return None

        first_line = lines[0].strip()
        if not first_line.startswith(command_if):
            return None

        condition = first_line[len(command_if) :].strip()
        lines = lines[1:]

        from python_preprocessor.parsing.parser import parser

        # then
        then_block: list[Ast] = []
        while True:

            if len(lines) == 0:
                raise Exception("Remaining lines is empty when parsing then block")
            first_line = lines[0].strip()

            if first_line.startswith(command_end):
                lines = lines[1:]
                return (
                    IfDerivativeAst(condition=condition, then_block=then_block),
                    lines,
                )

            if first_line.startswith(command_else) or first_line.startswith(
                command_else_if
            ):
                break

            result = parser.parse(lines)
            if result is None:
                raise Exception("General parser fail when parsing then block")

            ast, lines = result
            then_block.append(ast)

        # else if
        elif_nodes: list[tuple[str, list[Ast]]] = []
        if first_line.startswith(command_else_if):

            while True:
                elif_condition = first_line[len(command_else_if) :].strip()
                lines = lines[1:]
                elif_block: list[Ast] = []

                while True:

                    if len(lines) == 0:
                        raise Exception(
                            "Remaining lines is empty when parsing else if block"
                        )
                    first_line = lines[0].strip()

                    if first_line.startswith(command_end):
                        lines = lines[1:]
                        return (
                            IfDerivativeAst(
                                condition=condition,
                                then_block=then_block,
                                elif_nodes=elif_nodes,
                            ),
                            lines,
                        )

                    if first_line.startswith(command_else) or first_line.startswith(
                        command_else_if
                    ):
                        break

                    result = parser.parse(lines)
                    if result is None:
                        raise Exception(
                            "General parser fail when parsing else if block"
                        )

                    ast, lines = result
                    elif_block.append(ast)

                elif_nodes.append((elif_condition, elif_block))

                # Must be in front of checking command_else
                if first_line.startswith(command_else_if):
                    continue

                if first_line.startswith(command_else):
                    break

        # else
        lines = lines[1:]
        else_block: list[Ast] = []
        while True:

            if len(lines) == 0:
                raise Exception("Remaining lines is empty when parsing else block")
            first_line = lines[0].strip()

            if first_line.startswith(command_end):
                lines = lines[1:]
                return (
                    IfDerivativeAst(
                        condition=condition,
                        then_block=then_block,
                        else_block=else_block,
                        elif_nodes=elif_nodes,
                    ),
                    lines,
                )

            result = parser.parse(lines)
            if result is None:
                raise Exception("General parser fail when parsing else block")

            ast, lines = result
            else_block.append(ast)
