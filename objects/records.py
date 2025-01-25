import pyray as pr
class RecordsDrawer:
    def __init__(self, records):
        self.records = records
        print(self.records)

    def draw(self,additional_pos_x, additional_pos_y):
        # pr.draw_text("Records:", 10, 10, 20, pr.DARKGRAY)
        y_offset = 40
        for record in self.records:
            # print(f"Drawing record: {str(record)}")
            pr.draw_text(str(record), additional_pos_x + 10, additional_pos_y + y_offset, 20, pr.WHITE)
            y_offset += 30  # Увеличиваем отступ для следующей записи
