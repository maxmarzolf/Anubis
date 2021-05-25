from Anubis import Anubis
from Schema import Schema
from Validators import StringValidator, IntegerValidator, BooleanValidator


class testSchema(Schema):
    name = Schema.field("name", [StringValidator()])
    age = Schema.field("age", [IntegerValidator()])
    dob = Schema.field("date of birth", [StringValidator()])
    email = Schema.field("email", [StringValidator()])
    old = Schema.field("old", [BooleanValidator()])

a = Anubis("test.csv", ",", testSchema())
a.read_csv()
