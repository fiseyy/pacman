import json
import datetime

class Record:
    def __init__(self, score, datetime_str=None):
        self.datetime = datetime_str or datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.score = score

    def to_dict(self):
        return { self.datetime : self.score}

    def __str__(self):
        return f"{self.score} points : {self.datetime}"

class Records:
    def __init__(self):
        self.records: list[Record] = []

    def add_record(self, record):
        self.records.append(record)

    def get_records(self):
        self.records.sort(key=lambda x: x.score, reverse=True)  # Сортируем по оценке
        return self.records

    def load_records(self, filename="records.json"):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                for datetime_str, score in data.items():
                    # Убедимся, что score является числом
                    if isinstance(score, (int, float)):
                        record = Record(score=score, datetime_str=datetime_str)
                        self.records.append(record)
                    else:
                        print(f"Неверные данные для записи {datetime_str}: {score}")
        except FileNotFoundError:
            print(f"Файл {filename} не найден. Загружаем пустой список записей.")
        except json.JSONDecodeError:
            print(f"Ошибка при декодировании JSON из файла {filename}.")
        except Exception as e:
            print(f"Произошла ошибка: {e}")

    def save_records(self, filename="records.json"):
        try:
            # Создаем словарь, где ключами являются временные метки, а значениями — оценки
            data = {}
            for rec in self.records:
                # Проверяем, есть ли уже запись с такой временной меткой
                if rec.datetime in data:
                    print(f"Запись с временной меткой {rec.datetime} уже существует. Пропускаем.")
                else:
                    data[rec.datetime] = rec.score
            
            with open(filename, 'w') as file:
                json.dump(data, file, indent=4)
            print(f"Данные успешно сохранены в {filename}.")
        except Exception as e:
            print(f"Произошла ошибка при сохранении данных: {e}")