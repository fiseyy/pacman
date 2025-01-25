class GhostSpawners:
    def reset(self):
        self.ghost_spawners = []
        for y in range(len(self.field)):
            for x in range(len(self.field[y])):
                if self.field[y][x] == 'G':
                    self.ghost_spawners.append((x, y))
        self.free_ghost_spawners = self.ghost_spawners.copy()
    def __init__(self, field):
        self.field = field
        self.reset()
    def get_free_spawn_locations(self):
        return self.free_ghost_spawners
    def occupy_spawn_location(self, location):
        if location in self.free_ghost_spawners:
            self.free_ghost_spawners.remove(location)
            return True
        return False

class Field:
    def __init__(self, file_path):
        self.field = self.load_field(file_path)
        self.ghost_spawners = GhostSpawners(self.to_array())
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
    
    def __getitem__(self, index):
        return self.field[index]
    
    def __len__(self):
        return len(self.field)
    
    def __repr__(self):
        return '\n'.join(''.join(row) for row in self.field)

    def to_array(self):
        # print([row[:] for row in self.field])
        # return [row[:] for row in self.field]  <---- для этого будет field.to_array()[y][x]
        return [list(column) for column in zip(*self.field)] # <---- для этого будет field.to_array()[x][y]

    def update_field(self, new_field):
        """Обновляет игровое поле."""
        self.field_array = new_field