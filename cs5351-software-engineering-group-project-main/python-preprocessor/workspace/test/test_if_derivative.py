import unittest

from python_preprocessor.define.ast_.if_derivative_ast import IfDerivativeAst
from python_preprocessor.define.ast_.trivial_ast import TrivialAst
from python_preprocessor.parsing.if_derivative_parser import IfDerivativeParser

class TestIfDerivativeParser(unittest.TestCase):

    def match_ast(self, lines: list[str], expected_ast: IfDerivativeAst, expect_lines: list[str]):
        result = IfDerivativeParser().parse(lines)
        if result is None:
            self.fail()
        ast, lines = result
        self.assertEqual(ast, expected_ast)
        self.assertEqual(lines, expect_lines)

    def test_basic(self):
        lines = [
            "# pypre if condition",
            "line 1",
            "line 2",
            "# pypre endif",
        ]

        expected_ast = IfDerivativeAst(
            condition='condition',
            then_block=[
                TrivialAst(value='line 1'),
                TrivialAst(value='line 2')
            ],
            else_block=[],
            elif_nodes=[]
        )

        self.match_ast(lines, expected_ast, [])

    def test_empty(self):
        parser = IfDerivativeParser()
        lines = []
        result = parser.parse(lines)
        self.assertIsNone(result)

    def test_empty_block(self):
        lines = [
            "# pypre if condition",
            "# pypre else if condition 2",
            "# pypre else if condition 3",
            "# pypre else",
            "# pypre endif",
        ]

        expected_ast = IfDerivativeAst(
            condition='condition',
            then_block=[
            ],
            else_block=[
            ],
            elif_nodes=[
                ('condition 2', []),
                ('condition 3', [])
            ]
        )

        self.match_ast(lines, expected_ast, [])

    def test_complete_if_derivative(self):
        lines = [
            "# pypre if condition",
            "line 1",
            "line 2",
            "# pypre else if condition 2",
            "line 3",
            "line 4",
            "# pypre else if condition 3",
            "line 5",
            "line 6",
            "# pypre else",
            "line 7",
            "line 8",
            "# pypre endif",
        ]

        expected_ast = IfDerivativeAst(
            condition='condition',
            then_block=[
                TrivialAst(value='line 1'),
                TrivialAst(value='line 2')
            ],
            else_block=[
                TrivialAst(value='line 7'),
                TrivialAst(value='line 8')
            ],
            elif_nodes=[
                ('condition 2', [
                    TrivialAst(value='line 3'),
                    TrivialAst(value='line 4')
                ]),
                ('condition 3', [
                    TrivialAst(value='line 5'),
                    TrivialAst(value='line 6')
                ])
            ]
        )

        self.match_ast(lines, expected_ast, [])


    def test_nested_if_derivative(self):
        lines = [
            "# pypre if condition",
            "line 1",
            "line 2",
            "# pypre if condition 2",
            "line 3",
            "line 4",
            "# pypre endif",
            "line 5",
            "line 6",
            "# pypre if condition 3",
            "line 7",
            "line 8",
            "# pypre endif",
            "line 9",
            "line 10",
            "# pypre endif",
        ]

        expected_ast = IfDerivativeAst(
            condition='condition',
            then_block=[
                TrivialAst(value='line 1'),
                TrivialAst(value='line 2'),
                IfDerivativeAst(
                    condition='condition 2',
                    then_block=[
                        TrivialAst(value='line 3'),
                        TrivialAst(value='line 4')
                    ],
                    else_block=[],
                    elif_nodes=[]
                ),
                TrivialAst(value='line 5'),
                TrivialAst(value='line 6'),
                IfDerivativeAst(
                    condition='condition 3',
                    then_block=[
                        TrivialAst(value='line 7'),
                        TrivialAst(value='line 8')
                    ],
                    else_block=[],
                    elif_nodes=[]
                ),
                TrivialAst(value='line 9'),
                TrivialAst(value='line 10')
            ],
            else_block=[],
            elif_nodes=[]
        )

        self.match_ast(lines, expected_ast, [])


if __name__ == '__main__':
    unittest.main()
