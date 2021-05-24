from typing import List

class SchemaField():
    __name__ = "SchemaField"

    def __init__(self, field_name: str, validators: List = []):
        self.field_name = field_name
        self.validators = validators
    
    def __repr__(self):
        return f"<Field {self.field_name}: {len(self.validators)} validators.>"

    def __str__(self):
        return f"{self.field_name}: {len(self.validators)} validators."