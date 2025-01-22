class Field:
    def __init__(self, file_path):
        self.field = self.load_field(file_path)
        self.file_path = file_path
    
    def load_field(self, file_path=""):
        if file_path == "":
            file_path = self.file_path
        field_data = []
        with open(file_path, 'r') as file:
            for line in file:
                cleaned_line = line.strip()
                if cleaned_line:
                    field_data.append(list(cleaned_line))
        return field_data
    
    def __repr__(self):
        return '\n'.join(''.join(row) for row in self.field)