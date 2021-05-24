from typing import List

from SchemaField import SchemaField
from Validators import StringValidator, IntegerValidator

class Schema():
    def __init__(self):
        # for attr, val in self.__dict__.items():
        #     print(f'attr: {attr or ""}')
        #     print(f'val: {val or ""}')
        self.columns = {}
        self.schema = self.create_schema() # { field_name: [validators] }
        print("Now we're intitializing the instance object...")
    
    def create_schema(self):
        s = {}
        for i in dir(self):
            # print(f"{i}: (type) {type(getattr(d, i))}")
            # print(f"{i}: (isnt_dunder) {i[:2] != '__'}")
            # print(f"{i}: (isinstance) {isinstance(getattr(d, i), Field)}")
            if i[:2] != "__" and isinstance(getattr(self, i), SchemaField):
                #s.append(getattr(self, i))
                s[getattr(self, i).field_name] = getattr(self, i).validators
        
        return s

    @classmethod # since there's only once instance of the class, passing the class object works better here so the __init__() can be avoided?
    def field(cls, field_name, validators=[]):
        f = SchemaField(field_name, validators)
        print(f"Created <Field: {field_name}>")
        #print(f.__repr__())
        # print(f.__str__())
        # print(f'{field_name} added.')
        #schema[field_name] = { "name": field_name, "validators": validators }
        #self.columns.field_name = {"field_name": field_name, "validators": [validators]}
        return f
    
    # Makes the class callable and makes the call return the schema attribute. Makes it easier to use the validate() method on Anubis.
    def __call__(self):
        return self.schema


class Duaht(Schema):
    # ok because we'd only be making one instance of this class.
    name = Schema.field("name", [StringValidator()])
    age = Schema.field("age", [IntegerValidator()])

    def custom_validators(self):
        pass

    def __repr__(self):
        print(self.schema)
        #print(f'<Duaht {self.name}, {self.age}, {self.date_of_birth}, {self.email}>')

d = Duaht()
# print(type(d.name))
# print(d.name.__name__)
# print(dir(d))
# for i in dir(d):
    # print(f"{i}: (type) {type(getattr(d, i))}")
    # print(f"{i}: (isnt_dunder) {i[:2] != '__'}")
    # print(f"{i}: (isinstance) {isinstance(getattr(d, i), Field)}")
    # if i[:2] != "__" and isinstance(i, Field):
    #     print(f"{i} is a Field object.")
    # pass
print(d.schema)
# print(d.schema[0].field_name)
# print(d.schema[1].validators)
#print(f'getattr: {getattr(d, "name")}')
#d.__repr__()
# data = ["something", 3, True]
# print(d.schema["name"][0].evaluate(data[0]))
# print(d.schema["name"][0].evaluate(data[1]))
# print(d.schema["name"][0].evaluate(data[2]))