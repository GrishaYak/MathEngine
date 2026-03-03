from Errors.ParsingErrors import CannotProcessSymbol
from component import Component

# no brackets

letters = 'abcdefghijklmnopqrstuvwxyz'
letters += letters.upper()
letters = set(letters)
symbols = set(list('*^%/'))
numbers = set(list('0123456789'))
allowedSymbols = numbers | letters | symbols

class ActionTree:
    left: ActionTree | Component
    right: ActionTree | Component
    action = ''
    def __init__(self, left: ActionTree | Component, right: ActionTree | Component) -> None:
       self.left = left
       self.right = right
        
    
def breakExpression(expression: str) -> ActionTree:
    signs = set(list('+-*/'))
    prefix = ''
    expression: list[Component| ActionTree | str] = []
    for s in expression:
        if s not in allowedSymbols:
            raise CannotProcessSymbol()
        if s in letters:
            if prefix:
                expression.append(ActionTree())
        if s in signs:
            left = breakExpression(prefix)
            prefix = ''
        else:
            prefix += s
    
        
