from csv import reader
from typing import Any

from Schema import Schema

class Anubis():
    def __init__(self, file_name: str, delimiter: str, schema: Schema) -> None:
        self.file_name = file_name # validate file name later or in read_csv()
        self.delimiter = delimiter # validate delimiter later or in read_csv()
        self.schema = schema # validate that this is an object of Schema type later
        self.column_map = {} # maps the column names' integer position to the value (for translation in the schema)
        self.data = {} # data from the validation process

    def read_csv(self):
        if self.file_name == None or self.file_name[-4:] != '.csv' or self.delimiter == None or len(self.delimiter) == 0:
            return 'No CSV supplied.'

        with open(self.file_name, newline='') as f:
            r = reader(f, delimiter=self.delimiter) # may need some other params for odd character escapes/different delimiters

            row_number = 0 # used to get position
            col_number = 0 # used to get position

            """
                user: str, int, int

                name, age, email
                row: str, int, str (X) -> errors.csv || {row: {col: []}} 
            """
            
            for row in r: # each row is a list
                # create the column_map
                if row_number == 0:
                    for header in row:
                        #print(f"Adding {header} to column_map at key {col_number}")
                        self.column_map[col_number] = header
                        col_number = col_number + 1
                else:
                    if row_number == 1:
                        print(f"column_map: {self.column_map}")
                    for cell in row: # every item is a string
                        #print(f"Evaluating row {row_number}, col {col_number} ({cell}).")
                        print(f"[{row_number}, {col_number}] ({cell}): {self.validate(col_number, cell)}")
                        #if self.validate(col_number, cell) == False:
                            #print(f"Row {row_number} is not valid!")
                        #d = { 'loc': f'[{row_number}, {col_number}]', 'data': f'{i}', 'type': f'{type(i)}', 'valid': f'{getCount(i)}' }
                        
                        # self.data.append(d)
                        col_number = col_number + 1
                    pass

                row_number = row_number + 1
                col_number = 0 # reset column number to 0 with new row switch
            
            return self.data
        
    def validate(self, field_number: int, cell: Any) -> bool:
        # get the schema field name
        # print(self.column_map[field_number])
        # print(self.schema.schema)
        # print(f"Schema validators: {self.schema.schema[self.column_map[field_number]]}")

        #print(type(self.schema()))
        for v in self.schema()[self.column_map[field_number]]:
            print(f"{cell}: {v.evaluate(cell)}")
            if v.evaluate(cell) == False:
                return False
        
        return True

