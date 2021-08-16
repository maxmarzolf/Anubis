from datetime import datetime


class Validator():
    def __init__(self):
        pass

    # informal interface (meant to be overriden, no enforcement)
    def evaluate(self, value: str) -> bool:
        pass


class StringValidator(Validator):
    def __init__(self):
        super().__init__()

    # by default, just about everything is going to evaluate properly to a string with additional conditions applied to the string...
    def evaluate(self, value: str) -> bool:
        return isinstance(value, str)


class IntegerValidator(Validator):
    def __init__(self):
        super().__init__()

    def evaluate(self, value: str) -> bool:
        # Python is always going to evaluate :value as a string because it's coming from the CSV so, catch an error during a simple cast operation:
        try:
            v = int(value)
            return True
        except ValueError:
            return False


class FloatValidator(Validator):
    def __init__(self):
        super().__init__()

    def evaluate(self, value: str) -> bool:
        try:
            v = float(value)
            return True
        except ValueError:
            return False


class BooleanValidator(Validator):
    def __init__(self):
        super().__init__()
        self.vals = ["True", "true", "False", "false"] # might want to be more explicit because FaLSE or trUe is odd formatting...

    # boolean is goofy. anything with a value, event an empty string, will be truthy so this almost always evaluates to true
    def evaluate(self, value: str) -> bool:
        if value in self.vals:
            return True
        
        return False
        # try:
        #     v = bool(value)
        #     return True
        # except ValueError:
        #     return False


class DateTimeValidator(Validator):
    def __init__(self):
        super().__init__()

    def evaluate(self, value: str) -> bool:
        try:
            v = datetime.strptime(value, '%B %d, %Y')
            return True
        except ValueError:
            return False
    

"""
    All of these validators are trying to see if string objects fit into the general confines of other objects. They're all coming into the .evaluate() as strings so
    the validates are doing work to see if they can be converted to an integer, float, boolean, etc.
"""