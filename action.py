from component import Component
from expr import Expression
from action import Action

class Action:
    sign: str
    def __init__(self, sign: str) -> None:
        self.sign = sign
    
    def calculate(self, left: Component, sign: Action, right: Component) -> Component | Expression:
        if left.numeric != right.numeric:
            return Expression(str(left) + self.sign + str(right))
        if left.numeric == False and left.content == right.content:
            return self.calculate(Component('2'), Action('*'), left)
                