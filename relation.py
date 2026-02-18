from Errors.ParsingErrors import *
import expr
types = ['<=', '>=', '=', '<', '>']

def get_type_of(relation:str) -> int:
    counts = [relation.count(types[i]) for i in range(len(types))]
    if sum(counts) > 1:
        raise TooManyRelationSigns
    return counts.index(1)

class Relation:
    type: int
    left: expr.Expression
    right: expr.Expression
    def __init__(self, relation: str):
        self.type = get_type_of(relation)
        left_side, right_side = relation.split(types[self.type])
        self.left = expr.Expression(left_side)
        self.right = expr.Expression(right_side)
        
        
    

        
        