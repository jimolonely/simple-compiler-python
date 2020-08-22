"""
RPN:reverse polish notation
反向波兰表达式
(5+3)*12/4 --> 5 3 + 12 * 4 /
"""
import unittest

from .ast import NodeVisitor, Lexer, Parser


class RpnTranslator(NodeVisitor):

    def __init__(self, tree):
        self.tree = tree

    def visit_BinOp(self, node):
        left_val = self.visit(node.left)
        right_val = self.visit(node.right)
        return '{} {} {}'.format(left_val, right_val, node.op.value)

    def visit_Num(self, node):
        return node.value

    def translate(self):
        return self.visit(self.tree)


def rpn_translate(text):
    lexer = Lexer(text)
    parser = Parser(lexer)
    tree = parser.parse()
    translator = RpnTranslator(tree)
    return translator.translate()


class RpnTestCase(unittest.TestCase):

    def test01(self):
        self.assertEqual(rpn_translate('(2+3)'), '2 3 +')

    def test02(self):
        self.assertEqual(rpn_translate('(2+3)*5'), '2 3 + 5 *')

    def test03(self):
        self.assertEqual(rpn_translate('5+(2+3)*4 -3'), '5 2 3 + 4 * + 3 -')
