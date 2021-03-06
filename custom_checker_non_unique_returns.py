import astroid
from astroid import nodes

from pylint.checkers import BaseChecker
from pylint.interfaces import IAstroidChecker
from pylint.lint import PyLinter

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pylint.lint import PyLinter


def register(linter: "PyLinter") -> None:
    """This required method auto registers the checker during initialization.

    :param linter: The linter to register the checker to.
    """
    linter.register_checker(UniqueReturnChecker(linter))


class UniqueReturnChecker(BaseChecker):
    __implements__ = IAstroidChecker

    name = 'unique-returns'
    priority = -1
    msgs = {
        'W0001': (
            'Returns a non-unique constant.',
            'non-unique-returns',
            'All constants returned in a function should be unique.'
        ),
    }

    options = (
        (
            'ignore-ints',
            {
                'default': False, 'type': 'yn', 'metavar': '<y or n>',
                'help': 'Allow returning non-unique integers',
            }
        ),
    )

    def __init__(self, linter: PyLinter = None) -> None:
        super(UniqueReturnChecker, self).__init__(linter)
        # super().__init__(linter)
        self._function_stack = []

    def visit_functiondef(self, node: nodes.FunctionDef) -> None:
        self._function_stack.append([])

    def leave_functiondef(self, node: nodes.FunctionDef) -> None:
        self._function_stack.pop()

    def visit_return(self, node: nodes.Return) -> None:
        if not isinstance(node.value, nodes.Const):
            return

        for other_return in self._function_stack[-1]:
            if (node.value.value == other_return.value.value and
                    not (self.config.ignore_ints and node.value.pytype() == int)):
                self.add_message(
                    'non-unique-returns', node=node,
                )

        self._function_stack[-1].append(node)

