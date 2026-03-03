from Errors.ParsingErrors import TooLongVariable

letters = 'abcdefghijklmnopqrstuvwxyz'
letters += letters.upper()
letters = set(letters)
numbers = set(list('0123456789'))
allowedSymbols = numbers | letters

class Component:
    numeric: bool = True
    content: str | int
    
    def __init__(self, component: str) -> None:
        if component.isdigit():
            self.content = int(component)
            return
        if len(component) > 1:
            raise TooLongVariable
        self.numeric = False
        self.content = component
    
    def __str__(self) -> str:
        return str(self.content)
    