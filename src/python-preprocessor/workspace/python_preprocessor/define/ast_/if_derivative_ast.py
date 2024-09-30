from dataclasses import dataclass, field

from python_preprocessor.define.ast_.ast_ import Ast


@dataclass
class IfDerivativeAst(Ast):

    # if
    condition: str
    then_block: list[Ast]

    # else
    else_block: list[Ast] = field(default_factory=list)

    # else if
    # (condition: str, ast_list: list[Ast])
    elif_nodes: list[tuple[str, list[Ast]]] = field(default_factory=list)

    def to_string(self):
        message = f"""if {self.condition}
    {self.then_block}
"""
        if len(self.elif_nodes) != 0:

            for elif_node in self.elif_nodes:
                message += f"""else if {elif_node[0]}
    {elif_node[1]}
"""
        if len(self.else_block) != 0:
            message += f"""else
    {self.else_block}
"""
        message += "end"
        return message
