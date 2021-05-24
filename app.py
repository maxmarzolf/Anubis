from csv import reader

# stand-in for a validator, kind of.
def getCount(str):
    if len(str) > 12:
        return False

    return True



        

# fname = "something.csv"
# print(fname[-4:])

d = read_csv(csv="test.csv", delimiter=",")
print(d)

"""
    NOTES:
        > potentially worth considering NumPy for the data array that holds validation information (because it's going to get huge + the stats are going to be derived from it)
        > reader
            # how to separate the declaration of the reader from the schema
            # should the reader always require a schema?
            # what does the association between a reader and a schema look like?
            # make the reader a generic class that takes in arguments during instantiation; only has a read_csv() callable
                > instantiation params: file name, delimiter, header row, schema (class)
            # error handling (?)
            # how to map the attributes of the schema to column names in the CSV in a sane way?
        > schema
            # schema is going to have to map to column names, not positions (because the positions can change)
            # how?
"""