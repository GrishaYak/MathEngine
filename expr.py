from Errors.ParsingErrors import *
from component import Component
# no brackets
letters = 'abcdefghijklmnopqrstuvwxyz'
numbers = set(list('0123456789'))
allowedSymbols = numbers | set(list('*^%/' + letters + letters.upper()))

class Expression:
    components: list[Component]
    def __init__(self, expression: str) -> None:
        if '(' in expression or ')' in expression:
            raise BracketsInExpression
    
def breakExpression(expression: str) -> list[Expression]:
    signs = set(list('+-'))
    prefix = ''
    left: list[Expression] = []
    for s in expression:
        if s in signs:
            left = breakExpression(prefix)
            prefix = ''
        else:
            prefix += s
    
        
