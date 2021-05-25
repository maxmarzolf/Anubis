from csv import reader
from typing import Any

from Schema import Schema

class Anubis():
    def __init__(self, file_name: str, delimiter: str, schema: Schema) -> None:
        self.file_name = self._validate_csv_name(file_name)
        self.delimiter = self._validate_delimiter(delimiter)
        self.schema = self._validate_schema(schema)
        self.column_map = {} # maps the column names' integer position to the value (for translation in the schema)
        self.data = {} # data from the validation process

    def read_csv(self):
        with open(self.file_name, newline='') as f:
            r = reader(f, delimiter=self.delimiter) # may need some other params for odd character escapes/different delimiters

            row_number = 0 # used to get row position
            col_number = 0 # used to get column position
            
            for row in r: # each row is a list
                # create the column_map
                if row_number == 0:
                    for header in row:
                        #print(f"Adding {header} to column_map at key {col_number}")
                        self.column_map[col_number] = header
                        col_number = col_number + 1
                    self._validate_headers()
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
        
    def _validate_csv_name(self, csv_name: str) -> str:
        valid = not csv_name == None and csv_name[-4:] == '.csv'
        if valid:
            return csv_name
        else:
            raise ValueError('Invalid file provided.')
    
    def _validate_delimiter(self, delimiter: str) -> str:
        valid = delimiter in [","]
        if valid:
            return delimiter
        else:
            raise ValueError('Invalid delimiter supplied.')

    def _validate_schema(self, schema: Schema) -> Schema:
        valid = isinstance(schema, Schema)
        if valid:
            return schema
        else:
            raise ValueError('Invalid schema provided.')

    def _validate_headers(self) -> None:
        # Check that the items in the column_map var match the ones in schema. Otherwise, throw an error (unsure what kind of error would be useful here)
        pass

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

