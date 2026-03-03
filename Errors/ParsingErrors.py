
class TooManyRelationSigns(Exception):
    pass

class RelationSignNotFound(Exception):
    pass

class BracketsInExpression(Exception):
    pass

class CannotProcessSymbol(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class TooLongVariable(Exception):
    pass


