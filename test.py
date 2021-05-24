from Anubis import Anubis
from Schema import Schema
from Validators import StringValidator, IntegerValidator, BooleanValidator


class testSchema(Schema):
    name = Schema.field("name", [StringValidator()])
    age = Schema.field("age", [IntegerValidator()])
    dob = Schema.field("date of birth", [StringValidator()])
    email = Schema.field("email", [StringValidator()])
    old = Schema.field("old", [BooleanValidator()])

t = testSchema()
print(t.schema)

a = Anubis("test.csv", ",", testSchema())
#print(f"column_map: {a.column_map}")
a.read_csv()

# setting up the cli is going to require Click + Setuptools... yikes.